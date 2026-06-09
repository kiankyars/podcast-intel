# Podcast Intel

A local daily podcast intelligence pipeline modeled on Gavin Baker's described
workflow: scan more material than a person can watch, retain only points likely
to matter, and maintain both a daily log and cumulative topic files.

## Design

The system deliberately has a small number of moving parts:

1. RSS discovers episodes from a curated feed list.
2. Metadata filtering avoids expensive transcription on broad shows.
3. Transcripts are acquired in this order:
   - Podcasting 2.0 `podcast:transcript`
   - transcript embedded in RSS or linked from the episode page
   - YouTube captions through `yt-dlp`
   - local MLX Whisper transcription on Apple Silicon
4. `codex exec` analyzes each episode in a read-only temporary sandbox using a
   strict JSON schema.
5. The pipeline writes:
   - `digests/YYYY-MM-DD.md`: daily retained signals
   - `topics/*.md`: cumulative category logs
   - `episodes/...`: source metadata, transcript, structured analysis, summary
   - `data/state.json`: deduplication and resumable processing state

No database, web service, queue, or cloud account is required.

## Commands

```bash
./scripts/daily.sh

PYTHONPATH=src python3 -m podcast_intel discover --lookback 7
PYTHONPATH=src python3 -m podcast_intel run --lookback 7 --max-episodes 2
PYTHONPATH=src python3 -m podcast_intel doctor
PYTHONPATH=src python3 -m podcast_intel retry <episode-id>
PYTHONPATH=src python3 -m unittest discover -s tests
```

Use `--feed <id>` to constrain discovery or a run to one configured feed. Use
`--no-transcribe` to stop after publisher transcripts and YouTube captions.

## Configuration

- Edit `config.toml` to add feeds, tune the daily limits, or change categories.
- Edit `profile.md` to teach the analyst what is and is not interesting.
- A feed with `mode = "all"` processes every new episode.
- A feed with `mode = "filtered"` requires a keyword match in its title or
  description. `mode = "title_filtered"` checks only the title for noisy feeds.

The default lookback is fourteen days and the first run does not backfill a show's
full history.

## Optional Local Transcription

Publisher transcripts and captions cover many episodes. Install the Apple
Silicon fallback only when needed:

```bash
uv sync --extra asr
```

The first MLX transcription downloads the configured Whisper model. Audio is
deleted after successful transcription unless `keep_audio = true`.

## Scheduling

Use the project-scoped Codex app automation in [AUTOMATION.md](AUTOMATION.md).
The Codex app is the scheduler; `scripts/daily.sh` remains the stable,
manually-testable entry point.

The automation needs network access. The inner `codex exec` analysis process is
separately constrained to a read-only empty temporary directory, and podcast
content is explicitly treated as untrusted data.

## Operating Notes

- A transcript is saved before analysis. Failed analysis resumes without
  downloading or transcribing the episode again.
- Low-relevance episodes are recorded as processed but omitted from topic logs.
- Feed and episode failures appear in the digest and command output.
- Review the first several daily outputs and tune `profile.md`; editorial
  selection quality matters more than adding more infrastructure.
