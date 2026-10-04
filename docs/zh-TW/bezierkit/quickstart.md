---
seo_title: "bezierkit 快速開始"
description: "計算並分割三次貝茲曲線、由斜率建構曲線、匯出 SVG 與 TikZ，以及使用 bezierkit 命令列。"
---

# 快速開始

以下輸出都是以 bezierkit 0.5.0rc1 實際執行程式碼的結果。

## 求值、分割與取樣

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

輸出：

```text
Point(coords=(2.0, 1.5))
Point(coords=(4.5, 0.0))
True
200 sample points
```

`curve.at(t)` 在參數 `t`（範圍 `[0, 1]`）求出曲線上的點，`curve.derivative()` 回傳導數曲線，
`split` 則把曲線切成兩段。取樣結果也提供 `t`、`x` 與 `y` 陣列。

## 由斜率建構曲線

`PlanarSlopes` 根據兩個端點，以及兩端各自想要的斜率（dy/dx）建構三次曲線。

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

# 兩端的切線斜率（dy/dx）與指定值一致。
d = demand.derivative()
for t in (0.0, 1.0):
    dx, dy = d.at(t).coords
    print(f"t={t}: dy/dx = {dy / dx:.2f}")
```

輸出：

```text
Point(coords=(0.0, 5.0)) Point(coords=(5.0, 0.0))
t=0.0: dy/dx = -2.00
t=1.0: dy/dx = -0.30
```

## 匯出 SVG 與 TikZ

`PiecewiseBezier` 把多段三次曲線首尾相接。SVG 與 TikZ 匯出器直接輸出三次曲線的幾何，不會先把它壓平。

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

輸出：

```text
Point(coords=(2.0, 2.0))
M 0.00000 0.00000 C 0.66667 0.00000 1.33333 0.00000 2.00000 0.00000 C 2.00000 1.33333 2.00000 2.66667 2.00000 4.00000
\draw[thick] (0.00000,0.00000) .. controls (0.66667,0.00000) and (1.33333,0.00000) .. (2.00000,0.00000) .. controls (2.00000,1.33333) and (2.00000,2.66667) .. (2.00000,4.00000);
```

## 命令列

安裝 `cli` 額外功能後，可以直接在 shell 對同一條曲線取樣：

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

執行 `bezierkit --help` 可查看完整的指令樹。
