---
seo_title: "經濟學圖形的配色主題"
description: "用內建主題控制 econ-viz 圖形的顏色與線條粗細，包含色盲友善的預設配色，也可以自訂主題。"
---

# 主題

主題控制 Canvas 使用的所有顏色與線條粗細。

![預設主題範例](../../assets/themes/theme_default.png)

## 內建主題

### Default

```python
from econ_viz import Canvas, themes

cvs = Canvas(x_max=20, y_max=15, theme=themes.default)
```

### Nord

```python
cvs = Canvas(x_max=20, y_max=15, theme=themes.nord)
```

Nord 主題使用 [Nord 配色](https://www.nordtheme.com/)，以冷色藍與低飽和色調為主，適合學術簡報。

![Nord 主題範例](../../assets/themes/theme_nord.png)

## 自訂主題

```python
from econ_viz import Theme

my_theme = Theme(
    name="custom",
    axis_color="#333333",
    label_color="#333333",
    ic_color="#2563eb",
    ic_linewidth=1.5,
    budget_color="#dc2626",
    budget_linewidth=1.5,
    budget_fill_alpha=0.08,
    eq_color="#16a34a",
    eq_markersize=6.0,
    ray_color="#9ca3af",
    ray_linewidth=1.0,
    kink_color="#2563eb",
)

cvs = Canvas(x_max=20, y_max=15, theme=my_theme)
```

## 主題屬性

| 屬性 | 說明 |
|-----------|-------------|
| `name` | 主題名稱 |
| `axis_color` | 座標軸與箭頭的顏色 |
| `label_color` | 座標軸標籤與原點標籤的顏色 |
| `ic_color` | 無異曲線的顏色 |
| `ic_linewidth` | 無異曲線的線寬 |
| `budget_color` | 預算線的顏色 |
| `budget_linewidth` | 預算線的線寬 |
| `budget_fill_alpha` | 可行集合陰影的不透明度 |
| `eq_color` | 均衡點與垂直虛線的顏色 |
| `eq_markersize` | 均衡點的大小 |
| `ray_color` | 擴張路徑射線的顏色 |
| `ray_linewidth` | 擴張路徑射線的線寬 |
| `kink_color` | 拗折點標記的顏色 |
