---
seo_title: "自定义与高级效用模型"
description: "使用 econ-viz 创建自定义效用函数、多商品 Cobb-Douglas 模型，以及含劣等品或吉芬商品的 Haagsma 效用函数。"
---

# 高级模型

高级模型能以自定义函数、两种以上的商品，或劣等品与吉芬商品，扩展内置的效用模型。

## 可扩展模型

预先定义的两商品模型不足以描述偏好时，可以使用这组模型。

=== "自定义效用函数"

    `CustomUtility` 能把任何向量化的 Python 可调用函数包装成 econ-viz 模型。

    $$
    U(x,y)=\ln x+\ln y
    $$

    上式只是其中一个示例。函数必须接受两个 NumPy 数组，并返回形状相同的数组。

    **参数**

    | 参数 | 含义 |
    |------|------|
    | `func` | 以 $x$ 与 $y$ 为变量的向量化效用函数 |
    | `name` | 自定义模型的显示名称 |

    **代码**

    ```python
    import numpy as np
    from econ_viz import Canvas, levels, solve
    from econ_viz.models import CustomUtility

    model = CustomUtility(
        func=lambda x, y: np.log(x) + np.log(y),
        name="log+log",
    )
    eq = solve(model, px=2.0, py=3.0, income=30.0)

    (
        Canvas(x_max=20, y_max=15, title="Custom Utility")
        .add_utility(model, levels=levels.around(eq.utility, n=5))
        .add_budget(2.0, 3.0, 30.0)
        .add_equilibrium(eq)
        .save("custom.png")
    )
    ```

    ![自定义效用函数无差异曲线图](../../assets/advanced/advanced_custom.png)

=== "多商品 Cobb-Douglas"

    `MultiGoodCD` 描述 $N$ 种商品的 Cobb-Douglas 偏好。

    $$
    U(x_1,\ldots,x_N)=\prod_{i=1}^{N}x_i^{\alpha_i}
    $$

    `freeze()` 会固定 $x$ 与 $y$ 以外的商品，再返回能画在二维画布上的
    `CustomUtility`。

    **参数**

    | 参数 | 含义 |
    |------|------|
    | `shares` | 商品名称与指数 $\alpha_i$ 的对应 |
    | `freeze(...)` | $x$、$y$ 以外商品的固定数量 |

    **代码**

    ```python
    from econ_viz import Canvas, levels, solve
    from econ_viz.models import MultiGoodCD

    model = MultiGoodCD({"x": 0.3, "y": 0.3, "z": 0.4})
    two_good_model = model.freeze(z=10.0)
    eq = solve(two_good_model, px=2.0, py=3.0, income=30.0)

    (
        Canvas(x_max=20, y_max=15, title="Multi-Good Cobb-Douglas")
        .add_utility(
            two_good_model,
            levels=levels.around(eq.utility, n=5),
        )
        .add_budget(2.0, 3.0, 30.0, fill=True)
        .add_equilibrium(eq)
        .save("multigood.png")
    )
    ```

    ![多商品 Cobb-Douglas 投影图](../../assets/advanced/advanced_multigd.png)

## 劣等品与吉芬商品

`Haagsma` 实现 \citet{haagsma2012} 提出的效用函数。在这个函数中，商品 $x$ **一定是劣等品**，收入足够高时更会成为**吉芬商品**。

$$
U(x,y)=\alpha_x\ln(x-\gamma_x)-\alpha_y\ln(\gamma_y-y),
\qquad 0<\alpha_x<\alpha_y,\quad x>\gamma_x,\quad 0\le y<\gamma_y
$$

在内部解时，$x$ 的马歇尔需求有闭式解：

$$
x^*=\frac{\alpha_x(\gamma_y p_y-I)}{(\alpha_y-\alpha_x)\,p_x}+\frac{\alpha_y\gamma_x}{\alpha_y-\alpha_x}
$$

因此不论价格与收入为何，$\partial x^*/\partial I<0$。$\partial x^*/\partial p_x$ 的正负则取决于收入：

| 收入 | 商品 $x$ |
|------|----------|
| $I<\gamma_y p_y$ | 劣等品；$p_x$ 上升时需求仍会减少 |
| $I=\gamma_y p_y$ | 劣等品；替代效应与收入效应刚好抵消 |
| $\gamma_y p_y<I<\gamma_y p_y+\gamma_x p_x$ | 吉芬商品；需求随 $p_x$ 上升而增加 |

当 $I\ge\gamma_y p_y+\gamma_x p_x$ 时，消费者能让 $y$ 无限逼近 $\gamma_y$，效用没有上界，因此不存在最优解，`solve()` 会抛出错误。

**参数**

| 参数 | 含义 |
|------|------|
| `alpha_x` | 商品 $x$ 的权重 $\alpha_x$，须小于 `alpha_y` |
| `alpha_y` | 商品 $y$ 的权重 $\alpha_y$ |
| `gamma_x` | 商品 $x$ 的下限 $\gamma_x$ |
| `gamma_y` | 商品 $y$ 的上限 $\gamma_y$ |

`demand(px, py, income)` 返回闭式解的消费组合，`is_giffen(px, py, income)` 判断 $x$ 是否为吉芬商品。

**示例**

```python
from econ_viz import Canvas, Effect
from econ_viz.models import Haagsma
from econ_viz.optimizer import decompose_price_effect

model = Haagsma(alpha_x=1.0, alpha_y=2.0, gamma_x=2.0, gamma_y=27.0)
model.is_giffen(px=2.0, py=1.0, income=28.0)  # True

result = decompose_price_effect(model, px=(2.0, 1.0), py=1.0, income=28.0, method="hicks")

(
    Canvas(x_max=16, y_max=32, title="Haagsma: Giffen good")
    .add_decomposition(
        result,
        show_x_projections=True,
        substitution=Effect(label="SE"),
        income=Effect(label="IE"),
    )
    .save("haagsma.png")
)
```

$p_x$ 从 2 降到 1 时，替代效应使 $x$ 增加 4.5，收入效应却使 $x$ 减少 5，所以 $x$ 的需求反而下降。

![Haagsma 效用函数下吉芬商品的 Hicks 分解](../../assets/advanced/advanced_haagsma.png)
