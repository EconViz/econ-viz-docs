---
seo_title: "線性市場"
---

# 線性市場

<span id="sec-markets"></span>

## 直線

需求或供給曲線以反函數形式表示為直線：

$$
p = a + b Q
$$

其中 $a$ 為價格截距，$b$ 為斜率（需求 $b < 0$，供給 $b > 0$）。價格一律在縱軸、數量在橫軸，沿用 [Marshall (1890)](../project/references.md#marshall1890) 的畫法。離散的逐單位表（詳見[離散市場](discrete.md#sec-discrete)）與由個人曲線加總而成的分段線性市場曲線（詳見[由個人加總市場曲線](aggregation.md#sec-aggregation)）不是單一直線。

<!-- api: agora.principle_viz.guides_markets_1 -->

價格—數量平面上的直線，內部儲存為 $A p + B Q + C = 0$，因此也能表示水平線與垂直線。`from_inverse(a, b)` 建立 $p = a + b Q$；`from_standard(A, B, C)` 建立 $A p + B Q + C = 0$。套件根目錄另以 `line_from_inverse()` 與 `line_from_standard()` 提供這兩個建構函式。

```python
from principle_viz import line_from_inverse, line_from_standard

demand = line_from_inverse(10.0, -1.0)
# 6.0 7.0
print(demand.q_at(4), demand.p_at(3))
# 10.0 10.0
print(demand.p_intercept(), demand.q_intercept())
# (10.0, -1.0)
print(line_from_standard(1, 1, -10).to_inverse())
```

$(A, B, C) = (1, 1, -10)$ 與 $p = 10 - Q$ 等價。

水平線沒有 $Q(p)$，垂直線沒有 $p(Q)$；呼叫對應的方法會拋出 `NonInvertibleLineError`。

## 均衡

<!-- api: agora.principle_viz.guides_markets_2 -->

兩條直線的交點，回傳 `EquilibriumResult`（詳見[快速開始](../quickstart.md#sec-quickstart)）。兩線平行時拋出 `ParallelLinesError`，重合時拋出 `CoincidentLinesError`。

```python
from principle_viz import solve_equilibrium

eq = solve_equilibrium(demand, line_from_inverse(2.0, 1.0))
print(eq)
# EquilibriumResult(q_star=4.0, p_star=6.0,
#                   is_valid_market=True, notes=())
```

由 $10 - Q = 2 + Q$ 得均衡數量 4、均衡價格 6，`is_valid_market` 為 `True`，`notes` 為空。

## 比較靜態

<span id="sec-shifts"></span>

<!-- api: agora.principle_viz.guides_markets_3 -->

以反函數形式描述一條曲線的移動：`delta_intercept` 為正時向上平移、為負時向下，`delta_slope` 旋轉曲線。情境可同時移動需求、供給或兩者。兩者都位於 `principle_viz.core.shifts`。

需求增加使需求截距上升；供給增加則使供給截距*下降*，因為賣方在每個數量下都願意接受較低的價格。

<!-- api: agora.principle_viz.guides_markets_4 -->

求解移動前後的市場，結果包含下列欄位：

```python
from principle_viz import comparative_statics
from principle_viz.core.shifts import ShiftScenario, ShiftSpec

up = ShiftScenario(demand_shift=ShiftSpec(delta_intercept=3.0))
result = comparative_statics(demand, supply, up)
new = result.shifted_equilibrium
# 5.5 7.5
print(new.q_star, new.p_star)
# right up
print(result.direction_q, result.direction_p)
```

<!-- api: agora.principle_viz.guides_markets_5 -->

畫出移動的曲線、兩個均衡點，以及由舊均衡指向新均衡的虛線箭頭。在 `add_curves()` 中將原曲線命名為 $D_0$ 與 $S_0$。需求增加的結果如[需求增加。](markets.md#fig-shifts)，供給減少的結果如[供給減少。](markets.md#fig-shift-supply)。

```python
fig = MarketFigure(
    x_max=12, y_max=14, title="Increase in Demand"
)
fig.add_curves(
    demand,
    supply,
    q_max=10,
    demand_label="$D_0$",
    supply_label="$S_0$",
)
fig.add_comparative_statics(result, q_max=10)
fig.finalize()
```

<span id="fig-shifts"></span>

![需求增加。](../../../assets/principle-viz/agora/markets/shift_demand_increase.svg){ .ev-figure-sm }

<span id="fig-shift-supply"></span>

![供給減少。](../../../assets/principle-viz/agora/markets/shift_supply_decrease.svg){ .ev-figure-sm }

## 例外

<span id="sec-errors"></span>

套件拋出的所有例外都繼承自 `principle_viz.exceptions` 中的 `PrincipleVizError`，捕捉它即可一併處理。0.10.0 版以前的名稱 `PrincipleEconError` 是同一個類別。各例外的拋出時機如[例外類別](markets.md#tab-errors)。

<span id="tab-errors"></span>

| 例外 | 拋出時機 |
| --- | --- |
| `LineError` | 無法建立或轉換直線 |
| `NonInvertibleLineError` | 對水平線求 $Q(p)$，或對垂直線求 $p(Q)$ |
| `ParallelLinesError` | 需求與供給沒有交點 |
| `CoincidentLinesError` | 需求與供給是同一條直線 |
| `PolicyError` | 租稅、補貼、價格管制或貿易情境無效 |
| `DiscreteMarketError` | 離散逐單位表無效（詳見[離散市場](discrete.md#sec-discrete)） |
| `AggregationError`、`PiecewiseLinearError` | 個人曲線無法加總，或價格超出分段曲線範圍（詳見[由個人加總市場曲線](aggregation.md#sec-aggregation)） |
| `PPFError` | 生產可能曲線無效（詳見[生產可能曲線](ppf.md#sec-ppf)） |
