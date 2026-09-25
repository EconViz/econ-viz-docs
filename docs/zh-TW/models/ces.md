---
seo_title: "用 Python 繪製 CES 效用函數"
description: "畫出固定替代彈性（CES）效用的無異曲線，並觀察它如何涵蓋 Cobb-Douglas、Leontief 與完全替代等特例。"
---

# CES（固定替代彈性）

$$U(x, y) = \left(\alpha x^\rho + \beta y^\rho\right)^{1/\rho}$$

替代彈性為 $\sigma = 1/(1-\rho)$。CES 涵蓋以下幾個特例：

| $\rho$ | 極限 | 等同於 |
|--------|-------|---------------|
| $\rho \to 0$ | $x^\alpha y^\beta$ | Cobb-Douglas |
| $\rho \to -\infty$ | $\min(\alpha x, \beta y)$ | Leontief |
| $\rho = 1$ | $\alpha x + \beta y$ | 完全替代 |

![CES 無異曲線圖、預算線與均衡點](../../assets/models/ces.png)

## 參數

| 參數 | 型別 | 預設值 | 說明 |
|-----------|------|---------|-------------|
| `alpha` | float | 0.5 | 商品 $x$ 的比重參數 |
| `beta` | float | 0.5 | 商品 $y$ 的比重參數 |
| `rho` | float | 0.5 | 替代參數（$\rho \ne 1$） |

## 最適化

消費者求解

$$\max_{x,\,y}\; \left(\alpha x^\rho + \beta y^\rho\right)^{1/\rho} \quad \text{s.t.}\quad p_x x + p_y y = I$$

Lagrangian 函數為

$$\mathcal{L}(x, y, \lambda) = \left(\alpha x^\rho + \beta y^\rho\right)^{1/\rho} - \lambda\,(p_x x + p_y y - I)$$

一階條件：

$$\begin{aligned}
\frac{\partial \mathcal{L}}{\partial x} &= \alpha x^{\rho-1}\left(\alpha x^\rho + \beta y^\rho\right)^{1/\rho - 1} - \lambda p_x = 0 \\[6pt]
\frac{\partial \mathcal{L}}{\partial y} &= \beta y^{\rho-1}\left(\alpha x^\rho + \beta y^\rho\right)^{1/\rho - 1} - \lambda p_y = 0 \\[6pt]
\frac{\partial \mathcal{L}}{\partial \lambda} &= p_x x + p_y y - I = 0
\end{aligned}$$

把前兩個條件相除，消去共同因子，得到切點條件：

$$\frac{\alpha}{\beta}\left(\frac{y}{x}\right)^{1-\rho} = \frac{p_x}{p_y}$$

解出最適比例，並代入 $\sigma = 1/(1-\rho)$：

$$\frac{y^*}{x^*} = \left(\frac{\alpha\,p_y}{\beta\,p_x}\right)^{\!\sigma}$$

## 使用方式

=== "Python"

    ```python
    from econ_viz import Canvas, levels, solve
    from econ_viz.models import CES

    model = CES(rho=-0.5, alpha=0.5, beta=0.5)   # σ = 1/(1+0.5) ≈ 0.667
    eq    = solve(model, px=2.0, py=3.0, income=30.0)
    lvls  = levels.around(eq.utility, n=5)

    Canvas(x_max=20, y_max=15, title=r"CES $\rho = -0.5$") \
        .add_utility(model, levels=lvls) \
        .add_budget(2.0, 3.0, 30.0) \
        .add_equilibrium(eq) \
        .save("ces.png")
    ```

=== "CLI"

    ```bash
    econ-viz plot --model ces --rho -0.5 --alpha 0.5 \
                  --px 2 --py 3 --income 30 --output ces.png
    ```
