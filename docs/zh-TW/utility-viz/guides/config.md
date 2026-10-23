---
seo_title: "設定檔"
description: "把 utility-viz 圖形的樣式存成所有 EconViz 套件共用的 econ-viz.toml，用 Config 一次載入。"
---

# 設定檔

把顏色、線條、標籤與 legend 的設定存成 `econ-viz.toml`，載入一次就好，不用每個方法都傳一樣的參數。所有 EconViz 套件都讀取同一份檔案，並由 mosaickit 統一解析與檢查。

## 格式

頂層放置所有 EconViz 套件共用的設定：`base`、`[font]`、`[fonts]`，以及 `[color]` 中的 `background`、`axis` 與 `label` 顏色。utility-viz 自身的設定放在 `[utility]` 下；其他套件各有自己的表格，例如 `[principle]`，utility-viz 會略過這些表格。表格名稱對應 Theme 的屬性，欄位名稱與樣式物件的參數相同。沒寫到的設定沿用內建預設值。

```toml
# econ-viz.toml
base = "manual"                  # 共用主題

[font]
text = "serif"
math = "fonts/texgyrepagella-math.otf"

[fonts]
serif = ["fonts/NotoSerifTC-Regular.otf", "fonts/NotoSerifTC-Bold.otf"]

[color]                          # 各套件共用
background = "#ffffff"
axis = "#1a1a1a"
label = "#1a1a1a"

[utility.color]
ic = "#2E86AB"
budget = "#6C3483"
equilibrium = "#C0392B"

[utility.stroke.budget]          # theme.budget_stroke
width = 1.5
style = "solid"

[utility.stroke.ic]              # theme.ic_stroke
width = 1.8
opacity = 0.9

[utility.marker.equilibrium]     # theme.eq_marker
size = 5

[utility.label.point]            # theme.point_label
fontsize = 12
position = "top-right"
top = "2pt"

[utility.label.origin]
visible = false

[utility.fill.budget]            # theme.budget_fill
color = "lightgrey"
opacity = 0.3

[utility.legend]                 # theme.legend
position = "auto"
fontsize = 10

[principle]                      # 由 principle-viz 讀取
language = "zh-TW"
```

| 表格 | 設定的對象 | 欄位 |
|------|------------|------|
| `base` | 作為起點的共用主題 | `"manual"`、`"default"`、`"colorblind"`、`"monochrome"`、`"nord"`、`"paper"`、`"presentation"` |
| `[font]` | 內文與數學字型（共用） | `text`（`"sans"`、`"serif"`、`"mono"`）、`math`（數學字型檔） |
| `[fonts]` | 字型檔（共用） | `sans`、`serif`、`mono`：一個檔案或檔案清單 |
| `[color]` | 共用顏色 | `background`、`axis`、`label` |
| `[utility.color]` | Theme 的顏色，例如 `ic` → `ic_color` | 顏色字串 |
| `[utility.stroke.<name>]` | `theme.<name>_stroke` | `width`、`style`、`color`、`arrow`、`opacity` |
| `[utility.marker.<name>]` | `theme.<name>_marker` | `color`、`size`、`shape`、`opacity` |
| `[utility.label.<name>]` | `theme.<name>_label` | `text`、`position`、`offset`、`color`、`fontsize`、`visible`、`opacity`、`top`、`bottom`、`left`、`right` |
| `[utility.fill.<name>]` | `theme.<name>_fill` | `color`、`opacity` |
| `[utility.legend]` | `theme.legend` | `position`、`fontsize`、`frame`、`columns`、`visible`、`opacity` |

`eq` 也可以寫成 `equilibrium`（`[utility.marker.equilibrium]`、`[utility.color] equilibrium`）。相對路徑以設定檔所在資料夾為準。寫錯時，錯誤訊息會指出檔案與表格，並提示最接近的名稱：

```text
econ-viz.toml: [utility.stroke.budgt] no such setting; did you mean 'budget'? (choose: axis, box, budget, ...)
```

## 主題

`base` 從七個 EconViz 共用主題中選一個。同一名稱在 utility-viz、principle-viz 與其他套件中外觀一致：每個主題為各個角色指定顏色，再由各套件決定元素使用哪個角色。`[utility.*]` 表格仍可在其上調整單一元素。

