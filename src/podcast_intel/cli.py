from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Callable

from .analyze import write_analysis_request
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
from .transcripts import acquire_transcript


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
    maximum_seconds = int(config.run.max_total_hours * 3600)
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


def _write_pending_manifest(root: Path, pending: list[dict]) -> Path:
    path = root / "data" / "pending_analysis.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(pending, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return path


def prepare_pipeline(
    *,
    root: Path = ROOT,
    lookback_days: int | None = None,
    max_episodes: int | None = None,
    feed_ids: set[str] | None = None,
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
    pending: list[dict] = []

    for episode in selected:
        print(f"PROCESS {episode.feed_name}: {episode.title}", flush=True)
        transcript = _cached_transcript(state, episode)
        if not transcript:
            try:
                transcript = transcript_acquirer(
                    episode,
                    timeout=config.run.request_timeout_seconds,
                )
            except Exception as error:
                message = (
                    f"{episode.feed_name} / {episode.title}: "
                    f"{type(error).__name__}: {error}"
                )
                result.failed_episodes.append(message)
                state.update(episode.id, status="transcript_error", error=message)
                continue

        paths = write_transcript_artifact(root, episode, transcript)
        request_path = Path(paths["directory"]) / "analysis_request.md"
        analysis_path = Path(paths["directory"]) / "analysis.json"
        write_analysis_request(
            path=request_path,
            episode=episode,
            transcript=transcript.text,
            profile=profile,
            categories=config.categories,
            max_transcript_chars=config.run.max_transcript_chars,
        )
        state.update(
            episode.id,
            status="transcript_ready",
            raw_transcript=paths["raw_transcript"],
            transcript_path=paths["transcript"],
            transcript_source=transcript.source,
            transcript_source_url=transcript.source_url,
            request_path=str(request_path),
            analysis_path=str(analysis_path),
            feed_id=episode.feed_id,
            title=episode.title,
            published=episode.published.isoformat(),
            link=episode.link,
            error="",
        )
        pending.append(
            {
                "episode_id": episode.id,
                "title": episode.title,
                "feed_name": episode.feed_name,
                "request_path": str(request_path),
                "analysis_path": str(analysis_path),
                "schema_path": str(root / "schemas" / "episode-analysis.schema.json"),
            }
        )

    manifest = _write_pending_manifest(root, pending)
    result.selected = len(pending)
    result.digest_path = str(manifest)
    return result


def _episode_from_metadata(path: Path) -> Episode:
    payload = json.loads(path.read_text(encoding="utf-8"))
    published = datetime.fromisoformat(payload["published"])
    return Episode(
        id=payload["id"],
        feed_id=payload["feed_id"],
        feed_name=payload["feed_name"],
        feed_priority=int(payload["feed_priority"]),
        title=payload["title"],
        description_html=payload.get("description_html", ""),
        description_text=payload.get("description_text", ""),
        published=published,
        duration_seconds=int(payload.get("duration_seconds", 0)),
        link=payload.get("link", ""),
        audio_url=payload.get("audio_url", ""),
        transcript_urls=list(payload.get("transcript_urls", [])),
        web_links=list(payload.get("web_links", [])),
    )


def finalize_pipeline(*, root: Path = ROOT) -> RunResult:
    config, _, state = _load(root)
    result = RunResult()
    relevant: list[tuple[Episode, dict]] = []

    for episode_id, record in list(state.payload["episodes"].items()):
        if record.get("status") not in {"transcript_ready", "analysis_error"}:
            continue
        analysis_path = Path(str(record.get("analysis_path", "")))
        raw_path = Path(str(record.get("raw_transcript", "")))
        transcript_path = Path(str(record.get("transcript_path", "")))
        metadata_path = transcript_path.parent / "metadata.json"
        if not analysis_path.exists():
            continue
        try:
            analysis = json.loads(analysis_path.read_text(encoding="utf-8"))
            episode = _episode_from_metadata(metadata_path)
            transcript = Transcript(
                text=raw_path.read_text(encoding="utf-8"),
                source=str(record.get("transcript_source", "cached")),
                source_url=str(record.get("transcript_source_url", episode.link)),
            )
            paths = write_episode_artifacts(root, episode, transcript, analysis)
            score = int(analysis["relevance_score"])
            if score >= config.run.min_relevance_score:
                update_topics(root, episode, analysis, config.categories)
                relevant.append((episode, analysis))
                result.relevant += 1
            else:
                result.skipped += 1
            result.processed += 1
            state.update(
                episode_id,
                status="processed",
                relevance_score=score,
                analysis_path=paths["analysis"],
                summary_path=paths["summary"],
                error="",
            )
        except Exception as error:
            message = f"{record.get('title', episode_id)}: {type(error).__name__}: {error}"
            result.failed_episodes.append(message)
            state.update(episode_id, status="analysis_error", error=message)

    if relevant or result.failed_episodes:
        digest = write_daily_digest(
            root,
            datetime.now().astimezone().date(),
            relevant,
            processed_count=result.processed,
            skipped_count=result.skipped,
            failed_feeds=[],
            failed_episodes=result.failed_episodes,
        )
        result.digest_path = str(digest)
    return result


def _print_prepare_result(result: RunResult) -> None:
    if not result.selected and not result.failed_feeds and not result.failed_episodes:
        print(
            "NO_PENDING_EPISODES "
            f"discovered={result.discovered} filtered={result.skipped}"
        )
        return
    status = "PENDING_ANALYSIS"
    if result.failed_feeds or result.failed_episodes:
        status = "PENDING_ANALYSIS_WITH_FAILURES"
    print(
        f"{status} manifest={result.digest_path} pending={result.selected} "
        f"feed_failures={len(result.failed_feeds)} "
        f"episode_failures={len(result.failed_episodes)}"
    )
    for failure in result.failed_feeds:
        print(f"FEED_FAILURE {failure}")
    for failure in result.failed_episodes:
        print(f"EPISODE_FAILURE {failure}")


def _print_finalize_result(result: RunResult) -> None:
    if not result.processed and not result.failed_episodes:
        print("NO_COMPLETED_ANALYSES")
        return
    status = "FINALIZED_DIGEST"
    if result.failed_episodes:
        status = "FINALIZED_WITH_FAILURES"
    print(
        f"{status} digest={result.digest_path} relevant={result.relevant} "
        f"processed={result.processed} episode_failures={len(result.failed_episodes)}"
    )
    for failure in result.failed_episodes:
        print(f"EPISODE_FAILURE {failure}")


def command_prepare(args: argparse.Namespace) -> int:
    result = prepare_pipeline(
        lookback_days=args.lookback,
        max_episodes=args.max_episodes,
        feed_ids=set(args.feed) if args.feed else None,
    )
    _print_prepare_result(result)
    return 0 if not result.failed_feeds and not result.failed_episodes else 1


def command_finalize(_: argparse.Namespace) -> int:
    result = finalize_pipeline()
    _print_finalize_result(result)
    return 0 if not result.failed_episodes else 1


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


def command_audit_transcripts(args: argparse.Namespace) -> int:
    config = load_config(ROOT / "config.toml")
    episodes, failures = discover(
        config,
        feed_ids=set(args.feed) if args.feed else None,
    )
    feeds = {feed.id: feed for feed in config.feeds}
    since = datetime.now(timezone.utc) - timedelta(
        days=args.lookback or config.run.lookback_days
    )
    candidates = [
        episode
        for episode in episodes
        if episode.published >= since
        and metadata_matches(episode, feeds[episode.feed_id], config.keywords)
    ]
    candidates.sort(key=lambda item: (item.feed_priority, item.published), reverse=True)
    if args.max_episodes:
        candidates = candidates[: args.max_episodes]

    missing = 0
    for episode in candidates:
        try:
            transcript = acquire_transcript(
                episode,
                timeout=config.run.request_timeout_seconds,
            )
            print(
                f"OK      {transcript.source:24} "
                f"{episode.published.date()} {episode.feed_name}: {episode.title}"
            )
        except Exception as error:
            missing += 1
            print(
                f"MISSING {type(error).__name__:24} "
                f"{episode.published.date()} {episode.feed_name}: {episode.title} -- {error}"
            )
    for failure in failures:
        print(f"FEED_FAILURE {failure}", file=sys.stderr)
    return 1 if missing or failures else 0


def command_doctor(_: argparse.Namespace) -> int:
    config, _, _ = _load(ROOT)
    checks = {
        "python": sys.version.split()[0],
        "codex": shutil.which("codex") or "missing",
        "yt-dlp": shutil.which("yt-dlp") or "missing",
        "feeds": str(len(config.feeds)),
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

    prepare_parser = subparsers.add_parser(
        "prepare", help="discover episodes and write analysis requests"
    )
    prepare_parser.add_argument("--lookback", type=int)
    prepare_parser.add_argument("--max-episodes", type=int)
    prepare_parser.add_argument("--feed", action="append", help="limit to a feed id")
    prepare_parser.set_defaults(handler=command_prepare)

    finalize_parser = subparsers.add_parser(
        "finalize", help="render digests after analysis files are written"
    )
    finalize_parser.set_defaults(handler=command_finalize)

    discover_parser = subparsers.add_parser(
        "discover", help="list recent episodes without processing them"
    )
    discover_parser.add_argument("--lookback", type=int)
    discover_parser.add_argument("--feed", action="append", help="limit to a feed id")
    discover_parser.set_defaults(handler=command_discover)

    audit_parser = subparsers.add_parser(
        "audit-transcripts",
        help="check whether recent selected episodes have transcripts or captions",
    )
    audit_parser.add_argument("--lookback", type=int)
    audit_parser.add_argument("--max-episodes", type=int)
    audit_parser.add_argument("--feed", action="append", help="limit to a feed id")
    audit_parser.set_defaults(handler=command_audit_transcripts)

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
