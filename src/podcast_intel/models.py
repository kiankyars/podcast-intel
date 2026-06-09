from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Any


@dataclass(frozen=True)
class FeedConfig:
    id: str
    name: str
    url: str
    mode: str = "filtered"
    priority: int = 0
    exclude_title_patterns: tuple[str, ...] = ()


@dataclass(frozen=True)
class RunConfig:
    lookback_days: int
    max_episodes: int
    max_audio_hours: float
    min_relevance_score: int
    transcribe_missing: bool
    keep_audio: bool
    request_timeout_seconds: int
    max_transcript_chars: int
    analysis_provider: str
    codex_model: str
    whisper_model: str


@dataclass(frozen=True)
class AppConfig:
    run: RunConfig
    feeds: tuple[FeedConfig, ...]
    keywords: tuple[str, ...]
    categories: dict[str, str]


@dataclass
class Episode:
    id: str
    feed_id: str
    feed_name: str
    feed_priority: int
    title: str
    description_html: str
    description_text: str
    published: datetime
    duration_seconds: int
    link: str
    audio_url: str
    transcript_urls: list[dict[str, str]] = field(default_factory=list)
    web_links: list[dict[str, str]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["published"] = self.published.isoformat()
        return payload


@dataclass(frozen=True)
class Transcript:
    text: str
    source: str
    source_url: str


@dataclass
class RunResult:
    discovered: int = 0
    selected: int = 0
    processed: int = 0
    relevant: int = 0
    skipped: int = 0
    failed_feeds: list[str] = field(default_factory=list)
    failed_episodes: list[str] = field(default_factory=list)
    digest_path: str = ""

