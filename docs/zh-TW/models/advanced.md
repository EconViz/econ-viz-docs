---
seo_title: "自訂與進階效用模型"
description: "使用 econ-viz 建立自訂效用函數、多商品 Cobb-Douglas 模型，以及含劣等財或季芬財的 Haagsma 效用函數。"
---

# 進階模型

進階模型能以自訂函數、兩種以上的商品，或劣等財與季芬財，擴充內建的效用模型。

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

## 劣等財與季芬財

`Haagsma` 實作 \citet{haagsma2012} 提出的效用函數。在這個函數中，商品 $x$ **一定是劣等財**，所得夠高時更會成為**季芬財**。

$$
U(x,y)=\alpha_x\ln(x-\gamma_x)-\alpha_y\ln(\gamma_y-y),
\qquad 0<\alpha_x<\alpha_y,\quad x>\gamma_x,\quad 0\le y<\gamma_y
$$

在內部解時，$x$ 的馬歇爾需求有封閉解：

$$
x^*=\frac{\alpha_x(\gamma_y p_y-I)}{(\alpha_y-\alpha_x)\,p_x}+\frac{\alpha_y\gamma_x}{\alpha_y-\alpha_x}
$$

因此不論價格與所得為何，$\partial x^*/\partial I<0$。$\partial x^*/\partial p_x$ 的正負則取決於所得：

| 所得 | 商品 $x$ |
|------|----------|
| $I<\gamma_y p_y$ | 劣等財；$p_x$ 上升時需求仍會減少 |
| $I=\gamma_y p_y$ | 劣等財；替代效果與所得效果剛好抵銷 |
| $\gamma_y p_y<I<\gamma_y p_y+\gamma_x p_x$ | 季芬財；需求隨 $p_x$ 上升而增加 |

當 $I\ge\gamma_y p_y+\gamma_x p_x$ 時，消費者能讓 $y$ 無限逼近 $\gamma_y$，效用沒有上界，因此不存在最適解，`solve()` 會拋出錯誤。

**參數**

| 參數 | 意義 |
|------|------|
| `alpha_x` | 商品 $x$ 的權重 $\alpha_x$，須小於 `alpha_y` |
| `alpha_y` | 商品 $y$ 的權重 $\alpha_y$ |
| `gamma_x` | 商品 $x$ 的下限 $\gamma_x$ |
| `gamma_y` | 商品 $y$ 的上限 $\gamma_y$ |

`demand(px, py, income)` 回傳封閉解的消費組合，`is_giffen(px, py, income)` 判斷 $x$ 是否為季芬財。

**範例**

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

$p_x$ 從 2 降到 1 時，替代效果使 $x$ 增加 4.5，所得效果卻使 $x$ 減少 5，所以 $x$ 的需求反而下降。

![Haagsma 效用函數下季芬財的 Hicks 分解](../../assets/advanced/advanced_haagsma.png)
