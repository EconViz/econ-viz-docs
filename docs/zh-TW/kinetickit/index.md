---
seo_title: "KineticKit：可重現的 Python 2D 與 3D 動畫引擎"
description: "KineticKit 用不可變場景與動作建立可重現的 2D 與 3D 動畫，並輸出動態 SVG、串流 GIF 或互動 HTML。"
---

<h1 class="ev-visually-hidden">KineticKit：可重現的 Python 2D 與 3D 動畫引擎</h1>

<p align="center">
  <img src="../../assets/kinetickit/banner.svg" alt="kinetickit" style="max-width: 480px; width: 100%; margin: 2rem 0 1rem;">
</p>

KineticKit 是與應用領域無關的 2D 與 3D 動畫引擎。同一個不可變場景和動作，可以輸出成動態 SVG、串流 GIF 或單檔互動 HTML。

```bash
uv add --prerelease allow "kinetickit[studio]"
```

```python
from kinetickit import (
    Animation,
    Bounds2D,
    Point2D,
    Scene2D,
    Vec2,
)

dot = Point2D(id="dot", position=Vec2(1, 1), size=8)
scene = Scene2D(dot).bind(
    {"camera.view": Bounds2D(Vec2(0, 0), Vec2(10, 10))}
)
motion = dot.animate.position.to(Vec2(9, 9), duration=1.5)
Animation(scene, motion).save("dot.svg", width=400, height=400)
```

## KineticKit 負責什麼

<div class="grid cards" markdown>

-   :material-animation-play: **場景與動作**

    不可變的 2D 與 3D 節點、可組合動作、關鍵影格、路徑與網格變形，以及依穩定識別碼配對的場景轉場。

    [:octicons-arrow-right-24: 場景與動作](guides/scenes-motion.md)

-   :material-export: **三種輸出路徑**

    原生動態 SVG、記憶體有上限且最高 1200 DPI 的 GIF，以及經過明確能力檢查的互動 HTML。

    [:octicons-arrow-right-24: 輸出格式](guides/outputs.md)

-   :material-format-font: **字體與無障礙資訊**

    由 GlyphKit 建立的文字資產、內嵌字體子集、物件語意、減少動態效果政策與可攜互動。

    [:octicons-arrow-right-24: 字體與無障礙資訊](guides/typography-accessibility.md)

</div>

KineticKit 不包含經濟學或圖表語意。使用端套件要把自己的物件轉成點、線、路徑、形狀、文字資產、網格與曲面。

<!-- agora-navigation -->

## 文件導覽

- [簡介](guides/introduction.md)
- [安裝](installation.md)
- [快速開始](quickstart.md)
- [場景與動作](guides/scenes-motion.md)
- [輸出格式](guides/outputs.md)
- [字體與無障礙資訊](guides/typography-accessibility.md)
- [遷移既有動畫程式](migration.md)
- [時間、緩動與動作代數](guides/time-easing.md)
- [插值與座標變換](guides/interpolation-transforms.md)
- [相機幾何與投影](guides/projection.md)
- [路徑、網格與曲面變形](guides/morphing.md)
- [幀取樣與編碼](guides/sampling-encoding.md)
- [更新紀錄](project/changelog.md)

<!-- /agora-navigation -->
