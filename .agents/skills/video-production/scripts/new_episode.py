#!/usr/bin/env python3
"""Compatibility entry point for tools/new_episode.py."""

from pathlib import Path
from runpy import run_path


if __name__ == "__main__":
    entry_point = Path(__file__).resolve().parents[4] / "tools" / "new_episode.py"
    run_path(str(entry_point), run_name="__main__")
