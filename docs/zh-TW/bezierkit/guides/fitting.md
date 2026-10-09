---
seo_title: "擬合"
---

# 擬合

<span id="sec-fitting"></span>

擬合把平滑函數或一串取樣點轉為 `PiecewiseBezier`，並逐段量測、回報誤差，單位與曲線座標相同。相關函式位於 `bezierkit.fitting`。

## 自適應 Hermite 擬合

參數曲線 $C : [t_0, t_1] \to \mathbb{R}^d$ 在區間 $[a, b]$ 上的擬合，是逐一座標取[三次 Hermite 插值多項式](construction.md#def-hermite)的三次 Hermite 插值多項式（詳見[Hermite 插值](construction.md#prop-hermite)）。套件在 $q$ 個等距的量測參數 $\tau_j = a + j (b - a) / (q - 1)$（$j = 0, \ldots, q - 1$，$q$ 為 `error_samples`）上量測誤差：

$$
e = \max_{0 \le j \le q-1} \left\lVert C(\tau_j) - H(\tau_j) \right\rVert_2.
$$

此實測誤差是本套件的約定，絕不大於線段真實的最大誤差。

<!-- api: agora.bezierkit.guides_fitting_1 -->

在 $[t_0, t_1]$ 上擬合參數曲線 $C(t)$；`function` 回傳 `Point`，`derivative` 回傳 `Vector`。演算法為遞迴二分：

+ 以目前區間兩端的 $C$ 與 $C'$ 建立 Hermite 線段（詳見[Hermite 插值](construction.md#prop-hermite)）。
+ 量測誤差 $e$。
+ $e$ 不超過 `tolerance` 時保留此線段，並將 $e$ 記為其 `fit_error`；否則將區間對半，兩半各自擬合。

因此每個保留的線段在量測參數上都符合容許誤差。若區間到了 `max_depth` 仍不合格，或保留它會超過 `max_segments`，就拋出 `ToleranceNotMet`，而不回傳品質較差的路徑。

<!-- api: agora.bezierkit.guides_fitting_2 -->

擬合圖形 $y = f(x)$，$x \in [x_0, x_1]$：即以 $C(x) = (x, f(x))$、$C'(x) = (1, f'(x))$ 呼叫 `fit_parametric`，選項相同，誤差為 $(x, y)$ 平面上的歐氏距離。

```python
from bezierkit.fitting import fit_graph

path = fit_graph(
    lambda x: 4 / x**2,
    lambda x: -8 / x**3,
    x0=0.8,
    x1=3,
    tolerance=1e-3,
)
# 10
print(len(path.segments))
# 0.000676
print(max(s.fit_error for s in path))
```

<span id="fig-adaptive"></span>

![$4 / x^2$ 的自適應擬合。](../../../assets/bezierkit/agora/fitting/adaptive.svg){ .ev-figure-sm }

