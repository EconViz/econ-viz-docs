---
seo_title: "用 Python 绘制 Translog 效用函数"
description: "用 econ-viz 以 Python 画出弹性的对数二次 Translog 效用无差异曲线，并求解消费者均衡。"
---

# Translog

`Translog` 提供一种弹性的**对数二次**效用设置，可以近似各种平滑的偏好。

![Translog 范例](../../assets/models/translog.png)

```python
from econ_viz.models import Translog

model = Translog(
    alpha_x=0.5,
    alpha_y=0.5,
    beta_xx=0.1,
    beta_yy=-0.05,
    beta_xy=0.08,
)
```

## 函数形式

```text
ln U(x, y) = alpha_0
           + alpha_x ln x + alpha_y ln y
           + 0.5 beta_xx (ln x)^2
           + 0.5 beta_yy (ln y)^2
           + beta_xy ln x ln y
```

实现返回的是：

```text
U(x, y) = exp(ln U(x, y))
```

令 `beta_xx = beta_yy = beta_xy = 0`，模型就会退化成 Cobb-Douglas 式的对数线性形式。

## 参数

| 参数 | 默认值 | 意义 |
|-----------|---------|---------|
| `alpha_x` | `0.5` | `ln x` 的一次项系数 |
| `alpha_y` | `0.5` | `ln y` 的一次项系数 |
| `beta_xx` | `0.0` | `ln x` 的二次自身效应 |
| `beta_yy` | `0.0` | `ln y` 的二次自身效应 |
| `beta_xy` | `0.0` | 交叉项 `ln x ln y` |
| `alpha_0` | `0.0` | 对数效用的截距 |

`alpha_x` 与 `alpha_y` 必须**严格大于零**。

## 性质

- `utility_type` 为 `UtilityType.SMOOTH`
- 可搭配 `Canvas.add_utility(...)` 使用
- 可通过包的数值最优化流程搭配 `solve(...)` 使用

## 范例

```python
from econ_viz import Canvas, levels, solve
from econ_viz.models import Translog

model = Translog(alpha_x=0.6, alpha_y=0.4, beta_xy=0.12)
eq = solve(model, px=2.0, py=3.0, income=30.0)
lvls = levels.around(eq.utility, n=4)

Canvas(x_max=18, y_max=12, title="Translog utility") \
    .add_utility(model, levels=lvls, label="$U$") \
    .add_budget(2.0, 3.0, 30.0, label="$B$") \
    .add_equilibrium(eq) \
    .show_legend()
```
