---
seo_title: "Canvas：教科書風格的經濟學圖形"
description: "Canvas 是 econ-viz 的繪圖畫布，用來畫教科書風格的個體經濟學圖形：第一象限座標軸、箭頭、LaTeX 標籤、預算線與均衡點。"
---

# Canvas 畫布

`Canvas` 是核心的繪圖畫布。它管理一張 matplotlib 圖，樣式遵循個體經濟學教科書的慣例：**只畫第一象限**、座標軸末端有箭頭、標籤用 LaTeX 繪製、**不顯示數字刻度**。

## 建構函式

```python
from econ_viz import ArrowStyle, Axis, Canvas, Stroke, themes

cvs = Canvas(
    x_max=20,
    y_max=15,
    title=r"Cobb-Douglas $x^{0.5} y^{0.5}$",
    dpi=300,
    font="DejaVu Sans",
    math_font="stix",
    axis_stroke=Stroke(width=1.0, arrow=ArrowStyle.TRIANGLE),
    x_axis=Axis(label="x", label_position="right"),  # "top"、"right" 或 "bottom"
    y_axis=Axis(label="y", label_position="top"),    # "left"、"top" 或 "right"
    theme=themes.default,
)
```

| 參數 | 型別 | 預設值 | 說明 |
|-----------|------|---------|-------------|
| `x_max` | float | 10 | 橫軸上限 |
| `y_max` | float | 10 | 縱軸上限 |
| `x_axis` | `Axis` | None | 橫軸的標籤、標籤位置與線條 |
| `y_axis` | `Axis` | None | 縱軸的標籤、標籤位置與線條 |
| `x_label` | str | `"X"` | 橫軸 `Axis(label=...)` 的簡寫 |
| `y_label` | str | `"Y"` | 縱軸 `Axis(label=...)` 的簡寫 |
| `title` | str 或 None | None | 圖形標題 |
| `dpi` | int | 300 | 點陣匯出解析度（限制在 1–1200） |
| `x_label_pos` | str 或 `LabelPosition` | `"right"` | `Axis(label_position=...)` 的簡寫：箭頭上方、右側或下方 |
| `y_label_pos` | str 或 `LabelPosition` | `"top"` | `Axis(label_position=...)` 的簡寫：箭頭左側、上方或右側 |
| `font` | str 或序列 | None | 所有文字使用的字體或候補字體列表 |
| `math_font` | str | None | 數學字體：`dejavusans`、`dejavuserif`、`cm`、`stix` 或 `stixsans` |
| `axis_stroke` | `Stroke` | 主題預設值 | 同時設定兩軸的粗細、線條樣式、顏色與箭頭樣式 |
| `x_axis_stroke` | `Stroke` | None | 橫軸的個別覆寫，是 `Axis(stroke=...)` 的簡寫 |
| `y_axis_stroke` | `Stroke` | None | 縱軸的個別覆寫，是 `Axis(stroke=...)` 的簡寫 |
| `theme` | Theme | `themes.default` | 配色與樣式主題 |

同一項設定給了兩次時，以 `Axis` 的欄位為準。座標軸線條的優先順序由高到低是 `Axis.stroke`、`x_axis_stroke`、`axis_stroke`、`x_line_style` / `x_arrow_style`、`theme.axis_stroke`。

## 方法

所有繪圖方法都會回傳 `self`，所以可以串接呼叫。

### 效用曲線 {#add_utility data-toc-label="效用曲線"}

畫出效用函數的無異曲線。`levels` 傳入整數會自動決定曲線的間距，也可以傳入一串效用值，例如用 `levels.around(eq.utility, n=5)` 讓曲線分布在最適點周圍。

```python
cvs.add_utility(
    func,
    levels=3,          # 曲線數或效用值列表
    stroke=None,       # 預設 theme.ic_stroke
    ray_stroke=None,
    show_rays=False,
    show_kinks=False,
    kink_radius=1.0,
    show_bliss=True,   # 標出極樂點（Satiation）
    kink_marker=None,  # 預設 theme.kink_marker
    bliss_marker=None, # 預設 theme.bliss_marker
    ic_label=None,     # 曲線末端效用值的 Label
    bliss_label=None,  # str 或 Label
)
```

![用 add_utility 畫出的無異曲線](../../assets/canvas/add_utility.png){ .ev-figure-sm }

### 預算線 {#add_budget data-toc-label="預算線"}

畫出預算線 $p_x x + p_y y = I$。設定 `fill=True` 會在預算線下方的可行集合加上陰影。

```python
cvs.add_budget(
    px, py, income,
    stroke=None,       # 預設 theme.budget_stroke
    label=None,        # 圖例標籤（LaTeX）
    fill=False,        # True 或 Fill；預設 theme.budget_fill
)
```

![加上預算線與可行集合陰影](../../assets/canvas/add_budget.png){ .ev-figure-sm }

### 均衡點 {#add_equilibrium data-toc-label="均衡點"}

在最適消費組合畫上均衡點，並拉出到兩軸的垂直虛線。`eq` 傳入 `solve()` 的回傳值；`show_ray=True` 會一併畫出通過原點的擴張路徑。

```python
cvs.add_equilibrium(
    eq,                # solve() 的回傳值
    label="x^*",       # str 或 Label
    marker=None,       # 預設 theme.eq_marker
    drop_dashes=True,  # 到兩軸的虛線
    show_ray=False,    # 擴張路徑
    drop_stroke=None,
    ray_stroke=None,
)
```

![加上均衡點與垂直虛線](../../assets/canvas/add_equilibrium.png){ .ev-figure-sm }

### 射線 {#add_ray data-toc-label="射線"}

從原點畫一條斜率為 `slope`（dy/dx）的虛線射線，常用來表示擴張路徑或固定的消費比例。

