---
seo_title: "用 Python 绘制饱和（极乐点）效用"
description: "用 econ-viz 以 Python 画出饱和偏好在极乐点周围的椭圆形无差异曲线，这种偏好违反单调性。"
---

# 饱和（极乐点）

$$U(x, y) = -a(x - x^*)^2 - b(y - y^*)^2$$

效用越接近**极乐点** $(x^*, y^*)$ 越高，往任何方向远离都会下降。无差异曲线是以极乐点为中心的封闭椭圆。这违反了标准的**单调性公理**：消费者有可能拥有**太多**某种商品。

![饱和无差异曲线图（极乐点）](../../assets/models/satiation.png)

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|-----------|------|---------|-------------|
| `bliss_x` | float | 5.0 | 极乐点 $x^*$ 的 $x$ 座标 |
| `bliss_y` | float | 5.0 | 极乐点 $y^*$ 的 $y$ 座标 |
| `a` | float | 1.0 | 沿 $x$ 轴的曲率（必须为正） |
| `b` | float | 1.0 | 沿 $y$ 轴的曲率（必须为正） |

## 最优化

消费者求解

$$\max_{x,\,y}\; -a(x-x^*)^2 - b(y-y^*)^2 \quad \text{s.t.}\quad p_x x + p_y y = I$$

拉格朗日函数为

$$\mathcal{L}(x, y, \lambda) = -a(x-x^*)^2 - b(y-y^*)^2 - \lambda\,(p_x x + p_y y - I)$$

一阶条件：

$$\begin{aligned}
\frac{\partial \mathcal{L}}{\partial x} &= -2a(x - x^*) - \lambda p_x = 0 \\[6pt]
\frac{\partial \mathcal{L}}{\partial y} &= -2b(y - y^*) - \lambda p_y = 0 \\[6pt]
\frac{\partial \mathcal{L}}{\partial \lambda} &= p_x x + p_y y - I = 0
\end{aligned}$$

把前两个条件相除，得到切点条件：

$$\frac{a(x - x^*)}{b(y - y^*)} = \frac{p_x}{p_y}$$

如果极乐点 $(x^*, y^*)$ 位于预算集内部（也就是 $p_x x^* + p_y y^* \le I$），无限制的最大值就出现在极乐点本身，消费者**不会花完所有收入**。

!!! note "注意"
    `Satiation` 不能搭配 `solve()` 使用，因为标准的预算切点最优解可能落在极乐点的椭圆之外。在命令行工具中请加上 `--no-budget --no-equilibrium`，在 Python 中则省略 `add_budget` / `add_equilibrium`。

`add_utility()` 缺省会在极乐点画一个 ★ 标记（`show_bliss=True`）。传入 `show_bliss=False` 可以隐藏它。

## 使用方式

=== "Python"

    ```python
    import numpy as np
    from econ_viz import Canvas, levels
    from econ_viz.models import Satiation

    model = Satiation(bliss_x=6.0, bliss_y=4.0)

    x_pts = np.linspace(0.1, 12, 300)
    y_pts = np.linspace(0.1, 10, 300)
    X, Y  = np.meshgrid(x_pts, y_pts)
    lvls  = levels.percentile(model(X, Y), n=5)

    Canvas(x_max=12, y_max=10, title="Satiation — bliss at $(6, 4)$") \
        .add_utility(model, levels=lvls, show_bliss=True) \
        .save("satiation.png")

    # Pass show_bliss=False to hide the marker
    Canvas(x_max=12, y_max=10) \
        .add_utility(model, levels=lvls, show_bliss=False) \
        .save("satiation_no_marker.png")
    ```

=== "CLI"

    ```bash
    econ-viz plot --model satiation --bliss-x 6 --bliss-y 4 \
                  --x-max 12 --y-max 10 \
                  --no-budget --no-equilibrium \
                  --output satiation.png
    ```
