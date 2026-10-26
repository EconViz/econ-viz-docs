---
seo_title: "設定"
---

# 設定

<span id="sec-settings"></span>

`macro-viz` 讀取共用的 `econ-viz.toml`。`mosaickit` 負責解析並檢查檔案；`macro-viz` 只宣告 `[macro]` 之下接受哪些項目。

<!-- api: macro_viz.guides_settings_1 -->

沒有寫的鍵保留內建預設，完全沒有檔案時，圖形使用內建的顏色。

```python
from macro_viz import Config

Config.load("econ-viz.toml").use()
```

```toml
base = "manual"            # 共用外觀：白底黑線

[font]
text = "serif"
math = "texgyrepagella-math.otf"

[fonts]
serif = ["texgyrepagella-regular.otf", "texgyrepagella-italic.otf"]

[macro]
language = "en"            # en, zh-TW 或 zh-CN

[macro.stroke]
curve = 3.5                # 點

[macro.text]
scale = 1.5                # 所有文字大小的倍數
```

這些頁面的圖形由 `config/econ-viz.toml`、`config/econ-viz.zh-TW.toml` 與 `config/econ-viz.zh-CN.toml` 畫出（[下載範例](#sec-download)），三者只有字型與語言不同。

## 共用的鍵

`base`、`[font]`、`[fonts]`、`background`、`axis` 與 `label` 由所有 EconViz 套件共用，說明見 `mosaickit`。沒有深色主題：背景一律是白色。

## `[macro]` 各表

<span id="sec-macro-tables"></span>

<span id="tab-macro"></span>

| 鍵 | 意義 | 預設值 |
| --- | --- | --- |
| `palette` | 只用於 macro-viz 的色彩模型；優先於 `base` | base 的設定 |
| `language` | 內建圖形文字的語言：`en`、`zh-TW` 或 `zh-CN` | `en` |
| `color.<role>` | 角色的顏色：`background`、`axis`、`label`、`primary`、`secondary`、`tertiary` | 主題的設定 |
| `stroke.curve` | 粗理論曲線的線寬（點） | 3.5 |
| `stroke.shifted` | 變動後曲線的線寬（細實線） | 1.0 |
| `stroke.arrow` | 移動箭頭的線寬（實線，比曲線細） | 1.0 |
| `stroke.guide` | 點狀輔助線的線寬 | 1.0 |
| `stroke.line45` | 單面板圖形中 45 度線的線寬 | 0.8 |
| `stroke.diagonal` | 連動面板中 45 度線的線寬 | 0.6 |
| `stroke.link` | 連動面板之間虛線投影的線寬 | 0.7 |
| `marker.point` | 均衡點圓點的直徑（點） | 6.5 |
| `text.scale` | 所有文字大小的倍數 | 1.0 |
| `label.<group>.<side>` | 移動一組標籤（參見 [預設移動標籤](labels.md#sec-nudges)） | 無 |

顏色指定主題的角色，所以 `manual` 是黑白，彩色主題則有顏色。變動後的曲線一律是細實線，平行移動是直線箭頭，彎曲箭頭只代表轉動；設定可以改線寬，但不會改這些慣例。

## 程式碼中的主題

<!-- api: macro_viz.guides_settings_2 -->

`get_theme(name)` 依共用主題名稱（如 `"manual"`）建出 `mosaickit` 主題，包含 macro 的各個角色（`macro.curve.primary`、`macro.curve.primary.shifted`、`macro.movement`、`macro.point`、`macro.guide` 等）。`list_themes()` 列出名稱。`MANUAL_THEME` 是黑白主題。

```python
from macro_viz.themes import MANUAL_THEME, list_themes

list_themes()
MANUAL_THEME.resolve("macro.movement", fallback_category="path").stroke
```

<span id="sec-download"></span>

## 範例

範例壓縮檔包含 `examples/scripts/<topic>/*.py`、範例數字 `examples.toml` 與三份設定檔。每個腳本都接受 `--output`、`--config`、`--data` 與 `--suffix`；`--help` 會列出。腳本裡沒有寫死任何數字：數字來自 `examples.toml`。

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/macro-viz-examples.zip" download aria-label="下載範例"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下載範例</span></a></div>

```bash
uv run python examples/scripts/islm/islm.py --output out --config examples/econ-viz.toml
```
