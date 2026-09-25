---
seo_title: "快速开始：用 Python 绘制无差异曲线"
description: "用 econ-viz 在十行代码内，以 Python 画出第一张无差异曲线图、预算线与消费者均衡。"
---

# 快速开始

## 最简范例

```python
from econ_viz import Canvas, levels, solve
from econ_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.5, beta=0.5)
eq    = solve(model, px=2.0, py=3.0, income=30.0)
lvls  = levels.around(eq.utility, n=5)

cvs = Canvas(x_max=20, y_max=15, x_label="x", y_label="y",
             title=r"Cobb-Douglas $x^{0.5} y^{0.5}$")
cvs.add_utility(model, levels=lvls)
cvs.add_budget(2.0, 3.0, 30.0, fill=True)
cvs.add_equilibrium(eq, show_ray=True)
cvs.save("cobb_douglas.png")
```

![快速开始的均衡图](../assets/models/cobb_douglas.png)

## 逐步说明

### 选择模型

从 `econ_viz.models` 挑一个效用函数。完整清单请见[模型目录](models/index.md)。

```python
from econ_viz.models import CobbDouglas
model = CobbDouglas(alpha=0.5, beta=0.5)
```

### 求解均衡

`solve()` 会返回一个 `Equilibrium` named tuple，字段有 `x`、`y`、`utility` 与 `bundle_type`。

```python
from econ_viz import solve
eq = solve(model, px=2.0, py=3.0, income=30.0)
print(eq.x, eq.y, eq.utility)   # e.g. 7.5  5.0  5.303
```

### 选择无差异曲线的效用水准

```python
from econ_viz import levels
lvls = levels.around(eq.utility, n=5)   # 5 curves centred on the optimum
```

### 创建画布

```python
from econ_viz import Canvas
cvs = Canvas(x_max=20, y_max=15)
```

### 加入图层

`Canvas` 的方法都会返回 `self`，所以可以串接调用：

```python
cvs.add_utility(model, levels=lvls)
cvs.add_budget(2.0, 3.0, 30.0, fill=True)
cvs.add_equilibrium(eq, show_ray=True)
```

### 导出

=== "位图 / 矢量"

    ```python
    cvs.save("figure.png")    # PNG
    cvs.save("figure.pdf")    # PDF
    cvs.save("figure.svg")    # SVG
    ```

=== "交互"

    ```python
    cvs.show()   # opens a live matplotlib window
    ```

## 使用 LaTeX 解析器

```python
from econ_viz import parse_latex, Canvas, levels, solve

model = parse_latex(r"x^{0.4} y^{0.6}")
eq    = solve(model, px=2.0, py=3.0, income=30.0)
lvls  = levels.around(eq.utility, n=5)

Canvas(x_max=20, y_max=15) \
    .add_utility(model, levels=lvls) \
    .add_budget(2.0, 3.0, 30.0) \
    .add_equilibrium(eq) \
    .save("figure.png")
```

## 多面板图

`Figure` 可以把多个 `Canvas` 面板组合成一张图。

```python
from econ_viz import Figure, Layout, levels, solve
from econ_viz.models import CobbDouglas

fig = Figure(
    Layout.SIDE_BY_SIDE,
    x_max=20,
    y_max=15,
    x_label="x",
    y_label="y",
    title="Before / After Price Change",
    shared_y=True,
)

cases = [
    (CobbDouglas(alpha=0.5, beta=0.5), 2.0, 3.0, 30.0, r"Before: $p_x=2$"),
    (CobbDouglas(alpha=0.3, beta=0.7), 4.0, 3.0, 30.0, r"After: $p_x=4$"),
]

for idx, (model, px, py, income, title) in enumerate(cases):
    eq = solve(model, px=px, py=py, income=income)
    panel = fig[idx]
    panel.ax.set_title(title)
    panel.add_utility(model, levels=levels.around(eq.utility, n=5))
    panel.add_budget(px, py, income, fill=True)
    panel.add_equilibrium(eq, show_ray=True)

fig.save("comparison.png")
```

## 需求图

用 `PricePath` 搭配 `DemandDiagram`，把商品空间中的最优点与**马歇尔需求**链接起来。

```python
from econ_viz import DemandDiagram, LinearBudget, PricePath
from econ_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.5, beta=0.5)
budget = LinearBudget(px=2.0, py=2.0, income=40.0)
path = PricePath(model, budget=budget, price="px", price_range=(0.8, 6.0), n=40)

fig = DemandDiagram(path, title="Demand: Cobb-Douglas")
fig.add_marshallian_panel(price_markers=[1.5, 4.0])
fig.save("demand.png")
```

![快速开始的需求图](../assets/consumer/demand_cobb_douglas.png)
