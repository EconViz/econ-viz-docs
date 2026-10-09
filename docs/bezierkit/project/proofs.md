---
seo_title: "Proofs"
---

# Proofs

<span id="app-proofs"></span>

This appendix proves the lemmas, propositions, theorems and corollaries
stated in the chapters, in the order they appear. Throughout, $b_{i,n}$ is
the Bernstein polynomial of [Bernstein polynomials](../guides/curves.md#def-bernstein) and $B$ the Bézier curve of
[Bézier curve](../guides/curves.md#def-curve), of degree $n$ with control points $P_0, \ldots, P_n$. Where a
result is also proved in the literature, the chapter names the source; the
proofs here are written out so that the manual does not depend on a
particular edition of a book.

## The Bernstein basis and evaluation

??? note "Proof"

    [Binomial identities](../guides/curves.md#lem-binomial)

    _First identity._ We distinguish the position of $j$.
    - If $j < 0$ or $j > n$, all three coefficients vanish, since
      $j > n$ implies $j - 1 > n - 1$.
    - If $j = 0$, the left side is $1 + 0 = 1 = \binom{n}{0}$.
    - If $j = n$, it is $0 + 1 = 1 = \binom{n}{n}$.
    - If $1 \le j \le n - 1$, put the terms over the common denominator
      $j! (n - j)!$:

    $$
    \binom{n-1}{j} + \binom{n-1}{j-1} = ((n-1)! (n - j)) / (j! (n-j)!) + ((n-1)! j) / (j! (n-j)!) = (n-1)! n / (j! (n-j)!) = \binom{n}{j}.
    $$

    _Second identity._ If $i < 1$ or $i > n$ both sides vanish: for $i = 0$ the
    left side has the factor $i = 0$ and $\binom{n-1}{-1} = 0$; for $i < 0$ and
    $i > n$ every coefficient is zero. If $1 \le i \le n$,

    $$
    i \binom{n}{i} = i n! / (i! (n - i)!) = n (n-1)! / ((i-1)! (n-i)!) = n \binom{n-1}{i-1}.
    $$

??? note "Proof"

    [Bernstein basis](../guides/curves.md#prop-basis)

    The space $\Pi_n$ of real polynomials of degree at most $n$ has dimension
    $n + 1$, with basis $1, t, \ldots, t^n$. The $n + 1$ polynomials
    $b_{0,n}, \ldots, b_{n,n}$ lie in $\Pi_n$, so it suffices to show that they
    are linearly independent. Let $\sum_{i=0}^n c_i b_{i,n}(t) = 0$ for all
    $t$. For $t \in (0, 1)$ divide by $(1 - t)^n > 0$ and put
    $u = t / (1 - t) \in (0, \infty)$:

    $$
    \sum_{i=0}^n c_i \binom{n}{i} u^i = 0.
    $$

    A polynomial in $u$ with infinitely many roots is the zero polynomial, so
    $c_i \binom{n}{i} = 0$ for every $i$. Since $\binom{n}{i} \ne 0$, all
    $c_i = 0$.

??? note "Proof"

    [Partition of unity](../guides/curves.md#prop-unity)

    For $t \in [0, 1]$ both $t$ and $1 - t$ are non-negative, hence so is every
    $b_{i,n}(t)$. By the binomial theorem,

    $$
    \sum_{i=0}^n \binom{n}{i} t^i (1-t)^{n-i} = (t + (1 - t))^n = 1.
    $$

??? note "Proof"

    [Endpoints](../guides/curves.md#prop-endpoints)

    With the convention $0^0 = 1$, $b_{i,n}(0) = \binom{n}{i} 0^i$ equals $1$
    for $i = 0$ and $0$ for $i \ge 1$. Likewise
    $b_{i,n}(1) = \binom{n}{i} 0^{n-i}$ equals $1$ for $i = n$ and $0$ for
    $i < n$. Hence $B(0) = \sum_i b_{i,n}(0) P_i = P_0$ and
    $B(1) = \sum_i b_{i,n}(1) P_i = P_n$.

??? note "Proof"

    [Convex hull](../guides/curves.md#cor-hull)

    By [Partition of unity](../guides/curves.md#prop-unity), $B(t) = \sum_i \lambda_i P_i$ with $\lambda_i = b_{i,n}(t) \ge 0$
    and $\sum_i \lambda_i = 1$. A convex combination of points lies in their
    convex hull by definition.

??? note "Proof"

    [Affine invariance](../guides/curves.md#prop-affine)

    By linearity of $M$ and [Partition of unity](../guides/curves.md#prop-unity), which gives $\sum_i b_{i,n}(t) = 1$,

    $$
    \begin{aligned}A(B(t)) &= M \sum_i b_{i,n}(t) P_i + v \\ &= \sum_i b_{i,n}(t) M P_i + (\sum_i b_{i,n}(t)) v \\ &= \sum_i b_{i,n}(t) (M P_i + v) = \sum_i b_{i,n}(t) A(P_i).\end{aligned}
    $$

??? note "Proof"

    [de Casteljau](../guides/curves.md#thm-casteljau)

    By induction on $r$. For $r = 0$, $P_i^{(0)} = P_i = b_{0,0}(t) P_i$.
    Assume the claim holds for $r - 1$, for every admissible $i$. For
    $0 \le i \le n - r$ both $i$ and $i + 1$ are admissible for $r - 1$, so

    $$
    \begin{aligned}P_i^{(r)} &= (1 - t) \sum_{j=0}^{r-1} b_{j,r-1}(t) P_{i+j} + t \sum_{j=0}^{r-1} b_{j,r-1}(t) P_{i+1+j} \\ &= \sum_{j=0}^r [(1 - t) b_{j,r-1}(t) + t b_{j-1,r-1}(t)] P_{i+j},\end{aligned}
    $$

    where the second sum was re-indexed by $j + 1 \to j$, and the convention
    $b_{-1,r-1} = b_{r,r-1} = 0$ covers the two ends. For $0 \le j \le r$ the
    bracket is

    $$
    \binom{r-1}{j} t^j (1-t)^{r-j} + \binom{r-1}{j-1} t^j (1-t)^{r-j} = \binom{r}{j} t^j (1-t)^{r-j} = b_{j,r}(t)
    $$

    by [Binomial identities](../guides/curves.md#lem-binomial). For $r = n$ and $i = 0$ the claim reads
    $P_0^{(n)} = B(t)$.

??? note "Proof"

    [Degree elevation identity](../guides/curves.md#lem-raise-identity)

    Multiply $b_{i,n}(t)$ by $1 = (1 - t) + t$:

    $$
    b_{i,n}(t) = \binom{n}{i} t^i (1-t)^{n+1-i} + \binom{n}{i} t^{i+1} (1-t)^{n-i}.
    $$

    Since $\binom{n+1}{i} = (n + 1) / (n + 1 - i) \cdot \binom{n}{i}$ and
    $\binom{n+1}{i+1} = (n + 1) / (i + 1) \cdot \binom{n}{i}$ for
    $0 \le i \le n$,

    $$
    \binom{n}{i} = (n + 1 - i) / (n + 1) \binom{n+1}{i} = (i + 1) / (n + 1) \binom{n+1}{i+1}.
    $$

    The first term is therefore $(n + 1 - i) / (n + 1)$ times
    $b_{i,n+1}(t)$ and the second $(i + 1) / (n + 1)$ times
    $b_{i+1,n+1}(t)$.

??? note "Proof"

    [Degree elevation](../guides/curves.md#prop-raise-degree)

    By [Degree elevation identity](../guides/curves.md#lem-raise-identity),

    $$
    \begin{aligned}B(t) &= \sum_{i=0}^n [(n + 1 - i) / (n + 1) b_{i,n+1}(t) + (i + 1) / (n + 1) b_{i+1,n+1}(t)] P_i \\ &= \sum_{k=0}^n (n + 1 - k) / (n + 1) b_{k,n+1}(t) P_k + \sum_{k=1}^{n+1} k / (n + 1) b_{k,n+1}(t) P_{k-1},\end{aligned}
    $$

    where $k = i$ in the first sum and $k = i + 1$ in the second. The first sum
    may be extended to $k = n + 1$, since its coefficient vanishes there, and
    the second to $k = 0$, for the same reason. Collecting the coefficient of
    $b_{k,n+1}(t)$ gives $Q_k$.

## Derivatives, reversal and subdivision

??? note "Proof"

    [Derivative of the Bernstein polynomials](../guides/operations.md#lem-bernstein-derivative)

    We treat the possible values of $i$ in turn.
    - If $i < 0$ or $i > n$, then $b_{i,n} = 0$ and both terms on the right
      vanish.
    - If $i = 0$, $b_{0,n}(t) = (1 - t)^n$ has derivative $-n (1 - t)^{n-1} = n [b_{-1,n-1}(t) - b_{0,n-1}(t)]$.
    - If $i = n$, $b_{n,n}(t) = t^n$ has derivative $n t^{n-1} = n [b_{n-1,n-1}(t) - b_{n,n-1}(t)]$.
    - If $1 \le i \le n - 1$, the product rule gives

    $$
    b'_{i,n}(t) = \binom{n}{i} [i t^{i-1} (1-t)^{n-i} - (n - i) t^i (1-t)^{n-i-1}].
    $$

      By [Binomial identities](../guides/curves.md#lem-binomial), $i \binom{n}{i} = n \binom{n-1}{i-1}$, and, applying it
      to $n - i$ and using $\binom{n}{n-i} = \binom{n}{i}$,
      $(n - i) \binom{n}{i} = n \binom{n-1}{i}$. The two terms are therefore
      $n b_{i-1,n-1}(t)$ and $n b_{i,n-1}(t)$.

??? note "Proof"

    [Hodograph](../guides/operations.md#thm-hodograph)

    By linearity and [Derivative of the Bernstein polynomials](../guides/operations.md#lem-bernstein-derivative),

    $$
    B'(t) = n \sum_{i=0}^n b_{i-1,n-1}(t) P_i - n \sum_{i=0}^n b_{i,n-1}(t) P_i.
    $$

    In the first sum the term $i = 0$ vanishes; substituting $k = i - 1$ gives
    $\sum_{k=0}^{n-1} b_{k,n-1}(t) P_{k+1}$. In the second the term $i = n$
    vanishes. Hence

    $$
    B'(t) = n \sum_{k=0}^{n-1} b_{k,n-1}(t) (P_{k+1} - P_k).
    $$

??? note "Proof"

    [End tangents](../guides/operations.md#cor-end-tangents)

    By [Hodograph](../guides/operations.md#thm-hodograph), $B'$ is the Bézier curve of degree $n - 1$ with control
    points $D_k = n(P_{k+1} - P_k)$, $k = 0, \ldots, n - 1$. By
    [Endpoints](../guides/curves.md#prop-endpoints) applied to it, $B'(0) = D_0$ and $B'(1) = D_{n-1}$.

??? note "Proof"

    [Symmetry](../guides/operations.md#lem-symmetry)

    For $0 \le i \le n$, since $\binom{n}{i} = \binom{n}{n-i}$,

    $$
    b_{i,n}(1 - t) = \binom{n}{i} (1-t)^i t^{n-i} = \binom{n}{n-i} t^{n-i} (1-t)^i = b_{n-i,n}(t).
    $$

    For other $i$ both sides are zero.

??? note "Proof"

    [Reversal](../guides/operations.md#prop-reversal)

    Re-index with $j = n - i$ and use [Symmetry](../guides/operations.md#lem-symmetry):

    $$
    \sum_{i=0}^n b_{i,n}(t) P_{n-i} = \sum_{j=0}^n b_{n-j,n}(t) P_j = \sum_{j=0}^n b_{j,n}(1 - t) P_j = B(1 - t).
    $$

??? note "Proof"

    [Subdivision](../guides/operations.md#thm-subdivision)

    _Left part._ Since $1 - c s = (1 - s) + s (1 - c)$, the binomial theorem
    gives

    $$
    \begin{aligned}B(c s) &= \sum_{i=0}^n \binom{n}{i} (c s)^i [(1 - s) + s (1 - c)]^{n-i} P_i \\ &= \sum_{i=0}^n \sum_{k=0}^{n-i} \binom{n}{i} \binom{n-i}{k} c^i (1-c)^k s^{i+k} (1-s)^{n-i-k} P_i.\end{aligned}
    $$

    Substitute $j = i + k$, so that $0 \le i \le j \le n$ and $n - i - k = n - j$.
    Both $\binom{n}{i} \binom{n-i}{j-i}$ and $\binom{n}{j} \binom{j}{i}$ equal
    $n! / (i! (j-i)! (n-j)!)$, hence

    $$
    \begin{aligned}B(c s) &= \sum_{j=0}^n \binom{n}{j} s^j (1-s)^{n-j} \sum_{i=0}^j \binom{j}{i} c^i (1-c)^{j-i} P_i \\ &= \sum_{j=0}^n b_{j,n}(s) P_0^{(j)}.\end{aligned}
    $$

    The last step uses [de Casteljau](../guides/curves.md#thm-casteljau) with $r = j$ and $i = 0$:
    $P_0^{(j)} = \sum_{i=0}^j b_{i,j}(c) P_i$. This is the claim for the $L_j$.

    _Right part._ Let $\overline{B}$ be the curve with control points
    $\overline{P}_i = P_{n-i}$, so that $\overline{B}(u) = B(1 - u)$ by
    [Reversal](../guides/operations.md#prop-reversal), and put $\overline{c} = 1 - c$. The left part applied to
    $\overline{B}$ gives

    $$
    \overline{B}(\overline{c} s) = \sum_{j=0}^n b_{j,n}(s) \overline{L}_j,
    $$

    where, by [Symmetry](../guides/operations.md#lem-symmetry) and the substitution $l = j - i$,

    $$
    \overline{L}_j = \sum_{i=0}^j b_{i,j}(1 - c) P_{n-i} = \sum_{l=0}^j b_{l,j}(c) P_{n-j+l} = P_{n-j}^{(j)} = R_{n-j}.
    $$

    The next-to-last equality is [de Casteljau](../guides/curves.md#thm-casteljau) with $r = j$ and
    $i = n - j$, an admissible index since $n - j \le n - r$. Therefore, using
    [Symmetry](../guides/operations.md#lem-symmetry) once more,

    $$
    \begin{aligned}B(c + (1 - c) s) &= \overline{B}(\overline{c} (1 - s)) = \sum_{j=0}^n b_{j,n}(1 - s) R_{n-j} \\ &= \sum_{j=0}^n b_{n-j,n}(s) R_{n-j} = \sum_{k=0}^n b_{k,n}(s) R_k.\end{aligned}
    $$

??? note "Proof"

    [Segment extraction](../guides/operations.md#cor-segment)

    Write $a = t_0$ and $e = t_1$, so $0 \le a < e \le 1$. By
    [Subdivision](../guides/operations.md#thm-subdivision) with $c = e$, the left part is the Bézier curve
    $u |\to B(e u)$ with control points $L_0, \ldots, L_n$. Apply
    [Subdivision](../guides/operations.md#thm-subdivision) to it with $c' = a / e \in [0, 1)$ and keep the right
    part:

    $$
    s |\to B(e (a/e + (1 - a/e) s)) = B(a + (e - a) s).
    $$
