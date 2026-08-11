#!/usr/bin/env python3
import json
import re
import subprocess
import textwrap
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path


VIDEOS = [
    {
        "date": "2026-04-17",
        "id": "Eda9A_oWOlo",
        "title": "Ep. 009 - Using Open Source Data To Drive Investment Decisions (ChipBook)",
        "channel": "SemiAnalysis Weekly",
        "duration": "53:22",
    },
    {
        "date": "2026-01-15",
        "id": "QHueG_5DvSw",
        "title": 'Dylan Patel: Is the "Low Hanging Fruit" in AI Gone?',
        "channel": "SAIL Media",
        "duration": "14:01",
    },
    {
        "date": "2026-02-03",
        "id": "EvBddHMCFNk",
        "title": "FULL INTERVIEW: Dylan Patel Says We're Still Underestimating AI",
        "channel": "TBPN",
        "duration": "43:42",
    },
    {
        "date": "2026-02-05",
        "id": "DqBMzuzxZog",
        "title": 'Dylan Patel: NVIDIA\'s New Moat & Why China is "Semiconductor Pilled"',
        "channel": "The MAD Podcast with Matt Turck",
        "duration": "1:16:51",
    },
    {
        "date": "2026-02-26",
        "id": "UwnqWAYOjPU",
        "title": "Dylan Patel Explains the AI War While Cooking | In-Context Cooking",
        "channel": "Latent Space",
        "duration": "55:12",
    },
    {
        "date": "2026-03-09",
        "id": "E5B0cS6XRkg",
        "title": "Dylan Patel: AI in War, Jobs are Cooked, Chinese Hacking, Microsoft Cope, and Super Intelligence",
        "channel": "Matthew Berman",
        "duration": "1:29:32",
    },
    {
        "date": "2026-03-13",
        "id": "mDG_Hx3BSUE",
        "title": "Dylan Patel - The single biggest bottleneck to scaling AI compute",
        "channel": "Dwarkesh Patel",
        "duration": "2:30:44",
    },
    {
        "date": "2026-04-07",
        "id": "c88l8daXiv4",
        "title": "Dylan Patel (SemiAnalysis): The Datacenter in 2026: CPUs, RL Environments & Agent-Driven Workloads",
        "channel": "Daytona",
        "duration": "25:04",
    },
    {
        "date": "2026-04-20",
        "id": "zrMYIhmuXEo",
        "title": "Hardware-software codesign, with Clive Chan, Dylan Patel and Reiner Pope",
        "channel": "MatX",
        "duration": "30:58",
    },
    {
        "date": "2026-04-23",
        "id": "LF3aUIM57uw",
        "title": "The Supply and Demand of AI Tokens | Dylan Patel Interview",
        "channel": "Invest Like The Best",
        "duration": "45:33",
    },
    {
        "date": "2026-05-06",
        "id": "semianalysis-weekly-ep011-2026-05-06",
        "title": "Ep. 011 - GPT 5.5 vs Claude 4.7: OpenAI's Comeback From the Brink (Tokenomics)",
        "channel": "SemiAnalysis Weekly",
        "duration": "45:06",
        "note": "Supplemental May 2026 SemiAnalysis Weekly episode requested by user; public transcript unavailable, so this transcript was generated from episode audio.",
        "source_url": "https://podcasters.spotify.com/pod/show/jordan-nanos/episodes/Ep--011---GPT-5-5-vs-Claude-4-7-OpenAIs-Comeback-From-the-Brink-Tokenomics--Jordan-Nanos--Dylan-Patel--Doug-OLaughlin--Max-Kan-e3iuqlr",
        "audio_url": "https://anchor.fm/s/10fbee758/podcast/play/119548027/https%3A%2F%2Fd3ctxlq1ktw2nl.cloudfront.net%2Fstaging%2F2026-4-5%2F423557178-44100-2-f70a26217ac4b.mp3",
        "source_tool": "MLX Whisper large-v3-turbo audio transcription from downloaded episode audio",
    },
    {
        "date": "2025-09-22",
        "id": "vvlE8-MzxyA",
        "title": "Dylan Patel on the AI Chip Race - NVIDIA, Intel & the US Government vs. China",
        "channel": "a16z",
        "duration": "1:38:58",
        "note": "Supplemental non-2026 episode added for the Nvidia/hyperscaler cash-flow discussion.",
        "source_url": "https://www.a16z.news/p/dylan-patel-on-the-ai-chip-race-nvidia",
        "source_tool": "a16z transcript page",
    },
    {
        "date": "2025-09-30",
        "id": "kAIVualeQjM",
        "title": "Inside the Trillion-Dollar AI Buildout | Dylan Patel Interview",
        "channel": "Invest Like The Best",
        "duration": "2:02:22",
        "note": "Supplemental non-2026 episode requested by user.",
    },
    {
        "date": "2025-08-15",
        "id": "TIGZdRqi7Ec",
        "title": "Dylan Patel | Lost in Life to Founding SemiAnalysis",
        "channel": "Yesterday Podcast",
        "duration": "1:34:57",
        "note": "Supplemental non-2026 episode requested by user; public YouTube captions and Apple/RSS transcripts were unavailable, so this transcript was generated from episode audio.",
        "source_url": "https://yesterdayy.substack.com/p/dylan-patellost-in-life-to-founding",
        "youtube_url": "https://www.youtube.com/watch?v=TIGZdRqi7Ec",
        "source_tool": "OpenAI whisper-1 audio transcription from downloaded episode audio",
    },
]

