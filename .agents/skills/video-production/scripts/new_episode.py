#!/usr/bin/env python3
"""Create an editable episode brief from the library's imported writing templates."""

import argparse
import json
import math
from pathlib import Path


TEMPLATES = (
    Path(__file__).resolve().parents[1] / "assets/upstream/vibe-knowledge/templates"
)


def positive_seconds(value: str) -> float:
    seconds = float(value)
    if not math.isfinite(seconds) or seconds <= 0:
        raise argparse.ArgumentTypeError("片长须为大于 0 的有限秒数")
    return seconds


def main() -> None:
    parser = argparse.ArgumentParser(description="建立一期的事实清单、旁白骨架和分镜表。")
    parser.add_argument("directory", type=Path, help="本期的新目录")
    parser.add_argument("--title", required=True, help="本期选题")
    parser.add_argument("--template", required=True, type=str.upper, choices=tuple("ABCDEF"))
    parser.add_argument("--seconds", required=True, type=positive_seconds)
    args = parser.parse_args()
    title = args.title.strip()
    if not title or len(title.splitlines()) != 1:
        parser.error("--title 需要是一行非空文字")

    source = TEMPLATES / "narration" / f"{args.template}.json"
    template = json.loads(source.read_text(encoding="utf-8"))
    narration = {
        "title": title,
        "template": args.template,
        "target_seconds": args.seconds,
        "lexicon": template["lexicon"],
        "beats": template["beats"],
    }
    storyboard = [
        f"# {title} · 分镜",
        "",
        f"目标片长 {args.seconds:g} 秒，讲法母版 {args.template}。",
        "",
        "按选题取舍、合并或扩展旁白拍，再把对应的时间和动作填入表格。",
        "",
        "| 拍号 | 入点（秒） | 出点（秒） | 旁白锚点 | 画面动作 | 静音能看懂什么 | 事实 / 素材来源 |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    storyboard.extend(f"| {beat['id']} | | | | | | |" for beat in narration["beats"])
    files = {
        "facts.md": (TEMPLATES / "facts.md").read_text(encoding="utf-8"),
        "narration.json": json.dumps(narration, ensure_ascii=False, indent=2) + "\n",
        "storyboard.md": "\n".join(storyboard) + "\n",
    }

    destination = args.directory.expanduser()
    try:
        destination.mkdir(parents=True)
    except OSError as error:
        parser.exit(1, f"无法建立分集目录 {destination}。{error}\n")

    try:
        for filename, content in files.items():
            (destination / filename).write_text(content, encoding="utf-8")
    except OSError as error:
        for filename in files:
            (destination / filename).unlink(missing_ok=True)
        destination.rmdir()
        parser.exit(1, f"无法写入分集 {destination}。{error}\n")

    print(f"已建立 {destination.resolve()}（facts.md、narration.json、storyboard.md）")


if __name__ == "__main__":
    main()
