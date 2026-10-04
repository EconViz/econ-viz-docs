---
seo_title: "bezierkit 快速开始"
description: "计算并分割三次贝塞尔曲线、由斜率构造曲线、导出 SVG 与 TikZ，以及使用 bezierkit 命令行。"
---

# 快速开始

以下输出都是以 bezierkit 0.5.0rc1 实际运行代码的结果。

## 求值、分割与采样

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

输出：

```text
Point(coords=(2.0, 1.5))
Point(coords=(4.5, 0.0))
True
200 sample points
```

`curve.at(t)` 在参数 `t`（范围 `[0, 1]`）算出曲线上的点，`curve.derivative()` 返回导数曲线，
`split` 则把曲线切成两段。采样结果也提供 `t`、`x` 与 `y` 数组。

## 由斜率构造曲线

`PlanarSlopes` 根据两个端点，以及两端各自想要的斜率（dy/dx）构造三次曲线。

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

# 两端的切线斜率（dy/dx）与指定值一致。
d = demand.derivative()
for t in (0.0, 1.0):
    dx, dy = d.at(t).coords
    print(f"t={t}: dy/dx = {dy / dx:.2f}")
```

输出：

```text
Point(coords=(0.0, 5.0)) Point(coords=(5.0, 0.0))
t=0.0: dy/dx = -2.00
t=1.0: dy/dx = -0.30
```

## 导出 SVG 与 TikZ

`PiecewiseBezier` 把多段三次曲线首尾相接。SVG 与 TikZ 导出器直接输出三次曲线的几何，不会先把它压平。

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

输出：

```text
Point(coords=(2.0, 2.0))
M 0.00000 0.00000 C 0.66667 0.00000 1.33333 0.00000 2.00000 0.00000 C 2.00000 1.33333 2.00000 2.66667 2.00000 4.00000
\draw[thick] (0.00000,0.00000) .. controls (0.66667,0.00000) and (1.33333,0.00000) .. (2.00000,0.00000) .. controls (2.00000,1.33333) and (2.00000,2.66667) .. (2.00000,4.00000);
```

## 命令行

安装 `cli` 额外依赖后，可以直接在 shell 对同一条曲线采样：

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

运行 `bezierkit --help` 可查看完整的命令树。
