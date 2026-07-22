#!/bin/bash
set -euo pipefail

cd "$(dirname "$0")/.."

run_date="${PODCAST_INTEL_RUN_DATE:-$(date '+%Y-%m-%d')}"
remote="${PODCAST_INTEL_GIT_REMOTE:-origin}"
expected_branch="${PODCAST_INTEL_GIT_BRANCH:-main}"
current_branch="$(git branch --show-current)"

if [ "$current_branch" != "$expected_branch" ]; then
  echo "PUBLISH_FAILED expected_branch=$expected_branch current_branch=$current_branch" >&2
  exit 1
fi

if [ -n "$(git diff --cached --name-only)" ]; then
  echo "PUBLISH_FAILED reason=preexisting_staged_changes" >&2
  exit 1
fi

# Publish durable intelligence artifacts only. Raw transcripts, analysis
# requests, pending manifests, caches, and logs remain local.
if [ -f data/state.json ]; then
  git add -f -- data/state.json
fi

digest="digests/${run_date}.md"
if [ -f "$digest" ]; then
  git add -f -- "$digest"
fi

while IFS= read -r -d '' summary; do
  directory="${summary%/summary.md}"
  for artifact in metadata.json analysis.json summary.md; do
    path="${directory}/${artifact}"
    if [ -f "$path" ]; then
      git add -f -- "$path"
    fi
  done
done < <(find episodes -type f -name summary.md -print0)

while IFS= read -r -d '' topic; do
  git add -f -- "$topic"
done < <(find topics -maxdepth 1 -type f -name '*.md' -print0)

if git diff --cached --quiet; then
  if git log \
    --since="${run_date} 00:00:00" \
    --until="${run_date} 23:59:59" \
    --format='%s' | grep -Eq "^(Archive podcast intel for|Record podcast intel run for) ${run_date}$"; then
    git push "$remote" "$current_branch"
    echo "PUBLISHED_DAILY_SNAPSHOT date=$run_date status=already-published branch=$current_branch"
    exit 0
  fi
  message="Record podcast intel run for ${run_date}"
else
  message="Archive podcast intel for ${run_date}"
fi

file_count="$(git diff --cached --name-only | wc -l | tr -d ' ')"
git commit --allow-empty -m "$message"
git push "$remote" "$current_branch"

echo "PUBLISHED_DAILY_SNAPSHOT date=$run_date commit=$(git rev-parse --short HEAD) files=$file_count branch=$current_branch"
