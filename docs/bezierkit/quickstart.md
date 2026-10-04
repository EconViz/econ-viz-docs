---
seo_title: "bezierkit Quick Start"
description: "Evaluate and split a cubic Bézier curve, build one from slopes, export SVG and TikZ, and use the bezierkit command line."
---

# Quick Start

Every output below comes from running the code with bezierkit 0.5.0rc1.

## Evaluate, split and sample a curve

```python
from bezierkit import BezierCurve, Point
from bezierkit.sampling import UniformSampler

curve = BezierCurve.cubic(
    Point(0, 0),
    Point(1, 2),
    Point(3, 2),
    Point(4, 0),
)

print(curve.at(0.5))
print(curve.derivative().at(0.5))

left, right = curve.split(0.3)
print(left.at(1.0) == right.at(0.0))

sample = UniformSampler(200).sample(curve)
print(len(sample.points), "sample points")
```

Output:

```text
Point(coords=(2.0, 1.5))
Point(coords=(4.5, 0.0))
True
200 sample points
```

`curve.at(t)` evaluates the curve at parameter `t` in `[0, 1]`, `curve.derivative()` returns the derivative curve, and
`split` cuts the curve in two. The sample also exposes its `t`, `x` and `y` arrays.

## Build a curve from slopes

`PlanarSlopes` constructs a cubic from two end points and the slope (dy/dx) wanted at each end.

```python
from bezierkit import Point
from bezierkit.construction import PlanarSlopes

demand = PlanarSlopes(
    start=Point(0, 5),
    end=Point(5, 0),
    start_slope=-2,
    end_slope=-0.3,
).build()

print(demand.at(0.0), demand.at(1.0))

# The tangent at each end follows the requested slope (dy/dx).
d = demand.derivative()
for t in (0.0, 1.0):
    dx, dy = d.at(t).coords
    print(f"t={t}: dy/dx = {dy / dx:.2f}")
```

Output:

```text
Point(coords=(0.0, 5.0)) Point(coords=(5.0, 0.0))
t=0.0: dy/dx = -2.00
t=1.0: dy/dx = -0.30
```

## Export to SVG and TikZ

A `PiecewiseBezier` joins cubic segments end to end. The SVG and TikZ exporters write the cubic geometry natively,
without flattening it.

```python
from bezierkit import CubicBezierSegment, PiecewiseBezier, Point
from bezierkit.export.svg import to_svg_path_data
from bezierkit.export.tikz import to_tikz

path = PiecewiseBezier([
    CubicBezierSegment.from_line(Point(0, 0), Point(2, 0)),
    CubicBezierSegment.from_line(Point(2, 0), Point(2, 4)),
])
print(path.at(0.75))
print(to_svg_path_data(path, precision=5))
print(to_tikz(path, precision=5, options="thick"))
```

Output:

```text
Point(coords=(2.0, 2.0))
M 0.00000 0.00000 C 0.66667 0.00000 1.33333 0.00000 2.00000 0.00000 C 2.00000 1.33333 2.00000 2.66667 2.00000 4.00000
\draw[thick] (0.00000,0.00000) .. controls (0.66667,0.00000) and (1.33333,0.00000) .. (2.00000,0.00000) .. controls (2.00000,1.33333) and (2.00000,2.66667) .. (2.00000,4.00000);
```

## Command line

With the `cli` extra installed, the same curve can be sampled from the shell:

```bash
bezierkit sample \
  --points "0,0" --points "1,2" --points "3,2" --points "4,0" \
  --count 5 --format csv
```

```text
t,x,y
0.0,0.0,0.0
0.25,0.90625,1.125
0.5,2.0,1.5
0.75,3.09375,1.125
1.0,4.0,0.0
```

Run `bezierkit --help` for the complete command tree.
