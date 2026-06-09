from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Callable

from .analyze import AnalysisError, analyze_episode
from .config import load_config
from .feeds import fetch_feed, metadata_matches
from .models import AppConfig, Episode, RunResult, Transcript
from .render import (
    update_topics,
    write_daily_digest,
    write_episode_artifacts,
    write_transcript_artifact,
)
from .state import State
from .transcripts import (
    TranscriptUnavailable,
    TranscriberUnavailable,
    acquire_transcript,
)


ROOT = Path(__file__).resolve().parents[2]


def _load(root: Path) -> tuple[AppConfig, str, State]:
    config = load_config(root / "config.toml")
    profile = (root / "profile.md").read_text(encoding="utf-8")
    state = State(root / "data" / "state.json")
    state.prune_discovered()
    return config, profile, state


def discover(
    config: AppConfig,
    feed_ids: set[str] | None = None,
) -> tuple[list[Episode], list[str]]:
    episodes: list[Episode] = []
    failures: list[str] = []
    for feed in config.feeds:
        if feed_ids and feed.id not in feed_ids:
            continue
        try:
            fetched = fetch_feed(feed, config.run.request_timeout_seconds)
            episodes.extend(fetched)
        except Exception as error:
            failures.append(f"{feed.name}: {type(error).__name__}: {error}")
    return episodes, failures


def _candidate_episodes(
    *,
    config: AppConfig,
    episodes: list[Episode],
    state: State,
    lookback_days: int,
    max_episodes: int,
) -> tuple[list[Episode], int]:
    since = datetime.now(timezone.utc) - timedelta(days=lookback_days)
    feeds = {feed.id: feed for feed in config.feeds}
    candidates: list[Episode] = []
    skipped = 0
    for episode in episodes:
        status = state.status(episode.id)
        if status == "processed":
            continue
        retryable = status in {
            "retry",
            "transcript_ready",
            "analysis_error",
            "transcript_error",
        }
        if episode.published < since and not retryable:
            continue
        feed = feeds[episode.feed_id]
        if not metadata_matches(episode, feed, config.keywords):
            state.update(episode.id, status="metadata_skipped")
            skipped += 1
            continue
        candidates.append(episode)

    candidates.sort(
        key=lambda item: (item.feed_priority, item.published),
        reverse=True,
    )
    selected: list[Episode] = []
    total_seconds = 0
    maximum_seconds = int(config.run.max_audio_hours * 3600)
    for episode in candidates:
        estimated = episode.duration_seconds or 3600
        if selected and total_seconds + estimated > maximum_seconds:
            continue
        selected.append(episode)
        total_seconds += estimated
        if len(selected) >= max_episodes:
            break
    return selected, skipped


def _cached_transcript(state: State, episode: Episode) -> Transcript | None:
    record = state.get(episode.id)
    raw_path = record.get("raw_transcript")
    if not raw_path:
        return None
    path = Path(raw_path)
    if not path.exists():
        return None
    return Transcript(
        text=path.read_text(encoding="utf-8"),
        source=str(record.get("transcript_source", "cached")),
        source_url=str(record.get("transcript_source_url", episode.link)),
    )


def run_pipeline(
    *,
    root: Path = ROOT,
    lookback_days: int | None = None,
    max_episodes: int | None = None,
    transcribe_missing: bool | None = None,
    feed_ids: set[str] | None = None,
    analyzer: Callable[..., dict] = analyze_episode,
    transcript_acquirer: Callable[..., Transcript] = acquire_transcript,
) -> RunResult:
    config, profile, state = _load(root)
    result = RunResult()
    episodes, failures = discover(config, feed_ids)
    result.discovered = len(episodes)
    result.failed_feeds.extend(failures)

    selected, metadata_skipped = _candidate_episodes(
        config=config,
        episodes=episodes,
        state=state,
        lookback_days=lookback_days or config.run.lookback_days,
        max_episodes=max_episodes or config.run.max_episodes,
    )
    result.selected = len(selected)
    result.skipped = metadata_skipped
    relevant: list[tuple[Episode, dict]] = []

    for episode in selected:
        print(f"PROCESS {episode.feed_name}: {episode.title}", flush=True)
        transcript = _cached_transcript(state, episode)
        if not transcript:
            try:
                transcript = transcript_acquirer(
                    episode,
                    timeout=config.run.request_timeout_seconds,
                    transcribe_missing=(
                        config.run.transcribe_missing
                        if transcribe_missing is None
                        else transcribe_missing
                    ),
                    cache_dir=root / "data" / "cache" / "audio",
                    whisper_model=config.run.whisper_model,
                    keep_audio=config.run.keep_audio,
                )
                paths = write_transcript_artifact(root, episode, transcript)
                state.update(
                    episode.id,
                    status="transcript_ready",
                    raw_transcript=paths["raw_transcript"],
                    transcript_path=paths["transcript"],
                    transcript_source=transcript.source,
                    transcript_source_url=transcript.source_url,
                )
            except (TranscriptUnavailable, TranscriberUnavailable, Exception) as error:
                message = (
                    f"{episode.feed_name} / {episode.title}: "
                    f"{type(error).__name__}: {error}"
                )
                result.failed_episodes.append(message)
                state.update(episode.id, status="transcript_error", error=message)
                continue

        try:
            if config.run.analysis_provider != "codex":
                raise AnalysisError(
                    f"unsupported analysis provider: {config.run.analysis_provider}"
                )
            analysis = analyzer(
                root=root,
                episode=episode,
                transcript=transcript.text,
                profile=profile,
                categories=config.categories,
                max_transcript_chars=config.run.max_transcript_chars,
                model=config.run.codex_model,
            )
            paths = write_episode_artifacts(root, episode, transcript, analysis)
            score = int(analysis["relevance_score"])
            if score >= config.run.min_relevance_score:
                update_topics(root, episode, analysis, config.categories)
            state.update(
                episode.id,
                status="processed",
                relevance_score=score,
                analysis_path=paths["analysis"],
                summary_path=paths["summary"],
                error="",
            )
            result.processed += 1
            if score >= config.run.min_relevance_score:
                relevant.append((episode, analysis))
                result.relevant += 1
            else:
                result.skipped += 1
        except Exception as error:
            message = (
                f"{episode.feed_name} / {episode.title}: "
                f"{type(error).__name__}: {error}"
            )
            result.failed_episodes.append(message)
            state.update(episode.id, status="analysis_error", error=message)

    if relevant or result.failed_feeds or result.failed_episodes:
        digest = write_daily_digest(
            root,
            datetime.now().astimezone().date(),
            relevant,
            processed_count=result.processed,
            skipped_count=result.skipped,
            failed_feeds=result.failed_feeds,
            failed_episodes=result.failed_episodes,
        )
        result.digest_path = str(digest)
    return result


