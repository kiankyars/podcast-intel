#!/bin/bash
set -euo pipefail

cd "$(dirname "$0")/.."
mkdir -p logs

timestamp="$(date '+%Y-%m-%dT%H-%M-%S')"
if [ -x ".venv/bin/python" ]; then
  python=".venv/bin/python"
else
  python="python3"
fi

PYTHONPATH="$PWD/src" "$python" -m podcast_intel run 2>&1 |
  tee "logs/run-${timestamp}.log"
