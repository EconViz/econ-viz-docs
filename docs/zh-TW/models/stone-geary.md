---
seo_title: "用 Python 繪製 Stone-Geary 效用函數"
description: "用 econ-viz 以 Python 畫出含基本需求量的 Stone-Geary 效用無異曲線，並求解線性支出體系。"
---

# Stone-Geary

$$U(x, y) = (x - \bar{x})^{\alpha}(y - \bar{y})^{\beta}$$

Cobb-Douglas 的一般化形式，引入了**基本需求量** $\bar{x}$ 與 $\bar{y}$，也就是開始產生效用之前，每種商品至少需要的數量。消費者會先滿足基本需求，再像 Cobb-Douglas 消費者一樣分配剩下的**超額所得**。

效用只在超額區域 $x > \bar{x}$、$y > \bar{y}$ 內有定義。無異曲線的形狀跟 Cobb-Douglas 相同，只是從原點移動了 $(\bar{x}, \bar{y})$。畫布上會自動在 $x = \bar{x}$ 與 $y = \bar{y}$ 畫出虛線參考線。

![Stone-Geary 無異曲線圖、基本需求線、預算線與均衡點](../../assets/models/stone_geary.png)

## 參數

| 參數 | 型別 | 預設值 | 說明 |
|-----------|------|---------|-------------|
| `alpha` | float | 0.5 | 超額 $x$ 的支出比重（必須為正） |
| `beta` | float | 0.5 | 超額 $y$ 的支出比重（必須為正） |
| `bar_x` | float | 1.0 | 商品 $x$ 的基本需求量（不可為負） |
| `bar_y` | float | 1.0 | 商品 $y$ 的基本需求量（不可為負） |

## 最適化

令 $m = I - p_x \bar{x} - p_y \bar{y}$ 為**超額所得**，也就是滿足基本需求後剩下的預算。消費者求解

$$\max_{x,\,y}\; (x - \bar{x})^{\alpha}(y - \bar{y})^{\beta} \quad \text{s.t.}\quad p_x x + p_y y = I$$

令 $\tilde{x} = x - \bar{x}$、$\tilde{y} = y - \bar{y}$，問題化簡為

$$\max_{\tilde{x},\,\tilde{y}}\; \tilde{x}^{\alpha}\tilde{y}^{\beta} \quad \text{s.t.}\quad p_x \tilde{x} + p_y \tilde{y} = m$$

這就是以超額數量表示的標準 Cobb-Douglas 問題。因此 Marshall 需求為

$$x^* = \bar{x} + \frac{\alpha}{\alpha + \beta}\cdot\frac{m}{p_x}, \qquad y^* = \bar{y} + \frac{\beta}{\alpha + \beta}\cdot\frac{m}{p_y}$$

存在內部解的必要條件是 $m > 0$，也就是

$$I > p_x \bar{x} + p_y \bar{y}$$

如果不成立，`solve()` 會拋出 `InvalidParameterError`。

!!! note "與 Cobb-Douglas 的關係"
    令 $\bar{x} = \bar{y} = 0$，Stone-Geary 就完全等同於 Cobb-Douglas。
    Stone-Geary 的擴張路徑不會通過原點，而是從 $(\bar{x}, \bar{y})$ 出發的射線，所以畫布上不會畫擴張路徑射線。

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
    命令列工具目前還不支援 `StoneGeary`，請直接使用 Python API。

## LaTeX 解析

Stone-Geary 沒有標準的精簡 LaTeX 寫法，所以 `parse_latex()` 不支援它。請直接透過 Python API 建立模型。
