---
seo_title: "用 Python 绘制完全替代效用函数"
description: "用 econ-viz 以 Python 画出边际替代率固定的完全替代直线型无差异曲线，并找出角点解。"
---

# 完全替代

$$U(x, y) = ax + by$$

两种商品**完全替代**，边际替代率固定为 $\mathrm{MRS} = a/b$。无差异曲线是斜率为 $-a/b$ 的直线。

![完全替代无差异曲线图、预算线与均衡点](../../assets/models/perfect_substitutes.png)

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|-----------|------|---------|-------------|
| `a` | float | 1.0 | 商品 $x$ 的边际效用 |
| `b` | float | 1.0 | 商品 $y$ 的边际效用 |

## 最优化

消费者求解

$$\max_{x,\,y}\; ax + by \quad \text{s.t.}\quad p_x x + p_y y = I,\quad x, y \ge 0$$

因为目标函数是线性的，最优解一定是**角点解**。把所有收入都花在单一商品上时，间接效用分别为

$$V_x = \frac{a\,I}{p_x}, \qquad V_y = \frac{b\,I}{p_y}$$

因此马歇尔需求为

$$\begin{aligned}
x^* &= \begin{cases} I/p_x & \text{if } a/p_x > b/p_y \\ 0 & \text{if } a/p_x < b/p_y \end{cases} \\[10pt]
y^* &= \begin{cases} 0 & \text{if } a/p_x > b/p_y \\ I/p_y & \text{if } a/p_x < b/p_y \end{cases}
\end{aligned}$$

当 $a/p_x = b/p_y$ 时，预算线与某条无差异曲线重合，**在线每一个组合都是最优解**。

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
