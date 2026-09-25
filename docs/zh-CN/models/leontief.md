---
seo_title: "用 Python 绘制 Leontief 效用（完全互补）"
description: "用 econ-viz 以 Python 画出完全互补的 L 型 Leontief 无差异曲线，并求解位于折点的消费者最优解。"
---

# Leontief（完全互补）

$$U(x, y) = \min(ax, by)$$

两种商品以**固定比例**消费。无差异曲线呈**L 型**，折点落在扩张路径 $y = \tfrac{a}{b}\,x$ 上。

![Leontief 无差异曲线图、预算线与均衡点](../../assets/models/leontief.png)

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|-----------|------|---------|-------------|
| `a` | float | 1.0 | 商品 $x$ 的系数 |
| `b` | float | 1.0 | 商品 $y$ 的系数 |

## 最优化

消费者求解

$$\max_{x,\,y}\; \min(ax, by) \quad \text{s.t.}\quad p_x x + p_y y = I$$

$\mathrm{MRS}$ 在折点没有定义，所以标准的切点条件在内部永远不成立。最优解一定落在 $ax = by$ 的折点上。把 $y = \tfrac{a}{b}\,x$ 代入预算约束：

$$\begin{aligned}
p_x x + p_y \cdot \frac{a}{b}\,x &= I \\[6pt]
x\!\left(p_x + \frac{a\,p_y}{b}\right) &= I
\end{aligned}$$

因此马歇尔需求为

$$x^* = \frac{I}{p_x + \dfrac{a}{b}\,p_y}, \qquad y^* = \frac{a}{b}\,x^*$$

## 使用方式

=== "Python"

    ```python
    from econ_viz import Canvas, levels, solve
    from econ_viz.models import Leontief

    model = Leontief(a=1.0, b=1.0)
    eq    = solve(model, px=2.0, py=3.0, income=30.0)
    lvls  = levels.around(eq.utility, n=5)

    Canvas(x_max=20, y_max=15, title=r"Leontief $\min(x, y)$") \
        .add_utility(model, levels=lvls, show_rays=True, show_kinks=True) \
        .add_budget(2.0, 3.0, 30.0) \
        .add_equilibrium(eq) \
        .save("leontief.png")
    ```

=== "CLI"

    ```bash
    econ-viz plot --model leontief --a 1 --b 1 \
                  --px 2 --py 3 --income 30 --output leontief.png
    ```
