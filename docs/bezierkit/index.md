---
seo_title: "bezierkit: Bézier Curve Toolkit for Python"
description: "bezierkit is a small, renderer-independent Python toolkit for constructing, evaluating, fitting and exporting Bézier curves, with native SVG and TikZ output."
---

# bezierkit

`bezierkit` is a small mathematical toolkit for constructing and analyzing Bézier curves.

It is renderer-independent: it provides curve construction, evaluation, subdivision and sampling, and leaves
plotting to consumers such as Matplotlib, SVG or TikZ.

!!! note "Pre-release"

    bezierkit 0.5.0rc1 is a release candidate. Install it with `pip install --pre bezierkit` (see
    [Installation](installation.md)).

| | |
|---|---|
| Documented version | 0.5.0rc1 |
| Python | 3.10 or later |
| Dependencies | numpy (optional extras: `cli`, `matplotlib`) |
| Used by | [utility-viz](../utility-viz/index.md), for curves and TikZ output |
| Source | [github.com/EconViz/bezierkit](https://github.com/EconViz/bezierkit) |
| License | MIT |

## What it covers

- Curves of arbitrary degree and dimension: `BezierCurve`, `CubicBezierSegment` and `PiecewiseBezier`, with
  immutable `Point`, `Vector` and `PointSet` value objects
- Evaluation, derivatives, splitting and uniform sampling
- Curve construction from planar slopes (`bezierkit.construction.PlanarSlopes`)
- Interpolation, adaptive fitting of a function graph, and tracing of implicit level sets
- Exporters for a versioned JSON format, native SVG cubic path data and native TikZ `controls` commands
- An optional Matplotlib path adapter and an optional command line interface

## Scope

Rendering style and diagram semantics are intentionally outside this package. Intersections, B-splines and NURBS
are future work.

## Next steps

<div class="grid cards" markdown>

-   :material-download: **Installation**

    Install the pre-release with pip or uv.

    [:octicons-arrow-right-24: Installation](installation.md)

-   :material-rocket-launch-outline: **Quick start**

    Evaluate a curve, export it as SVG and TikZ, and use the command line.

    [:octicons-arrow-right-24: Quick start](quickstart.md)

</div>
