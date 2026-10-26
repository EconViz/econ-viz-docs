---
seo_title: "模型與圖形"
---

# 模型與圖形

<span id="sec-model-figure"></span>

## 先模型，後圖形

每個主題分成兩層。

- *模型*是凍結的資料類別（frozen dataclass），檢查輸入，並以方法回答問題：`CubicCost.marginal_cost`、`Monopolist.solve`、`IndustrySupply.quantity`。模型從不引入繪圖器，輸入不當時拋出自己的例外（`CostError`、`CompetitionError`、`UncertaintyError`）。
- `micro_viz.visuals` 中的*繪圖函式*把模型結果轉成 `mosaickit` 的 `Canvas`：`unit_cost_canvas(analysis)`、`monopoly_canvas(outcome, analysis)`。繪圖函式不含方程式，只安置模型算出的內容。

```python
from micro_viz import (
    CubicCost,
    LinearDemand,
    Monopolist,
    analyze_costs,
    monopoly_canvas,
)

demand = LinearDemand(intercept=30, slope=2)
cost = CubicCost(20, 6, -1.5, 0.15)
outcome = Monopolist(demand, cost).solve()
analysis = analyze_costs(cost, output_range=(1, 10))

monopoly_canvas(outcome, analysis, profit=True).save(
    "monopoly.svg"
)
```

## 共同選項

<span id="sec-options"></span>

每個繪圖函式都回傳 `Canvas`，並接受相同的關鍵字選項。本頁的函式簽名以 `**options` 表示它們。

<!-- api: micro_viz.guides_model_figure_1 -->

畫多欄的繪圖函式以 `titles`（每欄一個）取代 `title`。

## 套件結構

<span id="tab-layout"></span>

| 位置 | 內容 |
| --- | --- |
| `micro_viz/<topic>.py`、`micro_viz/<topic>/` | 模型與求解器，不含繪圖 |
| `micro_viz/visuals/` | 回傳 `Canvas` 的繪圖函式；`plane.py` 是平面圖的小工具組（`Plane`） |
| `micro_viz/locale/labels.json` | 所有內建文字，依編號與語言整理 |
| `micro_viz/theme.py`、`config.py` | 主題與 `[micro]` 設定結構 |
| `micro_viz/animation/` | 選用的參數動畫 |
| `examples/scripts/<topic>/` | 腳本，每個主題一個資料夾；本頁的圖形 |

## 圖層編號

繪圖函式替每個圖層指定穩定的編號，格式為 `micro.<prefix>.<kind>.<n>`，例如 `micro.cost.avc.label`。設定檔的逐圖標籤表以這些編號為對象（參見 [標籤與位置](labels.md#sec-labels)），動畫也以它們在影格之間配對圖層（參見 [動畫](animation.md#sec-animation)）。

## 多欄圖

有數欄的圖（市場與廠商、多廠房獨占、產業供給）使用 `mosaickit` 的 `CanvasGrid`。橫跨欄間空隙的虛線是從一格中的點連到下一格中的點的 `GridLink`，所以價格或邊際成本的水準線保持連續。

## 與其他套件的關係

- `mosaickit` 負責繪製一切：場景、圖層、主題、標籤位置、格狀排版與輸出。`micro-viz` 執行時只依賴它。
- `bezierkit` 提供曲線幾何。`micro-viz` 不直接引入它；圖形需要其公開的幾何 API 時才加入依賴。
- `kinetickit` 讓圖形成為動畫，只隨 `animation` 選用依賴安裝（參見 [動畫](animation.md#sec-animation)）。
- `utility-viz` 與 `principle-viz` 負責消費者理論與入門的市場圖。它們的物件可以搭配使用，`micro-viz` 不重寫它們。
