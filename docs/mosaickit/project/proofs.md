---
seo_title: "Proofs"
---

# Proofs

<span id="app-proofs"></span>

This appendix proves the lemmas, propositions, theorems and corollaries in
the order they appear in the chapters. The proofs assume exact arithmetic.
The code computes the same quantities in floating point, so it may decide a
configuration either way when it is within rounding error of a degenerate
case, such as a point on an edge or three nearly collinear points. For plane
vectors $u, v$, define $u \times v = u_x v_y - u_y v_x$.

## Packing and lanes

??? note "Proof"

    [Spreading is optimal](../guides/annotations.md#thm-spread)

    _Change of variables._ Put $o_k = \sum_{j < k} (s_j + g) + s_k / 2$,
    $y_k = x_k - o_k$ and $z_k = c_k - o_k$. Since
    $o_{k+1} - o_k = (s_k + s_{k+1}) / 2 + g$, the constraints of
    [Order-preserving packing](../guides/annotations.md#def-packing) read $y_1 \le \cdots \le y_n$, and the objective is
    $\sum_k (y_k - z_k)^2$. The problem is therefore to find the closest
    non-decreasing vector to $z$ in the least-squares sense.

    _What the code computes._ A cluster $B$ of consecutive items starting at
    $i$, with start $S_B$, places item $k \in B$ at

    $$
    x_k = S_B + \sum_{i \le l < k} (s_l + g) + s_k / 2 = S_B + o_k - O_i,
    $$

    where $O_i = \sum_{l < i} (s_l + g)$. Hence $y_k = S_B - O_i =: Y_B$ is
    constant on $B$, and the code's choice of $S_B$ as the mean of
    $c_k - (o_k - O_i)$ makes $Y_B$ the mean of $z_k$ over $B$; a new item
    alone has $Y = z_k$. Clusters $A$ and $B$ (with $B$ after $A$) are left
    apart when $S_A + \text{length}(A) + g \le S_B$; since
    $\text{length}(A) + g = O_{i_B} - O_{i_A}$, this says $Y_A \le Y_B$. The code is
    therefore the pool-adjacent-violators algorithm (PAVA): append $z_k$ as a
    block, and while the last two blocks have decreasing means, replace them
    by their union with its mean.

    _Invariants._ (a) Consecutive blocks have non-decreasing means: merging
    stops exactly when the last pair is in order, and earlier pairs are not
    touched. (b) In every block $B$ with mean $\mu_B$, every initial segment
    has mean at least $\mu_B$. A single item satisfies (b). When $A$ and $B$
    merge, $\mu_A > \mu_B$, and the merged mean $\mu$ lies strictly between them.
    An initial segment inside $A$ has mean at least $\mu_A > \mu$. Any other
    initial segment is $A$ followed by an initial segment $B'$ of $B$; if
    $B'$ is all of $B$ its mean is $\mu$, and otherwise the rest $B''$ of $B$
    has mean at most $\mu_B < \mu$ by (b) for $B$, so the segment, being the
    complement of $B''$ in a set with mean $\mu$, has mean at least $\mu$.

    _Optimality._ The objective is strictly convex and the constraints
    $y_k - y_{k+1} \le 0$ are linear, so a point satisfying the
    Karush–Kuhn–Tucker conditions is the unique minimizer
    [Boyd (2004)](references.md#boyd2004). Let $\lambda_k = 2 \sum_{l \le k} (z_l - y_l)$ for
    $k = 0, \ldots, n$. Stationarity,
    $2 (y_k - z_k) + \lambda_k - \lambda_{k-1} = 0$, holds by construction.
    Within a block the deviations $z_l - Y_B$ sum to zero, so $\lambda$ is zero
    at every block end, $\lambda_n = 0$ included. Inside a block starting at
    $i$, $\lambda_k = 2 \sum_{l=i}^k (z_l - Y_B) \ge 0$ by (b). Finally
    $\lambda_k > 0$ only when $k$ and $k + 1$ lie in the same block, where
    $y_k = y_{k+1}$ and the constraint is tight. With (a) for feasibility, all
    conditions hold.

??? note "Proof"

    [Properties of a spread](../guides/annotations.md#cor-spread)

    (i) Number the items in sorted order and let $i < j$. Summing the
    constraints from $i$ to $j - 1$,

    $$
    x_j - x_i \ge \sum_{k=i}^{j-1} ((s_k + s_{k+1}) / 2 + g) \ge (s_i + s_j) / 2 + g
    $$

    since every term is non-negative and the first and last contribute
    $s_i / 2$ and $s_j / 2$. (ii) If $c$ is a packing, it attains the
    objective $0$, so it is the unique minimizer of [Spreading is optimal](../guides/annotations.md#thm-spread). (iii) With
    the notation of that proof,

    $$
    \sum_{k \in B} (x_k - c_k) = \sum_{k \in B} (y_k - z_k) = |B| Y_B - \sum_{k \in B} z_k = 0
    $$

??? note "Proof"

    [First fit uses the fewest lanes](../guides/annotations.md#thm-lanes)

    An interval joins a lane only when it conflicts with nothing in it, and it
    never moves afterwards, so the result is a lane assignment. Any lane
    assignment puts $\omega$ pairwise conflicting intervals in $\omega$ distinct
    lanes, so at least $\omega$ lanes are needed.

    Conversely, write $J = [a_J, b_J]$ and suppose the intervals come in
    increasing order of $a$. By [Conflicting intervals](../guides/annotations.md#def-conflict), $I$ and $J$ conflict exactly
    when the half-open intervals $[a_I, b_I + g)$ and $[a_J, b_J + g)$ meet.
    Let $I$ be an interval placed in the highest lane $k$ used. Each lane
    $j < k$ held, when $I$ came, an interval $J_j$ conflicting with $I$. Each
    $J_j$ came earlier, so $a_{J_j} \le a_I$, and conflicting with $I$ it has
    $b_{J_j} + g > a_I$. Hence every $[a_{J_j}, b_{J_j} + g)$ contains $a_I$,
    and so does $[a_I, b_I + g)$ because $b_I - a_I + g > 0$. Half-open
    intervals sharing a point meet pairwise, so $J_0, \ldots, J_{k-1}, I$ are
    $k + 1$ pairwise conflicting intervals and $k + 1 \le \omega$.

## Rectangles, segments and polygons

??? note "Proof"

    [Nearest point of a rectangle](../guides/geometry.md#lem-nearest)

    $|q - p|^2 = (q_x - p_x)^2 + (q_y - p_y)^2$, and $R$ is the product of
    $[x_0, x_1]$ and $[y_0, y_1]$, so the two coordinates are minimized
    separately. On an interval, $t |\to (t - p_x)^2$ is strictly convex with
    unconstrained minimum at $p_x$, so its minimum over $[x_0, x_1]$ is
    attained only at $\min(\max(p_x, x_0), x_1)$; likewise for $y$.

??? note "Proof"

    [Orientation test](../guides/geometry.md#lem-orient)

    Subtracting the first row from the others,

    $$
    \text{orient}(a, b, c) = \det \begin{pmatrix}1 & a_x & a_y \\\ 1 & b_x & b_y \\\ 1 & c_x & c_y\end{pmatrix}.
    $$

    A cyclic permutation of the rows is even and a swap is odd, which gives
    the symmetries. Also

    $$
    \text{orient}(a, b, c) = (b - a) \times (c - a) = |b - a| |c - a| \sin \theta,
    $$

    where $\theta$ is the signed angle from
    $b - a$ to $c - a$; it is positive exactly when $\theta \in (0, \pi)$, that
    is when $c$ is left of the directed line, negative when it is right, and
    zero exactly when the two vectors are parallel or one vanishes, that is
    when the points are collinear.

??? note "Proof"

    [Segment intersection](../guides/geometry.md#thm-segments)

    First observe that if $\text{orient}(c, d, p) = 0$ and $p$ lies in the bounding box
    of $[c, d]$, then $p \in [c, d]$. Indeed, if $c = d$ the box is the point
    $c$; otherwise $p = c + t (d - c)$ for some real $t$ by collinearity, and
    on a coordinate where $d - c$ is non-zero the box condition forces
    $t \in [0, 1]$.

    _If._ Suppose $d_1 d_2 < 0$ and $d_3 d_4 < 0$. The orientation
    $\text{orient}(c, d, \cdot)$ is affine along $[a, b]$ and changes sign, so
    $[a, b]$ meets the line $L_{c d}$ at one point; likewise $[c, d]$ meets
    $L_{a b}$. The lines are not parallel, since $a$ and $b$ lie on opposite sides of
    $L_{c d}$, so they share exactly one point $z$, and
    both crossing points equal $z$, which therefore lies on both segments. In
    the other case some $d_i = 0$ and its endpoint lies in the other segment's
    box, hence on the other segment by the note.

    _Only if._ Let $z$ be a common point. If $d_1 d_2 > 0$, then $a$ and $b$
    lie strictly on one side of $L_{c d}$, and so does all of $[a, b]$,
    contradicting $z \in L_{c d}$; so $d_1 d_2 \le 0$, and likewise
    $d_3 d_4 \le 0$. If both are negative we are done. Otherwise some $d_i$ is
    zero; say $d_1 = 0$, the other cases being symmetric. If $d_2 \ne 0$,
    $[a, b]$ meets $L_{c d}$ only at $a$, so $z = a$ and $a \in [c, d]$: the
    test for $d_1$ succeeds. If $d_2 = 0$ too, all four points are collinear,
    the segments are overlapping intervals of one line, and an endpoint of
    one lies in the other, so one of the four tests succeeds.

??? note "Proof"

    [Segments and rectangles](../guides/geometry.md#lem-rect-segment)

    The edges of $R$ lie in $R$, so either test succeeding gives a common
    point ([Segment intersection](../guides/geometry.md#thm-segments)). Conversely, let $[a, b]$ meet $R$ while neither
    endpoint lies in $R$. The segment is connected and contains points in
    $R$ and outside it, so it meets the boundary of $R$, which is the union of
    the four edges; [Segment intersection](../guides/geometry.md#thm-segments) detects that edge.

??? note "Proof"

    [Distance to a segment](../guides/geometry.md#lem-segment-distance)

    $t |\to |a + t (b - a) - p|^2$ is a convex quadratic with unconstrained
    minimum at $(p - a) \cdot (b - a) / |b - a|^2$; over $[0, 1]$ its
    minimum is at the clamp of that value, as in the proof of
    [Nearest point of a rectangle](../guides/geometry.md#lem-nearest).

??? note "Proof"

    [Even-odd rule](../guides/geometry.md#prop-even-odd)

    Write $p = (x, y)$ and choose $\epsilon > 0$ smaller than every positive
    difference $|y_i - y|$ between a vertex height and $y$, and small enough
    that $p_\epsilon = (x, y + \epsilon)$ lies in the same component of
    $\mathbb{R}^2 \setminus \partial P$ as $p$ (possible because $p \notin \partial P$ and
    the components are open). No vertex lies on the line $Y = y + \epsilon$,
    and for every vertex $y_i > y$ if and only if $y_i > y + \epsilon$. So an
    edge passes the code's height test exactly when it crosses the line
    $Y = y + \epsilon$, at the abscissa

    $$
    X_\epsilon = x_0 + (y + \epsilon - y_0)(x_1 - x_0) / (y_1 - y_0).
    $$

    The code compares $x$ with $X_0$. If $x = X_0$, the point $(X_0, y)$ lies
    on the edge, because the height test puts $y$ between the endpoint
    heights, and $p \in \partial P$, which is excluded; so $x \ne X_0$, and by
    continuity $x < X_0$ if and only if $x < X_\epsilon$ for small $\epsilon$.
    Hence the code counts the edges crossed by the rightward ray from
    $p_\epsilon$, which passes through no vertex. Each such crossing moves the
    ray between the interior and the exterior, and far to the right it is
    outside, so the count is odd exactly when $p_\epsilon \in \text{int} P$, that is
    when $p \in \text{int} P$ [Haines (1994)](references.md#haines1994).

??? note "Proof"

    [Rectangles in polygons](../guides/geometry.md#thm-rect-inside)

    If $R \subset \text{int} P$, then $R$ misses $\partial P$, so no edge touches it
    ([Segments and rectangles](../guides/geometry.md#lem-rect-segment)), and its corners lie in $\text{int} P$, off the boundary,
    so they pass the even-odd test ([Even-odd rule](../guides/geometry.md#prop-even-odd)). Conversely, if no edge
    touches $R$, then $R \cap \partial P = \emptyset$ ([Segments and rectangles](../guides/geometry.md#lem-rect-segment)); in
    particular the corners are off the boundary, and passing the test puts
    them in $\text{int} P$. Since $R$ is connected and misses $\partial P$, it lies in
    one component of $\mathbb{R}^2 \setminus \partial P$; it contains a corner of
    $\text{int} P$, so $R \subset \text{int} P$.

??? note "Proof"

    [Rectangles overlapping polygons](../guides/geometry.md#cor-rect-overlap)

    If a corner passes the test, it lies in $\text{int} P$ when it is off the
    boundary ([Even-odd rule](../guides/geometry.md#prop-even-odd)) and in $\partial P$ otherwise; either way
    $R \cap \overline{P} \ne \emptyset$. If an edge touches $R$, then $R$ meets
    $\partial P$. Conversely, suppose $R$ meets $\overline{P}$. If it meets
    $\partial P$, some edge touches it. Otherwise $R$ misses $\partial P$ and
    meets $\text{int} P$, so, being connected, $R \subset \text{int} P$ and its corners
    pass the test.

??? note "Proof"

    [Leaving a polygon for good](../guides/geometry.md#prop-ray-exit)

    Suppose $p = o + t r \in \partial P$ for some $t > T$, on an edge $e$. If $e$
    is not parallel to $r$, the code solves $o + t r = a + u (b - a)$ for $e$
    and finds this $t \ge 0$ with $u \in [0, 1]$, so $T \ge t$, a contradiction.
    If $e$ is parallel to $r$, it lies on the ray's line $\ell$. Take the
    maximal run of consecutive edges on $\ell$ containing $e$. It is not all of
    $P$, whose vertices are not all collinear, so each end of the run is a
    vertex shared with an edge not on $\ell$, hence not parallel to $r$.
    Consecutive edges of the run cannot double back, since two edges leaving
    a vertex in the same direction along $\ell$ would overlap and $P$ is
    simple; so the run is a segment of $\ell$ whose far end, in the direction
    $r$, is an end vertex $v = o + t_v r$ with $t_v \ge t > T$. The adjacent
    non-parallel edge contains $v$ (with $u \in \lbrace 0, 1\rbrace$), so $T \ge t_v$, again
    a contradiction. Thus $\lbrace o + t r : t > T\rbrace$ misses $\partial P$; it is
    connected and unbounded, so it lies in the exterior.

## The pole of inaccessibility

??? note "Proof"

    [Signed distance is 1-Lipschitz](../guides/geometry.md#lem-lipschitz)

    For any set $S$, $|d(p, S) - d(q, S)| \le |p - q|$ by the triangle
    inequality, which settles the case of $p, q$ on the same side. Let
    $p \in \overline{P}$ and $q \notin \overline{P}$, and let $z$ be the last
    point of $\overline{P}$ on the segment from $p$ to $q$ (it exists since
    $\overline{P}$ is closed). Points just past $z$ are outside, so
    $z \notin \text{int} P$ and $z \in \partial P$. Then

    $$
    |f(p) - f(q)| = d(p, \partial P) + d(q, \partial P) \le |p - z| + |z - q| = |p - q|
    $$

??? note "Proof"

    [Pole of inaccessibility](../guides/geometry.md#thm-polylabel)

    The code computes $f$ exactly: off the boundary the sign is right by
    [Even-odd rule](../guides/geometry.md#prop-even-odd), and on it the distance is $0$. Let $b$ denote the best
    value so far; it only increases, and is always $f$ of an evaluated centre.

    _Termination._ Each split halves the half-size $h$. When a cell with
    $h \sqrt{2} \le \epsilon$ is popped, $b \ge f(c)$ after the update, so its
    bound exceeds $b$ by at most $h \sqrt{2} \le \epsilon$ and it is dropped,
    not split. The cells therefore form a finite tree, each pushed and popped
    once.

    _Invariant._ Every point of the bounding box lies in the closed square of
    a cell that is either in the queue or was dropped with
    $f(c) + h \sqrt{2} \le b + \epsilon$ for the $b$ of that moment. The initial
    squares, laid from the lower left corner in steps of the shorter side
    until they pass the far edges, cover the box; dropping keeps the
    invariant by the drop rule; splitting replaces a square by four that
    cover it.

    _Conclusion._ At the end the queue is empty. Let $p^*$ be a pole; it lies
    in $\overline{P}$, inside the box, in the square of a dropped cell with
    centre $c$ and half-size $h$. By [Signed distance is 1-Lipschitz](../guides/geometry.md#lem-lipschitz) and
    $|p^* - c| \le h \sqrt{2}$,

    $$
    f^* = f(p^*) \le f(c) + h \sqrt{2} \le b + \epsilon \le f(q) + \epsilon,
    $$

    where $q$ is the returned point and $f(q)$ the final $b$. If
    $f^* > \epsilon$ then $f(q) > 0$, so $q$ is at positive distance from
    $\partial P$ inside $\overline{P}$, that is in $\text{int} P$.

??? note "Proof"

    [Shape of a brace](../guides/geometry.md#prop-brace)

    Write $r$ for the radius and $\sigma = \delta / 2r \ge 1$ for the
    stretch. Before stretching, the curve consists of: the arc $A_1$ of the
    circle of centre $(0, \ell + r)$ from angle $-90 degree$ to $0 degree$; the
    segment $u = r$ from $v = \ell + r$ to $v = m - r$; the arc $A_2$ of centre
    $(2 r, m - r)$ from $180 degree$ to $90 degree$; the arc $A_3$ of centre
    $(2 r, m + r)$ from $270 degree$ to $180 degree$; the segment $u = r$ from
    $m + r$ to $h - r$; and the arc $A_4$ of centre $(0, h - r)$ from
    $0 degree$ to $90 degree$. (When $r = (h - \ell) / 4$ the segments have
    length zero.) It starts at $(0, \ell)$, ends at $(0, h)$, and $A_2$ and
    $A_3$ meet at $(2 r, m)$, which the stretch $(u, v) |\to (\sigma u, v)$
    sends to $(\delta, m)$.

    (i) On $A_1$ and $A_4$, $u \in [0, r]$; on the segments $u = r$; on $A_2$
    and $A_3$, $u \in [r, 2 r]$. After stretching, $u \in [0, \delta]$.

    (ii) The reflection $v |\to \ell + h - v$ swaps the centres of $A_1$ and
    $A_4$ and of $A_2$ and $A_3$, maps angles $\theta |\to -\theta$, and so maps
    $A_1$ onto $A_4$, $A_2$ onto $A_3$, and the two segments onto each other.

    (iii) Along an arc traversed with increasing angle the direction of
    motion is $(-\sin \theta, \cos \theta)$, and with decreasing angle
    $(\sin \theta, -\cos \theta)$. At the end of $A_1$ ($\theta = 0$) and the start
    of $A_2$ ($\theta = 180 degree$) both give $(0, 1)$, the direction of the
    segment between them; likewise at the end of $A_3$ and the start of $A_4$.
    At the tip, $A_2$ arrives with direction $(1, 0)$ ($\theta = 90 degree$)
    and $A_3$ leaves with $(-1, 0)$ ($\theta = 270 degree$): a cusp. The stretch
    and the final placement are invertible affine maps, which carry tangent
    directions along and keep them non-zero, so continuity and the cusp
    survive.

## Labels

??? note "Proof"

    [Crossing point](../guides/labels.md#lem-crossing)

    A common point satisfies $a + t r = c + u s$ with $r = b - a$ and
    $s = d - c$. Taking the cross product with $s$ removes $u$:
    $t (r \times s) = (c - a) \times s$. A proper crossing puts $a$ and $b$
    strictly on opposite sides of $L_{c d}$, so the lines are not parallel,
    $r \times s \ne 0$, and the point is unique. Since $\text{orient}(c, d, \cdot)$ is
    affine along $[a, b]$ with opposite signs at the ends, its zero is at
    some $t \in (0, 1)$.

??? note "Proof"

    [Choice of a callout](../guides/labels.md#prop-callout)

    After any enumeration prefix, the retained candidate is the first one with
    the least lexicographic key seen. If the near ring's least charge is $0$,
    its least key is $(0, \ell_{\min})$, so stopping returns its first zero-charge,
    shortest-leader candidate. Otherwise the same invariant over the far ring
    yields the first global minimum. The key depends only on the stated inputs,
    and enumeration order is fixed, so the result is deterministic.

## Styles, themes and binding

??? note "Proof"

    [Merging is a monoid](../guides/styles.md#prop-monoid)

    Per field, $x \circ y$ selects the first non-`None` value of $x,y$.
    Thus either association selects the first such value among $x,y,z$;
    `None` is a two-sided identity and $x \circ x=x$. This proves
    (i)–(iii) fieldwise, and induction gives the general rule. Bundles follow
    slot by slot, with a `None` slot as the empty style.

??? note "Proof"

    [Hex round trip](../guides/styles.md#prop-hex)

    A hex pair $k \in \lbrace 0, \ldots, 255\rbrace$ is read as $k / 255$ and written as
    $\text{round}(255 \cdot k / 255)$. Since double-precision error is at most
    $255 \cdot 2^{-52} < 1 / 2$, rounding recovers $k$. Alpha is handled
    likewise when included; three-digit input first doubles each digit.

??? note "Proof"

    [Resolution order](../guides/themes.md#thm-resolution)

    Write $\triangleright$ for merge. Starting from $D$, resolution processes
    $T,G,C$, merging each $M[k_n],\ldots,M[k_1]$ least-specific first; a missing
    key is the empty bundle. It merges last the layer bundle $E$ from
    `style_slots`. By associativity ([Merging is a monoid](../guides/styles.md#prop-monoid)), the result is

    $$
    E \triangleright C[k_1] \triangleright \cdots \triangleright C[k_n] \triangleright G[k_1] \triangleright \cdots \triangleright T[k_n] \triangleright D,
    $$

    so each field is the first non-`None` value in this order. Palette binding
    replaces color names and leaves all other fields unchanged.

??? note "Proof"

    [Overrides beat specificity](../guides/themes.md#cor-override)

    For role `axes.note`, the chain is (`axes.note`, `axes`, `text`), so
    $G[\text{text}]$ precedes $T[\text{axes.note}]$ in [Resolution order](../guides/themes.md#thm-resolution). Since no earlier
    entry sets size, its first non-`None` value is $G[\text{text}]$.

??? note "Proof"

    [Partial binding](../guides/parameters.md#thm-binding)

    Induct on $e$. If $\text{free}(e) \subseteq \text{dom} \beta$, then
    $\text{bind}(e,\beta)=e(\beta)$ is closed and equals $e(\beta \cup \gamma)$ because
    values depend only on free parameters. If $e=p \notin \text{dom} \beta$, the
    result is $p$, with free set $\lbrace p\rbrace =\text{free}(e) \setminus \text{dom} \beta$ and value
    $\gamma(p)=(\beta \cup \gamma)(p)$. Otherwise $e=e_1 \circ e_2$;
    binding acts on both operands (plain values become constants), giving

    $$
    (\text{free}(e_1) \setminus \text{dom} \beta) \cup (\text{free}(e_2) \setminus \text{dom} \beta) = \text{free}(e) \setminus \text{dom} \beta.
    $$

    Since $\gamma$ binds both parts, induction gives

    $$
    e_1(\beta \cup \gamma) \circ e_2(\beta \cup \gamma) = e(\beta \cup \gamma).
    $$

??? note "Proof"

    [Binding in stages](../guides/parameters.md#cor-stages)

    Applying [Partial binding](../guides/parameters.md#thm-binding) (i) twice gives free set
    $\text{free}(e) \setminus \text{dom} (\beta_1 \cup \beta_2)$. If $\gamma$ binds it and is
    disjoint from $\beta_1,\beta_2$, part (ii), applied twice, gives

    $$
    \text{bind}(\text{bind}(e, \beta_1), \beta_2)(\gamma) = \text{bind}(e, \beta_1)(\beta_2 \cup \gamma) = e(\beta_1 \cup \beta_2 \cup \gamma) = \text{bind}(e, \beta_1 \cup \beta_2)(\gamma)
    $$

    A canvas binds every scene expression in this way.

??? note "Proof"

    [Inferred grid shape](../guides/parameters.md#prop-grid-shape)

    From $r = \left\lceil n / c \right\rceil$, $r c \ge n > (r - 1) c$, so the first $r - 1$
    rows are full; the last holds $n-(r-1)c \in [1,c]$ cells and leaves fewer
    than $c$ empty. Since $c=\left\lceil \sqrt\lbrace n\rbrace \right\rceil$ gives $n/c \le c$, also $r \le c$.
