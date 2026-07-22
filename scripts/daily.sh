#!/bin/bash
set -euo pipefail

cd "$(dirname "$0")/.."
mkdir -p logs

# Keep uv's cache writable in unattended macOS runs while respecting an
# explicit caller override.
export UV_CACHE_DIR="${UV_CACHE_DIR:-${TMPDIR:-/tmp}/podcast-intel-uv-cache}"

timestamp="$(date '+%Y-%m-%dT%H-%M-%S')"
uv run podcast-intel prepare 2>&1 |
  tee "logs/run-${timestamp}.log"
