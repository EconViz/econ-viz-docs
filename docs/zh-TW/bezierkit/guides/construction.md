---
seo_title: "建構與 Hermite 插值"
---

# 建構與 Hermite 插值

<span id="sec-construction"></span>

三次曲線由兩個端點及其導數決定。本章的建構方法把這類端點條件轉為控制點，經濟學中只知道幾個數值與斜率的曲線，就是這樣變成 Bézier 曲線。

## 端點建構

每種建構都是帶有 `build()` 方法的不可變 dataclass，位於 `bezierkit.construction`。

<!-- api: agora.bezierkit.guides_construction_1 -->

滿足 $B(0) =$ `start`、$B(1) =$ `end`、$B'(0) =$ `start_derivative`、$B'(1) =$ `end_derivative` 的三次曲線，維度不限。

<span id="prop-endpoint"></span>

!!! abstract "命題 · 端點條件"

    設 $P_0, P_3, D_0, D_1 \in \mathbb{R}^d$。控制點為

    $$
    P_0, \quad P_0 + D_0 / 3, \quad P_3 - D_1 / 3, \quad P_3
    $$

    的三次 Bézier 曲線滿足 $B(0) = P_0$、$B(1) = P_3$、$B'(0) = D_0$、$B'(1) = D_1$，且它是唯一滿足這些條件、次數不超過 3 的多項式曲線。

<!-- api: agora.bezierkit.guides_construction_2 -->

