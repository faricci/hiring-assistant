#!/usr/bin/env bash
# Thin wrapper: run the hiring CLI with the repo's Python from any cwd.
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY="${PYTHON:-python3}"
command -v "$PY" >/dev/null 2>&1 || PY="python"
exec "$PY" "$DIR/hiring.py" "$@"
