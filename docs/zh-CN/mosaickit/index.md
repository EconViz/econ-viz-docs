---
seo_title: "mosaickit：与领域无关的图形场景与渲染工具包"
description: "mosaickit 是与领域无关的 Python 工具包，用场景、图层、样式、参数与渲染器组合出二维图形。"
---

<h1 class="ev-visually-hidden">mosaickit：与领域无关的图形场景与渲染</h1>

<p align="center">
  <img src="../../assets/mosaickit/banner.svg" alt="mosaickit" style="max-width: 480px; width: 100%; margin: 2rem 0 1rem;">
</p>

<p align="center"><em>与领域无关的 Python 工具包，用来组合二维图形。</em></p>

<p align="center">
  <a href="https://pypi.org/project/mosaickit/"><img alt="PyPI" src="https://img.shields.io/pypi/v/mosaickit?style=flat-square&label=pypi+package&color=181818&labelColor=f3f3f3&cacheSeconds=300"></a>
  <a href="https://pypi.org/project/mosaickit/"><img alt="Python" src="https://img.shields.io/pypi/pyversions/mosaickit?style=flat-square&color=181818&labelColor=f3f3f3"></a>
  <a href="https://opensource.org/licenses/MIT"><img alt="License" src="https://img.shields.io/badge/License-MIT-181818?style=flat-square&color=181818&labelColor=f3f3f3"></a>
</p>

```python
from mosaickit import (
    Canvas,
    Fill,
    FillLayer,
    MarkerLayer,
    PathLayer,
    Stroke,
    TextLayer,
    quadrant_axes,
)

canvas = Canvas().extend(quadrant_axes(10, 10))
canvas.add(
    FillLayer(
        [(1, 1), (1, 7), (8, 1)],
        fill=Fill(color="#377EB8", opacity=0.12),
        z_index=-1,
    )
)
canvas.add(
    PathLayer(
        [(1, 8), (2, 5), (4, 3), (7, 1.5), (9, 1)],
        stroke=Stroke(color="#984EA3", width=2),
    )
)
canvas.add(MarkerLayer([(4, 3)]))
canvas.add(TextLayer((4, 3), "A", offset=(8, 8)))
canvas.save("diagram.svg")
```

## 功能特色

<div class="grid cards" markdown>

-   :material-layers-outline: **精简的场景图**

    `PathLayer`、`FillLayer`、`MarkerLayer`、`TextLayer`、`ArrowLayer`、`LegendLayer` 与 `GroupLayer`。

-   :material-label-outline: **不遮住图形的标签**

    `RegionLabelLayer` 与 `PointLabelLayer` 自动避开图形，另有轴上标记、注记与大括号。

-   :material-axis-arrow: **坐标轴辅助函数**

    `quadrant_axes()`、`crosshair_axes()` 与 `box_frame()` 快速建立常见的坐标框架。

-   :material-palette-outline: **样式与主题**

    样式、主题与调色板，颜色可直接用名称指定。

-   :material-view-grid-outline: **参数与网格排版**

    参数与表达式、`CanvasGrid` 布局与 `Animation` 扫描。

-   :material-file-image-outline: **可替换的渲染器**

    内置 Matplotlib 渲染器输出 PNG、SVG 与 PDF，并提供 `Renderer` 协议供其他后端使用。

</div>

## 范围

mosaickit 负责与领域无关的场景组合、样式、主题、参数绑定、网格布局、动画帧、渲染器接口，
以及静态与动态输出。领域语义则属于构造在它之上的包。曲线构造与原生 TikZ 路径生成，
属于 [bezierkit](../bezierkit/index.md) 这类几何包的工作。

## 安装

```bash
uv add mosaickit
```

需要 Python 3.10 以上。可选功能与开发环境请见[安装](installation.md)，或直接看[快速入门](quickstart.md)。

<!-- agora-navigation -->

## 文档导航

以下章节涵盖 mosaickit 0.5.1。

- [简介](guides/introduction.md)
- [安装](installation.md)
- [快速入门](quickstart.md)
- [画布与场景](guides/canvas.md)
- [图层与坐标轴](guides/layers.md)
- [坐标轴注释](guides/annotations.md)
- [布局几何](guides/geometry.md)
- [区域标签与点标签](guides/labels.md)
- [样式与颜色](guides/styles.md)
- [主题与配置](guides/themes.md)
- [参数、网格与动画](guides/parameters.md)
- [绘制](guides/rendering.md)
- [证明](project/proofs.md)
- [更新记录](project/changelog.md)

<!-- /agora-navigation -->
