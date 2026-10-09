---
seo_title: "Quick start"
---

# Quick start

<span id="sec-quickstart"></span>

## A cubic curve

The curve used throughout this manual is the cubic with control points
$(0, 0)$, $(1, 2)$, $(3, 2)$ and $(4, 0)$ ([The cubic of [Quick start](quickstart.md#sec-quickstart), its control polygon and convex hull.](quickstart.md#fig-quickstart)).

```python
from bezierkit import BezierCurve, PiecewiseBezier, Point
from bezierkit.bezier import to_cubic
from bezierkit.export.tikz import to_tikz

curve = BezierCurve.cubic(
    Point(0, 0), Point(1, 2), Point(3, 2), Point(4, 0)
)
# Point(coords=(2.0, 1.5))
print(curve.at(0.5))
# Point(coords=(4.5, 0.0))
print(curve.derivative().at(0.5))
# two cubics that together trace curve
left, right = curve.split(0.4)

path = PiecewiseBezier([to_cubic(curve)])
print(to_tikz(path, precision=2, options="thick"))
# \draw[thick] (0.00,0.00) .. controls (1.00,2.00) and (3.00,2.00) .. (4.00,0.00);
```

<span id="fig-quickstart"></span>

![The cubic of [Quick start](quickstart.md#sec-quickstart), its control polygon and convex hull.](../assets/bezierkit/agora/curves/cubic.svg){ .ev-figure-sm }

The curve starts at $P_0$ and ends at $P_3$, leaves $P_0$ towards $P_1$ and
arrives at $P_3$ from $P_2$, and never leaves the shaded hull of its control
points ([Convex hull](guides/curves.md#cor-hull)). The last line is the curve as a TikZ path, ready to paste
into a LaTeX document.

## The pieces

- *Values.* `Point`, `Vector` and `PointSet` are immutable and
  dimension-checked ([Geometry values](guides/geometry.md#sec-geometry)).
- *Curves.* `BezierCurve` has any degree and dimension;
  `CubicBezierSegment` is the cubic that renderers consume; a
  `PiecewiseBezier` joins cubics into a path ([Bézier curves](guides/curves.md#sec-curves), [Cubic segments and paths](guides/paths.md#sec-paths)).
- *Constructions.* Endpoint conditions, slopes, derivatives or Hermite data
  become control points ([Constructions and Hermite interpolation](guides/construction.md#sec-construction)).
- *Approximation.* Smooth functions, sampled points and level sets
  $F(x, y) = c$ become cubic paths with a stated error ([Fitting](guides/fitting.md#sec-fitting),
  [Level sets](guides/implicit.md#sec-implicit)).
- *Output.* Samples, JSON, SVG path data and TikZ, and Matplotlib paths
  ([Sampling and export](guides/export.md#sec-export)).
