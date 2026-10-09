---
seo_title: "mosaickit：與領域無關的圖形場景與渲染工具組"
description: "mosaickit 是與領域無關的 Python 工具組，用場景、圖層、樣式、參數與渲染器組合出二維圖形。"
---

<h1 class="ev-visually-hidden">mosaickit：與領域無關的圖形場景與渲染</h1>

<p align="center">
  <img src="../../assets/mosaickit/banner.svg" alt="mosaickit" style="max-width: 480px; width: 100%; margin: 2rem 0 1rem;">
</p>

<p align="center"><em>與領域無關的 Python 工具組，用來組合二維圖形。</em></p>

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

-   :material-layers-outline: **精簡的場景圖**

    `PathLayer`、`FillLayer`、`MarkerLayer`、`TextLayer`、`ArrowLayer`、`LegendLayer` 與 `GroupLayer`。

-   :material-label-outline: **不遮住圖形的標籤**

    `RegionLabelLayer` 與 `PointLabelLayer` 自動避開圖形，另有軸上標記、註記與大括號。

-   :material-axis-arrow: **座標軸輔助函式**

    `quadrant_axes()`、`crosshair_axes()` 與 `box_frame()` 快速建立常見的座標框架。

-   :material-palette-outline: **樣式與主題**

    樣式、主題與調色盤，顏色可直接用名稱指定。

-   :material-view-grid-outline: **參數與格狀排版**

    參數與運算式、`CanvasGrid` 版面與 `Animation` 掃描。

-   :material-file-image-outline: **可替換的渲染器**

    內建 Matplotlib 渲染器輸出 PNG、SVG 與 PDF，並提供 `Renderer` 協定供其他後端使用。

</div>

## 範圍

mosaickit 負責與領域無關的場景組合、樣式、主題、參數綁定、網格排版、動畫影格、渲染器介面，
以及靜態與動態輸出。領域語意則屬於建構在它之上的套件。曲線建構與原生 TikZ 路徑產生，
屬於 [bezierkit](../bezierkit/index.md) 這類幾何套件的工作。

## 安裝

```bash
uv add mosaickit
```

需要 Python 3.10 以上。選用功能與開發環境請見[安裝](installation.md)，或直接看[快速入門](quickstart.md)。

<!-- agora-navigation -->

## 文件導覽

以下章節涵蓋 mosaickit 0.5.1。

- [簡介](guides/introduction.md)
- [安裝](installation.md)
- [快速入門](quickstart.md)
- [畫布與場景](guides/canvas.md)
- [圖層與座標軸](guides/layers.md)
- [座標軸註記](guides/annotations.md)
- [配置幾何](guides/geometry.md)
- [區域標籤與點標籤](guides/labels.md)
- [樣式與顏色](guides/styles.md)
- [主題與設定](guides/themes.md)
- [參數、網格與動畫](guides/parameters.md)
- [繪製](guides/rendering.md)
- [證明](project/proofs.md)
- [更新紀錄](project/changelog.md)

<!-- /agora-navigation -->
