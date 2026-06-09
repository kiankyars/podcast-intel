# Podcast Intel Automation

This repository is an unattended podcast-ingestion and synthesis workflow.

For a scheduled run:

1. Run `./scripts/daily.sh`.
2. If stdout starts with `NO_PENDING_EPISODES`, return no finding.
3. Otherwise read `data/pending_analysis.json`.
4. For each item, read `request_path` and write `analysis_path` as JSON matching `schemas/episode-analysis.schema.json`.
5. Run `uv run podcast-intel finalize`.
6. Report the digest path and the top three signals.
