---
seo_title: "自定义与高级效用模型"
description: "使用 econ-viz 创建自定义效用函数与多商品 Cobb-Douglas 模型。"
---

# 高级模型

高级模型能以自定义函数或两种以上的商品，扩展内置的效用模型。

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
