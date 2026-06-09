from __future__ import annotations

import hashlib
import html
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from urllib.parse import urljoin

from .models import Episode, FeedConfig


USER_AGENT = "podcast-intel/0.1 (+local research workflow)"
BLOCK_TAGS = {
    "article",
    "blockquote",
    "br",
    "div",
    "h1",
    "h2",
    "h3",
    "h4",
    "li",
    "p",
    "pre",
    "section",
}


class HTMLDocumentParser(HTMLParser):
    def __init__(self, base_url: str = ""):
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.parts: list[str] = []
        self.links: list[dict[str, str]] = []
        self.skip_depth = 0
        self.anchor_href = ""
        self.anchor_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag in {"script", "style", "svg", "noscript"}:
            self.skip_depth += 1
        if tag in BLOCK_TAGS:
            self.parts.append("\n")
        if tag == "a":
            self.anchor_href = urljoin(self.base_url, attributes.get("href") or "")
            self.anchor_parts = []

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "svg", "noscript"} and self.skip_depth:
            self.skip_depth -= 1
        if tag in BLOCK_TAGS:
            self.parts.append("\n")
        if tag == "a" and self.anchor_href:
            text = " ".join(" ".join(self.anchor_parts).split())
            self.links.append({"text": text, "url": self.anchor_href})
            self.anchor_href = ""
            self.anchor_parts = []

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        value = " ".join(data.split())
        if not value:
            return
        self.parts.append(value)
        if self.anchor_href:
            self.anchor_parts.append(value)

    def text(self) -> str:
        value = " ".join(self.parts)
        value = re.sub(r" *\n *", "\n", value)
        value = re.sub(r"\n{3,}", "\n\n", value)
        return value.strip()


def parse_html(value: str, base_url: str = "") -> tuple[str, list[dict[str, str]]]:
    parser = HTMLDocumentParser(base_url)
    parser.feed(html.unescape(value or ""))
    return parser.text(), parser.links


def fetch_bytes(url: str, timeout: int) -> tuple[bytes, str]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept-Encoding": "identity",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read(), response.headers.get_content_type()


def fetch_text(url: str, timeout: int) -> tuple[str, str]:
    body, content_type = fetch_bytes(url, timeout)
    return body.decode("utf-8", errors="replace"), content_type


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].casefold()


def _child_text(item: ET.Element, names: set[str]) -> str:
    for child in item:
        if _local_name(child.tag) in names and child.text:
            return child.text.strip()
    return ""


def _parse_date(value: str) -> datetime:
    if not value:
        return datetime.now(timezone.utc)
    try:
        parsed = parsedate_to_datetime(value)
    except (TypeError, ValueError):
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _parse_duration(value: str) -> int:
    if not value:
        return 0
    value = value.strip()
    if value.isdigit():
        return int(value)
    pieces = value.split(":")
    try:
        numbers = [int(float(piece)) for piece in pieces]
    except ValueError:
        return 0
    total = 0
    for number in numbers:
        total = total * 60 + number
    return total


def _episode_id(feed_id: str, guid: str, link: str, title: str) -> str:
    stable = "\n".join((feed_id, guid or link or title))
    return hashlib.sha256(stable.encode("utf-8")).hexdigest()[:20]


def parse_feed(xml_text: str, feed: FeedConfig) -> list[Episode]:
    root = ET.fromstring(xml_text)
    items = [
        element
        for element in root.iter()
        if _local_name(element.tag) in {"item", "entry"}
    ]
    episodes: list[Episode] = []
    for item in items:
        title = _child_text(item, {"title"})
        description_html = _child_text(
            item, {"description", "summary", "encoded", "content"}
        )
        link = _child_text(item, {"link"})
        guid = _child_text(item, {"guid", "id"})
        published = _parse_date(
            _child_text(item, {"pubdate", "published", "updated"})
        )
        duration = _parse_duration(_child_text(item, {"duration"}))
        audio_url = ""
        transcript_urls: list[dict[str, str]] = []
        for child in item:
            local = _local_name(child.tag)
            if local == "link" and not link:
                link = child.attrib.get("href", "")
            elif local == "enclosure":
                audio_url = child.attrib.get("url", "")
            elif local == "transcript":
                transcript_url = child.attrib.get("url", "")
                if transcript_url:
                    transcript_urls.append(
                        {
                            "url": transcript_url,
                            "type": child.attrib.get("type", ""),
                            "rel": child.attrib.get("rel", ""),
                        }
                    )
        description_text, web_links = parse_html(description_html, link)
        if not title:
            continue
        episodes.append(
            Episode(
                id=_episode_id(feed.id, guid, link, title),
                feed_id=feed.id,
                feed_name=feed.name,
                feed_priority=feed.priority,
                title=title,
                description_html=description_html,
                description_text=description_text,
                published=published,
                duration_seconds=duration,
                link=link,
                audio_url=audio_url,
                transcript_urls=transcript_urls,
                web_links=web_links,
            )
        )
    return episodes


def fetch_feed(feed: FeedConfig, timeout: int) -> list[Episode]:
    xml_text, _ = fetch_text(feed.url, timeout)
    return parse_feed(xml_text, feed)


def metadata_matches(
    episode: Episode,
    feed: FeedConfig,
    keywords: tuple[str, ...],
) -> bool:
    title_folded = episode.title.casefold()
    if any(pattern.casefold() in title_folded for pattern in feed.exclude_title_patterns):
        return False
    if feed.mode == "all":
        return True
    if feed.mode == "title_filtered":
        haystack = episode.title.casefold()
    else:
        haystack = f"{episode.title}\n{episode.description_text}".casefold()
    return any(keyword in haystack for keyword in keywords)