SKIPPED = [
    {
        "id": "HHmGbwA9dBY",
        "reason": "short event excerpt, not a podcast/interview episode",
        "title": "ClusterMax, InferenceMax & the Token Efficiency Race | Dylan Patel at Aria Networks Launch",
    },
    {
        "id": "LgMW96b6Ieg",
        "reason": "short CNBC TV segment, not a podcast episode",
        "title": "Nvidia CEO laying the foundation for regular enterprises to deploy AI: SemiAnalysis CEO Dylan Patel",
    },
    {
        "id": "1WIZNbmIOJw",
        "reason": "clip from Dwarkesh episode already included",
        "title": "How an H100 is worth more today than it was three years ago - Dylan Patel",
    },
    {
        "id": "_fUsvXs2mMA",
        "reason": "reupload of Invest Like The Best episode already included",
        "title": "The Supply and Demand of AI Tokens | Dylan Patel Interview",
    },
    {
        "id": "ON0ORL8BirQ",
        "reason": "summary of a 2025 Lex Fridman episode, not a 2026 original Dylan Patel podcast",
        "title": "Lex Fridman Podcast Summary: Dylan Patel & Nathan Lambert on the AI Arms Race",
    },
]


def slugify(value):
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")[:90]


def timestamp(seconds):
    total = int(float(seconds))
    hours, rem = divmod(total, 3600)
    minutes, secs = divmod(rem, 60)
    if hours:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


class TranscriptHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "svg"):
            self.skip += 1
        if tag in ("p", "h1", "h2", "h3", "h4", "li", "br", "div"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style", "svg") and self.skip:
            self.skip -= 1
        if tag in ("p", "h1", "h2", "h3", "h4", "li", "div"):
            self.parts.append("\n")

    def handle_data(self, data):
        if self.skip:
            return
        text = " ".join(data.split())
        if text:
            self.parts.append(text)

    def text(self):
        return "\n".join(part for part in self.parts if part.strip())


def stem_for(video):
    return f'{video["date"]}-{slugify(video["title"])}-{video["id"]}'


def cached_transcript(base, video):
    matches = sorted((base / "transcripts").glob(f"*{video['id']}.json"))
    if not matches:
        return None
    payload = json.loads(matches[0].read_text())
    return payload["transcript"]


def fetch_a16z_transcript(video):
    request = urllib.request.Request(
        video["source_url"],
        headers={"User-Agent": "Mozilla/5.0"},
    )
    with urllib.request.urlopen(request) as response:
        html = response.read().decode("utf-8", errors="ignore")
    parser = TranscriptHTMLParser()
    parser.feed(html)
    text = parser.text()
    start = text.index("Transcript:")
    transcript = text[start:].splitlines()
    cleaned = []
    last_time = 0
    timecode = re.compile(r"^(\d{2}):(\d{2}):(\d{2})\s+(.+)$")
    for line in transcript:
        line = line.strip()
        if not line or line in {"Transcript:", "This transcript has been edited lightly for readability."}:
            continue
        match = timecode.match(line)
        if match:
            hours, minutes, seconds, title = match.groups()
            last_time = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
            cleaned.append({"text": title, "start": last_time, "duration": 0})
        else:
            cleaned.append({"text": line, "start": last_time, "duration": 0})
    return cleaned


def fetch(video):
    if video.get("source_tool") == "a16z transcript page":
        return fetch_a16z_transcript(video)
    if "audio transcription" in video.get("source_tool", ""):
        raise RuntimeError(
            "cached audio-derived transcript missing; regenerate it with "
            "scripts/transcribe_dylan_patel_audio_openai.py"
        )

    result = subprocess.run(
        [
            "uv",
            "tool",
            "run",
            "youtube_transcript_api",
            "--languages",
            "en",
            "--format",
            "json",
        video["id"],
        ],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    parsed = json.loads(result.stdout)
    if len(parsed) != 1:
        raise ValueError(f"expected one transcript for {video['id']}, got {len(parsed)}")
    return parsed[0]


def write_outputs(base, video, transcript):
    stem = stem_for(video)
    json_path = base / "transcripts" / f"{stem}.json"
    md_path = base / "transcripts" / f"{stem}.md"

    payload = {
        "metadata": {
            **video,
            "url": video.get("source_url", f'https://www.youtube.com/watch?v={video["id"]}'),
            "fetched_at": datetime.now(timezone.utc).isoformat(),
            "source_tool": video.get("source_tool", "uv tool run youtube_transcript_api"),
            "language_preference": ["en"],
        },
        "transcript": transcript,
    }
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")

    lines = [
        f"# {video['title']}",
        "",
        f"- Date: {video['date']}",
        f"- Channel: {video['channel']}",
        f"- Duration: {video['duration']}",
        f"- URL: {video.get('source_url', f'https://www.youtube.com/watch?v={video['id']}')}",
        f"- Source: `{video.get('source_tool', f'uv tool run youtube_transcript_api --languages en --format json {video['id']}')}`",
        "- Note: timestamps are preserved in the paired JSON file.",
        "",
        "## Transcript",
        "",
    ]
    paragraphs = []
    buffer = []
    last_end = None
    for item in transcript:
        text = " ".join(item["text"].replace("\u00a0", " ").split())
        if not text:
            continue
        start = float(item.get("start", 0) or 0)
        duration = float(item.get("duration", 0) or 0)
        gap = 0 if last_end is None else start - last_end
        should_break = (
            gap > 3.5
            or text.startswith(">>")
            or (buffer and re.search(r"[.!?]$", buffer[-1]) and len(" ".join(buffer)) > 450)
        )
        if should_break and buffer:
            paragraphs.append(" ".join(buffer))
            buffer = []
        buffer.append(text)
        last_end = start + duration
    if buffer:
        paragraphs.append(" ".join(buffer))

    for paragraph in paragraphs:
        lines.append(textwrap.fill(paragraph, width=100))
        lines.append("")
    md_path.write_text("\n".join(lines) + "\n")

    return {
        **video,
        "url": video.get("source_url", f'https://www.youtube.com/watch?v={video["id"]}'),
        "json": str(json_path.relative_to(base)),
        "markdown": str(md_path.relative_to(base)),
        "segments": len(transcript),
    }


def main():
    base = Path(__file__).resolve().parents[1]
    (base / "transcripts").mkdir(exist_ok=True)

    indexed = []
    failures = []
    for video in VIDEOS:
        try:
            transcript = cached_transcript(base, video) or fetch(video)
            indexed.append(write_outputs(base, video, transcript))
            print(f"ok {video['id']} {len(transcript)} segments")
        except Exception as exc:
            failures.append({**video, "error": str(exc)})
            print(f"fail {video['id']}: {exc}")

    index = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "path_base": "repository_root",
        "selection_rule": "Original 2026 YouTube podcast/interview/conversation episodes featuring Dylan Patel, plus supplemental 2025 a16z and Yesterday Podcast episodes requested by the user; clips, reuploads, summaries, and short TV/event excerpts were skipped.",
        "source_discovery": [
            "yt-dlp metadata searches for Dylan Patel and Dylan Patel SemiAnalysis podcast",
            "web search cross-checks for Dwarkesh, Daytona, TBPN, and podcast index pages",
        ],
        "transcript_source": "uv tool run youtube_transcript_api, publisher transcript pages, or audio transcription where captions were unavailable",
        "videos": indexed,
        "skipped_candidates": SKIPPED,
        "failures": failures,
    }
    manifest_dir = base / "manifests"
    manifest_dir.mkdir(exist_ok=True)
    (manifest_dir / "dylan-patel-transcripts.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n"
    )

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
