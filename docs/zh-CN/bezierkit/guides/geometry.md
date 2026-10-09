---
seo_title: "几何数值对象"
---

# 几何数值对象

<span id="sec-geometry"></span>

所有数值对象都不可变，运算会返回新对象。坐标必须为有限值；创建对象时遇到 NaN 或无穷大会抛出 `ValueError`。

## 点与向量

<!-- api: agora.bezierkit.guides_geometry_1 -->

$\mathbb{R}^d$ 中的点或向量，由 $d \ge 1$ 个坐标给定。点与向量按仿射几何的规则运算（参见[点与向量的运算](geometry.md#tab-point-arithmetic)）。

<span id="tab-point-arithmetic"></span>

| 表达式 | 结果 |
| --- | --- |
| `point - point` | `Vector` |
| `point + vector`、`point - vector` | `Point` |
| `vector + vector`、`vector * scalar` | `Vector`；也可写成 `scalar * vector` |

维度不同时抛出 `DimensionMismatch`。`point + point` 不会被拒绝：它把坐标相加并返回 `Point`，只有在权重总和为一的组合中才有意义，例如 de Casteljau 算法中的平均。

```python
from bezierkit import Point, Vector

p = Point(1, 2)
# Point(coords=(7.0, 0.0))
q = p + Vector(3, -1) * 2
# Vector(coords=(6.0, -2.0))
v = q - p
# 6.324555320336759
print(v.norm())
```

## 点集合

<!-- api: agora.bezierkit.guides_geometry_2 -->

一批不可变的点，背后是只读的 $(\text{count}, d)$ NumPy 数组，批量求值与采样都返回此对象。提供 `count`、`dimension`、`array`（只读副本）、各栏 `x`、`y`、`z`，可逐个取出 `Point`，也可用索引存取。

## 参数

<!-- api: agora.bezierkit.guides_geometry_3 -->

`Interval(start, end)` 是闭区间，提供 `contains()`、`clamp()` 与 `linspace()`。

<!-- api: agora.bezierkit.guides_geometry_4 -->

由定义域检查单一参数或一维参数数组。每条曲线都使用它，因此对定义域为 $[0, 1]$ 的曲线调用 `at(1.2)` 会抛出 `ParameterOutOfDomain`。

## 异常

| 异常 | 抛出时机 |
| --- | --- |
| `BezierKitError` | 下列异常的基础类 |
| `DimensionMismatch` | 组合不同维度的点、向量或线段 |
| `DegreeError` | 曲线次数不适用于某项运算，或没有控制点 |
| `ParameterOutOfDomain` | 参数超出曲线定义域 $[0, 1]$ |
| `ToleranceNotMet` | 自适应拟合在限制内无法达到容差（详见[拟合](fitting.md#sec-fitting)） |

不属于几何的无效参数（例如负的容差）抛出 `ValueError`。