曲線彎曲劇烈處線段較短，接近直線處線段較長（參見[$4 / x^2$ 的自適應擬合。](fitting.md#fig-adaptive)，相鄰線段以不同顏色區分）。Hermite 誤差界限可預估二分需要的深度：

<span id="cor-depth"></span>

!!! abstract "推論 · 自適應擬合的深度"

    設 $C$ 的每個座標在 $[t_0, t_1]$ 上四階連續可微且 $|C_k^{(4)}| \le M$，令 $L = |t_1 - t_0|$，$d$ 為維度，$\epsilon > 0$ 為容許誤差。令

    $$
    k^* = \max(0, \left\lceil 1/4 \log_2 (\sqrt\lbrace d\rbrace M L^4 / (384 \epsilon)) \right\rceil),
    $$

    $M = 0$ 時 $k^* = 0$。深度 $k \ge k^*$ 的每個區間都能通過誤差檢查。因此若 `max_depth` $\ge k^*$ 且 `max_segments` $\ge 2^{k^*}$，`fit_parametric` 不會拋出 `ToleranceNotMet`，也不會產生深度大於 $k^*$ 的區間。

實測誤差是線段真實最大誤差的下界，因為只在量測參數上檢查。若曲線可能在量測點之間起伏，請增加 `error_samples`。

## 折線簡化

<span id="def-segment-distance"></span>

!!! abstract "定義 · 點到線段的距離"

    對 $x, a, b \in \mathbb{R}^d$，$x$ 到線段 $[a, b]$ 的距離為

    $$
    \text{dist}(x, [a, b]) = \min_{\lambda \in [0, 1]} \left\lVert x - a - \lambda (b - a) \right\rVert_2.
    $$

以遞迴分割簡化折線，就是 Ramer–Douglas–Peucker 演算法 [Ramer (1972)](../project/references.md#ramer1972)[Douglas (1973)](../project/references.md#douglas1973)。`fit_polyline` 全程使用[點到線段的距離](fitting.md#def-segment-distance)的距離。

<!-- api: agora.bezierkit.guides_fitting_3 -->

把取樣點簡化為由直線弦組成的路徑，每條弦以精確的三次曲線表示（詳見[直線與二次曲線的三次表示](paths.md#prop-elevation)）。步驟如下：

+ 刪除與前一點距離在 `duplicate_tolerance` 以內的點。封閉折線另外刪除結尾重複的起點，並旋轉為從字典序最小的點開始，使結果與取樣起點無關。
+ 保留兩端點；啟用 `preserve_corners` 時，另保留方向轉折至少 `corner_angle` 弧度的頂點。
+ 在相鄰的保留頂點之間套用遞迴步驟：若離弦最遠的頂點距離不超過 `tolerance`，以弦取代整段；否則保留該頂點，兩側遞迴處理。

每條弦的 `fit_error` 是被它取代的頂點到弦的最大距離（參見[以容許誤差 $0.08$ 簡化 41 個雜訊樣本。](fitting.md#fig-polyline)）。

遞迴最多有與頂點數相同的層數，每層對每個頂點至多掃描一次，因此最壞情況下與頂點數成平方關係。[Hershberger (1994)](../project/references.md#hershberger1994) 給出此演算法的 $O(n \log n)$ 實作。

<span id="prop-rdp"></span>

!!! abstract "命題 · 折線容許誤差"

    設 $v_0, \ldots, v_N$ 為通過步驟 1 的頂點（封閉折線有 $v_N = v_0$），$0 = a_0 < \ldots < a_m = N$ 為輸出保留的頂點指標，$\epsilon$ 為 `tolerance`。對每個 $j$ 與每個滿足 $a_j \le i \le a_{j+1}$ 的 $i$，

    $$
    \text{dist}(v_i, [v_{a_j}, v_{a_{j+1}}]) \le \epsilon.
    $$

    特別地，每個輸出線段的 `fit_error` 都不超過 $\epsilon$。

<span id="cor-rdp-path"></span>

!!! abstract "推論 · 與折線的偏差"

    沿用[折線容許誤差](fitting.md#prop-rdp)的記號：
    + 折線 $v_0 v_1 \ldots v_N$ 上的每個點，都與輸出的某條弦 $[v_{a_j}, v_{a_{j+1}}]$ 相距不超過 $\epsilon$。
    + 每個輸入點與某條弦相距不超過 $\epsilon + \delta$，其中 $\delta$ 為 `duplicate_tolerance`；通過步驟 1 的點相距不超過 $\epsilon$。

<span id="fig-polyline"></span>

![以容許誤差 $0.08$ 簡化 41 個雜訊樣本。](../../../assets/bezierkit/agora/fitting/polyline.svg){ .ev-figure-sm }

<!-- api: agora.bezierkit.guides_fitting_4 -->

各點到路徑中最近之弦 $P_0 P_3$ 的最大距離：可用來檢查[折線容許誤差](fitting.md#prop-rdp)與[與折線的偏差](fitting.md#cor-rdp-path)，也涵蓋步驟 1 刪除的點。

如同所有只看得到樣本的方法，`fit_polyline` 限制的是與樣本的偏差，而非與樣本之間未知連續曲線的偏差；需要更貼近時請加密取樣。
