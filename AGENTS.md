# Podcast Intel

The canonical scheduled workflow is the repo-local
`$podcast-intel-daily-run` skill in
`.agents/skills/podcast-intel-daily-run/SKILL.md`.

For every scheduled daily run, invoke that skill explicitly and follow it from
preparation through publication. Do not duplicate or partially reimplement its
workflow in the automation prompt.

For repository changes, run:

```bash
UV_CACHE_DIR=/private/tmp/podcast-intel-uv-cache \
  uv run python -m unittest discover -s tests
```
