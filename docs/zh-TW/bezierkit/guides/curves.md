---
seo_title: "Bézier 曲線"
---

# Bézier 曲線

<span id="sec-curves"></span>

## Bernstein 基底

<span id="def-bernstein"></span>

!!! abstract "定義 · Bernstein 多項式"

    $n \ge 0$ 次 Bernstein 多項式為

    $$
    b_{i,n}(t) = \binom{n}{i} t^i (1-t)^{n-i}, \quad i = 0, \ldots, n.
    $$

    其他整數 $i$ 令 $b_{i,n} = 0$。

這組多項式出自 [Bernstein (1912)](../project/references.md#bernstein1912)；[Farouki (2012)](../project/references.md#farouki2012)回顧其歷史與性質，三次的情形如[三次 Bernstein 多項式。](curves.md#fig-basis)。以下證明用到兩個二項式係數恆等式。

<span id="lem-binomial"></span>

!!! abstract "引理 · 二項式恆等式"

    令 $n \ge 1$，$i$、$j$ 為整數，並約定 $k < 0$ 或 $k > m$ 時 $\binom{m}{k} = 0$。則

    $$
    \binom{n-1}{j} + \binom{n-1}{j-1} = \binom{n}{j}
    $$

    且

    $$
    i \binom{n}{i} = n \binom{n-1}{i-1}.
    $$

<span id="fig-basis"></span>

![三次 Bernstein 多項式。](../../../assets/bezierkit/agora/curves/basis.svg){ .ev-figure-sm }

<span id="prop-basis"></span>

!!! abstract "命題 · Bernstein 基底"

    對 $n \ge 0$，多項式 $b_{0,n}, \ldots, b_{n,n}$ 是次數不超過 $n$ 的實係數多項式向量空間的一組基底。

這是 [Floater (2025)](../project/references.md#floater2025) 的定理 1.1；[證明](../project/proofs.md#app-proofs)從頭證明。

<span id="prop-unity"></span>

!!! abstract "命題 · 單位分割"

    對每個 $t \in [0, 1]$，所有 $b_{i,n}(t) \ge 0$，且

    $$
    \sum_{i=0}^n b_{i,n}(t) = 1.
    $$

<span id="def-curve"></span>

!!! abstract "定義 · Bézier 曲線"

    設 $P_0, \ldots, P_n \in \mathbb{R}^d$。以 $P_0, \ldots, P_n$ 為控制點的 $n$ 次 Bézier 曲線為

    $$
    B(t) = \sum_{i=0}^n b_{i,n}(t) P_i, \quad t \in [0, 1],
    $$

    其控制多邊形為折線 $P_0 P_1 \ldots P_n$。

此定義依循 [B{\'e}zier (1966)](../project/references.md#bezier1966)，形式如 [Farin (2002)](../project/references.md#farin2002) 與 [Prautzsch (2002)](../project/references.md#prautzsch2002)。

<span id="prop-endpoints"></span>

!!! abstract "命題 · 端點"

    $b_{i,n}(0)$ 在 $i = 0$ 時為 1，其餘為 0；$b_{i,n}(1)$ 在 $i = n$ 時為 1，其餘為 0。因此 $B(0) = P_0$、$B(1) = P_n$。

<span id="cor-hull"></span>

!!! abstract "推論 · 凸包"

    每個 $B(t)$（$t \in [0, 1]$）都位於控制點 $P_0, \ldots, P_n$ 的凸包內。

<span id="prop-affine"></span>

!!! abstract "命題 · 仿射不變性"

    對每個仿射映射 $A(x) = M x + v$ 與每個 $t \in [0, 1]$，

    $$
    A(B(t)) = \sum_{i=0}^n b_{i,n}(t) A(P_i).
    $$

    變換曲線等同於變換其控制點。

[凸包](curves.md#cor-hull)讓曲線不超出控制多邊形所張的區域；[仿射不變性](curves.md#prop-affine)則是匯出器與 Matplotlib 轉接器只需移動控制點，就能平移、縮放或旋轉曲線的原因。

<!-- api: agora.bezierkit.guides_curves_1 -->

某一次數的基底，位於 `bezierkit.bezier.basis`。在 $t$ 呼叫時，以陣列回傳 $i = 0, \ldots, n$ 的 $b_{i,n}(t)$；`matrix()` 對每個參數值回傳一列。

## 曲線

<!-- api: agora.bezierkit.guides_curves_2 -->

不可變的 Bézier 曲線，次數 $n \ge 0$、維度 $d \ge 1$ 均不限，參數範圍為 $[0, 1]$。`points` 可為 `Point` 序列、`PointSet`、$(n + 1) \times d$ 陣列或 `ControlPolygon`；所有控制點必須同一維度。

曲線的運算 `derivative()`、`split()`、`segment()` 與 `reversed()` 詳見[導數、反轉與分割](operations.md#sec-operations)。

## 求值

*de Casteljau 演算法*以反覆的線性插值計算 $B(t)$。

<span id="def-casteljau"></span>

!!! abstract "定義 · de Casteljau 點"

    對參數 $t$，令 $P_i^{(0)} = P_i$，並對 $r = 1, \ldots, n$ 令

    $$
    P_i^{(r)} = (1 - t) P_i^{(r-1)} + t P_{i+1}^{(r-1)}, \quad i = 0, \ldots, n - r.
    $$

每一輪對相鄰點取平均，多邊形少一個點；$n$ 輪後只剩一點（參見[de Casteljau 演算法 (t = 0.4)。](curves.md#fig-casteljau)）。此演算法源自 Paul de Casteljau 約 1959 年在 Citroën 的工作 [M{\"u}ller (2024)](../project/references.md#mueller2024)。

<span id="thm-casteljau"></span>

!!! abstract "定理 · de Casteljau"

    對 $0 \le r \le n$ 與 $0 \le i \le n - r$，

    $$
    P_i^{(r)} = \sum_{j=0}^r b_{j,r}(t) P_{i+j}.
    $$

    特別地，$P_0^{(n)} = B(t)$。

此敘述見 [Floater (2025)](../project/references.md#floater2025) 的定理 1.6 與 1.7。

<span id="fig-casteljau"></span>

![de Casteljau 演算法 (t = 0.4)。](../../../assets/bezierkit/agora/curves/casteljau.svg){ .ev-figure-sm }

每個中間點都是控制點的凸組合，演算法不會產生互相抵消的大數，因此在高次數時數值穩定。每個參數的計算量為 $O(n^2)$。

<!-- api: agora.bezierkit.guides_curves_3 -->

預設的求值策略，位於 `bezierkit.bezier.evaluation`：以 NumPy 一次對整批參數執行上述演算法。

<!-- api: agora.bezierkit.guides_curves_4 -->

以 Bernstein 矩陣乘上控制點。次數低、批次大時較快，但高次數時會加總可能互相抵消的項。依[de Casteljau](curves.md#thm-casteljau)，兩種策略計算的是同一個多項式。

```python
from bezierkit import BezierCurve
from bezierkit.bezier.evaluation import BernsteinEvaluator

fast = BezierCurve(
    curve.control_points, evaluator=BernsteinEvaluator()
)
# Point(coords=(2.0, 1.5)), as with the default
print(fast.at(0.5))
```

儲存庫的 `benchmarks/` 目錄比較兩者在 400、10,000 與 100,000 個參數值下的效能。

## 升階

$n$ 次曲線也是 $n + 1$ 次曲線；新的控制點是舊控制點中相鄰兩點的凸組合。

<span id="lem-raise-identity"></span>

!!! abstract "引理 · 升階恆等式"

    對 $n \ge 0$、$0 \le i \le n$ 與每個 $t$，

    $$
    b_{i,n}(t) = (n + 1 - i) / (n + 1) b_{i,n+1}(t) + (i + 1) / (n + 1) b_{i+1,n+1}(t).
    $$

<span id="prop-raise-degree"></span>

!!! abstract "命題 · 升階"

    設 $B$ 的控制點為 $P_0, \ldots, P_n$。對 $k = 0, \ldots, n + 1$ 令

    $$
    Q_k = k / (n + 1) P_{k-1} + (1 - k / (n + 1)) P_k,
    $$

    其中 $P_{-1}$ 與 $P_{n+1}$ 可任意選取，因為它們的係數為零。則

    $$
    B(t) = \sum_{k=0}^{n+1} b_{k,n+1}(t) Q_k \quad \text{對所有} t.
    $$

    曲線及其參數化都不變。

此公式是標準結果 [Farin (2002)](../project/references.md#farin2002)[Prautzsch (2002)](../project/references.md#prautzsch2002)；[證明](../project/proofs.md#app-proofs)的證明不依賴它們。[直線與二次曲線的三次表示](paths.md#prop-elevation)把它用在直線與二次曲線，也就是本套件需要的情形。
