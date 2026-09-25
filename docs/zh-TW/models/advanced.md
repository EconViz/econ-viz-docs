---
seo_title: "自訂與進階效用模型"
description: "使用 econ-viz 建立自訂效用函數與多商品 Cobb-Douglas 模型。"
---

# 進階模型

進階模型能以自訂函數或兩種以上的商品，擴充內建的效用模型。

## 可擴充模型

預先定義的兩商品模型不足以描述偏好時，可以使用這組模型。

=== "自訂效用函數"

    `CustomUtility` 能把任何向量化的 Python 可呼叫函數包裝成 econ-viz 模型。

    $$
    U(x,y)=\ln x+\ln y
    $$

    上式只是其中一個例子。函數必須接受兩個 NumPy 陣列，並回傳形狀相同的陣列。

    **參數**

    | 參數 | 意義 |
    |------|------|
    | `func` | 以 $x$ 與 $y$ 為變數的向量化效用函數 |
    | `name` | 自訂模型的顯示名稱 |

    **程式碼**

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

    ![自訂效用函數無異曲線圖](../../assets/advanced/advanced_custom.png)

=== "多商品 Cobb-Douglas"

    `MultiGoodCD` 描述 $N$ 種商品的 Cobb-Douglas 偏好。

    $$
    U(x_1,\ldots,x_N)=\prod_{i=1}^{N}x_i^{\alpha_i}
    $$

    `freeze()` 會固定 $x$ 與 $y$ 以外的商品，再回傳能畫在二維畫布上的
    `CustomUtility`。

    **參數**

    | 參數 | 意義 |
    |------|------|
    | `shares` | 商品名稱與指數 $\alpha_i$ 的對應 |
    | `freeze(...)` | $x$、$y$ 以外商品的固定數量 |

    **程式碼**

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

    ![多商品 Cobb-Douglas 投影圖](../../assets/advanced/advanced_multigd.png)