| `base` | 外觀 | 用途 |
|--------|------|------|
| `manual` | 白底、黑色座標軸與點、灰色曲線 | 手冊與 playground 的黑白樣式，適合列印與講義 |
| `default` | 色盲友善配色、透明背景 | 一般圖形 |
| `colorblind` | 與 `default` 相同的配色 | 需要在名稱上明確標示時 |
| `monochrome` | 只用黑色，以線型與標記區分圖層 | 黑白列印 |
| `nord` | Nord 冷色系 | 螢幕與投影片 |
| `paper` | 柔和色彩、較細線條 | 論文 |
| `presentation` | 色彩較鮮明，線條、標記與標籤分別放大為 1.5、1.3 與 1.25 倍 | 投影 |

內建主題不含深色主題：`base = "dark"` 會發出警告並改用 `default`。需要不透明背景時，請設定 `[color] background`。使用 `base = "manual"` 時，不必逐一寫出手冊的顏色與線寬：

```toml
base = "manual"

[font]
text = "serif"
```

## 微調標籤

`top`、`bottom`、`left` 與 `right` 會在標籤自動定位之後再移動，位置仍由套件決定，只做細部調整。在設定檔中，它們為同一類標籤設定預設值，單位可用 pt、mm、cm 或 in：

```toml
[utility.label.point]
top = "2pt"
```

在程式碼中，`Label` 可移動單一標籤，距離可為點數，或 `"10pt"`、`"0.5em"`（以標籤字級為單位）、`"2mm"` 等字串，並取代設定檔中該方向的值：

```python
from utility_viz import Label

cvs.add_equilibrium(eq, label=Label(top="10pt"))
cvs.add_point(5, 3, label=Label(text="A", left="6pt"))
```

principle-viz 也支援相同的微調，例如 `MarketFigure(labels={"market.equilibrium": Label(top="4pt")})`。

## 舊版設定檔

為 utility-viz 2.0.0b7 以前版本撰寫的設定檔，把 utility-viz 的表格放在頂層（`[color] ic`、`[stroke.budget]`、`[legend]` 等）。這類檔案在 3.0 以前仍可讀取，每次載入會發出一次棄用警告，指出各表格的新位置；同一個鍵同時出現在 `[utility]` 與頂層時，以 `[utility]` 為準。2.0 測試版至 2.0.0b6 使用的 `utility-viz.toml` 也仍可讀取，但會發出警告。`utility-viz init --migrate` 會把表格移到 `[utility]` 下，並保留註解：

```bash
uv run utility-viz init --migrate
```

有 `utility-viz.toml` 時，會將其改寫為 `econ-viz.toml` 並保留舊檔；沒有時，則直接改寫舊格式的 `econ-viz.toml`。

## 載入

`Config` 把主題與字體選項放在一起。從檔案讀進來後，可以讓它成為之後所有圖的預設值，也可以只把它的 `theme` 交給單一張 `Canvas`。

### 讀取設定檔 {#config_load data-toc-label="讀取設定檔"}

把一個 TOML 檔讀成 `Config`。

<!-- api: config.load -->

??? example "查看範例"

    ```python
    from utility_viz import Config

    config = Config.load("econ-viz.toml")
    theme = config.theme
    ```

### 自動尋找 {#config_discover data-toc-label="自動尋找"}

依序尋找：指定的路徑、`econ-viz.toml`、較舊的 `utility-viz.toml`（會發出警告）、內建預設值。和 `Config.load` 不同的是，找不到檔案時不會出錯。

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
    Config.load("econ-viz.toml").use()
    # 套用設定檔
    Canvas(x_max=20, y_max=15)

    theme = Config.load("econ-viz.toml").theme
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
uv run utility-viz init                       # 產生 econ-viz.toml
uv run utility-viz plot --model cobb-douglas --px 2 --py 3 --income 30 \
    --config econ-viz.toml --output cd.png
```

`mosaickit.econ_toml.use("econ-viz.toml")` 會一次為所有已安裝的 EconViz 套件載入此檔。
