#!/usr/bin/env python3
"""Compatibility entry point for tools/recommend_style.py."""

from pathlib import Path
from runpy import run_path


if __name__ == "__main__":
    entry_point = Path(__file__).resolve().parents[4] / "tools" / "recommend_style.py"
    run_path(str(entry_point), run_name="__main__")
