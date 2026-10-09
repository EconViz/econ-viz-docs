---
seo_title: "三次线段与路径"
---

# 三次线段与路径

<span id="sec-paths"></span>

绘图端画的是三次曲线：TikZ 的 `.. controls ..`、SVG 的 `C` 与 Matplotlib 的 `CURVE4` 都接收四个控制点。`CubicBezierSegment` 就是以数值对象表示的三次曲线，`PiecewiseBezier` 则把三次曲线连接成路径。

## 三次线段

<!-- api: agora.bezierkit.guides_paths_1 -->

不可变的三次曲线，四个控制点即字段 `p0`、`p1`、`p2`、`p3`（亦可用 `control_points` 或逐一取出）。求值、微分、分割、截取与反转的方式与 `BezierCurve` 相同，但 `split()`、`segment()` 与 `reversed()` 仍回传三次线段。`segment(t, t)` 回传四个控制点都是 $B(t)$ 的退化三次曲线。

## 紧密边界框

<span id="def-bbox"></span>

!!! abstract "定义 · 轴对齐边界框"

    非空有界集合 $K \subset \mathbb{R}^d$ 的轴对齐边界框，是包含 $K$ 的最小方框

    $$
    [\alpha_1, \beta_1] \times \ldots \times [\alpha_d, \beta_d],
    $$

    其中 $\alpha_k = \inf \lbrace x_k : x \in K\rbrace$、$\beta_k = \sup \lbrace x_k : x \in K\rbrace$。

