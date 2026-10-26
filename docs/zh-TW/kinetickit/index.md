---
seo_title: "Python 的確定性 2D 與 3D 動畫"
description: "KineticKit 用不可變的場景與動作建立確定性的 2D 與 3D 動畫，並輸出動態 SVG、串流 GIF 或獨立的互動 HTML。"
---

<h1 class="ev-visually-hidden">kinetickit：Python 的確定性 2D 與 3D 動畫</h1>

<p align="center"><em>與領域無關、精確且確定的 2D 與 3D 動畫引擎。</em></p>

<p align="center">
  <a href="https://github.com/EconViz/kinetickit"><img alt="GitHub" src="https://img.shields.io/badge/github-EconViz%2Fkinetickit-181818?style=flat-square&labelColor=f3f3f3"></a>
  <a href="https://pypi.org/project/kinetickit/"><img alt="PyPI" src="https://img.shields.io/pypi/v/kinetickit?include_prereleases&style=flat-square&label=pypi+package&color=181818&labelColor=f3f3f3&cacheSeconds=300"></a>
  <a href="https://pypi.org/project/kinetickit/"><img alt="Python" src="https://img.shields.io/pypi/pyversions/kinetickit?style=flat-square&color=181818&labelColor=f3f3f3"></a>
</p>

!!! warning "kinetickit 1.0 為測試版"

    kinetickit 1.0.0b2 是預發行版本。[相容性](compatibility.md)列出的契約打算保持穩定，但預發行版本之間可能改變，並一定附上變更紀錄。

```python
from kinetickit import Animation, Bounds2D, Point2D, Scene2D, Vec2, ease

dot = Point2D(id="dot", position=Vec2(1, 1), size=8, color="#e4572e")
scene = Scene2D(dot)
scene = scene.bind({scene.camera.ref("view"): Bounds2D(Vec2(0, 0), Vec2(10, 10))})

motion = dot.animate.position.to(Vec2(9, 9), duration=1.5, easing=ease.out_cubic)
animation = Animation(scene, motion)

animation.save("dot.svg", width=400, height=400)
```

## 功能

<div class="grid cards" markdown>

-   :material-animation-play: **場景與動作**

    不可變的 2D 與 3D 節點，以及用 `then`、`with_`、`delay`、`repeat`、`yoyo`、`reverse` 與 `trim` 組合的動作。

    [:octicons-arrow-right-24: 場景與動作](guides/scenes-motion.md)

-   :material-timer-outline: **時間與緩動**

    精確時間點的影格、緩動函數族與三次 Bézier 時間曲線、關鍵影格與標記。

    [:octicons-arrow-right-24: 時間與緩動](guides/time-easing.md)

-   :material-shape-polygon-plus: **變形與轉場**

    明確對應的路徑、網格與曲面變形，以及依穩定編號配對節點的場景轉場。

    [:octicons-arrow-right-24: 變形](guides/morphing.md)

-   :material-cube-outline: **3D 場景與相機**

    網格、高度場曲面、光源，以及共用同一套投影的透視或正交相機。

    [:octicons-arrow-right-24: 相機幾何與投影](guides/projection.md)

-   :material-export: **一個場景，三種輸出**

    動態 SVG、最高 1200 DPI 的串流 GIF，以及獨立的互動 HTML，寫檔前都會先檢查能力。

    [:octicons-arrow-right-24: 輸出格式](guides/outputs.md)

-   :material-format-font: **文字排版**

    文字以中性素材的形式進來，由 GlyphKit 用呼叫端提供的字型排版，並嵌入通過權限檢查的字型子集。

    [:octicons-arrow-right-24: 文字排版](guides/typography.md)

-   :material-human-greeting-variant: **無障礙與互動**

    角色、標籤與閱讀順序、減少動態的政策，以及綁定到節點編號、只含資料的互動。

    [:octicons-arrow-right-24: 無障礙與互動](guides/accessibility.md)

-   :material-puzzle-outline: **範例與轉接器**

    用基本圖形畫的圖表、透過轉接器動畫的一般 Python 物件模型，以及打光的 3D 曲面。

    [:octicons-arrow-right-24: 範例](guides/examples.md)

</div>

## 安裝

```bash
uv add --prerelease allow "kinetickit[studio]"
```

需要 Python 3.10 到 3.13。選用的額外安裝項見[安裝](installation.md)。

## 範例

本文件的每張圖都附上生成它的腳本。可一次下載全部。

[下載全部範例](../assets/kinetickit/kinetickit-examples.zip){ .md-button download="" }
