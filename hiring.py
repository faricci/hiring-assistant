#!/usr/bin/env python3
"""Root launcher so the toolkit runs from any shell: `python hiring.py <command>`."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from hiring.cli import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
