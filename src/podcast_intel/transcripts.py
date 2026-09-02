from __future__ import annotations

import json
import re
import shutil
import subprocess
import tempfile
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, unquote, urlparse

from .feeds import fetch_text, parse_html
from .models import Episode, Transcript


class TranscriptUnavailable(RuntimeError):
    pass


def timestamp(seconds: float | int | str | None) -> str:
    try:
        total = max(0, int(float(seconds or 0)))
    except (TypeError, ValueError):
        total = 0
    hours, remainder = divmod(total, 3600)
    minutes, secs = divmod(remainder, 60)
    if hours:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def _strip_markup(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    return " ".join(value.replace("\u00a0", " ").split())


def _parse_caption_text(value: str) -> str:
    blocks = re.split(r"\n\s*\n", value.replace("\r\n", "\n"))
    output: list[str] = []
    previous = ""
    for block in blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        cue_index = next((i for i, line in enumerate(lines) if "-->" in line), -1)
        if cue_index < 0:
            continue
        start = lines[cue_index].split("-->", 1)[0].strip().replace(",", ".")
        text = _strip_markup(" ".join(lines[cue_index + 1 :]))
        if not text or text == previous:
            continue
        previous = text
        output.append(f"[{start.split('.')[0]}] {text}")
    return "\n".join(output)


def _json_segment_text(payload: Any) -> str:
    if isinstance(payload, str):
        return payload
    if isinstance(payload, list):
        rendered = [_json_segment_text(item) for item in payload]
        return "\n".join(item for item in rendered if item)
    if not isinstance(payload, dict):
        return ""

    for key in ("segments", "results", "items", "events"):
        if isinstance(payload.get(key), list):
            lines: list[str] = []
            for item in payload[key]:
                if not isinstance(item, dict):
                    continue
                text = item.get("text") or item.get("body") or item.get("transcript")
                if not text and isinstance(item.get("segs"), list):
                    text = "".join(
                        str(segment.get("utf8", ""))
                        for segment in item["segs"]
                        if isinstance(segment, dict)
                    )
                text = " ".join(str(text or "").split())
                if not text:
                    continue
                start = (
                    item.get("start")
                    or item.get("start_time")
                    or item.get("startTime")
                    or (float(item.get("tStartMs", 0)) / 1000)
                )
                lines.append(f"[{timestamp(start)}] {text}")
            if lines:
                return "\n".join(lines)
    for key in ("transcript", "text", "body"):
        if key in payload:
            return _json_segment_text(payload[key])
    return ""


def normalize_transcript(value: str, content_type: str = "", url: str = "") -> str:
    lowered_type = content_type.casefold()
    lowered_url = url.casefold()
    if "json" in lowered_type or lowered_url.endswith((".json", ".json3")):
        try:
            return _json_segment_text(json.loads(value)).strip()
        except json.JSONDecodeError:
            pass
    if "vtt" in lowered_type or "subrip" in lowered_type or lowered_url.endswith(
        (".vtt", ".srt")
    ):
        return _parse_caption_text(value).strip()
    if "html" in lowered_type or "<html" in value[:1000].casefold():
        text, _ = parse_html(value, url)
        return extract_transcript_section(text)
    return value.strip()


def extract_transcript_section(text: str) -> str:
    match = re.search(r"(?:^|\n)\s*(?:full\s+)?transcript\s*:?\s*(?:\n|$)", text, re.I)
    if match and len(text) - match.end() >= 1000:
        return text[match.end() :].strip()
    return text.strip()


def has_transcript_heading(text: str) -> bool:
    return bool(
        re.search(r"(?:^|\n)\s*(?:full\s+)?transcript\s*:?\s*(?:\n|$)", text, re.I)
    )


def looks_like_transcript(text: str, direct: bool = False) -> bool:
    if len(text) < (1000 if direct else 7000):
        return False
    if direct:
        return True
    lowered = text.casefold()
    timestamp_count = len(
        re.findall(r"(?:^|\n)\s*[\[(]?\d{1,2}:\d{2}(?::\d{2})?[\])]?", text)
    )
    speaker_count = len(re.findall(r"(?:^|\n)[A-Z][A-Za-z .'-]{1,40}\s*:", text))
    return "transcript" in lowered or timestamp_count >= 6 or speaker_count >= 10


def _transcript_url_priority(candidate: dict[str, str]) -> tuple[int, str]:
    kind = candidate.get("type", "").casefold()
    url = candidate.get("url", "").casefold()
    if "text/plain" in kind or url.endswith(".txt"):
        return (0, url)
    if "json" in kind or url.endswith((".json", ".json3")):
        return (1, url)
    if "vtt" in kind or url.endswith(".vtt"):
        return (2, url)
    if "subrip" in kind or url.endswith(".srt"):
        return (3, url)
    return (4, url)


def _fetch_transcript_url(url: str, timeout: int) -> Transcript | None:
    try:
        value, content_type = fetch_text(url, timeout)
    except Exception:
        return None
    text = normalize_transcript(value, content_type, url)
    if not looks_like_transcript(text, direct=True):
        return None
    return Transcript(text=text, source="publisher_transcript", source_url=url)


def _youtube_urls(links: list[dict[str, str]]) -> list[str]:
    found: list[str] = []
    for link in links:
        raw = unquote(link.get("url", "")).replace("&amp;", "&")
        if not raw:
            continue
        parsed = urlparse(raw)
        host = parsed.netloc.casefold().removeprefix("www.")
        video_id = ""
        if host in {"youtube.com", "m.youtube.com"}:
            if parsed.path == "/watch":
                video_id = (parse_qs(parsed.query).get("v") or [""])[0]
            elif parsed.path.startswith("/shorts/"):
                video_id = parsed.path.split("/", 3)[2]
        elif host == "youtu.be":
            video_id = parsed.path.strip("/").split("/", 1)[0]
        if not re.fullmatch(r"[A-Za-z0-9_-]{6,}", video_id):
            continue
        canonical = f"https://www.youtube.com/watch?v={video_id}"
        if canonical not in found:
            found.append(canonical)
    return found


def _normalized_match_text(value: str) -> str:
    return " ".join(re.sub(r"[^\w]+", " ", value.casefold()).split())


def _episode_number(value: str) -> int | None:
    match = re.search(r"\bep(?:isode)?\.?\s*#?\s*0*(\d+)\b", value, re.I)
    return int(match.group(1)) if match else None


def _youtube_candidate_matches(episode: Episode, candidate: dict[str, Any]) -> bool:
    title = str(candidate.get("title") or "")
    expected_number = _episode_number(episode.title)
    if expected_number is not None and _episode_number(title) != expected_number:
        return False

    title_score = SequenceMatcher(
        None,
        _normalized_match_text(episode.title),
        _normalized_match_text(title),
    ).ratio()
    if title_score < 0.75:
        return False

    expected_channel = _normalized_match_text(episode.feed_name)
    channel = _normalized_match_text(
        str(candidate.get("channel") or candidate.get("uploader") or "")
    )
    if not expected_channel or not channel:
        return False
    channel_score = SequenceMatcher(None, expected_channel, channel).ratio()
    if channel_score < 0.70:
        return False

    if episode.duration_seconds:
        try:
            duration = float(candidate.get("duration") or 0)
        except (TypeError, ValueError):
            return False
        tolerance = max(120.0, episode.duration_seconds * 0.10)
        if duration <= 0 or abs(duration - episode.duration_seconds) > tolerance:
            return False
    return True


def _youtube_metadata(url: str) -> dict[str, Any] | None:
    if not shutil.which("yt-dlp"):
        return None
    command = [
        "yt-dlp",
        "--no-playlist",
        "--skip-download",
        "--dump-single-json",
        url,
    ]
    result = subprocess.run(
        command,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=180,
    )
    if result.returncode:
        return None
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError:
        return None
    return payload if isinstance(payload, dict) else None


def _youtube_captions(url: str) -> Transcript | None:
    if not shutil.which("yt-dlp"):
        return None
    with tempfile.TemporaryDirectory(prefix="podcast-intel-youtube-") as temporary:
        output = str(Path(temporary) / "%(id)s.%(ext)s")
        command = [
            "yt-dlp",
            "--no-playlist",
            "--skip-download",
            "--write-subs",
            "--write-auto-subs",
            "--sub-langs",
            "en.*,en",
            "--sub-format",
            "json3/vtt/best",
            "--output",
            output,
            url,
        ]
        result = subprocess.run(
            command,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=300,
        )
        if result.returncode:
            return None
        files = sorted(
            (
                path
                for path in Path(temporary).iterdir()
                if path.suffix.casefold() in {".json3", ".json", ".vtt", ".srt"}
            ),
            key=lambda path: (
                0 if ".en." in path.name else 1,
                len(path.name),
                path.name,
            ),
        )
        for path in files:
            text = normalize_transcript(
                path.read_text(encoding="utf-8", errors="replace"),
                url=path.name,
            )
            if looks_like_transcript(text, direct=True):
                return Transcript(text=text, source="youtube_captions", source_url=url)
    return None


def _youtube_search_url(episode: Episode) -> str:
    if not shutil.which("yt-dlp"):
        return ""
    search_title = episode.title.split(" | ", 1)[0]
    query = f"ytsearch5:{search_title} {episode.feed_name}"
    command = [
        "yt-dlp",
        "--flat-playlist",
        "--dump-single-json",
        query,
    ]
    result = subprocess.run(
        command,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=180,
    )
    if result.returncode:
        return ""
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError:
        return ""

    candidates: list[tuple[float, str]] = []
    for item in payload.get("entries") or []:
        if not isinstance(item, dict):
            continue
        video_id = item.get("id")
        if not video_id:
            continue
        url = f"https://www.youtube.com/watch?v={video_id}"
        metadata = _youtube_metadata(url)
        if not metadata or str(metadata.get("id") or "") != str(video_id):
            continue
        if not _youtube_candidate_matches(episode, metadata):
            continue
        title = str(metadata.get("title") or "")
        title_score = SequenceMatcher(
            None,
            _normalized_match_text(episode.title),
            _normalized_match_text(title),
        ).ratio()
        candidates.append((title_score, url))
    if not candidates:
        return ""
    _, url = max(candidates)
    return url


def acquire_transcript(
    episode: Episode,
    *,
    timeout: int,
) -> Transcript:
    for candidate in sorted(episode.transcript_urls, key=_transcript_url_priority):
        transcript = _fetch_transcript_url(candidate["url"], timeout)
        if transcript:
            return transcript

    embedded = extract_transcript_section(episode.description_text)
    if has_transcript_heading(episode.description_text) and looks_like_transcript(
        embedded, direct=True
    ):
        return Transcript(
            text=embedded,
            source="rss_embedded_transcript",
            source_url=episode.link,
        )

    all_links = list(episode.web_links)
    page_text = ""
    if episode.link:
        try:
            page_html, content_type = fetch_text(episode.link, timeout)
            if "html" in content_type or "<html" in page_html[:1000].casefold():
                page_text, page_links = parse_html(page_html, episode.link)
                all_links.extend(page_links)
        except Exception:
            pass

    transcript_links = [
        link["url"]
        for link in all_links
        if "transcript" in f"{link.get('text', '')} {link.get('url', '')}".casefold()
    ]
    for url in dict.fromkeys(transcript_links):
        transcript = _fetch_transcript_url(url, timeout)
        if transcript:
            return transcript

    page_section = extract_transcript_section(page_text)
    if has_transcript_heading(page_text) and looks_like_transcript(
        page_section, direct=True
    ):
        return Transcript(
            text=page_section,
            source="episode_page_transcript",
            source_url=episode.link,
        )

    for youtube_url in _youtube_urls(all_links):
        metadata = _youtube_metadata(youtube_url)
        if not metadata or not _youtube_candidate_matches(episode, metadata):
            continue
        transcript = _youtube_captions(youtube_url)
        if transcript:
            return transcript

    searched_youtube_url = _youtube_search_url(episode)
    if searched_youtube_url:
        transcript = _youtube_captions(searched_youtube_url)
        if transcript:
            return transcript

    raise TranscriptUnavailable("no publisher transcript or YouTube captions found")
