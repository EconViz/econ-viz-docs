---
seo_title: "bezierkit：Python 贝塞尔曲线工具包"
description: "bezierkit 是小巧、与渲染器无关的 Python 工具包，用来构造、计算、拟合与导出贝塞尔曲线，并原生支持 SVG 与 TikZ 输出。"
---

# bezierkit

`bezierkit` 是小巧的数学工具包，用来构造与分析贝塞尔曲线（Bézier curve）。

它与渲染器无关：只提供曲线的构造、求值、细分与采样，绘图则交给 Matplotlib、SVG 或 TikZ 等使用方处理。

!!! note "预发布版本"

    bezierkit 0.5.0rc1 是候选版本（release candidate），请用 `pip install --pre bezierkit` 安装
    （见[安装](installation.md)）。

| | |
|---|---|
| 本文档对应版本 | 0.5.0rc1 |
| Python | 3.10 以上 |
| 依赖 | numpy（可选的额外依赖：`cli`、`matplotlib`） |
| 被谁使用 | [utility-viz](../utility-viz/index.md)，用于曲线与 TikZ 输出 |
| 源代码 | [github.com/EconViz/bezierkit](https://github.com/EconViz/bezierkit) |
| 许可证 | MIT |

## 功能范围

- 任意次数与维度的曲线：`BezierCurve`、`CubicBezierSegment` 与 `PiecewiseBezier`，
  搭配不可变的 `Point`、`Vector` 与 `PointSet`
- 求值、导数、分割与均匀采样
- 由平面斜率构造曲线（`bezierkit.construction.PlanarSlopes`）
- 插值、函数图形的自适应拟合，以及隐函数等值线的追踪
- 导出器：具版本的 JSON 格式、原生 SVG 三次路径数据，以及原生 TikZ `controls` 命令
- 可选的 Matplotlib 路径适配器与命令行工具

## 范围

绘图样式与图形语义刻意不在这个包的范围内。交点、B 样条与 NURBS 属于未来的工作。

## 接下来

<div class="grid cards" markdown>

-   :material-download: **安装**

    用 pip 或 uv 安装预发布版本。

    [:octicons-arrow-right-24: 安装](installation.md)

-   :material-rocket-launch-outline: **快速开始**

    计算曲线、导出 SVG 与 TikZ，并使用命令行。

    [:octicons-arrow-right-24: 快速开始](quickstart.md)

</div>
