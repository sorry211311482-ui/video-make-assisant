# 视频生成助手 · 个人视频制作库

从选题整理讲法、画风、旁白和动作分镜，按镜头选择制作方法，交付可审阅的样片或成片。

## 制作库目录

| 目录 | 内容 |
| --- | --- |
| [制作流程](skill/SKILL.md) | 可供不同 AI 助手读取的知识动画制作指南与[制作路线](skill/production-routes.md) |
| [音效](sound-effects/) | 动作音效的素材来源、许可与合成做法 |
| [风格](styles/) | 暖纸纸雕与 44 套上游视觉风格说明 |
| [组件](components/) | 可复用的动画源码和各组件的接入说明 |
| [提示词](prompts/) | 可直接复制的导演方案和动作分镜提示词 |
| [脚本](scripts/) | 六套旁白母版、事实清单和选稿指南 |
| [工具](tools/) | 风格推荐和分集创建命令 |
| [来源与许可](sources/) | 上游版本、导入对应关系和许可 |

## 开始一集

在能访问本仓库文件的 AI 助手里，给出选题、预计时长和制作指南的路径。

> 请读取 `skill/SKILL.md`，按里面的流程设计一期 30 秒动画，讲青苗钱怎样从春借到秋还。

以下工具可从仓库根目录直接运行，需要 Python 3.8 或更新版本。

```bash
python3 tools/recommend_style.py '古代粮仓如何收粮放粮'
python3 tools/new_episode.py episodes/granary \
  --title '古代粮仓如何收粮放粮' --template D --seconds 45
```

第一条按选题给出三套风格参考。第二条在新目录里创建 `facts.md`、`narration.json` 和 `storyboard.md`。用事实清单核对出处，把旁白按拍改写，再在分镜表写清关键动作和旁白锚点。
