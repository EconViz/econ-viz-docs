---
seo_title: "解析 LaTeX 效用函数"
description: "用 parse_latex 把 x^{0.4} y^{0.6} 或 \\min(2x, 3y) 这类 LaTeX 算式，直接转成 econ-viz 的效用函数模型。"
---

# LaTeX 解析

`parse_latex` 会把 LaTeX 数学字符串直接转成具体的模型对象。

![从 LaTeX 解析出的 Cobb-Douglas](../assets/latex/latex_cobb_douglas_u.png)

```python
from econ_viz import parse_latex

model = parse_latex(r"x^{0.4} y^{0.6}")       # CobbDouglas(alpha=0.4, beta=0.6)
model = parse_latex(r"\min(2x, 3y)")           # Leontief(a=2.0, b=3.0)
model = parse_latex(r"2x + 3y")               # PerfectSubstitutes(a=2.0, b=3.0)
```

## 支持的形式

| 类型 | 格式 | 范例 |
|--------|---------|---------|
| Cobb-Douglas | `x^{α} y^{β}` 或 `x^α y^β` | `x^{0.3} y^{0.7}` |
| Leontief | `\min(ax, by)` 或 `min(ax, by)` | `\min(2x, y)` |
| 完全替代 | `ax + by` | `3x + 1.5y` |

系数与指数都可以省略，缺省为 1。

## 可接受的开头

以下开头会被自动去掉：

```
U(x,y) = x^{0.5} y^{0.5}
U = x^{0.5} y^{0.5}
x^{0.5} y^{0.5}
```

## 错误处理

无法辨识的格式会抛出 `econ_viz.exceptions.ParseError`：

```python
from econ_viz.exceptions import ParseError

try:
    model = parse_latex(r"x^2 + y^2")
except ParseError as e:
    print(e)
```

## 在命令行工具中使用

```bash
econ-viz plot --latex "x^{0.4} y^{0.6}" --px 2 --py 3 --income 30 -o out.png
```

![从 LaTeX 解析出的 Leontief](../assets/latex/latex_leontief_u.png)

![从 LaTeX 解析出的完全替代](../assets/latex/latex_perfect_subs_u.png)
