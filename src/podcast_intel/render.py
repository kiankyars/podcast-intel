from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path
from typing import Any

from .models import Episode, Transcript


def slugify(value: str) -> str:
    value = value.casefold()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")[:90] or "episode"


def signal_time(value: Any) -> str:
    cleaned = str(value or "").strip().strip("[]()")
    return f" [{cleaned}]" if cleaned else ""


def episode_directory(root: Path, episode: Episode) -> Path:
    published = episode.published.date().isoformat()
    return root / "episodes" / published / f"{slugify(episode.title)}-{episode.id}"


def write_episode_artifacts(
    root: Path,
    episode: Episode,
    transcript: Transcript,
    analysis: dict[str, Any],
) -> dict[str, str]:
    paths = write_transcript_artifact(root, episode, transcript)
    directory = episode_directory(root, episode)
    analysis_path = directory / "analysis.json"
    summary_path = directory / "summary.md"
    analysis_path.write_text(
        json.dumps(analysis, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    summary_path.write_text(
        render_episode_summary(episode, analysis),
        encoding="utf-8",
    )
    return paths | {
        "analysis": str(analysis_path),
        "summary": str(summary_path),
    }


def write_transcript_artifact(
    root: Path,
    episode: Episode,
    transcript: Transcript,
) -> dict[str, str]:
    directory = episode_directory(root, episode)
    directory.mkdir(parents=True, exist_ok=True)
    metadata_path = directory / "metadata.json"
    transcript_path = directory / "transcript.md"
    raw_path = directory / "transcript.txt"
    metadata = episode.to_dict()
    metadata["transcript_source"] = transcript.source
    metadata["transcript_source_url"] = transcript.source_url
    metadata_path.write_text(
        json.dumps(metadata, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    raw_path.write_text(transcript.text.rstrip() + "\n", encoding="utf-8")
    transcript_path.write_text(
        "\n".join(
            (
                f"# {episode.title}",
                "",
                f"- Podcast: {episode.feed_name}",
                f"- Published: {episode.published.date().isoformat()}",
                f"- Episode: {episode.link}",
                f"- Transcript source: {transcript.source}",
                f"- Transcript URL: {transcript.source_url}",
                "",
                "## Transcript",
                "",
                transcript.text,
                "",
            )
        ),
        encoding="utf-8",
    )
    return {
        "directory": str(directory),
        "metadata": str(metadata_path),
        "transcript": str(transcript_path),
        "raw_transcript": str(raw_path),
    }


def render_episode_summary(episode: Episode, analysis: dict[str, Any]) -> str:
    lines = [
        f"# {episode.title}",
        "",
        f"- Podcast: {episode.feed_name}",
        f"- Published: {episode.published.date().isoformat()}",
        f"- Source: {episode.link}",
        f"- Relevance: {analysis['relevance_score']}/5",
        "",
        analysis["summary"],
        "",
        f"**Why it matters:** {analysis['why_it_matters']}",
        "",
        "## Signals",
        "",
    ]
    for signal in analysis.get("signals", []):
        time = signal_time(signal.get("timestamp"))
        lines.append(
            f"- **{signal['claim']}**{time} "
            f"_{signal['category']}; {signal['kind']}; {signal['confidence']} confidence._ "
            f"{signal['evidence']}"
        )
    if analysis.get("changed_views"):
        lines.extend(("", "## Changed Views Or Tensions", ""))
        lines.extend(f"- {item}" for item in analysis["changed_views"])
    if analysis.get("follow_ups"):
        lines.extend(("", "## Follow-Ups", ""))
        lines.extend(f"- {item}" for item in analysis["follow_ups"])
    return "\n".join(lines).rstrip() + "\n"


def update_topics(
    root: Path,
    episode: Episode,
    analysis: dict[str, Any],
    categories: dict[str, str],
) -> None:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for signal in analysis.get("signals", []):
        grouped.setdefault(signal["category"], []).append(signal)
    for category, signals in grouped.items():
        path = root / "topics" / f"{category}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        marker = f"<!-- episode:{episode.id} -->"
        existing = path.read_text(encoding="utf-8") if path.exists() else ""
        if marker in existing:
            continue
        if not existing:
            existing = (
                f"# {category.replace('_', ' ').title()}\n\n"
                f"{categories.get(category, '')}\n"
            )
        block = [
            "",
            marker,
            f"## {episode.published.date().isoformat()} - [{episode.title}]({episode.link})",
            "",
        ]
        for signal in signals:
            time = signal_time(signal.get("timestamp"))
            block.append(f"- **{signal['claim']}**{time} {signal['evidence']}")
        path.write_text(existing.rstrip() + "\n" + "\n".join(block) + "\n", encoding="utf-8")


def write_daily_digest(
    root: Path,
    run_date: date,
    relevant: list[tuple[Episode, dict[str, Any]]],
    *,
    processed_count: int,
    skipped_count: int,
    failed_feeds: list[str],
    failed_episodes: list[str],
) -> Path:
    run_date_text = run_date.isoformat()
    path = root / "digests" / f"{run_date_text}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    sorted_relevant = sorted(
        relevant,
        key=lambda item: (
            int(item[1]["relevance_score"]),
            item[0].feed_priority,
            item[0].published,
        ),
        reverse=True,
    )
    lines = [
        "---",
        "layout: default",
        (
            "title: "
            + json.dumps(
                f"Podcast Intelligence - {run_date_text}",
                ensure_ascii=False,
            )
        ),
        "digest: true",
        f"date: {run_date_text}",
        f"permalink: /{run_date_text}/",
        "---",
        "",
        f"# {run_date_text}",
        "",
        (
            f"Processed {processed_count} episode(s); retained {len(relevant)}; "
            f"filtered {skipped_count}."
        ),
        "",
    ]
    all_signals: list[tuple[int, Episode, dict[str, Any]]] = []
    for episode, analysis in relevant:
        for signal in analysis.get("signals", []):
            all_signals.append((int(analysis["relevance_score"]), episode, signal))
    all_signals.sort(key=lambda item: (item[0], item[1].feed_priority), reverse=True)

    lines.extend(("## TL;DR", ""))
    for _, episode, signal in all_signals[:3]:
        time = signal_time(signal.get("timestamp"))
        lines.append(
            f"- **{signal['claim']}**{time} "
            f"([{episode.feed_name}]({episode.link})). {signal['evidence']}"
        )
    if not all_signals:
        lines.append("- No retained signals.")

    if len(all_signals) > 3:
        lines.extend(("", "## More findings", ""))
        for _, episode, signal in all_signals[3:10]:
            time = signal_time(signal.get("timestamp"))
            lines.append(
                f"- **{signal['claim']}**{time} "
                f"([{episode.feed_name}]({episode.link})). {signal['evidence']}"
            )

    lines.extend(("", "## Episodes", ""))
    for episode, analysis in sorted_relevant:
        lines.extend(
            (
                f"### [{episode.title}]({episode.link})",
                "",
                f"**{episode.feed_name} | relevance {analysis['relevance_score']}/5**",
                "",
                analysis["summary"],
                "",
                f"**Why it matters:** {analysis['why_it_matters']}",
                "",
            )
        )
    if failed_feeds or failed_episodes:
        lines.extend(("## Failures", ""))
        lines.extend(f"- Feed: {failure}" for failure in failed_feeds)
        lines.extend(f"- Episode: {failure}" for failure in failed_episodes)
        lines.append("")

    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return path
