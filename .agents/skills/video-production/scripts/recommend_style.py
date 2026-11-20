#!/usr/bin/env python3
# Matching adapted from vibe-knowledge/tools/recommend.py at c3a13a85f7cc560e5d396f063baecea4b2748e1e.
# Copyright (c) 2026 Berryxia (andyhuo520), MIT.
import argparse
import json
from collections import Counter
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
STYLE_DIRECTORY = Path("assets/upstream/vibe-knowledge/styles")
FALLBACK_STYLES = ("starfield", "variety", "caption-news", "chalk")
RECOMMENDATION_COUNT = 3


def recommend_styles(topic, catalog, include_enhanced):
    styles = {
        style["key"]: style
        for style in catalog["styles"]
        if style["tier"] == "基础" or include_enhanced
    }
    topic = topic.casefold()
    scored = []
    for style in styles.values():
        keyword_hits = [
            term for term in style["keywords"]
            if len(term) >= 2 and term.casefold() in topic
        ]
        tone_hits = [term for term in style["tone"] if term.casefold() in topic]
        score = sum(2 + len(term) for term in keyword_hits) + len(tone_hits)
        if score:
            scored.append((score, style, list(dict.fromkeys(keyword_hits + tone_hits))))
    scored.sort(key=lambda item: (-item[0], item[1]["no"]))

    selected = []
    family_counts = Counter()
    for _, style, hits in scored:
        family = style["fam"]
        if family_counts[family] < 2:
            selected.append((style, hits))
            family_counts[family] += 1
        if len(selected) == RECOMMENDATION_COUNT:
            break

    for key in (*FALLBACK_STYLES, *styles):
        if len(selected) == RECOMMENDATION_COUNT:
            break
        style = styles.get(key)
        if style and style["fam"] not in family_counts:
            selected.append((style, []))
            family_counts[style["fam"]] += 1

    results = []
    for style, hits in selected:
        template = style["templates"][0]
        if hits:
            reason = f"命中「{'、'.join(hits[:4])}」，适合{style['fit']}。"
        else:
            reason = f"适合{style['fit']}，可作为另一种视觉方向的备选。"
        results.append({
            "key": style["key"],
            "name": style["name"],
            "family": style["fam"],
            "tier": style["tier"],
            "reason": reason,
            "template": template,
            "template_name": catalog["templates"][template],
            "guide": (STYLE_DIRECTORY / style["key"] / "STYLE.md").as_posix(),
        })
    return results


def main():
    parser = argparse.ArgumentParser(
        description="根据选题推荐三套风格。输出中的指南路径相对于 video-production Skill 目录。",
    )
    parser.add_argument("topic", help="选题文字，多词选题用引号包住")
    parser.add_argument("--include-enhanced", action="store_true", help="同时纳入增强档风格作参考")
    parser.add_argument("--json", action="store_true", help="输出 JSON")
    args = parser.parse_args()
    if not args.topic.strip():
        parser.error("请输入选题")

    catalog_path = SKILL_ROOT / STYLE_DIRECTORY / "catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    recommendations = recommend_styles(args.topic, catalog, args.include_enhanced)
    if args.json:
        print(json.dumps(recommendations, ensure_ascii=False, indent=2))
        return

    for number, item in enumerate(recommendations, start=1):
        print(f"{number}. {item['name']}（{item['family']} · {item['tier']}）")
        print(f"   理由  {item['reason']}")
        print(f"   母版  {item['template']} {item['template_name']}")
        print(f"   指南  {item['guide']}")


if __name__ == "__main__":
    main()
