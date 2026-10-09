---
seo_title: "证明"
---

# 证明

<span id="app-proofs"></span>

本附录依各章出现的顺序，证明其中陈述的引理、命题、定理与推论。以下 $b_{i,n}$ 为[Bernstein 多项式](../guides/curves.md#def-bernstein)的 Bernstein 多项式，$B$ 为[Bézier 曲线](../guides/curves.md#def-curve)的 Bézier 曲线，次数为 $n$，控制点为 $P_0, \ldots, P_n$。若某个结果在文献中也有证明，章节中会标明出处；此处的证明写成自足的形式，使手册不依赖某一版本的书。

## Bernstein 基底与求值

??? note "证明"

    [二项式恒等式](../guides/curves.md#lem-binomial)

    _第一式。_ 依 $j$ 的位置分别讨论。
    - 若 $j < 0$ 或 $j > n$，三个系数都为零，因为 $j > n$ 蕴含 $j - 1 > n - 1$。
    - 若 $j = 0$，左边为 $1 + 0 = 1 = \binom{n}{0}$。
    - 若 $j = n$，左边为 $0 + 1 = 1 = \binom{n}{n}$。
    - 若 $1 \le j \le n - 1$，通分为 $j! (n - j)!$：

    $$
    \binom{n-1}{j} + \binom{n-1}{j-1} = ((n-1)! (n - j)) / (j! (n-j)!) + ((n-1)! j) / (j! (n-j)!) = (n-1)! n / (j! (n-j)!) = \binom{n}{j}.
    $$

    _第二式。_ 若 $i < 1$ 或 $i > n$，两边都为零：$i = 0$ 时左边含因子 $i = 0$，且 $\binom{n-1}{-1} = 0$；$i < 0$ 与 $i > n$ 时每个系数都为零。若 $1 \le i \le n$，

    $$
    i \binom{n}{i} = i n! / (i! (n - i)!) = n (n-1)! / ((i-1)! (n-i)!) = n \binom{n-1}{i-1}.
    $$

??? note "证明"

    [Bernstein 基底](../guides/curves.md#prop-basis)

    次数不超过 $n$ 的实系数多项式空间 $\Pi_n$ 的维度为 $n + 1$，一组基底为 $1, t, \ldots, t^n$。$n + 1$ 个多项式 $b_{0,n}, \ldots, b_{n,n}$ 都属于 $\Pi_n$，因此只需证明它们线性无关。设对所有 $t$ 有 $\sum_{i=0}^n c_i b_{i,n}(t) = 0$。对 $t \in (0, 1)$ 除以 $(1 - t)^n > 0$，并令 $u = t / (1 - t) \in (0, \infty)$：

    $$
    \sum_{i=0}^n c_i \binom{n}{i} u^i = 0.
    $$

    有无穷多个根的 $u$ 的多项式必为零多项式，所以每个 $i$ 都有 $c_i \binom{n}{i} = 0$。因 $\binom{n}{i} \ne 0$，所有 $c_i = 0$。

??? note "证明"

    [单位分解](../guides/curves.md#prop-unity)

    当 $t \in [0, 1]$ 时，$t$ 与 $1 - t$ 都非负，因此每个 $b_{i,n}(t)$ 都非负。由二项式定理，

    $$
    \sum_{i=0}^n \binom{n}{i} t^i (1-t)^{n-i} = (t + (1 - t))^n = 1.
    $$

??? note "证明"

    [端点](../guides/curves.md#prop-endpoints)

    约定 $0^0 = 1$。$b_{i,n}(0) = \binom{n}{i} 0^i$ 在 $i = 0$ 时为 $1$，在 $i \ge 1$ 时为 $0$。同理 $b_{i,n}(1) = \binom{n}{i} 0^{n-i}$ 在 $i = n$ 时为 $1$，在 $i < n$ 时为 $0$。因此 $B(0) = \sum_i b_{i,n}(0) P_i = P_0$，$B(1) = \sum_i b_{i,n}(1) P_i = P_n$。

??? note "证明"

    [凸包](../guides/curves.md#cor-hull)

    由[单位分解](../guides/curves.md#prop-unity)，$B(t) = \sum_i \lambda_i P_i$，其中 $\lambda_i = b_{i,n}(t) \ge 0$ 且 $\sum_i \lambda_i = 1$。由定义，点的凸组合位于这些点的凸包内。

??? note "证明"

    [仿射不变性](../guides/curves.md#prop-affine)

    由 $M$ 的线性与[单位分解](../guides/curves.md#prop-unity)（$\sum_i b_{i,n}(t) = 1$），

    $$
    \begin{aligned}A(B(t)) &= M \sum_i b_{i,n}(t) P_i + v \\ &= \sum_i b_{i,n}(t) M P_i + (\sum_i b_{i,n}(t)) v \\ &= \sum_i b_{i,n}(t) (M P_i + v) = \sum_i b_{i,n}(t) A(P_i).\end{aligned}
    $$

??? note "证明"

    [de Casteljau](../guides/curves.md#thm-casteljau)

    对 $r$ 作归纳。$r = 0$ 时，$P_i^{(0)} = P_i = b_{0,0}(t) P_i$。假设对 $r - 1$ 与每个容许的 $i$ 都成立。对 $0 \le i \le n - r$，$i$ 与 $i + 1$ 对 $r - 1$ 都是容许的，因此

    $$
    \begin{aligned}P_i^{(r)} &= (1 - t) \sum_{j=0}^{r-1} b_{j,r-1}(t) P_{i+j} + t \sum_{j=0}^{r-1} b_{j,r-1}(t) P_{i+1+j} \\ &= \sum_{j=0}^r [(1 - t) b_{j,r-1}(t) + t b_{j-1,r-1}(t)] P_{i+j},\end{aligned}
    $$

    其中第二个和式以 $j + 1 \to j$ 重新编号，两端由约定 $b_{-1,r-1} = b_{r,r-1} = 0$ 涵盖。对 $0 \le j \le r$，由[二项式恒等式](../guides/curves.md#lem-binomial)，方括号为

    $$
    \binom{r-1}{j} t^j (1-t)^{r-j} + \binom{r-1}{j-1} t^j (1-t)^{r-j} = \binom{r}{j} t^j (1-t)^{r-j} = b_{j,r}(t).
    $$

    取 $r = n$、$i = 0$，结论即为 $P_0^{(n)} = B(t)$。

??? note "证明"

    [升阶恒等式](../guides/curves.md#lem-raise-identity)

    把 $b_{i,n}(t)$ 乘以 $1 = (1 - t) + t$：

    $$
    b_{i,n}(t) = \binom{n}{i} t^i (1-t)^{n+1-i} + \binom{n}{i} t^{i+1} (1-t)^{n-i}.
    $$

    对 $0 \le i \le n$，$\binom{n+1}{i} = (n + 1) / (n + 1 - i) \cdot \binom{n}{i}$ 且 $\binom{n+1}{i+1} = (n + 1) / (i + 1) \cdot \binom{n}{i}$，所以

    $$
    \binom{n}{i} = (n + 1 - i) / (n + 1) \binom{n+1}{i} = (i + 1) / (n + 1) \binom{n+1}{i+1}.
    $$

    因此第一项是 $b_{i,n+1}(t)$ 的 $(n + 1 - i) / (n + 1)$ 倍，第二项是 $b_{i+1,n+1}(t)$ 的 $(i + 1) / (n + 1)$ 倍。

??? note "证明"

    [升阶](../guides/curves.md#prop-raise-degree)

    由[升阶恒等式](../guides/curves.md#lem-raise-identity)，

    $$
    \begin{aligned}B(t) &= \sum_{i=0}^n [(n + 1 - i) / (n + 1) b_{i,n+1}(t) + (i + 1) / (n + 1) b_{i+1,n+1}(t)] P_i \\ &= \sum_{k=0}^n (n + 1 - k) / (n + 1) b_{k,n+1}(t) P_k + \sum_{k=1}^{n+1} k / (n + 1) b_{k,n+1}(t) P_{k-1},\end{aligned}
    $$

    其中第一个和式取 $k = i$，第二个取 $k = i + 1$。第一个和式的系数在 $k = n + 1$ 为零，可延伸到 $k = n + 1$；第二个和式同理可延伸到 $k = 0$。合并 $b_{k,n+1}(t)$ 的系数即得 $Q_k$。

## 导数、反转与分割

??? note "证明"

    [Bernstein 多项式的导数](../guides/operations.md#lem-bernstein-derivative)

    依 $i$ 的取值分别讨论。
    - 若 $i < 0$ 或 $i > n$，则 $b_{i,n} = 0$，右边两项也为零。
    - 若 $i = 0$，$b_{0,n}(t) = (1 - t)^n$ 的导数为 $-n (1 - t)^{n-1} = n [b_{-1,n-1}(t) - b_{0,n-1}(t)]$。
    - 若 $i = n$，$b_{n,n}(t) = t^n$ 的导数为 $n t^{n-1} = n [b_{n-1,n-1}(t) - b_{n,n-1}(t)]$。
    - 若 $1 \le i \le n - 1$，由乘积法则，

    $$
    b'_{i,n}(t) = \binom{n}{i} [i t^{i-1} (1-t)^{n-i} - (n - i) t^i (1-t)^{n-i-1}].
    $$

      由[二项式恒等式](../guides/curves.md#lem-binomial)，$i \binom{n}{i} = n \binom{n-1}{i-1}$；以 $n - i$ 代替 $i$ 并利用 $\binom{n}{n-i} = \binom{n}{i}$，得 $(n - i) \binom{n}{i} = n \binom{n-1}{i}$。因此两项分别为 $n b_{i-1,n-1}(t)$ 与 $n b_{i,n-1}(t)$。

??? note "证明"

    [速端曲线](../guides/operations.md#thm-hodograph)

    由线性与[Bernstein 多项式的导数](../guides/operations.md#lem-bernstein-derivative)，

    $$
    B'(t) = n \sum_{i=0}^n b_{i-1,n-1}(t) P_i - n \sum_{i=0}^n b_{i,n-1}(t) P_i.
    $$

    第一个和式中 $i = 0$ 的项为零；代入 $k = i - 1$ 得 $\sum_{k=0}^{n-1} b_{k,n-1}(t) P_{k+1}$。第二个和式中 $i = n$ 的项为零。因此

    $$
    B'(t) = n \sum_{k=0}^{n-1} b_{k,n-1}(t) (P_{k+1} - P_k).
    $$

??? note "证明"

    [端点切线](../guides/operations.md#cor-end-tangents)

    由[速端曲线](../guides/operations.md#thm-hodograph)，$B'$ 是控制点为 $D_k = n(P_{k+1} - P_k)$（$k = 0, \ldots, n - 1$）的 $n - 1$ 次 Bézier 曲线。对它套用[端点](../guides/curves.md#prop-endpoints)，得 $B'(0) = D_0$、$B'(1) = D_{n-1}$。

??? note "证明"

    [对称性](../guides/operations.md#lem-symmetry)

    对 $0 \le i \le n$，由 $\binom{n}{i} = \binom{n}{n-i}$，

    $$
    b_{i,n}(1 - t) = \binom{n}{i} (1-t)^i t^{n-i} = \binom{n}{n-i} t^{n-i} (1-t)^i = b_{n-i,n}(t).
    $$

    其他 $i$ 两边都为零。

??? note "证明"

    [反转](../guides/operations.md#prop-reversal)

    令 $j = n - i$ 重新编号，并利用[对称性](../guides/operations.md#lem-symmetry)：

    $$
    \sum_{i=0}^n b_{i,n}(t) P_{n-i} = \sum_{j=0}^n b_{n-j,n}(t) P_j = \sum_{j=0}^n b_{j,n}(1 - t) P_j = B(1 - t).
    $$

??? note "证明"

    [分割](../guides/operations.md#thm-subdivision)

    _左段。_ 因 $1 - c s = (1 - s) + s (1 - c)$，由二项式定理，

    $$
    \begin{aligned}B(c s) &= \sum_{i=0}^n \binom{n}{i} (c s)^i [(1 - s) + s (1 - c)]^{n-i} P_i \\ &= \sum_{i=0}^n \sum_{k=0}^{n-i} \binom{n}{i} \binom{n-i}{k} c^i (1-c)^k s^{i+k} (1-s)^{n-i-k} P_i.\end{aligned}
    $$

    代入 $j = i + k$，则 $0 \le i \le j \le n$ 且 $n - i - k = n - j$。$\binom{n}{i} \binom{n-i}{j-i}$ 与 $\binom{n}{j} \binom{j}{i}$ 都等于 $n! / (i! (j-i)! (n-j)!)$，故

    $$
    \begin{aligned}B(c s) &= \sum_{j=0}^n \binom{n}{j} s^j (1-s)^{n-j} \sum_{i=0}^j \binom{j}{i} c^i (1-c)^{j-i} P_i \\ &= \sum_{j=0}^n b_{j,n}(s) P_0^{(j)}.\end{aligned}
    $$

    最后一步用[de Casteljau](../guides/curves.md#thm-casteljau)取 $r = j$、$i = 0$：$P_0^{(j)} = \sum_{i=0}^j b_{i,j}(c) P_i$。这就是 $L_j$ 的结论。

    _右段。_ 令 $\overline{B}$ 为控制点 $\overline{P}_i = P_{n-i}$ 的曲线，由[反转](../guides/operations.md#prop-reversal)，$\overline{B}(u) = B(1 - u)$；令 $\overline{c} = 1 - c$。对 $\overline{B}$ 套用左段，

    $$
    \overline{B}(\overline{c} s) = \sum_{j=0}^n b_{j,n}(s) \overline{L}_j,
    $$

    其中由[对称性](../guides/operations.md#lem-symmetry)与代换 $l = j - i$，

    $$
    \overline{L}_j = \sum_{i=0}^j b_{i,j}(1 - c) P_{n-i} = \sum_{l=0}^j b_{l,j}(c) P_{n-j+l} = P_{n-j}^{(j)} = R_{n-j}.
    $$

    倒数第二个等号是[de Casteljau](../guides/curves.md#thm-casteljau)取 $r = j$、$i = n - j$，此指标是容许的，因为 $n - j \le n - r$。因此再用一次[对称性](../guides/operations.md#lem-symmetry)，

    $$
    \begin{aligned}B(c + (1 - c) s) &= \overline{B}(\overline{c} (1 - s)) = \sum_{j=0}^n b_{j,n}(1 - s) R_{n-j} \\ &= \sum_{j=0}^n b_{n-j,n}(s) R_{n-j} = \sum_{k=0}^n b_{k,n}(s) R_k.\end{aligned}
    $$

??? note "证明"

    [截取](../guides/operations.md#cor-segment)

    令 $a = t_0$、$e = t_1$，则 $0 \le a < e \le 1$。由[分割](../guides/operations.md#thm-subdivision)取 $c = e$，左段是控制点为 $L_0, \ldots, L_n$ 的 Bézier 曲线 $u |\to B(e u)$。对它再套用[分割](../guides/operations.md#thm-subdivision)，取 $c' = a / e \in [0, 1)$ 并保留右段：

    $$
    s |\to B(e (a/e + (1 - a/e) s)) = B(a + (e - a) s).
    $$