以方向給定端點切線，控制柄長度為 $|P_1 - P_0| =$ `start_handle`、$|P_3 - P_2| =$ `end_handle`。方向會先正規化，因此只有方向有影響；控制柄長度必須為有限的非負值。依[端點條件](construction.md#prop-endpoint)，$B'(0)$ 等於 3 倍 `start_handle` 乘以起點的單位方向。

<!-- api: agora.bezierkit.guides_construction_3 -->

兩端斜率 $\mathrm{d} y / \mathrm{d} x$ 為給定值的平面三次曲線，以方向 $(1, m)$ 的 `TangentDirections` 建構。斜率必須為有限值；垂直切線請改用 `TangentDirections`。

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

## Hermite 插值

三次 Hermite 插值在區間兩端同時吻合函數值與導數。

<span id="def-hermite"></span>

!!! abstract "定義 · 三次 Hermite 插值多項式"

    設 $f$ 在 $[x_0, x_1]$ 上可微，$x_0 \ne x_1$。$f$ 的三次 Hermite 插值多項式是次數不超過 3、滿足

    $$
    H(x_i) = f(x_i), \quad H'(x_i) = f'(x_i), \quad i = 0, 1
    $$

    的多項式 $H$。對曲線則逐一插值每個座標。

這是 [Burden (2011)](../project/references.md#burden2011) 第 3.4 節中 Hermite 多項式取兩個節點的情形，該書的定義 3.8。這樣的多項式存在且唯一：

<span id="prop-hermite-unique"></span>

!!! abstract "命題 · 存在性與唯一性"

    [三次 Hermite 插值多項式](construction.md#def-hermite)的三次 Hermite 插值多項式存在且唯一。令 $h = x_1 - x_0$、$f_i = f(x_i)$、$m_i = f'(x_i)$，則

    $$
    H(x) = \sum_{i=0}^3 b_{i,3}((x - x_0) / h) c_i,
    $$

    其中係數為

    $$
    c_0 = f_0, \quad c_1 = f_0 + h m_0 / 3, \quad c_2 = f_1 - h m_1 / 3, \quad c_3 = f_1.
    $$

任意節點數的同一結論，見 [Stoer (2002)](../project/references.md#stoer2002) 的定理 (2.1.5.2)。在寬度為 $h = t_1 - t_0$ 的參數區間 $[t_0, t_1]$ 上，Bézier 線段在 $s = (t - t_0) / h$ 處求值，導數因此乘上 $h$。

<!-- api: agora.bezierkit.guides_construction_4 -->

控制點為 $P_0$、$P_0 + h D_0 / 3$、$P_3 - h D_1 / 3$、$P_3$ 的三次線段，位於 `bezierkit.interpolation`。$h = 0$ 時拋出 `ValueError`；$h$ 為負表示反向的區間。

<span id="prop-hermite"></span>

!!! abstract "命題 · Hermite 插值"

    對 `parametric_hermite` 回傳的線段，令 $H(t) = B((t - t_0) / h)$。則 $H(t_0) = P_0$、$H(t_1) = P_3$、$H'(t_0) = D_0$、$H'(t_1) = D_1$。

<!-- api: agora.bezierkit.guides_construction_5 -->

由函數值 $y_0 = f(x_0)$、$y_1 = f(x_1)$ 與斜率 $m_0 = f'(x_0)$、$m_1 = f'(x_1)$ 得到圖形 $y = f(x)$ 的插值曲線，即取 $P = (x, f(x))$、$D = (1, f'(x))$、$t = x$ 的參數形式。控制點為

$$
(x_0, y_0), \quad (x_0 + h/3, y_0 + h m_0 / 3), \quad (x_1 - h/3, y_1 - h m_1 / 3), \quad (x_1, y_1),
$$

其中 $h = x_1 - x_0$（參見[$4 / x^2$ 在 $[1, 1.5]$ 的 Hermite 插值。](construction.md#fig-hermite)）。

<span id="prop-graph-hermite"></span>

!!! abstract "命題 · 圖形形式"

    `graph_hermite` 的線段是 $f$ 在 $[x_0, x_1]$ 上的三次 Hermite 插值多項式 $H$ 的圖形：即 $s |\to (x_0 + h s, H(x_0 + h s))$，$s \in [0, 1]$。

```python
from bezierkit.interpolation import graph_hermite

# f(x) = 4 / x^2 on [1, 1.5]
segment = graph_hermite(
    x0=1, x1=1.5, y0=4, y1=16 / 9, m0=-8, m1=-64 / 27
)
```

<span id="fig-hermite"></span>

![$4 / x^2$ 在 $[1, 1.5]$ 的 Hermite 插值。](../../../assets/bezierkit/agora/construction/hermite.svg){ .ev-figure-sm }

## 插值誤差

<span id="thm-hermite-error"></span>

!!! abstract "定理 · Hermite 誤差界限"

    設 $f$ 在 $[x_0, x_1]$ 上四階連續可微，$x_0 < x_1$，$H$ 為其三次 Hermite 插值多項式（詳見[三次 Hermite 插值多項式](construction.md#def-hermite)），令 $h = x_1 - x_0$、$M = \max |f^{(4)}|$。對每個 $x \in [x_0, x_1]$，存在 $\xi \in [x_0, x_1]$ 使

    $$
    f(x) - H(x) = (f^{(4)}(\xi)) / 24 (x - x_0)^2 (x - x_1)^2,
    $$

    因此

    $$
    \max_{x \in [x_0, x_1]} |f(x) - H(x)| \le (M h^4) / 384.
    $$

誤差公式見 [Burden (2011)](../project/references.md#burden2011) 的定理 3.9（其證明留作該書習題 3.4.11）與 [Stoer (2002)](../project/references.md#stoer2002) 的定理 (2.1.5.9)。此界限是銳利的：對 $[0, 1]$ 上的 $f(x) = x^4$，誤差為 $x^2 (x - 1)^2$，於 $x = 1 / 2$ 的最大值 $1 / 16$ 等於 $M = 24$ 時的 $M h^4 / 384$。

區間減半時界限變為 1/16，自適應擬合正是利用這一點（詳見[擬合](fitting.md#sec-fitting)）。以 $f(x) = 4 / x^2$ 在 $[1, 1.5]$ 為例，$f^{(4)}(x) = 480 / x^6$，故 $M = 480$，界限為 $480 \cdot 0.5^4 / 384 \approx 0.078$。

<!-- api: agora.bezierkit.guides_construction_6 -->

[Hermite 誤差界限](construction.md#thm-hermite-error)的界限 $M |t_1 - t_0|^4 / 384$，位於 `bezierkit.fitting`。$M$ 必須為有限的非負值。

此界限適用於純量函數。對曲線 $t |\to (x(t), y(t))$，分別套用到每個座標。在 $\mathbb{R}^d$ 中，歐氏誤差至多為最大座標界限的 $\sqrt{d}$ 倍，因為對 $v \in \mathbb{R}^d$ 有 $\left\lVert v \right\rVert_2 \le \sqrt{d} \left\lVert v \right\rVert_\infty$（見 [Golub (2013)](../project/references.md#golub2013) 第 2.2 節）。
