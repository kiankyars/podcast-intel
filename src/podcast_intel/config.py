from __future__ import annotations

import tomllib
from pathlib import Path

from .models import AppConfig, FeedConfig, RunConfig


def load_config(path: Path) -> AppConfig:
    raw = tomllib.loads(path.read_text(encoding="utf-8"))
    run_raw = raw["run"]
    run = RunConfig(
        lookback_days=int(run_raw["lookback_days"]),
        max_episodes=int(run_raw["max_episodes"]),
        max_total_hours=float(run_raw["max_total_hours"]),
        min_relevance_score=int(run_raw["min_relevance_score"]),
        request_timeout_seconds=int(run_raw["request_timeout_seconds"]),
        max_transcript_chars=int(run_raw["max_transcript_chars"]),
    )
    feeds = tuple(
        FeedConfig(
            id=str(item["id"]),
            name=str(item["name"]),
            url=str(item["url"]),
            mode=str(item.get("mode", "filtered")),
            priority=int(item.get("priority", 0)),
            exclude_title_patterns=tuple(item.get("exclude_title_patterns", [])),
        )
        for item in raw.get("feeds", [])
    )
    keywords = tuple(
        keyword.casefold() for keyword in raw.get("selection", {}).get("keywords", [])
    )
    categories = {
        str(key): str(value) for key, value in raw.get("categories", {}).items()
    }
    if not feeds:
        raise ValueError("config.toml must contain at least one [[feeds]] entry")
    if not categories:
        raise ValueError("config.toml must define [categories]")
    return AppConfig(run=run, feeds=feeds, keywords=keywords, categories=categories)
