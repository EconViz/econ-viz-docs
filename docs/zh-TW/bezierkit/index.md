---
seo_title: "bezierkit：Python 貝茲曲線工具組"
description: "bezierkit 是小巧、與渲染器無關的 Python 工具組，用來建構、計算、擬合與匯出貝茲曲線，並原生支援 SVG 與 TikZ 輸出。"
---

# bezierkit

`bezierkit` 是小巧的數學工具組，用來建構與分析貝茲曲線（Bézier curve）。

它與渲染器無關：只提供曲線的建構、求值、細分與取樣，繪圖則交給 Matplotlib、SVG 或 TikZ 等使用端處理。

!!! note "預先發行版"

    bezierkit 0.5.0rc1 是候選版本（release candidate），請用 `pip install --pre bezierkit` 安裝
    （見[安裝](installation.md)）。

| | |
|---|---|
| 本文件對應版本 | 0.5.0rc1 |
| Python | 3.10 以上 |
| 依賴 | numpy（選用額外功能：`cli`、`matplotlib`） |
| 使用者 | [utility-viz](../utility-viz/index.md)，用於曲線與 TikZ 輸出 |
| 原始碼 | [github.com/EconViz/bezierkit](https://github.com/EconViz/bezierkit) |
| 授權 | MIT |

## 功能範圍

- 任意次數與維度的曲線：`BezierCurve`、`CubicBezierSegment` 與 `PiecewiseBezier`，
  搭配不可變的 `Point`、`Vector` 與 `PointSet`
- 求值、導數、分割與均勻取樣
- 由平面斜率建構曲線（`bezierkit.construction.PlanarSlopes`）
- 插值、函數圖形的自適應擬合，以及隱函數等值線的追蹤
- 匯出器：具版本的 JSON 格式、原生 SVG 三次路徑資料，以及原生 TikZ `controls` 指令
- 選用的 Matplotlib 路徑轉接器與命令列工具

## 範圍

繪圖樣式與圖形語意刻意不在這個套件的範圍內。交點、B 樣條與 NURBS 屬於未來的工作。

## 接下來

<div class="grid cards" markdown>

-   :material-download: **安裝**

    用 pip 或 uv 安裝預先發行版。

    [:octicons-arrow-right-24: 安裝](installation.md)

-   :material-rocket-launch-outline: **快速開始**

    計算曲線、匯出 SVG 與 TikZ，並使用命令列。

    [:octicons-arrow-right-24: 快速開始](quickstart.md)

</div>
