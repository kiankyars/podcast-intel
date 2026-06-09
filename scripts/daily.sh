#!/bin/bash
set -euo pipefail

cd "$(dirname "$0")/.."
mkdir -p logs

timestamp="$(date '+%Y-%m-%dT%H-%M-%S')"
uv run podcast-intel prepare 2>&1 |
  tee "logs/run-${timestamp}.log"
