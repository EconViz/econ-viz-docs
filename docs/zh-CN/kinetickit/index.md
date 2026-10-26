---
seo_title: "Python 的确定性 2D 与 3D 动画"
description: "KineticKit 用不可变的场景与动作创建确定性的 2D 与 3D 动画，并输出动态 SVG、串流 GIF 或独立的交互 HTML。"
---

<h1 class="ev-visually-hidden">kinetickit：Python 的确定性 2D 与 3D 动画</h1>

<p align="center"><em>与领域无关、精确且确定的 2D 与 3D 动画引擎。</em></p>

<p align="center">
  <a href="https://github.com/EconViz/kinetickit"><img alt="GitHub" src="https://img.shields.io/badge/github-EconViz%2Fkinetickit-181818?style=flat-square&labelColor=f3f3f3"></a>
  <a href="https://pypi.org/project/kinetickit/"><img alt="PyPI" src="https://img.shields.io/pypi/v/kinetickit?include_prereleases&style=flat-square&label=pypi+package&color=181818&labelColor=f3f3f3&cacheSeconds=300"></a>
  <a href="https://pypi.org/project/kinetickit/"><img alt="Python" src="https://img.shields.io/pypi/pyversions/kinetickit?style=flat-square&color=181818&labelColor=f3f3f3"></a>
</p>

!!! warning "kinetickit 1.0 为测试版"

    kinetickit 1.0.0b2 是预发行版本。[兼容性](compatibility.md)列出的契约打算保持稳定，但预发行版本之间可能改变，并一定附上变更纪录。

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

-   :material-animation-play: **场景与动作**

    不可变的 2D 与 3D 节点，以及用 `then`、`with_`、`delay`、`repeat`、`yoyo`、`reverse` 与 `trim` 组合的动作。

    [:octicons-arrow-right-24: 场景与动作](guides/scenes-motion.md)

-   :material-timer-outline: **时间与缓动**

    精确时间点的帧、缓动函数族与三次 Bézier 时间曲线、关键帧与标记。

    [:octicons-arrow-right-24: 时间与缓动](guides/time-easing.md)

-   :material-shape-polygon-plus: **变形与转场**

    明确对应的路径、网格与曲面变形，以及依稳定编号配对节点的场景转场。

    [:octicons-arrow-right-24: 变形](guides/morphing.md)

-   :material-cube-outline: **3D 场景与相机**

    网格、高度场曲面、光源，以及共用同一套投影的透视或正交相机。

    [:octicons-arrow-right-24: 相机几何与投影](guides/projection.md)

-   :material-export: **一个场景，三种输出**

    动态 SVG、最高 1200 DPI 的串流 GIF，以及独立的交互 HTML，写档前都会先检查能力。

    [:octicons-arrow-right-24: 输出格式](guides/outputs.md)

-   :material-format-font: **文本排版**

    文本以中性素材的形式进来，由 GlyphKit 用调用端提供的字体排版，并嵌入通过权限检查的字体子集。

    [:octicons-arrow-right-24: 文本排版](guides/typography.md)

-   :material-human-greeting-variant: **无障碍与交互**

    角色、标签与阅读顺序、减少动态的政策，以及绑定到节点编号、只含数据的交互。

    [:octicons-arrow-right-24: 无障碍与交互](guides/accessibility.md)

-   :material-puzzle-outline: **示例与适配器**

    用基本图形画的图表、通过适配器动画的一般 Python 对象模型，以及打光的 3D 曲面。

    [:octicons-arrow-right-24: 示例](guides/examples.md)

</div>

## 安装

```bash
uv add --prerelease allow "kinetickit[studio]"
```

需要 Python 3.10 到 3.13。选用的额外安装项见[安装](installation.md)。

## 示例

本文档的每张图都附上生成它的脚本。可一次下载全部。

[下载全部示例](../assets/kinetickit/kinetickit-examples.zip){ .md-button download="" }
