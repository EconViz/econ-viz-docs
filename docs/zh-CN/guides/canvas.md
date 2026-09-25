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
    x_label_pos="right",   # "right" 或 "bottom"
    y_label_pos="top",     # "top" 或 "left"
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

### 效用曲线 {#add_utility data-toc-label="效用曲线"}

画出效用函数的无差异曲线。`levels` 传入整数会自动决定曲线的间距，也可以传入一组效用值，例如用 `levels.around(eq.utility, n=5)` 让曲线分布在最优点周围。

```python
cvs.add_utility(
    func,
    levels=3,          # 曲线数或效用值列表
    color=None,        # 默认 theme.ic_color
    linewidth=None,    # 默认 theme.ic_linewidth
    show_rays=False,
    show_kinks=False,
    kink_radius=1.0,
    show_bliss=True,   # 标出极乐点（Satiation）
)
```

![用 add_utility 画出的无差异曲线](../../assets/canvas/add_utility.png){ .ev-figure-sm }

### 预算线 {#add_budget data-toc-label="预算线"}

画出预算线 $p_x x + p_y y = I$。设置 `fill=True` 会在预算线下方的可行集加上阴影。

```python
cvs.add_budget(
    px, py, income,
    color=None,
    linewidth=None,
    linestyle="-",
    label=None,        # 图例标签（LaTeX）
    fill=False,        # 可行集阴影
    fill_alpha=None,   # 默认 theme.budget_fill_alpha
)
```

![加上预算线与可行集阴影](../../assets/canvas/add_budget.png){ .ev-figure-sm }

### 均衡点 {#add_equilibrium data-toc-label="均衡点"}

在最优消费组合画上均衡点，并画出到两轴的垂直虚线。`eq` 传入 `solve()` 的返回值；`show_ray=True` 会同时画出通过原点的扩展路径。

```python
cvs.add_equilibrium(
    eq,                # solve() 的返回值
    color=None,
    markersize=None,
    label="x^*",
    drop_dashes=True,  # 到两轴的虚线
    show_ray=False,    # 扩展路径
)
```

![加上均衡点与垂直虚线](../../assets/canvas/add_equilibrium.png){ .ev-figure-sm }

### 射线 {#add_ray data-toc-label="射线"}

从原点画一条斜率为 `slope`（dy/dx）的虚线射线，常用来表示扩展路径或固定的消费比例。

```python
cvs.add_ray(
    slope,             # dy/dx
    color=None,
    linewidth=None,
)
```

![通过最优点的扩展路径射线](../../assets/canvas/add_ray.png){ .ev-figure-sm }

### 标记点 {#add_point data-toc-label="标记点"}

标记任意一点，例如要与最优点比较的消费组合。`label` 会以 LaTeX 数学模式显示，`offset` 用来调整标签的位置，单位是 points。

```python
cvs.add_point(
    x, y,
    label=None,
    color=None,
    markersize=6.0,
    offset=(5, 5),     # 标签偏移（pt）
)
```

![预算线上标记的 A 点](../../assets/canvas/add_point.png){ .ev-figure-sm }

### 显示与保存 {#show-save data-toc-label="显示与保存"}

`show()` 会打开交互窗口。`save()` 根据扩展名决定格式，支持 `.png`、`.pdf`、`.svg`，以及输出 TikZ 的 `.tex`。`save()` 也会释放 matplotlib 的资源，所以要放在最后调用。

```python
cvs.show()               # 交互窗口
cvs.save("figure.png")   # .png / .pdf / .svg / .tex
```

![完成的图形](../../assets/canvas/show_save.png){ .ev-figure-sm }

## 串接调用

```python
Canvas(x_max=20, y_max=15) \
    .add_utility(model, levels=lvls) \
    .add_budget(2.0, 3.0, 30.0, fill=True) \
    .add_equilibrium(eq, show_ray=True) \
    .save("figure.png")
```
