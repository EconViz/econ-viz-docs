---
seo_title: "用 Python 繪製 Cobb-Douglas 效用函數"
description: "用 econ-viz 以 Python 畫出 Cobb-Douglas 效用的無異曲線，求解最適消費組合並推導需求函數。"
---

# Cobb-Douglas

$$U(x, y) = x^\alpha \cdot y^\beta$$

教科書中最常見的效用函數。無異曲線**平滑**、**嚴格凸向原點**，並以兩軸為漸近線。

![Cobb-Douglas 無異曲線圖、預算線與均衡點](../../assets/models/cobb_douglas.png)

## 參數

| 參數 | 型別 | 預設值 | 說明 |
|-----------|------|---------|-------------|
| `alpha` | float | 0.5 | 商品 $x$ 的指數 |
| `beta` | float | 0.5 | 商品 $y$ 的指數 |

## 最適化

消費者求解

$$\max_{x,\,y}\; x^\alpha y^\beta \quad \text{s.t.}\quad p_x x + p_y y = I$$

Lagrangian 函數為

$$\mathcal{L}(x, y, \lambda) = x^\alpha y^\beta - \lambda\,(p_x x + p_y y - I)$$

一階條件：

$$\begin{aligned}
\frac{\partial \mathcal{L}}{\partial x} &= \alpha x^{\alpha-1} y^\beta - \lambda p_x = 0 \\[6pt]
\frac{\partial \mathcal{L}}{\partial y} &= \beta x^\alpha y^{\beta-1} - \lambda p_y = 0 \\[6pt]
\frac{\partial \mathcal{L}}{\partial \lambda} &= p_x x + p_y y - I = 0
\end{aligned}$$

把前兩個條件相除，得到切點條件 $\mathrm{MRS} = p_x/p_y$：

$$\frac{\alpha y}{\beta x} = \frac{p_x}{p_y}$$

代回預算限制式，得到 Marshall 需求：

$$x^* = \frac{\alpha}{\alpha + \beta}\cdot\frac{I}{p_x}, \qquad y^* = \frac{\beta}{\alpha + \beta}\cdot\frac{I}{p_y}$$

## 使用方式

=== "Python"

    ```python
    from econ_viz import Canvas, levels, solve
    from econ_viz.models import CobbDouglas

    model = CobbDouglas(alpha=0.5, beta=0.5)
    eq    = solve(model, px=2.0, py=3.0, income=30.0)
    lvls  = levels.around(eq.utility, n=5)

    Canvas(x_max=20, y_max=15, title=r"Cobb-Douglas $x^{0.5} y^{0.5}$") \
        .add_utility(model, levels=lvls) \
        .add_budget(2.0, 3.0, 30.0, fill=True) \
        .add_equilibrium(eq, show_ray=True) \
        .save("cobb_douglas.png")
    ```

=== "CLI"

    ```bash
    econ-viz plot --model cobb-douglas --alpha 0.5 --beta 0.5 \
                  --px 2 --py 3 --income 30 --output cobb_douglas.png
    ```
