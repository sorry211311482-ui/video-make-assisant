---
name: video-production
description: 用项目的视频制作库设计或制作知识动画，从选题挑叙事母版和视觉风格，编制事实清单、旁白和动作分镜，并使用 HyperFrames 做可编辑预览。也用于把试片中的原创风格或可复用组件收回库里。
---

# 视频制作

## 从选题到样镜

1. **导演方案。** 写出观众最后应懂的一句话，以及哪个画面动作能演给观众看。[六套叙事母版](assets/upstream/vibe-knowledge/references/01-templates.md)提供拆拍思路。需要选画风时运行 `python3 scripts/recommend_style.py "选题"`，打开候选的 `STYLE.md`。历史机制题材优先考虑已经在青苗钱试片验证过的[暖纸纸雕](references/paper-cut.md)。用户已指定的讲法、片长和画风可直接沿用。
2. **查证和分镜。** 需要新建分集时，从本目录运行 `python3 scripts/new_episode.py <分集目录> --title "选题" --template D --seconds 45`。用 `facts.md` 给人物、年份、数字、引文和关键机制配出处，再写 `narration.json`。在 `storyboard.md` 用同一拍号记录画面动作、旁白锚点和静音时能读到的信息。按目标片长合并或扩展母版的拍数。用「情境示意」等字样注明推演、复原和假设画面。
3. **做可编辑样镜。** 开始做 HyperFrames 工程时，先读适用的 HyperFrames 技能和项目说明。挑一个承担叙事的镜头，先看静音播放能否读懂动作顺序和结果，再用实际旁白对齐关键词与字幕。需要纸面确认或落账动作，可用[朱砂印章组件](references/stamp.md)。
4. **核对交付。** 检查事实与画面是否一致，检查关键时间点、动作前后和结尾停留，记录实际看到的预览与检查结果。按用户指定的阶段交付脚本、预览或成片。外部生成、用音和发布遵循该期已经明确的授权。

## 复用资料

- [上游风格索引](assets/upstream/vibe-knowledge/styles/INDEX.md)用来挑阅读参考。各 `STYLE.md` 中的样片、引擎说明和增强档配置对应原作者工程。用本项目的 HyperFrames 源文件实现选中的画法。
- 要将原创做法收回库时，保存可编辑源码、原片时间区间、用于验收的画面变化，以及新项目允许替换的内容。声明代码和素材的来源。
- [来源和导入范围](assets/upstream/vibe-knowledge/SOURCE.md)记录原始版本、许可和本地改写。
