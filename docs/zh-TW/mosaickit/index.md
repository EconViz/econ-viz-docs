---
seo_title: "mosaickit：與領域無關的圖形場景與渲染工具組"
description: "mosaickit 是與領域無關的 Python 工具組，用場景、圖層、樣式、參數與渲染器組合出二維圖形。"
---

# mosaickit

`mosaickit` 是與領域無關的工具組，用可重複使用的場景、圖層、樣式、參數與渲染器組合出二維圖形。

領域套件負責定義自己的模型與語意角色，mosaickit 則負責組合它們的視覺圖層並完成渲染。
mosaickit 對任何領域一無所知，也不依賴模型套件或曲線擬合套件。

![用 mosaickit 圖層組成的圖形](../../assets/mosaickit/diagram.svg){ width="360" }

| | |
|---|---|
| 本文件對應版本 | 0.5.1 |
| Python | 3.10 以上（專案支援 3.10 至 3.13） |
| 依賴 | numpy、matplotlib（Python 3.10 另需 tomli） |
| 使用者 | [utility-viz](../utility-viz/index.md)、[principle-viz](../principle-viz/index.md) |
| 原始碼 | [github.com/EconViz/mosaickit](https://github.com/EconViz/mosaickit) |
| 授權 | MIT |

## 功能範圍

- 精簡的場景圖：`PathLayer`、`FillLayer`、`MarkerLayer`、`TextLayer`、`ArrowLayer`、`LegendLayer` 與 `GroupLayer`
- 不會壓到其他元素的標籤（`RegionLabelLayer`、`PointLabelLayer`），以及座標軸上的標註
  （`AxisMarkLayer`、`AxisNoteLayer`、`BraceLayer`、`SpanBraceLayer`）
- 座標軸輔助函式，例如 `quadrant_axes()`、`crosshair_axes()` 與 `box_frame()`
- 樣式、主題與調色盤，顏色可以用名稱指定
- 參數與運算式、`CanvasGrid` 網格排版，以及 `Animation` 動畫掃描
- 內建的 Matplotlib 渲染器（輸出 PNG、SVG、PDF），並提供 `Renderer` 協定以接入其他後端

## 範圍

mosaickit 負責與領域無關的場景組合、樣式、主題、參數綁定、網格排版、動畫影格、渲染器介面，
以及靜態與動態輸出。領域語意則屬於建構在它之上的套件。曲線建構與原生 TikZ 路徑產生，
屬於 [bezierkit](../bezierkit/index.md) 這類幾何套件的工作。

## 接下來

<div class="grid cards" markdown>

-   :material-download: **安裝**

    用 pip 或 uv 安裝套件。

    [:octicons-arrow-right-24: 安裝](installation.md)

-   :material-rocket-launch-outline: **快速開始**

    用圖層組出畫布，並存成 SVG。

    [:octicons-arrow-right-24: 快速開始](quickstart.md)

</div>