```python
cvs.add_ray(
    slope,             # dy/dx
    stroke=None,       # 預設 theme.ray_stroke
)
```

![通過最適點的擴張路徑射線](../../assets/canvas/add_ray.png){ .ev-figure-sm }

### 標記點 {#add_point data-toc-label="標記點"}

標記任意一點，例如要跟最適點比較的消費組合。`label` 會以 LaTeX 數學模式顯示；要移動標籤或改樣式時，傳入 `Label`。

```python
cvs.add_point(
    x, y,
    label=None,        # str 或 Label
    marker=None,       # 預設 theme.point_marker
)
```

![預算線上標記的 A 點](../../assets/canvas/add_point.png){ .ev-figure-sm }

### 顯示與儲存 {#show-save data-toc-label="顯示與儲存"}

`show()` 會開啟互動視窗。`save()` 依副檔名決定格式，支援 `.png`、`.pdf`、`.svg`，以及輸出 TikZ 的 `.tex`。`save()` 也會釋放 matplotlib 的資源，所以要放在最後呼叫。

```python
cvs.show()               # 互動視窗
cvs.save("figure.png")   # .png / .pdf / .svg / .tex
```

![完成的圖形](../../assets/canvas/show_save.png){ .ev-figure-sm }

## 樣式

每一類元素都有自己的樣式物件。沒有指定的欄位會沿用主題預設值，所以只要設定想改的部分。

| 物件 | 控制項目 | 主題預設值 |
|------|----------|------------|
| `Stroke` | 線條粗細、線條樣式、顏色、箭頭 | `theme.budget_stroke`、`theme.ic_stroke` 等 |
| `Marker` | 點的顏色、大小、形狀 | `theme.eq_marker`、`theme.point_marker` 等 |
| `Label` | 標籤文字、位置、位移、顏色、大小、是否顯示 | `theme.point_label`、`theme.ic_label` 等 |
| `Fill` | 陰影顏色與透明度 | `theme.budget_fill` |
| `Axis` | 單一座標軸的標籤、標籤位置與線條 | 無 |

```python
from econ_viz import Canvas, Fill, Label, Marker, Stroke

(
    Canvas(x_max=20, y_max=15)
    .add_utility(model, levels=lvls, ic_label=Label(text="U={:.1f}", position="top"))
    .add_budget(2.0, 3.0, 30.0, stroke=Stroke(color="black"),
                fill=Fill(color="lightgrey", alpha=0.4))
    .add_equilibrium(eq, marker=Marker(color="#C0392B", shape="s"),
                     label=Label(position="bottom-left", offset=8))
    .add_point(12.0, 2.0, label=Label(text="A", position="left"))
    .save("styles.png")
)
```

![自訂線條、陰影、標記點與標籤](../../assets/canvas/styles.png){ .ev-figure-sm }

**建議用 `Stroke` 設定線條樣式**。另外的 `color`、`linewidth`、`linestyle` 參數仍可當作簡寫使用，畫出來的結果相同。標籤預設沿用所屬點的 `Marker` 顏色，除非另外指定；位置可用 `top`、`bottom`、`left`、`right` 與 `top-right` 等四個角落，`Label(visible=False)` 可隱藏標籤。

下方的線條樣式與箭頭樣式，座標軸透過 `x_*` 與 `y_*` 參數設定，其他線條則透過 `Stroke` 套用。

### 線條樣式

座標軸可使用 `LineStyle.SOLID`、`DASHED`、`DOTTED` 或 `DASHDOT`。也可以直接傳入對應的 `solid`、`dashed`、`dotted` 或 `dashdot` 字串。其他線條則透過 `Stroke(style=...)` 設定。

```python
import matplotlib.pyplot as plt

from econ_viz import Canvas, LineStyle

styles = [
    LineStyle.SOLID,
    LineStyle.DASHED,
    LineStyle.DOTTED,
    LineStyle.DASHDOT,
]

fig, axes = plt.subplots(2, 2, figsize=(7, 7))
for ax, style in zip(axes.flat, styles):
    Canvas(
        title=style.value,
        x_line_style=style,
        y_line_style=style,
        fig=fig,
        ax=ax,
    )

fig.tight_layout()
fig.savefig("line_styles.png", dpi=160, transparent=True)
```

![可用的線條樣式](../../assets/canvas/line_styles.png)

### 箭頭樣式

座標軸可使用 `ArrowStyle.SIMPLE`、`TRIANGLE`、`FANCY` 或 `WEDGE`。其他可見線條則透過 `Stroke(arrow=...)` 加上相同的箭頭樣式。

```python
import matplotlib.pyplot as plt

from econ_viz import ArrowStyle, Canvas

styles = [
    ArrowStyle.SIMPLE,
    ArrowStyle.TRIANGLE,
    ArrowStyle.FANCY,
    ArrowStyle.WEDGE,
]

fig, axes = plt.subplots(2, 2, figsize=(7, 7))
for ax, style in zip(axes.flat, styles):
    Canvas(
        title=style.name.title(),
        x_arrow_style=style,
        y_arrow_style=style,
        fig=fig,
        ax=ax,
    )

fig.tight_layout()
fig.savefig("arrow_styles.png", dpi=160, transparent=True)
```

![可用的箭頭樣式](../../assets/canvas/arrow_styles.png)

路徑、效果分解、`DemandDiagram`、`Figure` 與 `EdgeworthBox` 也可以使用 `Stroke`。沒有指定的欄位會沿用目前主題。

## 串接呼叫

```python
Canvas(x_max=20, y_max=15) \
    .add_utility(model, levels=lvls) \
    .add_budget(2.0, 3.0, 30.0, fill=True) \
    .add_equilibrium(eq, show_ray=True) \
    .save("figure.png")
```
