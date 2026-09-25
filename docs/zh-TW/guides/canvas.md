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
    x_label_pos="right",   # "right" 或 "bottom"
    y_label_pos="top",     # "top" 或 "left"
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

### 效用曲線 {#add_utility data-toc-label="效用曲線"}

畫出效用函數的無異曲線。`levels` 傳入整數會自動決定曲線的間距，也可以傳入一串效用值，例如用 `levels.around(eq.utility, n=5)` 讓曲線分布在最適點周圍。

```python
cvs.add_utility(
    func,
    levels=3,          # 曲線數或效用值列表
    color=None,        # 預設 theme.ic_color
    linewidth=None,    # 預設 theme.ic_linewidth
    show_rays=False,
    show_kinks=False,
    kink_radius=1.0,
    show_bliss=True,   # 標出極樂點（Satiation）
)
```

![用 add_utility 畫出的無異曲線](../../assets/canvas/add_utility.png){ .ev-figure-sm }

### 預算線 {#add_budget data-toc-label="預算線"}

畫出預算線 $p_x x + p_y y = I$。設定 `fill=True` 會在預算線下方的可行集合加上陰影。

```python
cvs.add_budget(
    px, py, income,
    color=None,
    linewidth=None,
    linestyle="-",
    label=None,        # 圖例標籤（LaTeX）
    fill=False,        # 可行集合陰影
    fill_alpha=None,   # 預設 theme.budget_fill_alpha
)
```

![加上預算線與可行集合陰影](../../assets/canvas/add_budget.png){ .ev-figure-sm }

### 均衡點 {#add_equilibrium data-toc-label="均衡點"}

在最適消費組合畫上均衡點，並拉出到兩軸的垂直虛線。`eq` 傳入 `solve()` 的回傳值；`show_ray=True` 會一併畫出通過原點的擴張路徑。

```python
cvs.add_equilibrium(
    eq,                # solve() 的回傳值
    color=None,
    markersize=None,
    label="x^*",
    drop_dashes=True,  # 到兩軸的虛線
    show_ray=False,    # 擴張路徑
)
```

![加上均衡點與垂直虛線](../../assets/canvas/add_equilibrium.png){ .ev-figure-sm }

### 射線 {#add_ray data-toc-label="射線"}

從原點畫一條斜率為 `slope`（dy/dx）的虛線射線，常用來表示擴張路徑或固定的消費比例。

```python
cvs.add_ray(
    slope,             # dy/dx
    color=None,
    linewidth=None,
)
```

![通過最適點的擴張路徑射線](../../assets/canvas/add_ray.png){ .ev-figure-sm }

### 標記點 {#add_point data-toc-label="標記點"}

標記任意一點，例如要跟最適點比較的消費組合。`label` 會以 LaTeX 數學模式顯示，`offset` 用來調整標籤的位置，單位是 points。

```python
cvs.add_point(
    x, y,
    label=None,
    color=None,
    markersize=6.0,
    offset=(5, 5),     # 標籤位移（pt）
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

## 串接呼叫

```python
Canvas(x_max=20, y_max=15) \
    .add_utility(model, levels=lvls) \
    .add_budget(2.0, 3.0, 30.0, fill=True) \
    .add_equilibrium(eq, show_ray=True) \
    .save("figure.png")
```
