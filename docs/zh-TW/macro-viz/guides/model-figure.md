---
seo_title: "模型與圖形"
---

# 模型與圖形

<span id="sec-model-figure"></span>

## 先有模型，再有圖形

每個主題都有兩層。

- *模型*是凍結的 dataclass，輸入會被檢查，方法回答問題：`KeynesianCross.equilibrium`、`ISLM.equilibrium`、`Solow.steady_state`。模型從不匯入繪圖器，輸入有誤時引發 `ValidationError`。
- *比較*是 `analyze_*` 函式的回傳值：基準模型、變動後的模型、各項變動的方向（`Direction.UP`、`DOWN`、`NONE`）與新均衡。入口函式有 `analyze_autonomous_shift`、`analyze_fiscal_policy`、`analyze_demand_shock`、`analyze_change` 與 `compare`。
- *繪圖函式*在 `macro_viz.visuals`，把模型或比較轉成 `mosaickit` 的 `Canvas`：`islm_canvas(shift)`、`adas_canvas(model)`。繪圖函式裡沒有方程式，只放置模型算出的結果。

```python
from macro_viz.adas import (
    AggregateDemand,
    AggregateSupply,
    ASADModel,
    analyze_demand_shock,
)
from macro_viz.visuals import adas_canvas

supply = AggregateSupply.linear(1.0, 100, 0.6)
demand = AggregateDemand(80, 45, 1)
model = ASADModel(supply, demand)

shock = analyze_demand_shock(model, autonomous=115)
shock.output_direction  # Direction.UP
adas_canvas(shock).save("adas_demand_shock.svg")
```

<span id="fig-model-demand-shock"></span>

<figure class="ev-fig" markdown>

![AS-AD 中的需求衝擊](../../../assets/macro-viz/adas/adas_demand_shock.zh-TW.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/adas/adas.py" download aria-label="下載生圖原始檔"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下載生圖原始檔</span></a></div>

<figcaption markdown>AS-AD 中的需求衝擊</figcaption>

</figure>

## 共同選項

<span id="sec-options"></span>

單面板的繪圖函式都回傳 `Canvas`，並接受相同的關鍵字選項。在這些頁面的簽名中，它們以名稱出現，轉交給其他函式時則寫成 `**options`。

<!-- api: macro_viz.guides_model_figure_1 -->

連動面板的繪圖函式回傳 `CanvasGrid`，並以版面選項取代上述選項（參見 [連動面板](panels.md#sec-panels)）。

## 套件結構

<span id="tab-layout"></span>

| 位置 | 內容 |
| --- | --- |
| `macro_viz/<topic>/` | 模型與比較，不依賴繪圖器（`keynesian`、`money`、`adas`、`islm`、`growth`、`labor`、`open_economy`、`panels`） |
| `macro_viz/visuals/` | 回傳 `Canvas` 的繪圖函式；`_theory.py` 與 `_kit.py` 是共用的工具 |
| `macro_viz/locale/labels.json` | 所有內建文字，依語言與編號索引 |
| `macro_viz/themes.py`, `config.py` | manual 主題與 `[macro]` 設定結構 |
| `macro_viz/animation.py` | 選用的 GIF 與隨參數變化的動畫 SVG |
| `examples/scripts/` | 每個主題一個腳本；這些頁面的圖形 |

## 圖層編號

繪圖函式為每個圖層指定穩定的編號，例如 `macro.islm.is`、`macro.islm.is.shifted` 或 `macro.islm.equilibrium.shifted.label`。標籤表與動畫都以這些編號定位：動畫依編號在各幀之間對應圖層（參見 [動畫](animation.md#sec-animation)）。

## 與其他套件的關係

- `mosaickit` 負責所有繪製：場景、圖層、主題、標籤位置、格線與輸出。
- `bezierkit` 提供連動面板中轉動記號的曲線幾何。
- `kinetickit` 負責動畫，只隨 `animation` 選項安裝。
