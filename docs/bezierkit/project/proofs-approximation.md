---
seo_title: "Approximation proofs"
---

# Approximation proofs

## Cubic segments and paths

??? note "Proof"

    [Bounding box of a cubic](../guides/paths.md#prop-bbox)

    Multiplying out the cubic Bernstein form gives

    $$
    \begin{aligned}B(t) &= (1-t)^3 P_0 + 3t(1-t)^2 P_1 + 3t^2(1-t) P_2 + t^3 P_3 \\ &= (1 - 3t + 3t^2 - t^3) P_0 + (3t - 6t^2 + 3t^3) P_1 + (3t^2 - 3t^3) P_2 + t^3 P_3 \\ &= a t^3 + b t^2 + c t + P_0,\end{aligned}
    $$

    with $a$, $b$ and $c$ as stated, by collecting the powers of $t$.

    Fix a coordinate $k$. The function $B_k$ is a polynomial, hence
    continuous on the compact interval $[0, 1]$, so it attains a minimum and a
    maximum there. Let $t^*$ be a point where it attains one of them. If
    $t^* \in (0, 1)$, then $B_k$ is differentiable with an extremum at an
    interior point, so $B'_k (t^*) = 0$ (Fermat's theorem). Two cases remain.
    - $B'_k$ is not identically zero. It is a polynomial of degree at most 2,
      so it has at most two roots, and $t^*$ is one of them if $t^*$ lies in
      $(0, 1)$. In every case $t^* \in T_k$.
    - $B'_k$ is identically zero. Then $B_k$ is constant, so its extrema are
      attained at $t = 0$ as well, and $0 \in T_k$.
    Therefore the minimum and the maximum of $B_k$ over $[0, 1]$ equal those
    over the finite set $T_k \subset [0, 1]$, which are $\alpha_k$ and $\beta_k$ as
    stated, since they are the infimum and supremum of $B_k$ over the curve.
    By [Axis-aligned bounding box](../guides/paths.md#def-bbox), the bounding box is the product of the intervals
    $[\alpha_k, \beta_k]$: a box that contains the curve contains every value
    $B_k (t)$, hence $\alpha_k$ and $\beta_k$, and the product of these intervals
    contains the curve.

??? note "Proof"

    [Lines and quadratics as cubics](../guides/paths.md#prop-elevation)

    _Line._ The line $t |\to (1 - t) P_0 + t P_3$ is a Bézier curve of degree 1
    with controls $R_0 = P_0$ and $R_1 = P_3$. By [Degree elevation](../guides/curves.md#prop-raise-degree) with
    $n = 1$, it is the quadratic with controls

    $$
    Q_0 = P_0, \quad Q_1 = 1/2 P_0 + 1/2 P_3, \quad Q_2 = P_3.
    $$

    Applying [Degree elevation](../guides/curves.md#prop-raise-degree) again, with $n = 2$, gives the cubic with
    controls

    $$
    \begin{aligned}S_0 &= Q_0 = P_0, \\ S_1 &= 1/3 Q_0 + 2/3 Q_1 = 2/3 P_0 + 1/3 P_3, \\ S_2 &= 2/3 Q_1 + 1/3 Q_2 = 1/3 P_0 + 2/3 P_3, \\ S_3 &= Q_2 = P_3,\end{aligned}
    $$

    and $S_i = P_0 + i/3 (P_3 - P_0)$ for $i = 0, \ldots, 3$.

    _Quadratic._ By [Degree elevation](../guides/curves.md#prop-raise-degree) with $n = 2$ and controls
    $P_0, C, P_3$, the cubic controls are

    $$
    Q_0 = P_0, \quad Q_1 = 1/3 P_0 + 2/3 C, \quad Q_2 = 2/3 C + 1/3 P_3, \quad Q_3 = P_3,
    $$

    and $Q_1 = P_0 + 2/3 (C - P_0)$, $Q_2 = P_3 + 2/3 (C - P_3)$.

    Each step is an identity in $t$, so the curve and its parameterization are
    unchanged.

??? note "Proof"

    [Continuity of cubic joins](../guides/paths.md#prop-continuity)

    Write $B_S$ and $B_T$ for the cubic Bézier curves with controls $P_i$ and
    $Q_i$, so that $S(u) = B_S ((u - u_0 + h_S) / h_S)$ and
    $T(u) = B_T ((u - u_0) / h_T)$. At $u = u_0$ the arguments are $1$ and
    $0$. By [Endpoints](../guides/curves.md#prop-endpoints), $S(u_0) = P_3$ and $T(u_0) = Q_0$. By the chain
    rule and [End tangents](../guides/operations.md#cor-end-tangents),

    $$
    S'(u_0) = (B'_S (1)) / h_S = (3(P_3 - P_2)) / h_S, \quad T'(u_0) = (B'_T (0)) / h_T = (3(Q_1 - Q_0)) / h_T.
    $$

    + By [Parametric continuity](../guides/paths.md#def-continuity) with $k = 0$, $C$ is $C^0$ at $u_0$ if and only if
      $S(u_0) = T(u_0)$, that is $P_3 = Q_0$.
    + With $P_3 = Q_0$, [Parametric continuity](../guides/paths.md#def-continuity) with $k = 1$ adds
      $S'(u_0) = T'(u_0)$, which is the stated equation after division by 3.
    + With $P_3 = Q_0$, by [Geometric continuity $G^1$](../guides/paths.md#def-geometric-continuity) the join is $G^1$ if and
      only if $S'(u_0) \ne 0$, $T'(u_0) \ne 0$, and $T'(u_0) = \lambda S'(u_0)$ for
      some $\lambda > 0$. The two tangents are non-zero if and only if
      $P_3 \ne P_2$ and $Q_1 \ne Q_0$, and then

    $$
    Q_1 - Q_0 = (\lambda h_T / h_S) (P_3 - P_2).
    $$

      Conversely, if $Q_1 - Q_0 = \mu (P_3 - P_2)$ with $\mu > 0$, then
      $\lambda = \mu h_S / h_T > 0$ gives $T'(u_0) = \lambda S'(u_0)$.
    + A path of $m$ segments under the uniform parameterization gives each
      segment the span $1 / m$, so $h_S = h_T$ and the equation in 2
      reduces to $P_3 - P_2 = Q_1 - Q_0$.

## Constructions and interpolation

??? note "Proof"

    [Endpoint conditions](../guides/construction.md#prop-endpoint)

    For the curve $B$ with the stated controls, [Endpoints](../guides/curves.md#prop-endpoints) gives
    $B(0) = P_0$ and $B(1) = P_3$, and [End tangents](../guides/operations.md#cor-end-tangents) gives

    $$
    B'(0) = 3(P_1 - P_0) = D_0, \quad B'(1) = 3(P_3 - P_2) = D_1.
    $$

    Now let $\Gamma$ be any polynomial curve of degree at most 3 with
    $\Gamma(0) = P_0$, $\Gamma(1) = P_3$, $\Gamma'(0) = D_0$ and $\Gamma'(1) = D_1$.
    By [Bernstein basis](../guides/curves.md#prop-basis), applied to each coordinate, there are unique $R_0, \ldots, R_3$
    with $\Gamma(t) = \sum_i b_{i,3}(t) R_i$. The computation above, applied to
    the controls $R_i$, shows

    $$
    \Gamma(0) = R_0, \quad \Gamma(1) = R_3, \quad \Gamma'(0) = 3(R_1 - R_0), \quad \Gamma'(1) = 3(R_3 - R_2).
    $$

    Comparing with the four conditions gives $R_0 = P_0$, $R_3 = P_3$,
    $R_1 = P_0 + D_0 / 3$ and $R_2 = P_3 - D_1 / 3$. So $R_i$ are the
    stated controls and $\Gamma = B$.

??? note "Proof"

    [Existence and uniqueness](../guides/construction.md#prop-hermite-unique)

    Put $G(s) = H(x_0 + h s)$. The map $H |\to G$ is a bijection of the
    polynomials of degree at most 3 onto themselves, with inverse
    $G |\to G((x - x_0) / h)$. By the chain rule,
    $H(x_i) = f_i$ and $H'(x_i) = m_i$ for $i = 0, 1$ are equivalent to

    $$
    G(0) = f_0, \quad G(1) = f_1, \quad G'(0) = h m_0, \quad G'(1) = h m_1.
    $$

    By [Endpoint conditions](../guides/construction.md#prop-endpoint) with $d = 1$, $P_0 = f_0$, $P_3 = f_1$, $D_0 = h m_0$ and
    $D_1 = h m_1$, exactly one polynomial $G$ of degree at most 3 satisfies
    these four conditions, and its Bernstein coefficients are
    $c_0, \ldots, c_3$. Hence $H$ exists, is unique, and equals
    $\sum_i b_{i,3}((x - x_0) / h) c_i$.

??? note "Proof"

    [Hermite interpolation](../guides/construction.md#prop-hermite)

    At $t = t_0$ and $t = t_1$ the segment is evaluated at $s = 0$ and
    $s = 1$, so $H(t_0) = P_0$ and $H(t_1) = P_3$ by [Endpoints](../guides/curves.md#prop-endpoints). By the
    chain rule $H'(t) = B'(s) / h$. By [End tangents](../guides/operations.md#cor-end-tangents),
    $B'(0) = 3(P_1 - P_0) = h D_0$ and $B'(1) = 3(P_3 - P_2) = h D_1$, so
    $H'(t_0) = D_0$ and $H'(t_1) = D_1$. Nothing requires $h > 0$.

??? note "Proof"

    [Graph form](../guides/construction.md#prop-graph-hermite)

    Write the segment as $(X(s), Y(s))$. The controls of $X$ are

    $$
    x_0, \quad x_0 + h/3, \quad x_1 - h/3 = x_0 + 2h/3, \quad x_1,
    $$

    which by [Lines and quadratics as cubics](../guides/paths.md#prop-elevation) (the line from $x_0$ to $x_1$) are those of the
    line $s |\to x_0 + h s$. Hence $X(s) = x_0 + h s$. The controls of $Y$ are
    $y_0, y_0 + h m_0 / 3, y_1 - h m_1 / 3, y_1$, which are the
    coefficients $c_0, \ldots, c_3$ of [Existence and uniqueness](../guides/construction.md#prop-hermite-unique) for the data
    $y_i = f(x_i)$ and $m_i = f'(x_i)$. Hence
    $Y(s) = H(x_0 + h s)$, and the segment is $s |\to (x_0 + h s, H(x_0 + h s))$.

??? note "Proof"

    [Hermite error bound](../guides/construction.md#thm-hermite-error)

    The case $x \in \lbrace x_0, x_1\rbrace$ is trivial: both sides of the first formula
    vanish, for any $\xi$. Let $x_0 < x < x_1$, and put

    $$
    E = f - H, \quad w(t) = (t - x_0)^2 (t - x_1)^2, \quad K = E(x) / w(x), \quad g = E - K w.
    $$

    Then $w(x) > 0$, $g$ is four times continuously differentiable, and
    $g(x_0) = g(x) = g(x_1) = 0$, because $E$ and $w$ vanish at $x_0$ and
    $x_1$, and $g(x) = E(x) - K w(x) = 0$. Moreover $g'(x_0) = g'(x_1) = 0$:
    $E'(x_i) = f'(x_i) - H'(x_i) = 0$ by [Cubic Hermite interpolant](../guides/construction.md#def-hermite), and $w$ has a double root
    at each $x_i$, so $w'(x_i) = 0$.

    By Rolle's theorem (Theorem 1.7 of [Burden (2011)](references.md#burden2011)), $g'$ vanishes at
    some $\xi_1 \in (x_0, x)$ and at some $\xi_2 \in (x, x_1)$. So $g'$ has the
    four distinct zeros $x_0 < \xi_1 < \xi_2 < x_1$. The function $g'$ is
    continuous and three times differentiable, so by the generalized Rolle
    theorem (Theorem 1.10 of [Burden (2011)](references.md#burden2011)) there is a
    $\xi \in (x_0, x_1)$ with $g^{(4)}(\xi) = 0$. Since $H$ has degree at most 3
    and $w$ is a monic polynomial of degree 4, $H^{(4)} = 0$ and
    $w^{(4)} = 24$, so

    $$
    0 = g^{(4)}(\xi) = f^{(4)}(\xi) - 24 K, \quad \text{that is} \quad K = (f^{(4)}(\xi)) / 24.
    $$

    Hence $f(x) - H(x) = E(x) = K w(x)$, which is the first formula.

    For the bound, $(x - x_0)(x_1 - x)$ is a product of two non-negative
    numbers with the sum $h$, so it is at most $(h / 2)^2$. Thus
    $w(x) \le h^4 / 16$ and

    $$
    |f(x) - H(x)| \le M / 24 \cdot h^4 / 16 = (M h^4) / 384.
    $$

## Fitting and level sets

??? note "Proof"

    [Depth of adaptive fitting](../guides/fitting.md#cor-depth)

    Let $[a, b]$ be an interval at depth $k$, so $b - a = L / 2^k$. On it,
    each coordinate of the Hermite segment is the cubic Hermite interpolant of
    the same coordinate of $C$ ([Hermite interpolation](../guides/construction.md#prop-hermite) and [Existence and uniqueness](../guides/construction.md#prop-hermite-unique)), so
    [Hermite error bound](../guides/construction.md#thm-hermite-error) bounds its error by
    $M (b - a)^4 / 384$. The Euclidean error at any parameter is at most
    $\sqrt{d}$ times the largest coordinate error, since
    $\left\lVert v \right\rVert_2 \le \sqrt{d} \left\lVert v \right\rVert_\infty$ for $v \in \mathbb{R}^d$: indeed
    $\left\lVert v \right\rVert_2^2 = \sum_k v_k^2 \le d \left\lVert v \right\rVert_\infty^2$. In particular the measured
    error, a maximum over probe parameters, satisfies

    $$
    e \le \sqrt{d} M L^4 / (384 \cdot 2^{4k}).
    $$

    This is at most $\epsilon$ if and only if
    $2^{4k} \ge \sqrt{d} M L^4 / (384 \epsilon)$, that is, if
    $k \ge 1/4 \log_2 (\sqrt{d} M L^4 / (384 \epsilon))$. Every depth
    $k \ge k^*$ satisfies this, so every interval at such a depth is accepted.

    Suppose now that `max_depth` $\ge k^*$ and `max_segments` $\ge 2^{k^*}$.
    An interval is split only if it fails, which happens only at a depth
    $k < k^*$. So all intervals have depth at most $k^*$ and no
    `ToleranceNotMet` is raised for the depth. The accepted intervals are
    disjoint pieces obtained by halving $[t_0, t_1]$ at most $k^*$ times, so
    there are at most $2^{k^*}$ of them. A failing interval would give at least
    two accepted segments, so the number of segments accepted so far plus two
    never exceeds this final count, which is at most `max_segments`; the
    segment limit is therefore not exceeded either.

??? note "Proof"

    [Polyline tolerance](../guides/fitting.md#prop-rdp)

    Let `rdp`$(i, j)$ denote the recursive step of the algorithm on the indices
    $i < j$, which returns an increasing list of indices from $i$ to $j$. We
    show by strong induction on $j - i$ that for every two consecutive
    indices $u < v$ in the returned list, every index $l$ with
    $u \le l \le v$ satisfies $\text{dist}(v_l, [v_u, v_v]) \le \epsilon$.

    _Base case._ If $j \le i + 1$, the list is $(i, j)$, and the only indices
    between $i$ and $j$ inclusive are $i$ and $j$, whose vertices are the
    chord's end points, at distance zero.

    _Step._ Otherwise let $\delta^*$ be the largest distance from a vertex
    strictly between $i$ and $j$ to $[v_i, v_j]$. If $\delta^* \le \epsilon$, the
    list is $(i, j)$, and the claim holds by the choice of $\delta^*$ and because
    the end points have distance zero. If $\delta^* > \epsilon$, the step chooses
    an index $m$ with $i < m < j$ and returns the list of $\text{rdp}(i, m)$
    followed by that of $\text{rdp}(m, j)$, with $m$ occurring once. Two consecutive
    indices of the result are consecutive in one of the two lists. Since
    $m - i$ and $j - m$ are smaller than $j - i$, the induction hypothesis
    applies to both.

    Steps 2 and 3 apply `rdp` between every two consecutive kept vertices
    of step 2 and concatenate the results. The output keeps exactly the
    returned indices $a_0 < \ldots < a_m$, and every two consecutive ones
    are consecutive in one of these lists. This proves the inequality. The
    `fit_error` of an output segment is $\max_{a_j \le i \le a_{j+1}} \text{dist}(v_i, [v_{a_j}, v_{a_{j+1}}])$,
    hence at most $\epsilon$.

??? note "Proof"

    [Deviation from the polyline](../guides/fitting.md#cor-rdp-path)

    1. The distance to a convex set is a convex function. For the segment
    $K = [a, b]$, let $x_1, x_2$ be points with
    $\text{dist}(x_i, K) \le \epsilon$, attained at $y_i \in K$ (the minimum exists by
    compactness), and let $\lambda \in [0, 1]$. Then
    $\lambda y_1 + (1 - \lambda) y_2 \in K$ and by the triangle inequality

    $$
    \left\lVert \lambda x_1 + (1 - \lambda) x_2 - (\lambda y_1 + (1 - \lambda) y_2) \right\rVert_2 \le \lambda \left\lVert x_1 - y_1 \right\rVert_2 + (1 - \lambda) \left\lVert x_2 - y_2 \right\rVert_2 \le \epsilon.
    $$

    So $\text{dist}(\lambda x_1 + (1 - \lambda) x_2, K) \le \epsilon$.

    A point $x$ of the polyline lies on an edge $[v_i, v_{i+1}]$, so it is
    $\lambda v_i + (1 - \lambda) v_{i+1}$. Choose $j$ with $a_j \le i < a_{j+1}$;
    then $i + 1 \le a_{j+1}$, since indices are integers, and both $v_i$ and
    $v_{i+1}$ are within $\epsilon$ of $[v_{a_j}, v_{a_{j+1}}]$ by
    [Polyline tolerance](../guides/fitting.md#prop-rdp). By the convexity just proved, so is $x$.

    2. A point left by step 1 is some $v_i$, and $v_i$ lies within $\epsilon$ of
    a chord by [Polyline tolerance](../guides/fitting.md#prop-rdp). A dropped input point $p$ is within $\delta$ of the
    vertex kept before it, say $v$; then
    $\text{dist}(p, [a, b]) \le \left\lVert p - v \right\rVert_2 + \text{dist}(v, [a, b]) \le \delta + \epsilon$ for a chord $[a, b]$
    within $\epsilon$ of $v$. The final copy of the first point of a closed
    polyline is dropped under the same condition, with $v = v_0$.

??? note "Proof"

    [Centre of the bilinear interpolant](../guides/implicit.md#prop-center)

    Substituting the four corners of $[0, 1]^2$ into $u$ shows that only one of
    the four terms is non-zero at each corner, with the coefficient $1$, so $u$
    takes the corner values. At $s = t = 1 / 2$ each of the four products
    of weights equals $1/2 \cdot 1/2 = 1/4$, so
    $u(1/2, 1/2) = 1/4 (f_{00} + f_{10} + f_{11} + f_{01})$.

??? note "Proof"

    [Tangent of a level set](../guides/implicit.md#thm-gradient)

    Since $\nabla F(p) \ne 0$, either $F_y (p) \ne 0$ or $F_x (p) \ne 0$.

    _Case $F_y (p) \ne 0$._ Apply [Implicit function theorem](../guides/implicit.md#thm-ift): there are $I$, $J$ and a $C^1$
    function $\phi : I \to J$ with $\phi(p_x) = p_y$ and
    $L_c \cap (I \times J) = \lbrace (x, \phi(x)) : x \in I\rbrace$. Put $N = I \times J$ and
    $\gamma(x) = (x, \phi(x))$. Differentiating $F(x, \phi(x)) = c$ by the chain
    rule gives $F_x + F_y \phi' = 0$ at $\gamma(x)$. By continuity of $F_y$, we
    may shrink $I$ and $J$ so that $F_y \ne 0$ on $N$; then

    $$
    \gamma'(x) = (1, \phi'(x)) = (1, -F_x / F_y) = 1 / F_y (F_y, -F_x),
    $$

    which is non-zero and parallel to $(F_y, -F_x)$ at $\gamma(x)$.

    _Case $F_x (p) \ne 0$._ Exchange the roles of $x$ and $y$: there is a $C^1$
    function $\psi$ with $L_c \cap N = \lbrace (\psi(y), y)\rbrace$, curve
    $\gamma(y) = (\psi(y), y)$ and $\psi' = -F_y / F_x$, so

    $$
    \gamma'(y) = (-F_y / F_x, 1) = -1 / F_x (F_y, -F_x),
    $$

    again non-zero and parallel to $(F_y, -F_x)$.

    Finally $\nabla F \cdot (F_y, -F_x) = F_x F_y - F_y F_x = 0$.

## Export

??? note "Proof"

    [Rounding error](../guides/export.md#prop-rounding)

    The difference of the curves is

    $$
    \widetilde{B}(t) - B(t) = \sum_{i=0}^n b_{i,n}(t) (\widetilde{P}_i - P_i).
    $$

    By [Partition of unity](../guides/curves.md#prop-unity), the weights $b_{i,n}(t)$ are non-negative and sum to 1, so
    for each coordinate

    $$
    |\widetilde{B}_k (t) - B_k (t)| \le \sum_{i=0}^n b_{i,n}(t) |\widetilde{P}_{i,k} - P_{i,k}| \le \epsilon.
    $$

    Since $\left\lVert v \right\rVert_2 \le \sqrt{d} \left\lVert v \right\rVert_\infty$ for $v \in \mathbb{R}^d$ (Section 2.2 of
    [Golub (2013)](references.md#golub2013)), we get $\left\lVert \widetilde{B}(t) - B(t) \right\rVert_2 \le \sqrt{d} \epsilon$.

    The exporters write each coordinate with Python's fixed-point format
    with $p$ decimals, which gives the multiple of $10^{-p}$ nearest to the
    coordinate; it differs from the coordinate by at most
    $1/2 \cdot 10^{-p}$. The exporters also write a coordinate whose absolute
    value is less than $1/2 \cdot 10^{-p}$ as $0$, which changes it by that
    value, again at most $1/2 \cdot 10^{-p}$.
