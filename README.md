# 视频生成助手 · 个人视频制作库

给选题挑讲法和画风，建立一份可继续制作的旁白与分镜，再用 HyperFrames 做可编辑动画。

## 开始一集

在此项目发起新的 Codex 会话，调用 [`$video-production`](.agents/skills/video-production/SKILL.md)，给出选题和预计时长。例如「用 `$video-production` 设计一期 30 秒动画，讲青苗钱怎样从春借到秋还」。

以下工具可从仓库根目录直接运行，需要 Python 3.8 或更新版本。

```bash
python3 .agents/skills/video-production/scripts/recommend_style.py '古代粮仓如何收粮放粮'
python3 .agents/skills/video-production/scripts/new_episode.py episodes/granary \
  --title '古代粮仓如何收粮放粮' --template D --seconds 45
```

第一条按选题给出三套风格参考。第二条在新目录里创建 `facts.md`、`narration.json` 和 `storyboard.md`。用事实清单核对出处，把旁白按拍改写，再在分镜表写清关键动作和旁白锚点。

## 库里有什么

- [六套叙事母版](.agents/skills/video-production/assets/upstream/vibe-knowledge/references/01-templates.md)有猜谜、两难选择、痛点原理、一条主线、闯关和六面轮转，配套旁白骨架可直接建集。
- [44 套上游风格说明](.agents/skills/video-production/assets/upstream/vibe-knowledge/styles/INDEX.md)可按家族浏览。[暖纸纸雕](.agents/skills/video-production/references/paper-cut.md)记录本项目青苗钱试片的分层、动作和镜头做法。
- [朱砂印章](.agents/skills/video-production/references/stamp.md)提供能放进 HyperFrames 项目的动画源码与接入示例。
- [上游来源及许可](.agents/skills/video-production/assets/upstream/vibe-knowledge/SOURCE.md)记录固定版本与导入范围，该目录收录上游代码和文档中的复用内容。
