---
seo_title: "Canvas：教科書風格的經濟學圖形"
description: "Canvas 是 econ-viz 的繪圖畫布，用來畫教科書風格的個體經濟學圖形：第一象限座標軸、箭頭、LaTeX 標籤、預算線與均衡點。"
---

# Canvas 畫布

`Canvas` 是核心的繪圖畫布。它管理一張 matplotlib 圖，樣式遵循個體經濟學教科書的慣例：**只畫第一象限**、座標軸末端有箭頭、標籤用 LaTeX 繪製、**不顯示數字刻度**。

## 建構函式

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

| 參數 | 型別 | 預設值 | 說明 |
|-----------|------|---------|-------------|
| `x_max` | float | 10 | 橫軸上限 |
| `y_max` | float | 10 | 縱軸上限 |
| `x_label` | str | `"X"` | 橫軸末端的標籤 |
| `y_label` | str | `"Y"` | 縱軸末端的標籤 |
| `title` | str 或 None | None | 圖形標題 |
| `dpi` | int | 300 | 點陣匯出解析度（限制在 1–1200） |
| `x_label_pos` | str | `"right"` | `"right"` 把標籤放在軸的末端；`"bottom"` 使用一般的 xlabel |
| `y_label_pos` | str | `"top"` | `"top"` 把標籤放在軸的末端；`"left"` 使用一般的 ylabel |
| `theme` | Theme | `themes.default` | 配色與樣式主題 |

## 方法

所有繪圖方法都會回傳 `self`，所以可以串接呼叫。

### 增加效用函數：`add_utility` {#add_utility data-toc-label="增加效用函數"}

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

![用 add_utility 畫出的無異曲線](../assets/canvas/add_utility.png){ .ev-figure-sm }

### 增加預算線：`add_budget` {#add_budget data-toc-label="增加預算線"}

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

![加上預算線與可行集合陰影](../assets/canvas/add_budget.png){ .ev-figure-sm }

### 增加均衡點：`add_equilibrium` {#add_equilibrium data-toc-label="增加均衡點"}

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

![加上均衡點與垂直虛線](../assets/canvas/add_equilibrium.png){ .ev-figure-sm }

### 增加射線：`add_ray` {#add_ray data-toc-label="增加射線"}

```python
cvs.add_ray(
    slope,             # dy/dx
    color=None,
    linewidth=None,
)
```

![通過最適點的擴張路徑射線](../assets/canvas/add_ray.png){ .ev-figure-sm }

### 增加標記點：`add_point` {#add_point data-toc-label="增加標記點"}

```python
cvs.add_point(
    x, y,
    label=None,
    color=None,
    markersize=6.0,
    offset=(5, 5),     # text offset in points
)
```

![預算線上標記的 A 點](../assets/canvas/add_point.png){ .ev-figure-sm }

### 顯示與儲存：`show` / `save` {#show-save data-toc-label="顯示與儲存"}

```python
cvs.show()               # interactive window
cvs.save("figure.png")   # raster (.png, .pdf, .svg)
```

![完成的圖形](../assets/canvas/show_save.png){ .ev-figure-sm }

## 串接呼叫

```python
Canvas(x_max=20, y_max=15) \
    .add_utility(model, levels=lvls) \
    .add_budget(2.0, 3.0, 30.0, fill=True) \
    .add_equilibrium(eq, show_ray=True) \
    .save("figure.png")
```
