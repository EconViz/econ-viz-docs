---
seo_title: "用 Python 繪製 Leontief 效用（完全互補）"
description: "用 econ-viz 以 Python 畫出完全互補的 L 型 Leontief 無異曲線，並求解位於拗折點的消費者最適解。"
---

# Leontief（完全互補）

$$U(x, y) = \min(ax, by)$$

兩種商品以**固定比例**消費。無異曲線呈**L 型**，拗折點落在擴張路徑 $y = \tfrac{a}{b}\,x$ 上。

![Leontief 無異曲線圖、預算線與均衡點](../../assets/models/leontief.png)

## 參數

| 參數 | 型別 | 預設值 | 說明 |
|-----------|------|---------|-------------|
| `a` | float | 1.0 | 商品 $x$ 的係數 |
| `b` | float | 1.0 | 商品 $y$ 的係數 |

## 最適化

消費者求解

$$\max_{x,\,y}\; \min(ax, by) \quad \text{s.t.}\quad p_x x + p_y y = I$$

$\mathrm{MRS}$ 在拗折點沒有定義，所以標準的切點條件在內部永遠不成立。最適解一定落在 $ax = by$ 的拗折點上。把 $y = \tfrac{a}{b}\,x$ 代入預算限制式：

$$\begin{aligned}
p_x x + p_y \cdot \frac{a}{b}\,x &= I \\[6pt]
x\!\left(p_x + \frac{a\,p_y}{b}\right) &= I
\end{aligned}$$

因此 Marshall 需求為

$$x^* = \frac{I}{p_x + \dfrac{a}{b}\,p_y}, \qquad y^* = \frac{a}{b}\,x^*$$

## 使用方式

=== "Python"

    ```python
    from econ_viz import Canvas, levels, solve
    from econ_viz.models import Leontief

    model = Leontief(a=1.0, b=1.0)
    eq    = solve(model, px=2.0, py=3.0, income=30.0)
    lvls  = levels.around(eq.utility, n=5)

    Canvas(x_max=20, y_max=15, title=r"Leontief $\min(x, y)$") \
        .add_utility(model, levels=lvls, show_rays=True, show_kinks=True) \
        .add_budget(2.0, 3.0, 30.0) \
        .add_equilibrium(eq) \
        .save("leontief.png")
    ```

=== "CLI"

    ```bash
    econ-viz plot --model leontief --a 1 --b 1 \
                  --px 2 --py 3 --income 30 --output leontief.png
    ```
