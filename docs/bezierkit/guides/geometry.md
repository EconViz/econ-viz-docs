---
seo_title: "Geometry values"
---

# Geometry values

<span id="sec-geometry"></span>

All values are immutable: operations return new objects. Coordinates must be
finite; NaN and infinities raise `ValueError` when a value is created.

## Points and vectors

<!-- api: agora.bezierkit.guides_geometry_1 -->

A point or a vector in $\mathbb{R}^d$, given by its $d \ge 1$ coordinates. Points
and vectors combine as in affine geometry ([Arithmetic of points and vectors](geometry.md#tab-point-arithmetic)).

<span id="tab-point-arithmetic"></span>

| Expression | Result |
| --- | --- |
| `point - point` | A `Vector` |
| `point + vector`, `point - vector` | A `Point` |
| `vector + vector`, `vector * scalar` | A `Vector`; `scalar * vector` works too |

Mixing dimensions raises `DimensionMismatch`. `point + point` is not
rejected: it adds the coordinates and returns a `Point`, which is meaningful
only in combinations whose weights sum to one, such as the averages inside
de Casteljau's algorithm.

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

## Point sets

<!-- api: agora.bezierkit.guides_geometry_2 -->

An immutable batch of points backed by a read-only $(\text{count}, d)$ NumPy
array, as returned by batch evaluation and sampling. It offers `count`,
`dimension`, `array` (a read-only copy), the columns `x`, `y`, `z`,
iteration over `Point`s and indexing.

## Parameters

<!-- api: agora.bezierkit.guides_geometry_3 -->

`Interval(start, end)` is a closed interval with `contains()`, `clamp()`
and `linspace()`.

<!-- api: agora.bezierkit.guides_geometry_4 -->

Validates a scalar or a one-dimensional array of parameters against a
domain. Every curve uses it, so `at(1.2)` on a curve over $[0, 1]$ raises
`ParameterOutOfDomain`.

## Errors

| Exception | Raised when |
| --- | --- |
| `BezierKitError` | Base class of the exceptions below |
| `DimensionMismatch` | Points, vectors or segments of different dimensions are combined |
| `DegreeError` | A curve has the wrong degree for an operation, or no control points |
| `ParameterOutOfDomain` | A parameter lies outside the curve's domain $[0, 1]$ |
| `ToleranceNotMet` | Adaptive fitting cannot reach its tolerance within its limits ([Fitting](fitting.md#sec-fitting)) |

Invalid arguments that are not geometry, such as a negative tolerance, raise
`ValueError`.
