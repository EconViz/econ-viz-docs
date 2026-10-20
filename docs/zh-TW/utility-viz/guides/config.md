---
seo_title: "設定檔"
description: "把 utility-viz 圖形的樣式存成 utility-viz.toml 設定檔，用 Config 一次載入。"
---

# 設定檔

把顏色、線條、標籤與 legend 的設定存成 `utility-viz.toml`，載入一次就好，不用每個方法都傳一樣的參數。

## 格式

段落名稱對應 Theme 的屬性，欄位名稱與樣式物件的參數相同。沒寫到的設定沿用內建預設值。

```toml
# utility-viz.toml
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

`Config` 把主題與字體選項放在一起。從檔案讀進來後，可以讓它成為之後所有圖的預設值，也可以只把它的 `theme` 交給單一張 `Canvas`。

### 讀取設定檔 {#config_load data-toc-label="讀取設定檔"}

把一個 TOML 檔讀成 `Config`。

<!-- api: config.load -->

??? example "查看範例"

    ```python
    from utility_viz import Config

    config = Config.load("utility-viz.toml")
    theme = config.theme
    ```

### 自動尋找 {#config_discover data-toc-label="自動尋找"}

依序尋找：指定的路徑、`utility-viz.toml`、內建預設值。和 `Config.load` 不同的是，找不到檔案時不會出錯。

<!-- api: config.discover -->

??? example "查看範例"

    ```python
    from utility_viz import Config

    # 找不到檔案時回到內建預設值
    config = Config.discover()
    ```

### 套用 {#config_use data-toc-label="套用"}

讓這份 `Config` 成為之後建立的圖的預設值，並回傳它自己。只想影響單一張圖時，把它的 `theme` 傳給 `Canvas(theme=...)`。

<!-- api: config.use -->

??? example "查看範例"

    ```python
    from utility_viz import Canvas, Config

    # 之後建立的圖
    Config.load("utility-viz.toml").use()
    # 套用設定檔
    Canvas(x_max=20, y_max=15)

    theme = Config.load("utility-viz.toml").theme
    # 或只套用在這張圖
    Canvas(theme=theme)
    ```

### 還原 {#config_reset data-toc-label="還原"}

回到內建預設值。`Config.active()` 可以查目前使用的是哪一份 `Config`。

<!-- api: config.reset -->

<!-- api: config.active -->

??? example "查看範例"

    ```python
    from utility_viz import Config

    # 回到內建預設值
    Config.reset()
    ```

方法明確傳入的參數仍然優先於設定檔：以上面的設定為例，`add_budget(..., stroke=Stroke(width=1))` 會畫出 1 pt 粗、其餘沿用設定檔樣式的線。

## 命令列

`utility-viz init` 會產生一份附註解的範本，列出所有可以設定的名稱；`utility-viz plot` 則透過 `--config` 讀取同一份設定檔：

```bash
uv run utility-viz init                       # 產生 utility-viz.toml
uv run utility-viz plot --model cobb-douglas --px 2 --py 3 --income 30 \
    --config utility-viz.toml --output cd.png
```