def _print_run_result(result: RunResult) -> None:
    if not result.relevant and not result.failed_feeds and not result.failed_episodes:
        print(
            "NO_NEW_RELEVANT_EPISODES "
            f"discovered={result.discovered} selected={result.selected} "
            f"processed={result.processed} filtered={result.skipped}"
        )
        return
    status = "RUN_COMPLETED"
    if result.failed_feeds or result.failed_episodes:
        status = "RUN_COMPLETED_WITH_FAILURES"
    print(
        f"{status} digest={result.digest_path} relevant={result.relevant} "
        f"processed={result.processed} feed_failures={len(result.failed_feeds)} "
        f"episode_failures={len(result.failed_episodes)}"
    )
    for failure in result.failed_feeds:
        print(f"FEED_FAILURE {failure}")
    for failure in result.failed_episodes:
        print(f"EPISODE_FAILURE {failure}")


def command_run(args: argparse.Namespace) -> int:
    result = run_pipeline(
        lookback_days=args.lookback,
        max_episodes=args.max_episodes,
        transcribe_missing=False if args.no_transcribe else None,
        feed_ids=set(args.feed) if args.feed else None,
    )
    _print_run_result(result)
    return 0 if not result.failed_feeds and not result.failed_episodes else 1


def command_discover(args: argparse.Namespace) -> int:
    config, _, _ = _load(ROOT)
    episodes, failures = discover(
        config,
        feed_ids=set(args.feed) if args.feed else None,
    )
    since = datetime.now(timezone.utc) - timedelta(
        days=args.lookback or config.run.lookback_days
    )
    feeds = {feed.id: feed for feed in config.feeds}
    recent = [episode for episode in episodes if episode.published >= since]
    recent.sort(key=lambda item: item.published, reverse=True)
    for episode in recent:
        selected = metadata_matches(episode, feeds[episode.feed_id], config.keywords)
        duration = (
            f"{episode.duration_seconds / 60:.0f}m"
            if episode.duration_seconds
            else "unknown"
        )
        print(
            f"{'SELECT' if selected else 'SKIP  '} "
            f"{episode.published.date()} {duration:>7} "
            f"{episode.feed_name}: {episode.title}"
        )
    for failure in failures:
        print(f"FEED_FAILURE {failure}", file=sys.stderr)
    return 0 if not failures else 1


def command_doctor(_: argparse.Namespace) -> int:
    config, _, _ = _load(ROOT)
    checks = {
        "python": sys.version.split()[0],
        "codex": shutil.which("codex") or "missing",
        "yt-dlp": shutil.which("yt-dlp") or "missing",
        "ffmpeg": shutil.which("ffmpeg") or "missing",
        "mlx-whisper": (
            "installed" if importlib.util.find_spec("mlx_whisper") else "missing (optional)"
        ),
        "feeds": str(len(config.feeds)),
        "analysis_provider": config.run.analysis_provider,
    }
    print(json.dumps(checks, indent=2))
    required_missing = checks["codex"] == "missing" or checks["yt-dlp"] == "missing"
    return 1 if required_missing else 0


def command_retry(args: argparse.Namespace) -> int:
    _, _, state = _load(ROOT)
    record = state.get(args.episode_id)
    if not record:
        print(f"unknown episode id: {args.episode_id}", file=sys.stderr)
        return 1
    state.update(
        args.episode_id,
        status="retry",
        raw_transcript="",
        transcript_path="",
        transcript_source="",
        transcript_source_url="",
        analysis_path="",
        summary_path="",
        error="",
    )
    print(f"RETRY_READY {args.episode_id} {record.get('title', '')}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="podcast-intel")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="run the daily pipeline")
    run_parser.add_argument("--lookback", type=int)
    run_parser.add_argument("--max-episodes", type=int)
    run_parser.add_argument("--no-transcribe", action="store_true")
    run_parser.add_argument("--feed", action="append", help="limit to a feed id")
    run_parser.set_defaults(handler=command_run)

    discover_parser = subparsers.add_parser(
        "discover", help="list recent episodes without processing them"
    )
    discover_parser.add_argument("--lookback", type=int)
    discover_parser.add_argument("--feed", action="append", help="limit to a feed id")
    discover_parser.set_defaults(handler=command_discover)

    doctor_parser = subparsers.add_parser("doctor", help="check local prerequisites")
    doctor_parser.set_defaults(handler=command_doctor)

    retry_parser = subparsers.add_parser(
        "retry", help="mark an episode for transcript acquisition and analysis again"
    )
    retry_parser.add_argument("episode_id")
    retry_parser.set_defaults(handler=command_retry)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    raise SystemExit(args.handler(args))
