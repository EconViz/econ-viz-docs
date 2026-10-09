---
seo_title: "近似方法的證明"
---

# 近似方法的證明

## 三次線段與路徑

??? note "證明"

    [三次曲線的邊界框](../guides/paths.md#prop-bbox)

    展開三次 Bernstein 形式並依 $t$ 的次方合併，

    $$
    \begin{aligned}B(t) &= (1-t)^3 P_0 + 3t(1-t)^2 P_1 + 3t^2(1-t) P_2 + t^3 P_3 \\ &= (1 - 3t + 3t^2 - t^3) P_0 + (3t - 6t^2 + 3t^3) P_1 + (3t^2 - 3t^3) P_2 + t^3 P_3 \\ &= a t^3 + b t^2 + c t + P_0,\end{aligned}
    $$

    其中 $a$、$b$、$c$ 如命題所述。

    固定座標 $k$。$B_k$ 是多項式，在緊緻區間 $[0, 1]$ 上連續，因此在其上取得最小值與最大值。設 $t^*$ 是取得其中一個的點。若 $t^* \in (0, 1)$，則 $B_k$ 在內點有極值且可微，故 $B'_k (t^*) = 0$（Fermat 定理）。分兩種情形。
    - $B'_k$ 不恆為零。它是次數至多為 2 的多項式，至多有兩個根；若 $t^*$ 在 $(0, 1)$ 內，它就是其中之一。每種情形都有 $t^* \in T_k$。
    - $B'_k$ 恆為零。則 $B_k$ 為常數，其極值在 $t = 0$ 也取得，且 $0 \in T_k$。
    因此 $B_k$ 在 $[0, 1]$ 上的最小值與最大值，等於它在有限集 $T_k \subset [0, 1]$ 上的最小值與最大值，也就是命題中的 $\alpha_k$ 與 $\beta_k$，因為它們就是 $B_k$ 在曲線上的下確界與上確界。由[軸對齊邊界框](../guides/paths.md#def-bbox)，邊界框是各區間 $[\alpha_k, \beta_k]$ 的乘積：包含曲線的方框必包含每個值 $B_k (t)$，因而包含 $\alpha_k$ 與 $\beta_k$；而這些區間的乘積本身就包含曲線。

??? note "證明"

    [直線與二次曲線的三次表示](../guides/paths.md#prop-elevation)

    _直線。_直線 $t |\to (1 - t) P_0 + t P_3$ 是控制點為 $R_0 = P_0$、$R_1 = P_3$ 的一次 Bézier 曲線。由[升階](../guides/curves.md#prop-raise-degree)取 $n = 1$，它是控制點為

    $$
    Q_0 = P_0, \quad Q_1 = 1/2 P_0 + 1/2 P_3, \quad Q_2 = P_3
    $$

    的二次曲線。再套用[升階](../guides/curves.md#prop-raise-degree)取 $n = 2$，得到控制點為

    $$
    \begin{aligned}S_0 &= Q_0 = P_0, \\ S_1 &= 1/3 Q_0 + 2/3 Q_1 = 2/3 P_0 + 1/3 P_3, \\ S_2 &= 2/3 Q_1 + 1/3 Q_2 = 1/3 P_0 + 2/3 P_3, \\ S_3 &= Q_2 = P_3\end{aligned}
    $$

    的三次曲線，亦即對 $i = 0, \ldots, 3$ 有 $S_i = P_0 + i/3 (P_3 - P_0)$。

    _二次曲線。_由[升階](../guides/curves.md#prop-raise-degree)取 $n = 2$ 與控制點 $P_0, C, P_3$，三次控制點為

    $$
    Q_0 = P_0, \quad Q_1 = 1/3 P_0 + 2/3 C, \quad Q_2 = 2/3 C + 1/3 P_3, \quad Q_3 = P_3,
    $$

    即 $Q_1 = P_0 + 2/3 (C - P_0)$、$Q_2 = P_3 + 2/3 (C - P_3)$。

    每一步都是關於 $t$ 的恆等式，因此曲線與其參數化不變。

??? note "證明"

    [三次曲線接點的連續性](../guides/paths.md#prop-continuity)

    令 $B_S$、$B_T$ 為控制點分別是 $P_i$ 與 $Q_i$ 的三次 Bézier 曲線，使 $S(u) = B_S ((u - u_0 + h_S) / h_S)$、$T(u) = B_T ((u - u_0) / h_T)$。在 $u = u_0$ 處，兩個引數分別為 $1$ 與 $0$。由[端點](../guides/curves.md#prop-endpoints)，$S(u_0) = P_3$、$T(u_0) = Q_0$。由連鎖律與[端點切線](../guides/operations.md#cor-end-tangents)，

    $$
    S'(u_0) = (B'_S (1)) / h_S = (3(P_3 - P_2)) / h_S, \quad T'(u_0) = (B'_T (0)) / h_T = (3(Q_1 - Q_0)) / h_T.
    $$

    + 由[參數連續性](../guides/paths.md#def-continuity)取 $k = 0$，$C$ 在 $u_0$ 為 $C^0$ 若且唯若 $S(u_0) = T(u_0)$，即 $P_3 = Q_0$。
    + 當 $P_3 = Q_0$，[參數連續性](../guides/paths.md#def-continuity)取 $k = 1$ 多出 $S'(u_0) = T'(u_0)$ 的條件，兩邊除以 3 即所述等式。
    + 當 $P_3 = Q_0$，由[幾何連續性 $G^1$](../guides/paths.md#def-geometric-continuity)，接點為 $G^1$ 若且唯若 $S'(u_0) \ne 0$、$T'(u_0) \ne 0$，且存在 $\lambda > 0$ 使 $T'(u_0) = \lambda S'(u_0)$。兩個切向量皆非零，若且唯若 $P_3 \ne P_2$ 且 $Q_1 \ne Q_0$，此時

    $$
    Q_1 - Q_0 = (\lambda h_T / h_S) (P_3 - P_2).
    $$

      反之，若 $Q_1 - Q_0 = \mu (P_3 - P_2)$ 且 $\mu > 0$，取 $\lambda = \mu h_S / h_T > 0$，即得 $T'(u_0) = \lambda S'(u_0)$。
    + 均勻參數化下，$m$ 段路徑的每段占 $1 / m$，故 $h_S = h_T$，第 2 項的等式化為 $P_3 - P_2 = Q_1 - Q_0$。

## 建構與插值

??? note "證明"

    [端點條件](../guides/construction.md#prop-endpoint)

    對具所述控制點的曲線 $B$，由[端點](../guides/curves.md#prop-endpoints)得 $B(0) = P_0$、$B(1) = P_3$，由[端點切線](../guides/operations.md#cor-end-tangents)得

    $$
    B'(0) = 3(P_1 - P_0) = D_0, \quad B'(1) = 3(P_3 - P_2) = D_1.
    $$

    再設 $\Gamma$ 是任一次數至多為 3、滿足 $\Gamma(0) = P_0$、$\Gamma(1) = P_3$、$\Gamma'(0) = D_0$、$\Gamma'(1) = D_1$ 的多項式曲線。對每個座標套用[Bernstein 基底](../guides/curves.md#prop-basis)，存在唯一的 $R_0, \ldots, R_3$ 使 $\Gamma(t) = \sum_i b_{i,3}(t) R_i$。對控制點 $R_i$ 作上述計算，得

    $$
    \Gamma(0) = R_0, \quad \Gamma(1) = R_3, \quad \Gamma'(0) = 3(R_1 - R_0), \quad \Gamma'(1) = 3(R_3 - R_2).
    $$

    與四個條件比較，得 $R_0 = P_0$、$R_3 = P_3$、$R_1 = P_0 + D_0 / 3$、$R_2 = P_3 - D_1 / 3$。所以 $R_i$ 就是所述的控制點，$\Gamma = B$。

??? note "證明"

    [存在性與唯一性](../guides/construction.md#prop-hermite-unique)

    令 $G(s) = H(x_0 + h s)$。映射 $H |\to G$ 是次數至多為 3 的多項式集合上的雙射，反映射為 $G |\to G((x - x_0) / h)$。由連鎖律，$H(x_i) = f_i$ 與 $H'(x_i) = m_i$（$i = 0, 1$）等價於

    $$
    G(0) = f_0, \quad G(1) = f_1, \quad G'(0) = h m_0, \quad G'(1) = h m_1.
    $$

    由[端點條件](../guides/construction.md#prop-endpoint)取 $d = 1$、$P_0 = f_0$、$P_3 = f_1$、$D_0 = h m_0$、$D_1 = h m_1$，恰有一個次數至多為 3 的多項式 $G$ 滿足這四個條件，其 Bernstein 係數為 $c_0, \ldots, c_3$。因此 $H$ 存在、唯一，且等於 $\sum_i b_{i,3}((x - x_0) / h) c_i$。

??? note "證明"

    [Hermite 插值](../guides/construction.md#prop-hermite)

    在 $t = t_0$ 與 $t = t_1$，線段分別於 $s = 0$ 與 $s = 1$ 求值，由[端點](../guides/curves.md#prop-endpoints)得 $H(t_0) = P_0$、$H(t_1) = P_3$。由連鎖律，$H'(t) = B'(s) / h$。由[端點切線](../guides/operations.md#cor-end-tangents)，$B'(0) = 3(P_1 - P_0) = h D_0$、$B'(1) = 3(P_3 - P_2) = h D_1$，故 $H'(t_0) = D_0$、$H'(t_1) = D_1$。證明中不需要 $h > 0$。

??? note "證明"

    [圖形形式](../guides/construction.md#prop-graph-hermite)

    將線段寫成 $(X(s), Y(s))$。$X$ 的控制點為

    $$
    x_0, \quad x_0 + h/3, \quad x_1 - h/3 = x_0 + 2h/3, \quad x_1,
    $$

    由[直線與二次曲線的三次表示](../guides/paths.md#prop-elevation)（由 $x_0$ 到 $x_1$ 的直線），它們正是直線 $s |\to x_0 + h s$ 的控制點，故 $X(s) = x_0 + h s$。$Y$ 的控制點為 $y_0, y_0 + h m_0 / 3, y_1 - h m_1 / 3, y_1$，即[存在性與唯一性](../guides/construction.md#prop-hermite-unique)中對資料 $y_i = f(x_i)$、$m_i = f'(x_i)$ 的係數 $c_0, \ldots, c_3$。因此 $Y(s) = H(x_0 + h s)$，線段為 $s |\to (x_0 + h s, H(x_0 + h s))$。

??? note "證明"

    [Hermite 誤差界限](../guides/construction.md#thm-hermite-error)

    $x \in \lbrace x_0, x_1\rbrace$ 的情形是平凡的：第一個公式兩邊皆為零，對任何 $\xi$ 都成立。設 $x_0 < x < x_1$，並令

    $$
    E = f - H, \quad w(t) = (t - x_0)^2 (t - x_1)^2, \quad K = E(x) / w(x), \quad g = E - K w.
    $$

    則 $w(x) > 0$，$g$ 四階連續可微，且 $g(x_0) = g(x) = g(x_1) = 0$：$E$ 與 $w$ 在 $x_0$、$x_1$ 為零，而 $g(x) = E(x) - K w(x) = 0$。此外 $g'(x_0) = g'(x_1) = 0$：由[三次 Hermite 插值多項式](../guides/construction.md#def-hermite)，$E'(x_i) = f'(x_i) - H'(x_i) = 0$，而 $w$ 在每個 $x_i$ 有二重根，故 $w'(x_i) = 0$。

    由 Rolle 定理（[Burden (2011)](references.md#burden2011) 的定理 1.7），$g'$ 在某個 $\xi_1 \in (x_0, x)$ 與某個 $\xi_2 \in (x, x_1)$ 為零。因此 $g'$ 有四個相異零點 $x_0 < \xi_1 < \xi_2 < x_1$。$g'$ 連續且三階可微，由廣義 Rolle 定理（[Burden (2011)](references.md#burden2011) 的定理 1.10），存在 $\xi \in (x_0, x_1)$ 使 $g^{(4)}(\xi) = 0$。由於 $H$ 的次數至多為 3，而 $w$ 是首項係數為 1 的四次多項式，$H^{(4)} = 0$、$w^{(4)} = 24$，因此

    $$
    0 = g^{(4)}(\xi) = f^{(4)}(\xi) - 24 K, \quad \text{即} \quad K = (f^{(4)}(\xi)) / 24.
    $$

    故 $f(x) - H(x) = E(x) = K w(x)$，這就是第一個公式。

    關於界限：$(x - x_0)(x_1 - x)$ 是兩個和為 $h$ 的非負數之積，至多為 $(h / 2)^2$。因此 $w(x) \le h^4 / 16$，

    $$
    |f(x) - H(x)| \le M / 24 \cdot h^4 / 16 = (M h^4) / 384.
    $$

## 擬合與等值線

??? note "證明"

    [自適應擬合的深度](../guides/fitting.md#cor-depth)

    設 $[a, b]$ 是深度 $k$ 的區間，則 $b - a = L / 2^k$。在此區間上，Hermite 線段的每個座標都是 $C$ 同一座標的三次 Hermite 插值多項式（詳見[Hermite 插值](../guides/construction.md#prop-hermite)與[存在性與唯一性](../guides/construction.md#prop-hermite-unique)），因此由[Hermite 誤差界限](../guides/construction.md#thm-hermite-error)，其誤差不超過 $M (b - a)^4 / 384$。任一參數處的歐氏誤差至多為最大座標誤差的 $\sqrt{d}$ 倍，因為對 $v \in \mathbb{R}^d$ 有 $\left\lVert v \right\rVert_2 \le \sqrt{d} \left\lVert v \right\rVert_\infty$：事實上 $\left\lVert v \right\rVert_2^2 = \sum_k v_k^2 \le d \left\lVert v \right\rVert_\infty^2$。特別地，在量測參數上取最大值得到的實測誤差滿足

    $$
    e \le \sqrt{d} M L^4 / (384 \cdot 2^{4k}).
    $$

    此值不超過 $\epsilon$，若且唯若 $2^{4k} \ge \sqrt{d} M L^4 / (384 \epsilon)$，也就是 $k \ge 1/4 \log_2 (\sqrt{d} M L^4 / (384 \epsilon))$。每個 $k \ge k^*$ 都滿足此式，所以該深度的每個區間都會被接受。

    再設 `max_depth` $\ge k^*$ 且 `max_segments` $\ge 2^{k^*}$。區間只有在不合格時才會被分割，而這只發生在深度 $k < k^*$。因此所有區間的深度至多為 $k^*$，不會因深度而拋出 `ToleranceNotMet`。被接受的區間是把 $[t_0, t_1]$ 對半至多 $k^*$ 次得到的互不重疊的片段，所以至多有 $2^{k^*}$ 個。不合格的區間至少會產生兩個被接受的線段，因此「目前已接受的線段數加二」不會超過這個最終數目，而它至多為 `max_segments`；所以線段數上限也不會被超過。

??? note "證明"

    [折線容許誤差](../guides/fitting.md#prop-rdp)

    以 `rdp`$(i, j)$ 表示演算法對指標 $i < j$ 執行的遞迴步驟，它回傳由 $i$ 到 $j$ 的遞增指標列表。對 $j - i$ 作強歸納，證明對回傳列表中任兩個相鄰指標 $u < v$，每個滿足 $u \le l \le v$ 的指標 $l$ 都有 $\text{dist}(v_l, [v_u, v_v]) \le \epsilon$。

    _基底。_若 $j \le i + 1$，列表為 $(i, j)$，且介於 $i$ 與 $j$（含）之間的指標只有 $i$ 與 $j$，其頂點就是弦的端點，距離為零。

    _歸納步驟。_否則令 $\delta^*$ 為嚴格介於 $i$ 與 $j$ 之間的頂點到 $[v_i, v_j]$ 的最大距離。若 $\delta^* \le \epsilon$，列表為 $(i, j)$，由 $\delta^*$ 的選取以及端點距離為零，結論成立。若 $\delta^* > \epsilon$，步驟選取指標 $m$，$i < m < j$，並回傳 $\text{rdp}(i, m)$ 的列表接上 $\text{rdp}(m, j)$ 的列表，$m$ 只出現一次。結果中任兩個相鄰指標，在這兩個列表之一中也是相鄰的。由於 $m - i$ 與 $j - m$ 都小於 $j - i$，歸納假設適用於兩者。

    步驟 2 與 3 對步驟 2 保留的每兩個相鄰頂點執行 `rdp` 並串接結果。輸出恰保留回傳的指標 $a_0 < \ldots < a_m$，其中每兩個相鄰指標在某個列表中也相鄰。這就證明了不等式。輸出線段的 `fit_error` 是 $\max_{a_j \le i \le a_{j+1}} \text{dist}(v_i, [v_{a_j}, v_{a_{j+1}}])$，因此不超過 $\epsilon$。

??? note "證明"

    [與折線的偏差](../guides/fitting.md#cor-rdp-path)

    1. 到凸集的距離是凸函數。對線段 $K = [a, b]$，設 $x_1, x_2$ 滿足 $\text{dist}(x_i, K) \le \epsilon$，並在 $y_i \in K$ 取得（由緊緻性，最小值存在），$\lambda \in [0, 1]$。則 $\lambda y_1 + (1 - \lambda) y_2 \in K$，由三角不等式，

    $$
    \left\lVert \lambda x_1 + (1 - \lambda) x_2 - (\lambda y_1 + (1 - \lambda) y_2) \right\rVert_2 \le \lambda \left\lVert x_1 - y_1 \right\rVert_2 + (1 - \lambda) \left\lVert x_2 - y_2 \right\rVert_2 \le \epsilon.
    $$

    所以 $\text{dist}(\lambda x_1 + (1 - \lambda) x_2, K) \le \epsilon$。

    折線上的點 $x$ 位於某條邊 $[v_i, v_{i+1}]$ 上，即 $x = \lambda v_i + (1 - \lambda) v_{i+1}$。選取 $j$ 使 $a_j \le i < a_{j+1}$；因指標為整數，$i + 1 \le a_{j+1}$，由[折線容許誤差](../guides/fitting.md#prop-rdp)，$v_i$ 與 $v_{i+1}$ 都在 $[v_{a_j}, v_{a_{j+1}}]$ 的 $\epsilon$ 範圍內。由剛證的凸性，$x$ 亦然。

    2. 通過步驟 1 的點就是某個 $v_i$，由[折線容許誤差](../guides/fitting.md#prop-rdp)，它離某條弦不超過 $\epsilon$。被刪除的輸入點 $p$ 與其前一個保留的頂點（記為 $v$）相距不超過 $\delta$；設弦 $[a, b]$ 與 $v$ 相距不超過 $\epsilon$，則

    $$
    \text{dist}(p, [a, b]) \le \left\lVert p - v \right\rVert_2 + \text{dist}(v, [a, b]) \le \delta + \epsilon.
    $$

    封閉折線結尾重複的起點在同樣條件下被刪除，取 $v = v_0$ 即可。

??? note "證明"

    [雙線性插值的中心值](../guides/implicit.md#prop-center)

    把 $[0, 1]^2$ 的四個角代入 $u$，每個角只有一項不為零且係數為 $1$，所以 $u$ 在角點取角點值。在 $s = t = 1 / 2$，四個權重乘積都等於 $1/2 \cdot 1/2 = 1/4$，因此 $u(1/2, 1/2) = 1/4 (f_{00} + f_{10} + f_{11} + f_{01})$。

??? note "證明"

    [等值集的切線](../guides/implicit.md#thm-gradient)

    因為 $\nabla F(p) \ne 0$，$F_y (p) \ne 0$ 或 $F_x (p) \ne 0$。

    _情形 $F_y (p) \ne 0$。_套用[隱函數定理](../guides/implicit.md#thm-ift)：存在 $I$、$J$ 與 $C^1$ 函數 $\phi : I \to J$，$\phi(p_x) = p_y$，且 $L_c \cap (I \times J) = \lbrace (x, \phi(x)) : x \in I\rbrace$。令 $N = I \times J$、$\gamma(x) = (x, \phi(x))$。對 $F(x, \phi(x)) = c$ 用連鎖律微分，在 $\gamma(x)$ 處得 $F_x + F_y \phi' = 0$。由 $F_y$ 的連續性，可縮小 $I$ 與 $J$ 使 $F_y \ne 0$ 在 $N$ 上成立；於是

    $$
    \gamma'(x) = (1, \phi'(x)) = (1, -F_x / F_y) = 1 / F_y (F_y, -F_x),
    $$

    它非零，且在 $\gamma(x)$ 處平行於 $(F_y, -F_x)$。

    _情形 $F_x (p) \ne 0$。_交換 $x$ 與 $y$ 的角色：存在 $C^1$ 函數 $\psi$ 使 $L_c \cap N = \lbrace (\psi(y), y)\rbrace$，曲線 $\gamma(y) = (\psi(y), y)$，且 $\psi' = -F_y / F_x$，故

    $$
    \gamma'(y) = (-F_y / F_x, 1) = -1 / F_x (F_y, -F_x),
    $$

    同樣非零且平行於 $(F_y, -F_x)$。

    最後 $\nabla F \cdot (F_y, -F_x) = F_x F_y - F_y F_x = 0$。

## 匯出

??? note "證明"

    [四捨五入誤差](../guides/export.md#prop-rounding)

    兩條曲線的差為

    $$
    \widetilde{B}(t) - B(t) = \sum_{i=0}^n b_{i,n}(t) (\widetilde{P}_i - P_i).
    $$

    由[單位分割](../guides/curves.md#prop-unity)，權重 $b_{i,n}(t)$ 非負且和為 1，因此對每個座標，

    $$
    |\widetilde{B}_k (t) - B_k (t)| \le \sum_{i=0}^n b_{i,n}(t) |\widetilde{P}_{i,k} - P_{i,k}| \le \epsilon.
    $$

    由於對 $v \in \mathbb{R}^d$ 有 $\left\lVert v \right\rVert_2 \le \sqrt{d} \left\lVert v \right\rVert_\infty$（見 [Golub (2013)](references.md#golub2013) 第 2.2 節），得 $\left\lVert \widetilde{B}(t) - B(t) \right\rVert_2 \le \sqrt{d} \epsilon$。

    匯出器以 Python 的定點格式寫出每個座標的 $p$ 位小數，得到最接近該座標的 $10^{-p}$ 的整數倍，與原座標相差至多 $1/2 \cdot 10^{-p}$。匯出器也把絕對值小於 $1/2 \cdot 10^{-p}$ 的座標寫成 $0$，改變量即該絕對值，同樣至多為 $1/2 \cdot 10^{-p}$。
