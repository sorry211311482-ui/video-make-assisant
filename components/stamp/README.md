# 文字落印

用印章强调账本结论、审批结果或章节里的关键字。落印时，文字用 0.06 秒显现，并在 0.18 秒内从 1.6 倍缩回原尺寸。外层剪辑的结束时刻决定印章留在画面上多久。

把组件的 [stamp.js](stamp.js) 复制到 HyperFrames 项目的 `assets/components/stamp.js`。项目的 `index.html` 在本地 GSAP 之后加载它。

```html
<script src="assets/components/stamp.js"></script>
```

下例放在 `compositions/proof.html`。把根工程中的场景挂载指向这个文件，给 `proof` 至少 2.4 秒。印章从场景的第 1 秒开始，留到第 2.4 秒。把实际文字写进 HTML，或用 `textContent` 赋值。

```html
<template>
  <style>
    #root {
      position: absolute;
      inset: 0;
    }
    #proof-stamp {
      position: absolute;
      top: 460px;
      inset-inline: 0;
      text-align: center;
      font: 900 120px/1.1 sans-serif;
      color: #b23a2e;
    }
    #proof-stamp span {
      display: inline-block;
      border: 6px solid currentColor;
      border-radius: 12px;
      padding: 4px 26px;
      transform: rotate(-8deg);
    }
  </style>
  <div id="root" data-composition-id="proof" data-width="1920" data-height="1080">
    <div id="proof-stamp-clip" class="clip" data-start="1" data-duration="1.4" data-track-index="1">
      <div id="proof-stamp"><span>已结清</span></div>
    </div>
  </div>
  <script>
    (() => {
      const timeline = gsap.timeline({ paused: true });
      const stamp = document.getElementById("proof-stamp");
      window.addVideoProductionStamp(timeline, stamp, 1);
      window.__timelines = window.__timelines || {};
      window.__timelines.proof = timeline;
    })();
  </script>
</template>
```

在已有场景里，把调用放到场景注册时间轴之前，第三个参数用场景内的秒数。移动落印点时，同时更新外层 `data-start` 和第三个参数。留读或延长显示时调整外层 `data-duration`，它应大于 0.18 秒。颜色、字体、边框和内层文字的倾斜角度可在 CSS 里替换。

动作来自 Vibe 知识大赏的 `know.js`，沿用原版的显现和缩放节奏，用 HyperFrames 的外层剪辑控制退场。复用源码时随附原始 MIT 许可。 [上游印章源码](https://github.com/andyhuo520/vibe-knowledge/blob/c3a13a85f7cc560e5d396f063baecea4b2748e1e/skills/vibe-knowledge/kit/know.js#L410-L419) · [许可证](../../sources/vibe-knowledge/LICENSE)
