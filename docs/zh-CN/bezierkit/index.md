---
seo_title: "bezierkit：Python 贝塞尔曲线工具包"
description: "bezierkit 是小巧、与渲染器无关的 Python 工具包，用来构造、计算、拟合与导出贝塞尔曲线，并原生支持 SVG 与 TikZ 输出，每个依据的定理都附有证明。"
---

<h1 class="ev-visually-hidden">bezierkit：Python 贝塞尔曲线工具包</h1>

<p align="center">
  <img src="../../assets/bezierkit/banner.svg" alt="bezierkit" style="max-width: 480px; width: 100%; margin: 2rem 0 1rem;">
</p>

<p align="center"><em>小巧且与渲染器无关的贝塞尔曲线 Python 包。</em></p>

<p align="center">
  <a href="https://pypi.org/project/bezierkit/"><img alt="PyPI" src="https://img.shields.io/pypi/v/bezierkit?style=flat-square&label=pypi+package&color=181818&labelColor=f3f3f3&cacheSeconds=300"></a>
  <a href="https://pypi.org/project/bezierkit/"><img alt="Python" src="https://img.shields.io/pypi/pyversions/bezierkit?style=flat-square&color=181818&labelColor=f3f3f3"></a>
  <a href="https://opensource.org/licenses/MIT"><img alt="License" src="https://img.shields.io/badge/License-MIT-181818?style=flat-square&color=181818&labelColor=f3f3f3"></a>
</p>

```python
from bezierkit import BezierCurve, Point
from bezierkit.sampling import UniformSampler

curve = BezierCurve.cubic(
    Point(0, 0),
    Point(1, 2),
    Point(3, 2),
    Point(4, 0),
)

# Point(coords=(2.0, 1.5))
print(curve.at(0.5))

# cut the curve in two
left, right = curve.split(0.3)

sample = UniformSampler(200).sample(curve)
print(len(sample.points), "sample points")
```

## 功能特色

<div class="grid cards" markdown>

-   :material-vector-bezier: **任意次数的曲线**

    `BezierCurve`、`CubicBezierSegment` 与 `PiecewiseBezier`，搭配不可变的 `Point`、`Vector` 与 `PointSet` 值对象。

    [:octicons-arrow-right-24: Bézier 曲线](guides/curves.md)

-   :material-function-variant: **求值与分割**

    以 de Casteljau 算法求值，并对曲线求导、分割、截取与反转。

    [:octicons-arrow-right-24: 导数、分割与反转](guides/operations.md)

-   :material-chart-bell-curve: **由斜率构造**

    用 `PlanarSlopes` 由端点与端点斜率构造三次曲线，或由 Hermite 数据构造。

    [:octicons-arrow-right-24: 构造与 Hermite 插值](guides/construction.md)

-   :material-vector-polyline: **拟合与等值线**

    函数图形的自适应拟合与实测误差、折线简化，以及隐函数等值线的描绘。

    [:octicons-arrow-right-24: 拟合](guides/fitting.md)

-   :material-export: **原生导出**

    具版本的 JSON 格式、SVG 三次路径数据与 TikZ `controls` 命令，不会摊平成折线。

    [:octicons-arrow-right-24: 采样与导出](guides/export.md)

-   :material-console: **选用功能**

    Matplotlib 路径适配器与命令行工具。

    [:octicons-arrow-right-24: 命令行](cli.md)

</div>

## 数学与证明

指南把算法所依据的性质写成定理：Bernstein 基底的保证、de Casteljau 算法为何能求值并分割曲线、Hermite 插值最多偏离多少，以及导出器因四舍五入损失多少精度。每个证明都折叠在定理下方，点开才会展开，因此页面平常读起来就是 API 文档。标准参考书为 Farin (2002) 与 Prautzsch 等人 (2002)，见[参考文献](project/references.md)。

!!! abstract "符号"

    点位于某个维度 $d \ge 1$ 的 $\mathbb{R}^d$ 中；多数图使用 $d = 2$。$n$ 次 Bézier 曲线有 $n + 1$ 个控制点
    $P_0, \dots, P_n$，定义为映射

    $$
    B(t) = \sum_{i=0}^{n} b_{i,n}(t)\, P_i, \qquad t \in [0, 1],
    $$

    其中 $b_{i,n}(t) = \binom{n}{i} t^i (1-t)^{n-i}$ 为 Bernstein 多项式。软件包中每条曲线的参数范围都是 $[0, 1]$；
    超出范围的参数会抛出 `ParameterOutOfDomain`。

## 阅读指引

| 主题 | 页面 |
|---|---|
| 点、向量、参数、例外 | [几何数值对象](guides/geometry.md) |
| Bernstein 基底、曲线、求值 | [Bézier 曲线](guides/curves.md) |
| 导数、分割、反转 | [导数、分割与反转](guides/operations.md) |
| 三次线段与分段路径 | [三次线段与路径](guides/paths.md) |
| 构造与 Hermite 插值 | [构造与 Hermite 插值](guides/construction.md) |
| 拟合函数与折线 | [拟合](guides/fitting.md) |
| 描绘等值线 | [等值线](guides/implicit.md) |
| 采样、JSON、SVG、TikZ、Matplotlib | [采样与导出](guides/export.md) |
| 命令行 | [命令行](cli.md) |

初次使用时，先读[快速开始](quickstart.md)与 [Bézier 曲线](guides/curves.md)。

!!! warning "范围"

    绘图样式与图形语意刻意不在这个软件包的范围内：它本身不绘图。交点、B 样条与 NURBS 属于未来的工作。

## 安装

```bash
uv add bezierkit
```

需要 Python 3.10 以上。选用功能与开发环境请见[安装](installation.md)，或直接看[快速入门](quickstart.md)。

<!-- agora-navigation -->

## 文档导航

以下章节涵盖 bezierkit 1.0.0。

- [简介](guides/introduction.md)
- [安装](installation.md)
- [快速开始](quickstart.md)
- [几何数值对象](guides/geometry.md)
- [Bézier 曲线](guides/curves.md)
- [导数、反转与分割](guides/operations.md)
- [三次线段与路径](guides/paths.md)
- [建构与 Hermite 插值](guides/construction.md)
- [拟合](guides/fitting.md)
- [等值线](guides/implicit.md)
- [采样与导出](guides/export.md)
- [命令行界面](cli.md)
- [证明](project/proofs.md)
- [近似方法的证明](project/proofs-approximation.md)
- [更新纪录](project/changelog.md)

<!-- /agora-navigation -->
