---
seo_title: "LaTeX 解析"
---

# LaTeX 解析

<span id="sec-latex"></span>

<!-- api: agora.utility_viz.tools_latex_1 -->

將 LaTeX 效用函數解析為模型，回傳值可用於 `solve()`、`Canvas` 或其他接受模型的 API。

```python
from utility_viz import parse_latex

# CobbDouglas(alpha=0.4, beta=0.6)
model = parse_latex(r"x^{0.4} y^{0.6}")
# Leontief(a=2.0, b=3.0)
model = parse_latex(r"\min(2x, 3y)")
# PerfectSubstitutes(a=2.0, b=3.0)
model = parse_latex(r"2x + 3y")
```

## 支援的形式

支援的輸入形式參見[支援的效用函數。](latex.md#tab-latex)。省略的係數或指數預設為 1。

<span id="tab-latex"></span>

| 類型 | 格式 | 範例 |
| --- | --- | --- |
| Cobb-Douglas | `x^{α} y^{β}` 或 `x^α y^β` | `x^{0.3} y^{0.7}` |
| 完全互補 | `\min(ax, by)` 或 `min(ax, by)` | `\min(2x, y)` |
| 完全替代 | `ax + by` | `3x + 1.5y` |
| CES | `(αx^ρ + βy^ρ)^{1/ρ}` | `(0.4x^{-0.5}+0.6y^{-0.5})^{-2}` |

可省略開頭的 `U =` 或 `u(x, y) =`：

```text
U(x,y) = x^{0.5} y^{0.5}
U = x^{0.5} y^{0.5}
x^{0.5} y^{0.5}
```

```python
from utility_viz import (
    Canvas,
    Config,
    levels,
    parse_latex,
    solve,
)

# 本手冊圖形所用的設定
Config.load("manual.toml").use()

# Leontief(a=2.0, b=3.0)
model = parse_latex(r"\min(2x, 3y)")
eq = solve(model, px=2.0, py=3.0, income=30.0)

cvs = Canvas(x_max=20, y_max=15, x_label="$x$", y_label="$y$")
cvs.add_utility(
    model,
    levels=levels.around(eq.utility, n=5),
    show_kinks=True,
)
cvs.add_budget(2.0, 3.0, 30.0)
cvs.add_equilibrium(eq)
cvs.save("leontief.png")
```

![Leontief 範例。](../../../assets/utility-viz/agora/latex/leontief.svg){ .ev-figure-sm }

Leontief 範例。 [下載繪製腳本](../../../assets/utility-viz/agora/latex/leontief.py){ .ev-download download="" }
{ .ev-caption }

```python
from utility_viz import (
    Canvas,
    Config,
    levels,
    parse_latex,
    solve,
)

# 本手冊圖形所用的設定
Config.load("manual.toml").use()

# PerfectSubstitutes(a=2.0, b=3.0)
model = parse_latex(r"2x + 3y")
eq = solve(model, px=2.0, py=3.0, income=30.0)

cvs = Canvas(x_max=20, y_max=15, x_label="$x$", y_label="$y$")
cvs.add_utility(model, levels=levels.around(eq.utility, n=5))
cvs.add_budget(2.0, 3.0, 30.0)
cvs.add_equilibrium(eq)
cvs.save("perfect_substitutes.png")
```

![完全替代輸入範例。](../../../assets/utility-viz/agora/latex/perfect_substitutes.svg){ .ev-figure-sm }

完全替代輸入範例。 [下載繪製腳本](../../../assets/utility-viz/agora/latex/perfect_substitutes.py){ .ev-download download="" }
{ .ev-caption }

## 錯誤處理

無法解析時會拋出 `utility_viz.ParseError`，錯誤訊息包含支援的格式：

```python
from utility_viz import ParseError, parse_latex

try:
    model = parse_latex(r"x^2 + y^2")
except ParseError as e:
    print(e)

# Unrecognised LaTeX utility function: 'x^2 + y^2'
# Supported forms:
#   Cobb-Douglas       : x^{alpha} y^{beta}
#   Leontief           : \min(ax, by)
#   Perfect Substitutes: ax + by
#   CES                : (alpha x^{rho} + beta y^{rho})^{1/rho}
```

## 在命令列工具中使用

`utility-viz plot --latex` 使用相同的解析器，接受相同的輸入格式（詳見[繪圖](../getting-started/cli.md#sec-cli-plot)）：

```bash
utility-viz plot --latex "x^{0.4} y^{0.6}" --px 2 --py 3 --income 30 -o out.png
```