控制点凸包包含曲线（详见[凸包](curves.md#cor-hull)），但可能比曲线大得多。`bounding_box` 回传曲线本身的[轴对齐边界框](paths.md#def-bbox)所定义的方框（参见[三次曲线的紧密边界框。](paths.md#fig-bbox)），其候选点来自各坐标导数的根。

<span id="prop-bbox"></span>

!!! abstract "命题 · 三次曲线的边界框"

    设 $B$ 是控制点为 $P_0, \ldots, P_3 \in \mathbb{R}^d$ 的三次曲线，令

    $$
    a = -P_0 + 3P_1 - 3P_2 + P_3, \quad b = 3P_0 - 6P_1 + 3P_2, \quad c = 3(P_1 - P_0).
    $$

    则 $B(t) = a t^3 + b t^2 + c t + P_0$。对每个坐标 $k$，令 $T_k$ 由 $0$、$1$ 与下式在 $(0, 1)$ 内的根组成

    $$
    B'_k (t) = 3a_k t^2 + 2 b_k t + c_k
    $$

    （此多项式不恒为零时）；若它恒为零，则 $T_k = \lbrace 0, 1\rbrace$。于是 $B([0, 1])$ 的边界框坐标为

    $$
    \alpha_k = \min_{t \in T_k} B_k (t), \quad \beta_k = \max_{t \in T_k} B_k (t).
    $$

<!-- api: agora.bezierkit.guides_paths_2 -->

回传 `(low, high)` 两点，分别为曲线在各轴的最小值与最大值，由[三次曲线的边界框](paths.md#prop-bbox)的候选参数求值而得。

<span id="fig-bbox"></span>

![三次曲线的紧密边界框。](../../../assets/bezierkit/agora/paths/bbox.svg){ .ev-figure-sm }

## 升阶

升阶（详见[升阶](curves.md#prop-raise-degree)）把 $n$ 次曲线写成参数化相同的 $n + 1$ 次曲线。本套件用它把直线与二次曲线写成三次曲线，使每个绘图端都收到四个控制点。对[升阶](curves.md#prop-raise-degree)套用一次或两次，即得下列控制点。

<span id="prop-elevation"></span>

!!! abstract "命题 · 直线与二次曲线的三次表示"

    由 $P_0$ 到 $P_3$、参数化为 $(1 - t) P_0 + t P_3$ 的直线，是控制点为

    $$
    P_0, \quad P_0 + 1/3 (P_3 - P_0), \quad P_0 + 2/3 (P_3 - P_0), \quad P_3
    $$

    的三次曲线。控制点为 $P_0, C, P_3$ 的二次曲线，是控制点为

    $$
    P_0, \quad P_0 + 2/3 (C - P_0), \quad P_3 + 2/3 (C - P_3), \quad P_3
    $$

    的三次曲线。两种情形下曲线与其参数化都不变。

<!-- api: agora.bezierkit.guides_paths_3 -->

位于 `bezierkit.bezier`。依[直线与二次曲线的三次表示](paths.md#prop-elevation)将一次、二次或三次 `BezierCurve` 转为 `CubicBezierSegment`（传入线段时原样回传）；更高次数抛出 `DegreeError`。

<!-- api: agora.bezierkit.guides_paths_4 -->

由 `p0` 到 `p3` 的直线的三次表示。

<!-- api: agora.bezierkit.guides_paths_5 -->

控制点如给定的二次曲线的三次表示。

```python
from bezierkit.bezier import to_cubic

q = BezierCurve.quadratic(Point(0, 0), Point(3, 6), Point(9, 0))
print(to_cubic(q).control_points)
# (Point(coords=(0.0, 0.0)), Point(coords=(2.0, 4.0)),
#  Point(coords=(5.0, 4.0)), Point(coords=(9.0, 0.0)))
```

## 分段路径

<!-- api: agora.bezierkit.guides_paths_6 -->

由三次线段组成的路径。相邻线段必须相接：每段的 `p3` 与下一段的 `p0` 距离不得超过 `continuity_tolerance`，封闭路径最后的 `p3` 与第一个 `p0` 亦然，否则抛出 `ValueError`。`closed` 是给导出器的信息（SVG 的 `Z`、TikZ 的 `cycle`），不会额外加入封闭线段。

本套件以均匀方式将路径参数化。这是本套件的约定，并非通用概念：由 $m$ 段 $S_0, \ldots, S_{m-1}$ 组成的路径是映射

$$
P(t) = S_k (m t - k), \quad k = \min(\left\lfloor m t \right\rfloor, m - 1), \quad t \in [0, 1].
$$

不论长短，每段都占 $[0, 1]$ 的 $1 / m$。

```python
from bezierkit import CubicBezierSegment, PiecewiseBezier

path = PiecewiseBezier(
    [
        CubicBezierSegment.from_line(Point(0, 0), Point(2, 0)),
        CubicBezierSegment.from_line(Point(2, 0), Point(2, 4)),
    ]
)
# Point(coords=(2.0, 2.0))
print(path.at(0.75))
# Point(coords=(2.0, 2.0))
print(path.segment(0.25, 0.75).at(1.0))
```

`compound()` 把多条路径合为一条，各子路径保持分开，例如有洞的形状。复合路径没有单一的参数化：求值、分割或截取会抛出 `ValueError`；反转与导出则可正常使用。分割或截取封闭路径也会抛出异常（整条路径或单点除外），因为封闭路径没有可保留的起点与终点。

## 连续性

两条曲线在接点相接。设 $h_S, h_T > 0$，$S : [u_0 - h_S, u_0] \to \mathbb{R}^d$ 与 $T : [u_0, u_0 + h_T] \to \mathbb{R}^d$ 具有所需阶数的连续导数（区间端点取单边导数），$C$ 为在前一区间等于 $S$、在后一区间等于 $T$ 的曲线。

<span id="def-continuity"></span>

!!! abstract "定义 · 参数连续性"

    对 $k \ge 0$，若 $S^{(j)}(u_0) = T^{(j)}(u_0)$ 对 $j = 0, \ldots, k$ 成立，称曲线 $C$ 在 $u_0$ 为 $C^k$。

<span id="def-geometric-continuity"></span>

!!! abstract "定义 · 几何连续性 $G^1$"

    若 $S(u_0) = T(u_0)$，切矢量 $S'(u_0)$ 与 $T'(u_0)$ 皆非零，且存在 $\lambda > 0$ 使 $T'(u_0) = \lambda S'(u_0)$，称曲线 $C$ 在 $u_0$ 为 $G^1$；也就是两侧的单位切矢量相同。

参数连续性与几何连续性是连接曲线的标准概念 [Farin (2002)](../project/references.md#farin2002)[Prautzsch (2002)](../project/references.md#prautzsch2002)；任意阶 $k$ 的几何连续性见 [Barsky (1989)](../project/references.md#barsky1989)。本手册只用到 $C^0$、$C^1$ 与 $G^1$。切矢量非零的 $C^1$ 接点必为 $G^1$。

<span id="prop-continuity"></span>

!!! abstract "命题 · 三次曲线接点的连续性"

    设 $S$、$T$ 是控制点分别为 $P_0, \ldots, P_3$ 与 $Q_0, \ldots, Q_3$ 的三次曲线，并分别在 $(u - u_0 + h_S) / h_S$ 与 $(u - u_0) / h_T$ 求值。
    + $C$ 在 $u_0$ 为 $C^0$，若且唯若 $P_3 = Q_0$。
    + 若 $P_3 = Q_0$，则 $C$ 在 $u_0$ 为 $C^1$，若且唯若

    $$
    (P_3 - P_2) / h_S = (Q_1 - Q_0) / h_T.
    $$

    + 若 $P_3 = Q_0$、$P_3 \ne P_2$ 且 $Q_1 \ne Q_0$，则 $C$ 在 $u_0$ 为 $G^1$，若且唯若存在 $\mu > 0$ 使 $Q_1 - Q_0 = \mu (P_3 - P_2)$。
    + 在 `PiecewiseBezier` 的均匀参数化下 $h_S = h_T$，因此第 2 项的条件即为 $P_3 - P_2 = Q_1 - Q_0$。

`PiecewiseBezier` 只要求 $C^0$，也就是端点相接。接点是否也要平滑由调用端决定：无异曲线的折角或折线的转角本来就该保留。
