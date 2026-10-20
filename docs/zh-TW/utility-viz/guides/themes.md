---
seo_title: "主題與設定"
---

# 主題與設定

<span id="sec-themes"></span>

`Theme` 定義圖形的預設外觀；`Config` 從 TOML 檔案載入主題覆寫與字型設定。`Canvas`、`Figure`、`DemandDiagram`、價格效果分解及 `EdgeworthBox` 共用這些樣式物件。

## 內建主題

<!-- api: agora.utility_viz.guides_themes_1 -->

Python API 提供下列主題。主題物件不可變；需要調整欄位時，可建立新的 `Theme`，或以 `Config` 覆寫指定欄位。

<span id="tab-themes"></span>

| 名稱 | 特性 |
| --- | --- |
| `default` | 色盲友善的預設配色 |
| `colorblind` | 與 `default` 相同的配色別名 |
| `nord` | 採用 Nord 色盤的冷色系主題 |
| `paper` | 透明背景與出版用細線條 |
| `monochrome` | 以線型與標記區分圖層的黑白主題 |
| `presentation` | 放大標籤、線條與標記，供投影使用 |
| `dark` | 深色背景與相應的前景色 |

Python API 與設定檔的 `base` 可使用全部七個名稱 (命令列直接傳入 `--theme` 時，只接受 `colorblind` 別名以外的六個主題。)。

