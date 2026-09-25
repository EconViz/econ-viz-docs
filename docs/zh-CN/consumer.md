---
seo_title: "多面板图与需求图"
description: "用 econ-viz 创建多面板教学图、价格消费曲线与收入消费曲线，以及联动的马歇尔需求图。"
---

# 多面板图与需求图

`econ-viz` 在 `Canvas` 之上提供更高级的教学组件：

- `Figure`：多面板布局
- `PricePath` 与 `IncomePath`：让预算与均衡随参数移动
- `DemandDiagram`：联动的商品空间图与马歇尔需求图

## 多面板 `Figure`

一个面板不够用时就用 `Figure`，例如变动前后的比较、效应分解图或课堂演示文稿。

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
    panel.add_utility(model, levels=levels.around(eq.utility, n=5), label="IC")
    panel.add_budget(px, py, income, fill=True, label="BC")
    panel.add_equilibrium(eq, show_ray=True)

fig[0].show_legend(loc="upper right")
fig.save("figure_side_by_side.png")
```

![多面板并排比较](../assets/consumer/figure_side_by_side.png)

### 可用的布局

- `Layout.SINGLE`
- `Layout.STACKED`
- `Layout.SIDE_BY_SIDE`
- `Layout.TOP_TWO_BOTTOM_ONE`
- `Layout.TOP_ONE_BOTTOM_TWO`
- `Layout.GRID_2X2`
- `Layout.GRID_3X3`

`Figure[idx]` 会返回一个面板 `Canvas`，所以布局建好之后，绘图 API 完全相同。

## 路径工具

路径对象会让某一个预算参数逐步变动，并在每一步重新求解消费者问题。

```python
from econ_viz import IncomePath, LinearBudget, PricePath
from econ_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.5, beta=0.5)
budget = LinearBudget(px=2.0, py=2.0, income=40.0)

price_path = PricePath(model, budget=budget, price="px", price_range=(0.8, 6.0), n=40)
income_path = IncomePath(model, budget=budget, income_range=(20.0, 80.0), n=30)
```

这些路径可以用来：

- 用 `Canvas.add_path(...)` 画出 PCC / ICC 形式的均衡轨迹
- 传入 `DemandDiagram`
- 观察价格或收入变动时，消费束如何移动

## `DemandDiagram`

`DemandDiagram` 会创建上下两个面板的图：

- **上方面板**：无差异曲线、预算线与均衡点
- **下方面板**：对应的马歇尔需求曲线

```python
from econ_viz import DemandDiagram, LinearBudget, PricePath
from econ_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.5, beta=0.5)
budget = LinearBudget(px=2.0, py=2.0, income=40.0)
path = PricePath(model, budget=budget, price="px", price_range=(0.8, 6.0), n=40)

fig = DemandDiagram(path, title="Demand: Cobb-Douglas")
fig.add_marshallian_panel(
    price_markers=[1.5, 4.0],
    show_pcc=False,
    show_demand_guides=True,
)
fig.save("demand_cobb_douglas.png")
```

![联动的马歇尔需求图](../assets/consumer/demand_cobb_douglas.png)

### 注意事项

- `DemandDiagram` 目前只接受 `PricePath`
- 平滑、有折点与角点解的需求情况会分别处理，让下方面板在经济意义上保持正确
- `show_pcc=True` 会在商品空间面板上叠加价格消费曲线

## `Canvas.add_path(...)`

不需要完整的需求图时，也可以直接在 `Canvas` 上画出路径。

```python
from econ_viz import Canvas, levels

eq = price_path.equilibria[len(price_path.equilibria) // 2]
lvls = levels.around(eq.utility, n=5)

Canvas(x_max=25, y_max=20) \
    .add_utility(model, levels=lvls) \
    .add_path(price_path, label="PCC") \
    .save("price_path.png")
```
