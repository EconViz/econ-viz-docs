---
seo_title: "导数、反转与分割"
---

# 导数、反转与分割

<span id="sec-operations"></span>

每项运算只作用于控制点，并返回沿用原曲线求值策略的新曲线。

## 导数

Bézier 曲线的导数 $B'(t)$ 是其坐标函数（$t$ 的多项式）的导数，为 $\mathbb{R}^d$ 中的向量。

<span id="lem-bernstein-derivative"></span>

!!! abstract "引理 · Bernstein 多项式的导数"

    对 $n \ge 1$ 与每个整数 $i$，

    $$
    b'_{i,n}(t) = n [b_{i-1,n-1}(t) - b_{i,n-1}(t)].
    $$

此为 [Floater (2025)](../project/references.md#floater2025) 的引理 1.4。

<span id="thm-hodograph"></span>

!!! abstract "定理 · 速端曲线"

    $n$ 次 Bézier 曲线（$n \ge 1$）的导数是 $n - 1$ 次 Bézier 曲线

    $$
    B'(t) = \sum_{i=0}^{n-1} b_{i,n-1}(t) \cdot n (P_{i+1} - P_i).
    $$

控制点为 $n(P_{i+1} - P_i)$ 的曲线称为 $B$ 的速端曲线（[Floater (2025)](../project/references.md#floater2025) 的定理 1.8；另见 [Farin (2002)](../project/references.md#farin2002)）。

<span id="cor-end-tangents"></span>

!!! abstract "推论 · 端点切线"

    $B'(0) = n(P_1 - P_0)$，$B'(1) = n(P_n - P_{n-1})$。

这说明了曲线为何朝 $P_1$ 的方向离开 $P_0$，并从 $P_{n-1}$ 的方向抵达 $P_n$。

<!-- api: agora.bezierkit.guides_operations_1 -->

以 `BezierCurve` 返回 `order` 阶导数，即套用[速端曲线](operations.md#thm-hodograph) `order` 次。常数（0 次）的导数是 0 次的零曲线；`order=0` 返回曲线本身。

```python
d = curve.derivative()
print(list(d.control_points))
# [Point(coords=(3.0, 6.0)), Point(coords=(6.0, 0.0)), Point(coords=(3.0, -6.0))]
# Point(coords=(4.5, 0.0)): the tangent at the top is horizontal
print(d.at(0.5))
```

## 反转

<span id="lem-symmetry"></span>

!!! abstract "引理 · 对称性"

    对所有 $i$ 与 $t$，$b_{i,n}(1 - t) = b_{n-i,n}(t)$。

<span id="prop-reversal"></span>

!!! abstract "命题 · 反转"

    控制点为 $P_n, \ldots, P_0$ 的曲线就是 $t |\to B(1 - t)$。

<!-- api: agora.bezierkit.guides_operations_2 -->

根据[反转](operations.md#prop-reversal)，返回反向遍历的曲线。

## 分割

在 $t = c$ 运行 de Casteljau 算法不只得到曲线值：每一轮的第一个点构成 $c$ 之前那段曲线的控制多边形，最后一个点构成 $c$ 之后那段的控制多边形（参见[在 $t = 0.4$ 分割三次曲线。](operations.md#fig-split)）。

<span id="thm-subdivision"></span>

!!! abstract "定理 · 分割"

    令 $c \in [0, 1]$，并在 $t = c$ 计算[de Casteljau 点](curves.md#def-casteljau)的各点。令 $L_j = P_0^{(j)}$、$R_j = P_j^{(n-j)}$，$j = 0, \ldots, n$。则对每个 $s \in [0, 1]$

    $$
    B(c s) = \sum_{j=0}^n b_{j,n}(s) L_j
    $$

    且

    $$
    B(c + (1 - c) s) = \sum_{j=0}^n b_{j,n}(s) R_j.
    $$

这是经典结果，见 [Floater (2025)](../project/references.md#floater2025)（第 8.4 节，由 blossom 导出）与 [Farin (2002)](../project/references.md#farin2002)。

<span id="fig-split"></span>

![在 $t = 0.4$ 分割三次曲线。](../../../assets/bezierkit/agora/curves/split.svg){ .ev-figure-sm }

<!-- api: agora.bezierkit.guides_operations_3 -->

`split(c)` 返回[分割](operations.md#thm-subdivision)的两条曲线，次数不变，参数范围都是 $[0, 1]$。`segment(t0, t1)` 返回曲线在 $t_0$ 与 $t_1$ 之间的部分，重新参数化到 $[0, 1]$；$t_0 = t_1$ 时返回单点 $B(t_0)$，即 0 次曲线。参数超出 $[0, 1]$ 或 $t_0 > t_1$ 时抛出异常。

`segment()` 分割两次：先在 $t_1$ 分割并保留左段，再在 $t_0 / t_1$ 分割该段并保留右段。

<span id="cor-segment"></span>

!!! abstract "推论 · 截取"

    对 $0 \le t_0 < t_1 \le 1$，`segment(t0, t1)` 返回的曲线为 $s |\to B(t_0 + (t_1 - t_0) s)$。

```python
left, right = curve.split(0.4)
# both B(0.4) = (1.552, 1.44)
print(left.at(1.0), right.at(0.0))
# B(0.5) = (2.0, 1.5)
print(curve.segment(0.25, 0.75).at(0.5))
```
