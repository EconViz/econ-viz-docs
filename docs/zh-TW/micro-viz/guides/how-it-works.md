---
seo_title: "運作方式"
---

# 運作方式

<span id="sec-how"></span>

## 先模型，後圖形

每個主題分兩層。

- **模型**是凍結的 dataclass：輸入會檢查，方法回答問題，例如 `CubicCost.marginal_cost`、`Monopolist.solve`、`IndustrySupply.quantity`。模型**不引入**任何繪圖套件，輸入不合法時丟出自己的錯誤（`CostError`、`CompetitionError`、`UncertaintyError`）。
- `micro_viz.visuals` 裡的**繪圖函式**把模型結果變成 `mosaickit` 的 `Canvas`，例如 `unit_cost_canvas(analysis)`、`monopoly_canvas(outcome, analysis)`。繪圖函式裡沒有方程式，只負責擺放模型算出來的東西。

```python
from micro_viz import CubicCost, LinearDemand, Monopolist, analyze_costs, monopoly_canvas

demand = LinearDemand(intercept=30, slope=2)
cost = CubicCost(20, 6, -1.5, 0.15)
outcome = Monopolist(demand, cost).solve()
analysis = analyze_costs(cost, output_range=(1, 10))

monopoly_canvas(outcome, analysis, profit=True).save("monopoly.svg")
```

## 套件結構

| 位置 | 內容 |
| --- | --- |
| `micro_viz/<主題>.py`、`micro_viz/<主題>/` | 模型與求解器，不含繪圖 |
| `micro_viz/visuals/` | 回傳 `Canvas` 的繪圖函式；`plane.py` 是平面圖的小工具（`Plane`） |
| `micro_viz/locale/labels.json` | 所有內建文字，依編號與語言存放 |
| `micro_viz/theme.py`、`config.py` | 主題與 `[micro]` 設定的結構 |
| `micro_viz/animation/` | 選用的參數動畫 |
| `examples/scripts/` | 每個主題一支腳本，也是本文件的圖 |

## 多面板圖形

多個面板的圖（市場與廠商、多廠獨占、產業供給）使用 `mosaickit` 的 `CanvasGrid`。橫跨面板間隙的虛線是 `GridLink`，從一格的某點連到下一格的某點，所以價格或邊際成本的水準線是**連續**的一條。

## 與其他套件的關係

- **mosaickit** 負責所有繪製：場景、圖層、主題、標籤位置、網格與輸出。`micro-viz` 執行時只依賴它。
- **bezierkit** 提供曲線幾何。`micro-viz` 目前不直接引入；當圖形需要它的公開幾何 API（由角度決定的旋轉連接線）時才加入依賴。
- **kinetickit** 讓圖形動起來，只隨 `animation` 選用依賴安裝（見[動畫](animation.md#sec-animation)）。
- **glyphkit** 負責動畫 SVG 的文字，經由 mosaickit 引入。
- **utility-viz** 與 **principle-viz** 負責消費者理論與入門市場圖，這裡可以使用它們的物件，但 `micro-viz` 不重寫。