預設主題的顏色取自一組色盲友善的配色 [{thriveth} (2014)](../project/references.md#thriveth2014)。

`themes.COLORBLIND_CYCLE_HEX` 與 `themes.COLORBLIND_CYCLE_RGB` 提供這組配色的十六進位與 RGB 值。經濟學教學大量依賴圖形，因此不應只靠顏色傳達意義，以免視覺障礙的學生無法辨識 [Kugler (1996)](../project/references.md#kugler1996)。

下列各圖用內建主題（`dark` 除外）畫出同一張 Cobb-Douglas 圖，線寬沿用本手冊，底色為白色。

```python
from dataclasses import replace

from utility_viz import Canvas, levels, solve, themes
from utility_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.5, beta=0.5)
eq = solve(model, px=2.0, py=3.0, income=30.0)

# 主題配色 本手冊線寬
theme = replace(
    themes.default,
    background_color="#ffffff",
    ic_linewidth=2.6,
    budget_linewidth=2.6,
    eq_markersize=5.0,
)

cvs = Canvas(
    x_max=20,
    y_max=15,
    x_label="$x$",
    y_label="$y$",
    theme=theme,
)
cvs.add_utility(model, levels=levels.around(eq.utility, n=3))
cvs.add_budget(2.0, 3.0, 30.0, fill=True)
cvs.add_equilibrium(eq)
cvs.save("theme_default.png")
```

<figure class="ev-fig" markdown>

![`default` 主題](../../../assets/utility-viz/agora/themes/default.svg){ .ev-figure-sm }

<a class="ev-download" href="../../../assets/utility-viz/agora/themes/default.zh-TW.py" download aria-label="下載生圖原始檔"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下載生圖原始檔</span></a>

<figcaption markdown>`default` 主題</figcaption>

</figure>

```python
from dataclasses import replace

from utility_viz import Canvas, levels, solve, themes
from utility_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.5, beta=0.5)
eq = solve(model, px=2.0, py=3.0, income=30.0)

# 主題配色 本手冊線寬
theme = replace(
    themes.nord,
    background_color="#ffffff",
    ic_linewidth=2.6,
    budget_linewidth=2.6,
    eq_markersize=5.0,
)

cvs = Canvas(
    x_max=20,
    y_max=15,
    x_label="$x$",
    y_label="$y$",
    theme=theme,
)
cvs.add_utility(model, levels=levels.around(eq.utility, n=3))
cvs.add_budget(2.0, 3.0, 30.0, fill=True)
cvs.add_equilibrium(eq)
cvs.save("theme_nord.png")
```

<figure class="ev-fig" markdown>

![`nord` 主題](../../../assets/utility-viz/agora/themes/nord.svg){ .ev-figure-sm }

<a class="ev-download" href="../../../assets/utility-viz/agora/themes/nord.zh-TW.py" download aria-label="下載生圖原始檔"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下載生圖原始檔</span></a>

<figcaption markdown>`nord` 主題</figcaption>

</figure>

```python
from dataclasses import replace

from utility_viz import Canvas, levels, solve, themes
from utility_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.5, beta=0.5)
eq = solve(model, px=2.0, py=3.0, income=30.0)

# 主題配色 本手冊線寬
theme = replace(
    themes.paper,
    background_color="#ffffff",
    ic_linewidth=2.6,
    budget_linewidth=2.6,
    eq_markersize=5.0,
)

cvs = Canvas(
    x_max=20,
    y_max=15,
    x_label="$x$",
    y_label="$y$",
    theme=theme,
)
cvs.add_utility(model, levels=levels.around(eq.utility, n=3))
cvs.add_budget(2.0, 3.0, 30.0, fill=True)
cvs.add_equilibrium(eq)
cvs.save("theme_paper.png")
```

<figure class="ev-fig" markdown>

![`paper` 主題](../../../assets/utility-viz/agora/themes/paper.svg){ .ev-figure-sm }

<a class="ev-download" href="../../../assets/utility-viz/agora/themes/paper.zh-TW.py" download aria-label="下載生圖原始檔"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下載生圖原始檔</span></a>

<figcaption markdown>`paper` 主題</figcaption>

</figure>

```python
from dataclasses import replace

from utility_viz import Canvas, levels, solve, themes
from utility_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.5, beta=0.5)
eq = solve(model, px=2.0, py=3.0, income=30.0)

# 主題配色 本手冊線寬
theme = replace(
    themes.monochrome,
    background_color="#ffffff",
    ic_linewidth=2.6,
    budget_linewidth=2.6,
    eq_markersize=5.0,
)

cvs = Canvas(
    x_max=20,
    y_max=15,
    x_label="$x$",
    y_label="$y$",
    theme=theme,
)
cvs.add_utility(model, levels=levels.around(eq.utility, n=3))
cvs.add_budget(2.0, 3.0, 30.0, fill=True)
cvs.add_equilibrium(eq)
cvs.save("theme_monochrome.png")
```

<figure class="ev-fig" markdown>

![`monochrome` 主題](../../../assets/utility-viz/agora/themes/monochrome.svg){ .ev-figure-sm }

<a class="ev-download" href="../../../assets/utility-viz/agora/themes/monochrome.zh-TW.py" download aria-label="下載生圖原始檔"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下載生圖原始檔</span></a>

<figcaption markdown>`monochrome` 主題</figcaption>

</figure>

```python
from dataclasses import replace

from utility_viz import Canvas, levels, solve, themes
from utility_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.5, beta=0.5)
eq = solve(model, px=2.0, py=3.0, income=30.0)

# 主題配色 本手冊線寬
theme = replace(
    themes.presentation,
    background_color="#ffffff",
    ic_linewidth=2.6,
    budget_linewidth=2.6,
    eq_markersize=5.0,
)

cvs = Canvas(
    x_max=20,
    y_max=15,
    x_label="$x$",
    y_label="$y$",
    theme=theme,
)
cvs.add_utility(model, levels=levels.around(eq.utility, n=3))
cvs.add_budget(2.0, 3.0, 30.0, fill=True)
cvs.add_equilibrium(eq)
cvs.save("theme_presentation.png")
```

<figure class="ev-fig" markdown>

![`presentation` 主題](../../../assets/utility-viz/agora/themes/presentation.svg){ .ev-figure-sm }

<a class="ev-download" href="../../../assets/utility-viz/agora/themes/presentation.zh-TW.py" download aria-label="下載生圖原始檔"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下載生圖原始檔</span></a>

<figcaption markdown>`presentation` 主題</figcaption>

</figure>

## 自訂主題

<!-- api: agora.utility_viz.guides_themes_2 -->

`Theme` 保存圖形元素的顏色、線寬與樣式預設值。未指定的欄位使用類別預設值；繪圖方法明確收到的樣式參數優先於主題。

`Theme` 也包含射線、拗折點、補償預算線與價格效果箭頭的顏色和線寬。`axis_stroke`、`drop_stroke`、`projection_stroke`、`guide_stroke` 與 `box_stroke` 保存其他線條的預設值；標記、標籤、填色及圖例則由 `Marker`、`Label`、`Fill` 與 `Legend` 屬性提供（詳見[樣式](canvas.md#sec-styles)）。

## 設定檔

<!-- api: agora.utility_viz.guides_themes_3 -->

`Config.load()` 讀取 TOML 檔案並回傳 `Config`。`use()` 將其設為後續圖形的預設設定；`reset()` 恢復內建預設值。

### 教學：統一樣式

同一份講義或論文的圖形，通常要共用相同的顏色與線條。與其在每個 `Canvas` 重複傳入參數，不如把樣式寫在專案根目錄的 `utility-viz.toml`，讓 Python 與命令列讀取同一份設定。

+ *建立範本。*在專案根目錄執行下列指令，會產生含註解的 `utility-viz.toml`，列出每個區段可用的名稱與欄位：

  ```bash
  utility-viz init
  ```

  範本中的設定預設都是註解；只保留需要修改的項目即可，其餘可以刪除。

+ *選擇基底主題。*`base` 指定起始的內建主題（[內建主題](themes.md#tab-themes)），其餘設定都在它之上覆寫：

  ```toml
  base = "paper"
  ```

+ *覆寫顏色與樣式。*只寫出要改的欄位：

  ```toml
  [color]
  ic = "#1B4F72"
  eq = "#C0392B"

  [stroke.budget]
  width = 1.6
  style = "dashed"

  [marker.eq]
  size = 5

  [label.point]
  fontsize = 11
  position = "right"
  ```

  區段名稱對應主題屬性：`[color]` 的 `ic` 對應 `ic_color`，`[stroke.budget]` 對應 `theme.budget_stroke`；區段內的欄位就是 `Stroke`、`Marker`、`Label`、`Fill`、`Legend` 的參數（詳見[樣式](canvas.md#sec-styles)）。字型寫在 `[font]` 的 `text` 與 `math`。省略的欄位保留基底主題的值。

+ *在 Python 中套用。*在建立任何圖形之前載入一次：

  ```python
  from utility_viz import Config

  # 預設讀 ./utility-viz.toml
  Config.load().use()
  ```

  此後建立的 `Canvas`、`Figure`、`DemandDiagram` 與 `EdgeworthBox` 都使用這組設定；呼叫 `Config.reset()` 可恢復內建預設值。

+ *在命令列套用。*`utility-viz plot` 會自動讀取目前目錄的 `utility-viz.toml`；要使用其他檔案時，以 `--config` 指定設定檔：

  ```bash
  utility-viz plot --config utility-viz.toml --model cobb-douglas \
    --px 2 --py 3 --income 30 --output figure.png
  ```

設定的優先順序由高到低為：直接傳入 `Canvas` 或繪圖方法的參數、設定檔、基底主題。例如 `Canvas(theme=themes.default)` 會略過設定檔中的主題。

設定檔寫錯時，`Config.load()` 會拋出 `InvalidParameterError`，並列出可用的名稱。例如把 `[stroke.budget]` 誤寫成 `[stroke.budgt]`：

```text
utility-viz.toml: [stroke.budgt]: no such setting (choose: axis, box, budget, ...)
```

### 設定檔查找順序

<span id="sec-config-lookup"></span>

<!-- api: agora.utility_viz.guides_themes_4 -->

尋找並讀取設定檔；找不到時不會出錯。

`Config.load()`、`Config.discover()` 與 `utility-viz plot` 依下列順序決定設定檔：

+ 明確指定的路徑（`Config.load("file.toml")` 或 `--config`）：檔案必須存在，且只讀取該檔；
+ 目前目錄（或 `directory=`）中的 `utility-viz.toml`；
+ 舊的 `econ-viz.toml`，並發出棄用警告；
+ 內建預設值。

兩個檔案同時存在時，以 `utility-viz.toml` 為準，舊檔會被略過並發出警告。兩個函式只在找不到檔案時有差異：`Config.load()` 與 1.x 相同，拋出 `InvalidParameterError`（"config file not found"）；`Config.discover()` 則回傳內建預設值。`utility-viz init --migrate` 可將舊檔轉為 `utility-viz.toml`（詳見[建立設定檔](../getting-started/cli.md#sec-cli-init)）。
