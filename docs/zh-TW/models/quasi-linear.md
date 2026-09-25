---
seo_title: "用 Python 繪製準線性效用函數"
description: "用 econ-viz 以 Python 畫出準線性效用的無異曲線，非線性商品沒有所得效果，並求解需求。"
---

# 準線性

$$U(x, y) = f(x) + y \quad \text{or} \quad U(x, y) = x + f(y)$$

其中一種商品以**線性**方式進入效用函數，另一種則透過**嚴格凹、嚴格遞增**的轉換函數 $f$ 進入。每個所得水準下的無異曲線形狀都相同，也就是非線性商品**沒有所得效果**。

![準線性無異曲線圖、預算線與均衡點](../../assets/models/quasi_linear.png)

## 參數

| 參數 | 型別 | 預設值 | 說明 |
|-----------|------|---------|-------------|
| `v_func` | Callable | `numpy.log` | 嚴格遞增、嚴格凹的純量函數 $f(z)$ |
| `linear_in` | `'x'` 或 `'y'` | `'y'` | 哪一種商品以線性方式進入 |

建立模型時，會在 $z \in [0.1, 10]$ 上以數值方法檢查 `v_func`：非單調或凸函數會拋出 `ValueError`。

## 最適化

以 $U = f(x) + y$ 為標準形式，消費者求解

$$\max_{x,\,y}\; f(x) + y \quad \text{s.t.}\quad p_x x + p_y y = I$$

Lagrangian 函數為

$$\mathcal{L}(x, y, \lambda) = f(x) + y - \lambda\,(p_x x + p_y y - I)$$

一階條件：

$$\begin{aligned}
\frac{\partial \mathcal{L}}{\partial x} &= f'(x) - \lambda p_x = 0 \\[6pt]
\frac{\partial \mathcal{L}}{\partial y} &= 1 - \lambda p_y = 0 \\[6pt]
\frac{\partial \mathcal{L}}{\partial \lambda} &= p_x x + p_y y - I = 0
\end{aligned}$$

由第二個條件得到 $\lambda = 1/p_y$，所以最適的 $x^*$ 滿足

$$f'(x^*) = \frac{p_x}{p_y}$$

這使得 $x^*$ **與所得 $I$ 無關**，正是準線性形式的特徵。剩下的所得全部由 $y^*$ 吸收：

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
    命令列工具不支援 `QuasiLinear`，請直接使用 Python API。
