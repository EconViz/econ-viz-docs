---
seo_title: "用 Python 繪製完全替代效用函數"
description: "用 econ-viz 以 Python 畫出邊際替代率固定的完全替代直線型無異曲線，並找出角解。"
---

# 完全替代

$$U(x, y) = ax + by$$

兩種商品**完全替代**，邊際替代率固定為 $\mathrm{MRS} = a/b$。無異曲線是斜率為 $-a/b$ 的直線。

![完全替代無異曲線圖、預算線與均衡點](../../assets/models/perfect_substitutes.png)

## 參數

| 參數 | 型別 | 預設值 | 說明 |
|-----------|------|---------|-------------|
| `a` | float | 1.0 | 商品 $x$ 的邊際效用 |
| `b` | float | 1.0 | 商品 $y$ 的邊際效用 |

## 最適化

消費者求解

$$\max_{x,\,y}\; ax + by \quad \text{s.t.}\quad p_x x + p_y y = I,\quad x, y \ge 0$$

因為目標函數是線性的，最適解一定是**角解**。把所有所得都花在單一商品上時，間接效用分別為

$$V_x = \frac{a\,I}{p_x}, \qquad V_y = \frac{b\,I}{p_y}$$

因此 Marshall 需求為

$$\begin{aligned}
x^* &= \begin{cases} I/p_x & \text{if } a/p_x > b/p_y \\ 0 & \text{if } a/p_x < b/p_y \end{cases} \\[10pt]
y^* &= \begin{cases} 0 & \text{if } a/p_x > b/p_y \\ I/p_y & \text{if } a/p_x < b/p_y \end{cases}
\end{aligned}$$

當 $a/p_x = b/p_y$ 時，預算線與某條無異曲線重合，**線上每一個組合都是最適解**。

## 使用方式

=== "Python"

    ```python
    from econ_viz import Canvas, levels, solve
    from econ_viz.models import PerfectSubstitutes

    model = PerfectSubstitutes(a=1.0, b=2.0)
    eq    = solve(model, px=2.0, py=3.0, income=30.0)
    lvls  = levels.around(eq.utility, n=5)

    Canvas(x_max=20, y_max=15, title=r"Perfect Substitutes $x + 2y$") \
        .add_utility(model, levels=lvls) \
        .add_budget(2.0, 3.0, 30.0) \
        .add_equilibrium(eq) \
        .save("perfect_substitutes.png")
    ```

=== "CLI"

    ```bash
    econ-viz plot --model perfect-substitutes --a 1 --b 2 \
                  --px 2 --py 3 --income 30 --output ps.png
    ```
