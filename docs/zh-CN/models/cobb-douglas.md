---
seo_title: "用 Python 绘制 Cobb-Douglas 效用函数"
description: "用 econ-viz 以 Python 画出 Cobb-Douglas 效用的无差异曲线，求解最优消费束并推导需求函数。"
---

# Cobb-Douglas

$$U(x, y) = x^\alpha \cdot y^\beta$$

教科书中最常见的效用函数。无差异曲线**平滑**、**严格凸向原点**，并以两轴为渐近线。

![Cobb-Douglas 无差异曲线图、预算线与均衡点](../../assets/models/cobb_douglas.png)

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|-----------|------|---------|-------------|
| `alpha` | float | 0.5 | 商品 $x$ 的指数 |
| `beta` | float | 0.5 | 商品 $y$ 的指数 |

## 最优化

消费者求解

$$\max_{x,\,y}\; x^\alpha y^\beta \quad \text{s.t.}\quad p_x x + p_y y = I$$

拉格朗日函数为

$$\mathcal{L}(x, y, \lambda) = x^\alpha y^\beta - \lambda\,(p_x x + p_y y - I)$$

一阶条件：

$$\begin{aligned}
\frac{\partial \mathcal{L}}{\partial x} &= \alpha x^{\alpha-1} y^\beta - \lambda p_x = 0 \\[6pt]
\frac{\partial \mathcal{L}}{\partial y} &= \beta x^\alpha y^{\beta-1} - \lambda p_y = 0 \\[6pt]
\frac{\partial \mathcal{L}}{\partial \lambda} &= p_x x + p_y y - I = 0
\end{aligned}$$

把前两个条件相除，得到切点条件 $\mathrm{MRS} = p_x/p_y$：

$$\frac{\alpha y}{\beta x} = \frac{p_x}{p_y}$$

代回预算约束，得到马歇尔需求：

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
