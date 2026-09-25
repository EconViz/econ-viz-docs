---
seo_title: "用 Python 绘制 CES 效用函数"
description: "画出固定替代弹性（CES）效用的无差异曲线，并观察它如何涵盖 Cobb-Douglas、Leontief 与完全替代等特例。"
---

# CES（固定替代弹性）

$$U(x, y) = \left(\alpha x^\rho + \beta y^\rho\right)^{1/\rho}$$

替代弹性为 $\sigma = 1/(1-\rho)$。CES 涵盖以下几个特例：

| $\rho$ | 极限 | 等同于 |
|--------|-------|---------------|
| $\rho \to 0$ | $x^\alpha y^\beta$ | Cobb-Douglas |
| $\rho \to -\infty$ | $\min(\alpha x, \beta y)$ | Leontief |
| $\rho = 1$ | $\alpha x + \beta y$ | 完全替代 |

![CES 无差异曲线图、预算线与均衡点](../../assets/models/ces.png)

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|-----------|------|---------|-------------|
| `alpha` | float | 0.5 | 商品 $x$ 的比重参数 |
| `beta` | float | 0.5 | 商品 $y$ 的比重参数 |
| `rho` | float | 0.5 | 替代参数（$\rho \ne 1$） |

## 最优化

消费者求解

$$\max_{x,\,y}\; \left(\alpha x^\rho + \beta y^\rho\right)^{1/\rho} \quad \text{s.t.}\quad p_x x + p_y y = I$$

拉格朗日函数为

$$\mathcal{L}(x, y, \lambda) = \left(\alpha x^\rho + \beta y^\rho\right)^{1/\rho} - \lambda\,(p_x x + p_y y - I)$$

一阶条件：

$$\begin{aligned}
\frac{\partial \mathcal{L}}{\partial x} &= \alpha x^{\rho-1}\left(\alpha x^\rho + \beta y^\rho\right)^{1/\rho - 1} - \lambda p_x = 0 \\[6pt]
\frac{\partial \mathcal{L}}{\partial y} &= \beta y^{\rho-1}\left(\alpha x^\rho + \beta y^\rho\right)^{1/\rho - 1} - \lambda p_y = 0 \\[6pt]
\frac{\partial \mathcal{L}}{\partial \lambda} &= p_x x + p_y y - I = 0
\end{aligned}$$

把前两个条件相除，消去共同因子，得到切点条件：

$$\frac{\alpha}{\beta}\left(\frac{y}{x}\right)^{1-\rho} = \frac{p_x}{p_y}$$

解出最优比例，并代入 $\sigma = 1/(1-\rho)$：

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
