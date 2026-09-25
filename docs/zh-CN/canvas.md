---
seo_title: "Canvas：教科书风格的经济学图形"
description: "Canvas 是 econ-viz 的绘图画布，用来画教科书风格的微观经济学图形：第一象限坐标轴、箭头、LaTeX 标签、预算线与均衡点。"
---

# Canvas 画布

`Canvas` 是核心的绘图画布。它管理一张 matplotlib 图，样式遵循微观经济学教科书的惯例：**只画第一象限**、坐标轴末端有箭头、标签用 LaTeX 绘制、**不显示数字刻度**。

## 构造函数

```python
from econ_viz import Canvas

cvs = Canvas(
    x_max=20,
    y_max=15,
    x_label="x",
    y_label="y",
    title=r"Cobb-Douglas $x^{0.5} y^{0.5}$",
    dpi=300,
    x_label_pos="right",   # "right" (axis tip) or "bottom"
    y_label_pos="top",     # "top" (axis tip) or "left"
    theme=themes.default,
)
```

| 参数 | 类型 | 默认值 | 说明 |
|-----------|------|---------|-------------|
| `x_max` | float | 10 | 横轴上限 |
| `y_max` | float | 10 | 纵轴上限 |
| `x_label` | str | `"X"` | 横轴末端的标签 |
| `y_label` | str | `"Y"` | 纵轴末端的标签 |
| `title` | str 或 None | None | 图形标题 |
| `dpi` | int | 300 | 位图导出分辨率（限制在 1–1200） |
| `x_label_pos` | str | `"right"` | `"right"` 把标签放在轴的末端；`"bottom"` 使用一般的 xlabel |
| `y_label_pos` | str | `"top"` | `"top"` 把标签放在轴的末端；`"left"` 使用一般的 ylabel |
| `theme` | Theme | `themes.default` | 配色与样式主题 |

## 方法

所有绘图方法都会返回 `self`，所以可以串接调用。

### 添加效用函数：`add_utility` {#add_utility data-toc-label="添加效用函数"}

```python
cvs.add_utility(
    func,
    levels=3,          # int (auto-spaced) or explicit list of floats
    color=None,        # falls back to theme.ic_color
    linewidth=None,    # falls back to theme.ic_linewidth
    show_rays=False,
    show_kinks=False,
    kink_radius=1.0,
    show_bliss=True,   # draw ★ at bliss point (Satiation models only)
)
```

![用 add_utility 画出的无差异曲线](../assets/canvas/add_utility.png){ .ev-figure-sm }

### 添加预算线：`add_budget` {#add_budget data-toc-label="添加预算线"}

```python
cvs.add_budget(
    px, py, income,
    color=None,
    linewidth=None,
    linestyle="-",
    label=None,        # legend label (LaTeX math mode)
    fill=False,        # shade the feasible set
    fill_alpha=None,   # falls back to theme.budget_fill_alpha
)
```

![加上预算线与可行集阴影](../assets/canvas/add_budget.png){ .ev-figure-sm }

### 添加均衡点：`add_equilibrium` {#add_equilibrium data-toc-label="添加均衡点"}

```python
cvs.add_equilibrium(
    eq,                # Equilibrium namedtuple from solve()
    color=None,
    markersize=None,
    label="x^*",
    drop_dashes=True,  # dashed perpendicular lines to both axes
    show_ray=False,    # expansion-path ray from origin
)
```

![加上均衡点与垂直虚线](../assets/canvas/add_equilibrium.png){ .ev-figure-sm }

### 添加射线：`add_ray` {#add_ray data-toc-label="添加射线"}

```python
cvs.add_ray(
    slope,             # dy/dx
    color=None,
    linewidth=None,
)
```

![通过最优点的扩展路径射线](../assets/canvas/add_ray.png){ .ev-figure-sm }

### 添加标记点：`add_point` {#add_point data-toc-label="添加标记点"}

```python
cvs.add_point(
    x, y,
    label=None,
    color=None,
    markersize=6.0,
    offset=(5, 5),     # text offset in points
)
```

![预算线上标记的 A 点](../assets/canvas/add_point.png){ .ev-figure-sm }

### 显示与保存：`show` / `save` {#show-save data-toc-label="显示与保存"}

```python
cvs.show()               # interactive window
cvs.save("figure.png")   # raster (.png, .pdf, .svg)
```

![完成的图形](../assets/canvas/show_save.png){ .ev-figure-sm }

## 串接调用

```python
Canvas(x_max=20, y_max=15) \
    .add_utility(model, levels=lvls) \
    .add_budget(2.0, 3.0, 30.0, fill=True) \
    .add_equilibrium(eq, show_ray=True) \
    .save("figure.png")
```
