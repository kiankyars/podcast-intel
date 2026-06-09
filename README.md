# Podcast Intel

A local daily podcast intelligence pipeline modeled on Gavin Baker's described
workflow: scan more material than a person can watch, retain only points likely
to matter, and maintain both a daily log and cumulative topic files.

## Design

The system deliberately has a small number of moving parts:

1. RSS discovers episodes from a curated feed list.
2. Metadata filtering avoids expensive transcription on broad shows.
3. Transcripts are acquired in this order:
   - `podcast:transcript` links in RSS
   - transcript embedded in RSS or linked from the episode page
   - YouTube captions through `yt-dlp`
4. The Codex automation reads each generated request and writes structured
   analysis JSON.
5. The pipeline writes:
   - `digests/YYYY-MM-DD.md`: daily retained signals
   - `topics/*.md`: cumulative category logs
   - `episodes/...`: source metadata, transcript, structured analysis, summary
   - `data/state.json`: deduplication and resumable processing state

No database, web service, queue, or cloud account is required.

## Commands

```bash
./scripts/daily.sh

uv run podcast-intel discover --lookback 7
uv run podcast-intel audit-transcripts --lookback 14
uv run podcast-intel prepare --lookback 7 --max-episodes 2
uv run podcast-intel finalize
uv run podcast-intel doctor
uv run podcast-intel retry <episode-id>
uv run python -m unittest discover -s tests
```

Use `--feed <id>` to constrain discovery or preparation to one configured feed.
Use `audit-transcripts` to check whether recent selected episodes have
transcripts or captions.

## Configuration

- Edit `config.toml` to add feeds, tune the daily limits, or change categories.
- Edit `profile.md` to teach the analyst what is and is not interesting.
- A feed with `mode = "all"` processes every new episode.
- A feed with `mode = "filtered"` requires a keyword match in its title or
  description. `mode = "title_filtered"` checks only the title for noisy feeds.

The default lookback is fourteen days and the first run does not backfill a show's
full history.

## Transcript Sources

`podcast:transcript` is an RSS tag used by podcast publishers to attach a
transcript URL to an episode. The audit command checks this plus embedded
transcripts, episode-page transcript links, and YouTube captions. If none exist,
the episode is reported as missing a transcript instead of running local ASR.

## Scheduling

Use the project-scoped Codex app automation in [AUTOMATION.md](AUTOMATION.md).
The Codex app is the scheduler and the analyst. `scripts/daily.sh` only
discovers episodes, fetches transcripts, and writes analysis requests. The
automation writes the JSON analyses and then runs `finalize`.

The automation needs network access so the preparation step can fetch feeds,
episode pages, and captions.

## Operating Notes

- A transcript is saved before analysis. Failed analysis resumes without
  downloading the transcript again.
- Low-relevance episodes are recorded as processed but omitted from topic logs.
- Feed and episode failures appear in the digest and command output.
- Review the first several daily outputs and tune `profile.md`; editorial
  selection quality matters more than adding more infrastructure.
