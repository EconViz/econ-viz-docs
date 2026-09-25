---
seo_title: "用 Python 绘制 Stone-Geary 效用函数"
description: "用 econ-viz 以 Python 画出含基本需求量的 Stone-Geary 效用无差异曲线，并求解线性支出体系。"
---

# Stone-Geary

$$U(x, y) = (x - \bar{x})^{\alpha}(y - \bar{y})^{\beta}$$

Cobb-Douglas 的推广形式，引入了**基本需求量** $\bar{x}$ 与 $\bar{y}$，也就是开始产生效用之前，每种商品至少需要的数量。消费者会先满足基本需求，再像 Cobb-Douglas 消费者一样分配剩下的**超额收入**。

效用只在超额区域 $x > \bar{x}$、$y > \bar{y}$ 内有定义。无差异曲线的形状跟 Cobb-Douglas 相同，只是从原点移动了 $(\bar{x}, \bar{y})$。画布上会自动在 $x = \bar{x}$ 与 $y = \bar{y}$ 画出虚线参考线。

![Stone-Geary 无差异曲线图、基本需求线、预算线与均衡点](../../assets/models/stone_geary.png)

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|-----------|------|---------|-------------|
| `alpha` | float | 0.5 | 超额 $x$ 的支出比重（必须为正） |
| `beta` | float | 0.5 | 超额 $y$ 的支出比重（必须为正） |
| `bar_x` | float | 1.0 | 商品 $x$ 的基本需求量（不可为负） |
| `bar_y` | float | 1.0 | 商品 $y$ 的基本需求量（不可为负） |

## 最优化

令 $m = I - p_x \bar{x} - p_y \bar{y}$ 为**超额收入**，也就是满足基本需求后剩下的预算。消费者求解

$$\max_{x,\,y}\; (x - \bar{x})^{\alpha}(y - \bar{y})^{\beta} \quad \text{s.t.}\quad p_x x + p_y y = I$$

令 $\tilde{x} = x - \bar{x}$、$\tilde{y} = y - \bar{y}$，问题化简为

$$\max_{\tilde{x},\,\tilde{y}}\; \tilde{x}^{\alpha}\tilde{y}^{\beta} \quad \text{s.t.}\quad p_x \tilde{x} + p_y \tilde{y} = m$$

这就是以超额数量表示的标准 Cobb-Douglas 问题。因此马歇尔需求为

$$x^* = \bar{x} + \frac{\alpha}{\alpha + \beta}\cdot\frac{m}{p_x}, \qquad y^* = \bar{y} + \frac{\beta}{\alpha + \beta}\cdot\frac{m}{p_y}$$

存在内点解的必要条件是 $m > 0$，也就是

$$I > p_x \bar{x} + p_y \bar{y}$$

如果不成立，`solve()` 会抛出 `InvalidParameterError`。

!!! note "与 Cobb-Douglas 的关系"
    令 $\bar{x} = \bar{y} = 0$，Stone-Geary 就完全等同于 Cobb-Douglas。
    Stone-Geary 的扩张路径不会通过原点，而是从 $(\bar{x}, \bar{y})$ 出发的射线，所以画布上不会画扩张路径射线。

## 使用方式

=== "Python"

    ```python
    from econ_viz import Canvas, levels, solve
    from econ_viz.models import StoneGeary

    model = StoneGeary(alpha=0.5, beta=0.5, bar_x=2.0, bar_y=2.0)
    eq    = solve(model, px=2.0, py=3.0, income=30.0)
    lvls  = levels.around(eq.utility, n=5)

    # Subsistence lines (dashed) are drawn automatically
    Canvas(x_max=20, y_max=15, title=r"Stone-Geary  $\bar{x}=2,\ \bar{y}=2$") \
        .add_utility(model, levels=lvls) \
        .add_budget(2.0, 3.0, 30.0, fill=True) \
        .add_equilibrium(eq) \
        .save("stone_geary.png")
    ```

!!! note "注意"
    命令行工具目前还不支持 `StoneGeary`，请直接使用 Python API。

## LaTeX 解析

Stone-Geary 没有标准的精简 LaTeX 写法，所以 `parse_latex()` 不支持它。请直接通过 Python API 创建模型。
