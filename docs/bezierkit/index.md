---
seo_title: "bezierkit: Bézier Curve Toolkit for Python"
description: "bezierkit is a small, renderer-independent Python toolkit for constructing, evaluating, fitting and exporting Bézier curves, with native SVG and TikZ output and proofs for every theorem it relies on."
---

<h1 class="ev-visually-hidden">bezierkit: Bézier curve toolkit for Python</h1>

<p align="center">
  <img src="../assets/bezierkit/banner.svg" alt="bezierkit" style="max-width: 480px; width: 100%; margin: 2rem 0 1rem;">
</p>

<p align="center"><em>A small, renderer-independent Python toolkit for Bézier curves.</em></p>

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

## Features

<div class="grid cards" markdown>

-   :material-vector-bezier: **Curves of any degree**

    `BezierCurve`, `CubicBezierSegment` and `PiecewiseBezier`, with immutable `Point`, `Vector` and `PointSet` value objects.

    [:octicons-arrow-right-24: Bézier curves](guides/curves.md)

-   :material-function-variant: **Evaluation and subdivision**

    Evaluate with de Casteljau's algorithm, then differentiate, split, restrict and reverse a curve.

    [:octicons-arrow-right-24: Derivatives and subdivision](guides/operations.md)

-   :material-chart-bell-curve: **Construction from slopes**

    Build a cubic from end points and end slopes with `PlanarSlopes`, or from Hermite data.

    [:octicons-arrow-right-24: Constructions](guides/construction.md)

-   :material-vector-polyline: **Fitting and level sets**

    Adaptive fitting of a function graph with a measured error, polyline simplification, and tracing of implicit level sets.

    [:octicons-arrow-right-24: Fitting](guides/fitting.md)

-   :material-export: **Native export**

    A versioned JSON format, SVG cubic path data and TikZ `controls` commands, never flattened into line pieces.

    [:octicons-arrow-right-24: Sampling and export](guides/export.md)

-   :material-console: **Optional extras**

    A Matplotlib path adapter and a command line interface.

    [:octicons-arrow-right-24: Command line](cli.md)

</div>

## Mathematics and proofs

The guides state the properties the algorithms rely on as theorems: what the Bernstein basis guarantees, why de
Casteljau's algorithm evaluates and subdivides a curve, how far a Hermite interpolant can stray, and what the exporters
lose to rounding. Every proof is folded under its theorem, so the pages read as API documentation until you open one.
The standard references are Farin (2002) and Prautzsch et al. (2002); see [References](project/references.md).

!!! abstract "Notation"

    A point lives in $\mathbb{R}^d$ for some $d \ge 1$; most figures use $d = 2$. A Bézier curve of degree $n$ has
    $n + 1$ control points $P_0, \dots, P_n$ and is the map

    $$
    B(t) = \sum_{i=0}^{n} b_{i,n}(t)\, P_i, \qquad t \in [0, 1],
    $$

    where $b_{i,n}(t) = \binom{n}{i} t^i (1-t)^{n-i}$ are the Bernstein polynomials. Every curve in the package is
    parameterized over $[0, 1]$; a parameter outside it raises `ParameterOutOfDomain`.

## Reading guide

| Topic | Page |
|---|---|
| Points, vectors, parameters, errors | [Geometry values](guides/geometry.md) |
| Bernstein basis, curves, evaluation | [Bézier curves](guides/curves.md) |
| Derivatives, subdivision, reversal | [Derivatives and subdivision](guides/operations.md) |
| Cubic segments and piecewise paths | [Cubic segments and paths](guides/paths.md) |
| Constructions and Hermite interpolation | [Constructions](guides/construction.md) |
| Fitting functions and polylines | [Fitting](guides/fitting.md) |
| Tracing level sets | [Level sets](guides/implicit.md) |
| Sampling, JSON, SVG, TikZ, Matplotlib | [Sampling and export](guides/export.md) |
| Command line | [Command line](cli.md) |

On first use, read the [Quick start](quickstart.md) and [Bézier curves](guides/curves.md).

!!! warning "Scope"

    Rendering style and diagram semantics are intentionally outside this package: it draws nothing. Intersections,
    B-splines and NURBS are future work.

## Install

```bash
uv add bezierkit
```

Requires Python 3.10 or later. See [Installation](installation.md) for extras and the development setup, or go straight to the [Quick start](quickstart.md).

<!-- agora-navigation -->

## Documentation

The following chapters cover bezierkit 1.0.0.

- [Introduction](guides/introduction.md)
- [Installation](installation.md)
- [Quick start](quickstart.md)
- [Geometry values](guides/geometry.md)
- [Bézier curves](guides/curves.md)
- [Derivatives, reversal and subdivision](guides/operations.md)
- [Cubic segments and paths](guides/paths.md)
- [Constructions and Hermite interpolation](guides/construction.md)
- [Fitting](guides/fitting.md)
- [Level sets](guides/implicit.md)
- [Sampling and export](guides/export.md)
- [Command-line interface](cli.md)
- [Proofs](project/proofs.md)
- [Approximation proofs](project/proofs-approximation.md)
- [Change history](project/changelog.md)

<!-- /agora-navigation -->
