---
seo_title: "Constructions and Hermite interpolation"
---

# Constructions and Hermite interpolation

<span id="sec-construction"></span>

A cubic is fixed by its endpoints and the derivatives there. The
constructions in this chapter turn such endpoint conditions into control
points, which is how economic curves known by a few values and slopes become
Bézier curves.

## Endpoint constructions

Each construction is a frozen dataclass with a `build()` method, in
`bezierkit.construction`.

<!-- api: agora.bezierkit.guides_construction_1 -->

The cubic with $B(0) =$ `start`, $B(1) =$ `end`,
$B'(0) =$ `start_derivative` and $B'(1) =$ `end_derivative`, in any
dimension.

<span id="prop-endpoint"></span>

!!! abstract "Proposition · Endpoint conditions"

    Let $P_0, P_3, D_0, D_1 \in \mathbb{R}^d$. The cubic Bézier curve with controls

    $$
    P_0, \quad P_0 + D_0 / 3, \quad P_3 - D_1 / 3, \quad P_3
    $$

    satisfies $B(0) = P_0$, $B(1) = P_3$, $B'(0) = D_0$ and $B'(1) = D_1$, and
    it is the only polynomial curve of degree at most 3 that does.

<!-- api: agora.bezierkit.guides_construction_2 -->

Endpoint tangents given as directions, with the handle lengths
$|P_1 - P_0| =$ `start_handle` and $|P_3 - P_2| =$ `end_handle`. The
directions are normalized, so only their orientation matters; handles must
be finite and non-negative. By [Endpoint conditions](construction.md#prop-endpoint), $B'(0) = 3 \cdot$
`start_handle` times the unit start direction.

<!-- api: agora.bezierkit.guides_construction_3 -->

A planar cubic whose ends have the slopes $\mathrm{d} y / \mathrm{d} x$ given, built
as `TangentDirections` with directions $(1, m)$. Slopes must be finite; a
vertical tangent needs `TangentDirections`.

```python
from bezierkit.construction import PlanarSlopes

demand = PlanarSlopes(
    start=Point(0, 5),
    end=Point(5, 0),
    start_slope=-2,
    end_slope=-0.3,
).build()
# (0.447, 4.106): one unit from (0, 5) along slope -2
print(demand.control_points[1])
```

## Hermite interpolation

Cubic Hermite interpolation matches a function and its derivative at both
ends of an interval.

<span id="def-hermite"></span>

!!! abstract "Definition · Cubic Hermite interpolant"

    Let $f$ be differentiable on $[x_0, x_1]$ with $x_0 \ne x_1$. A cubic
    Hermite interpolant of $f$ is a polynomial $H$ of degree at most 3 with

    $$
    H(x_i) = f(x_i), \quad H'(x_i) = f'(x_i), \quad i = 0, 1.
    $$

    For a curve, interpolate each coordinate.

This is the case of two nodes of the Hermite polynomial in Section 3.4 of
[Burden (2011)](../project/references.md#burden2011), where it is Definition 3.8. Such a polynomial exists
and is unique:

<span id="prop-hermite-unique"></span>

!!! abstract "Proposition · Existence and uniqueness"

    The cubic Hermite interpolant of [Cubic Hermite interpolant](construction.md#def-hermite) exists and is unique. With
    $h = x_1 - x_0$, $f_i = f(x_i)$ and $m_i = f'(x_i)$ it is

    $$
    H(x) = \sum_{i=0}^3 b_{i,3}((x - x_0) / h) c_i,
    $$

    where the coefficients are

    $$
    c_0 = f_0, \quad c_1 = f_0 + h m_0 / 3, \quad c_2 = f_1 - h m_1 / 3, \quad c_3 = f_1.
    $$

The same statement, for any number of nodes, is Theorem (2.1.5.2) of
[Stoer (2002)](../project/references.md#stoer2002). Over a parameter interval $[t_0, t_1]$ of width
$h = t_1 - t_0$, the Bézier segment is evaluated at $s = (t - t_0) / h$,
which rescales derivatives by $h$.

<!-- api: agora.bezierkit.guides_construction_4 -->

The cubic segment with controls $P_0$, $P_0 + h D_0 / 3$,
$P_3 - h D_1 / 3$, $P_3$, in `bezierkit.interpolation`. $h = 0$ raises
`ValueError`; a negative $h$ reverses the interval.

<span id="prop-hermite"></span>

!!! abstract "Proposition · Hermite interpolation"

    Let $H(t) = B((t - t_0) / h)$ for the segment returned by
    `parametric_hermite`. Then $H(t_0) = P_0$, $H(t_1) = P_3$,
    $H'(t_0) = D_0$ and $H'(t_1) = D_1$.

<!-- api: agora.bezierkit.guides_construction_5 -->

The interpolant of a graph $y = f(x)$ from the values $y_0 = f(x_0)$,
$y_1 = f(x_1)$ and slopes $m_0 = f'(x_0)$, $m_1 = f'(x_1)$: the
parametric form with $P = (x, f(x))$, $D = (1, f'(x))$ and $t = x$. Its
controls are

$$
(x_0, y_0), \quad (x_0 + h/3, y_0 + h m_0 / 3), \quad (x_1 - h/3, y_1 - h m_1 / 3), \quad (x_1, y_1),
$$

with $h = x_1 - x_0$ ([Hermite interpolant of $4 / x^2$ on $[1, 1.5]$.](construction.md#fig-hermite)).

<span id="prop-graph-hermite"></span>

!!! abstract "Proposition · Graph form"

    The segment of `graph_hermite` is the graph of the cubic Hermite
    interpolant $H$ of $f$ on $[x_0, x_1]$: it is
    $s |\to (x_0 + h s, H(x_0 + h s))$, $s \in [0, 1]$.

```python
from bezierkit.interpolation import graph_hermite

# f(x) = 4 / x^2 on [1, 1.5]
segment = graph_hermite(
    x0=1, x1=1.5, y0=4, y1=16 / 9, m0=-8, m1=-64 / 27
)
```

<span id="fig-hermite"></span>

![Hermite interpolant of $4 / x^2$ on $[1, 1.5]$.](../../assets/bezierkit/agora/construction/hermite.svg){ .ev-figure-sm }

## Interpolation error

<span id="thm-hermite-error"></span>

!!! abstract "Theorem · Hermite error bound"

    Let $f$ be four times continuously differentiable on $[x_0, x_1]$ with
    $x_0 < x_1$, let $H$ be its cubic Hermite interpolant ([Cubic Hermite interpolant](construction.md#def-hermite)), and
    put $h = x_1 - x_0$ and $M = \max |f^{(4)}|$ on the interval. For every
    $x \in [x_0, x_1]$ there is a $\xi \in [x_0, x_1]$ with

    $$
    f(x) - H(x) = (f^{(4)} (\xi)) / 24 (x - x_0)^2 (x - x_1)^2,
    $$

    and therefore

    $$
    \max_{x \in [x_0, x_1]} |f(x) - H(x)| \le (M h^4) / 384.
    $$

The error formula is Theorem 3.9 of [Burden (2011)](../project/references.md#burden2011), whose proof is
left to Exercise 3.4.11 there, and Theorem (2.1.5.9) of
[Stoer (2002)](../project/references.md#stoer2002). The bound is sharp: for $f(x) = x^4$ on $[0, 1]$ the
error is $x^2 (x - 1)^2$, whose maximum $1 / 16$ at $x = 1 / 2$
equals $M h^4 / 384$ with $M = 24$.

Halving the interval divides the bound by 16, which is what adaptive fitting
exploits ([Fitting](fitting.md#sec-fitting)). For $f(x) = 4 / x^2$ on $[1, 1.5]$,
$f^{(4)}(x) = 480 / x^6$, so $M = 480$ and the bound is
$480 \cdot 0.5^4 / 384 \approx 0.078$.

<!-- api: agora.bezierkit.guides_construction_6 -->

The bound $M |t_1 - t_0|^4 / 384$ of [Hermite error bound](construction.md#thm-hermite-error), in
`bezierkit.fitting`. $M$ must be finite and non-negative.

The bound is for a scalar function. For a curve $t |\to (x(t), y(t))$, apply
it to each coordinate. In $\mathbb{R}^d$ the Euclidean error is at most $\sqrt{d}$
times the largest coordinate bound, because $\left\lVert v \right\rVert_2 \le \sqrt{d} \left\lVert v \right\rVert_\infty$
for $v \in \mathbb{R}^d$ (Section 2.2 of [Golub (2013)](../project/references.md#golub2013)).
