---
seo_title: "用 Python 绘制拟线性效用函数"
description: "用 econ-viz 以 Python 画出拟线性效用的无差异曲线，非线性商品没有收入效应，并求解需求。"
---

# 拟线性

$$U(x, y) = f(x) + y \quad \text{or} \quad U(x, y) = x + f(y)$$

其中一种商品以**线性**方式进入效用函数，另一种则通过**严格凹、严格递增**的转换函数 $f$ 进入。每个收入水平下的无差异曲线形状都相同，也就是非线性商品**没有收入效应**。

![拟线性无差异曲线图、预算线与均衡点](../../assets/models/quasi_linear.png)

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|-----------|------|---------|-------------|
| `v_func` | Callable | `numpy.log` | 严格递增、严格凹的标量函数 $f(z)$ |
| `linear_in` | `'x'` 或 `'y'` | `'y'` | 哪一种商品以线性方式进入 |

创建模型时，会在 $z \in [0.1, 10]$ 上以数值方法检查 `v_func`：非单调或凸函数会抛出 `ValueError`。

## 最优化

以 $U = f(x) + y$ 为标准形式，消费者求解

$$\max_{x,\,y}\; f(x) + y \quad \text{s.t.}\quad p_x x + p_y y = I$$

拉格朗日函数为

$$\mathcal{L}(x, y, \lambda) = f(x) + y - \lambda\,(p_x x + p_y y - I)$$

一阶条件：

$$\begin{aligned}
\frac{\partial \mathcal{L}}{\partial x} &= f'(x) - \lambda p_x = 0 \\[6pt]
\frac{\partial \mathcal{L}}{\partial y} &= 1 - \lambda p_y = 0 \\[6pt]
\frac{\partial \mathcal{L}}{\partial \lambda} &= p_x x + p_y y - I = 0
\end{aligned}$$

由第二个条件得到 $\lambda = 1/p_y$，所以最优的 $x^*$ 满足

$$f'(x^*) = \frac{p_x}{p_y}$$

这使得 $x^*$ **与收入 $I$ 无关**，正是拟线性形式的特征。剩下的收入全部由 $y^*$ 吸收：

$$y^* = \frac{I - p_x\,x^*}{p_y}$$

## 使用方式

=== "Python"

    ```python
    import numpy as np
    from econ_viz import Canvas, levels, solve
    from econ_viz.models import QuasiLinear

    model = QuasiLinear(v_func=np.log, linear_in="y")   # U = log(x) + y
    eq    = solve(model, px=2.0, py=1.0, income=20.0)
    lvls  = levels.around(eq.utility, n=5)

    Canvas(x_max=15, y_max=15, title=r"Quasi-Linear $\ln(x) + y$") \
        .add_utility(model, levels=lvls) \
        .add_budget(2.0, 1.0, 20.0) \
        .add_equilibrium(eq) \
        .save("quasi_linear.png")
    ```

!!! note "注意"
    命令行工具不支持 `QuasiLinear`，请直接使用 Python API。
