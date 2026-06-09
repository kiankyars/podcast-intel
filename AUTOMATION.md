Run ./scripts/daily.sh in this project and wait for it to finish.

Open data/pending_analysis.json. For each item:
- read request_path
- write analysis_path as JSON matching schemas/episode-analysis.schema.json

Then run:

uv run podcast-intel finalize

Report the generated digest path and the three highest-signal findings.
