---
seo_title: "設定檔"
description: "把 econ-viz 圖形的樣式存成 econ-viz.toml 設定檔，用 Config 一次載入。"
---

# 設定檔

把顏色、線條、標籤與 legend 的設定存成 `econ-viz.toml`，載入一次就好，不用每個方法都傳一樣的參數。

## 格式

段落名稱對應 Theme 的屬性，欄位名稱與樣式物件的參數相同。沒寫到的設定沿用內建預設值。

```toml
# econ-viz.toml
base = "default"                 # default or nord

[font]
text = "TeX Gyre Pagella"
math = "stix"

[color]
ic = "#2E86AB"
budget = "#6C3483"
equilibrium = "#C0392B"

[stroke.budget]                  # theme.budget_stroke
width = 1.5
style = "solid"

[stroke.ic]                      # theme.ic_stroke
width = 1.8
opacity = 0.9

[marker.equilibrium]             # theme.eq_marker
size = 5

[label.point]                    # theme.point_label
fontsize = 12
position = "top-right"

[label.origin]
visible = false

[fill.budget]                    # theme.budget_fill
color = "lightgrey"
opacity = 0.3

[legend]                         # theme.legend
position = "auto"
fontsize = 10
```

| 段落 | 設定的對象 | 欄位 |
|------|------------|------|
| `base` | 作為基礎的內建主題 | `"default"`、`"nord"` |
| `[font]` | 內文與數學字體 | `text`、`math` |
| `[color]` | Theme 的顏色，例如 `ic` → `ic_color` | 顏色字串 |
| `[stroke.<name>]` | `theme.<name>_stroke` | `width`、`style`、`color`、`arrow`、`opacity` |
| `[marker.<name>]` | `theme.<name>_marker` | `color`、`size`、`shape`、`opacity` |
| `[label.<name>]` | `theme.<name>_label` | `position`、`offset`、`color`、`fontsize`、`visible`、`opacity` |
| `[fill.<name>]` | `theme.<name>_fill` | `color`、`opacity` |
| `[legend]` | `theme.legend` | `position`、`fontsize`、`frame`、`columns`、`visible`、`opacity` |

`eq` 也可以寫成 `equilibrium`（`[marker.equilibrium]`、`[color] equilibrium`）。段落、名稱或欄位寫錯時，錯誤訊息會列出可用的選項。

## 載入

```python
from econ_viz import Canvas, Config

Config.load("econ-viz.toml").use()     # 之後建立的圖
Canvas(x_max=20, y_max=15)             # 套用設定檔

theme = Config.load("econ-viz.toml").theme
Canvas(theme=theme)                    # 或只套用在這張圖

Config.reset()                         # 回到內建預設值
```

方法明確傳入的參數仍然優先於設定檔：以上面的設定為例，`add_budget(..., stroke=Stroke(width=1))` 會畫出 1 pt 粗、其餘沿用設定檔樣式的線。

## 命令列

`econ-viz init` 會產生一份附註解的範本，列出所有可以設定的名稱；`econ-viz plot` 則透過 `--config` 讀取同一份設定檔：

```bash
uv run econ-viz init                       # 產生 econ-viz.toml
uv run econ-viz plot --model cobb-douglas --px 2 --py 3 --income 30 \
    --config econ-viz.toml --output cd.png
```
