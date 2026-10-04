---
seo_title: "principle-viz 快速開始"
description: "用 principle-viz 求解線性市場均衡、比較從量稅的效果，並畫出供需圖。"
---

# 快速開始

以下輸出都是以 principle-viz 0.10.0 實際執行程式碼的結果。

## 求解並繪製市場

需求為 `P = 10 - Q`，供給為 `P = 2 + Q`。`Line.from_inverse(intercept, slope)` 以反函數形式
`P = intercept + slope * Q` 建立直線。

```python
from principle_viz.core.equilibrium import solve_equilibrium
from principle_viz.core.line import Line
from principle_viz.plot.figure import MarketFigure

demand = Line.from_inverse(10.0, -1.0)  # P = 10 - Q
supply = Line.from_inverse(2.0, 1.0)  # P = 2 + Q
eq = solve_equilibrium(demand, supply)
print(eq)

fig = MarketFigure(x_max=12, y_max=12, title="Basic Equilibrium")
fig.add_curves(demand, supply, q_max=10)
fig.add_equilibrium(eq)
fig.finalize()
fig.save("basic_equilibrium.png")
fig.close()
```

輸出：

```text
EquilibriumResult(q_star=4.0, p_star=6.0, is_valid_market=True, notes=())
```

![基本均衡圖](../../assets/principle-viz/basic_equilibrium.png){ width="360" }

## 比較租稅效果

`compare_tax_scenario` 會分別求解課稅前後的市場。這裡是對生產者課徵每單位 1 的從量稅。

```python
from principle_viz.core.line import Line
from principle_viz.policy.analysis import compare_tax_scenario
from principle_viz.policy.tax import TaxOn, TaxScenario, TaxType

demand = Line.from_inverse(10.0, -1.0)
supply = Line.from_inverse(2.0, 1.0)

scenario = TaxScenario(tax_type=TaxType.PER_UNIT_TAX, amount=1.0, tax_on=TaxOn.PRODUCER)
result = compare_tax_scenario(demand, supply, scenario)

print(f"before tax: Q = {result.baseline_equilibrium.q_star}, P = {result.baseline_equilibrium.p_star}")
print(f"after tax:  Q = {result.post_tax.q_star}")
print(f"buyers pay {result.post_tax.consumer_price}, sellers keep {result.post_tax.producer_price}")
print(f"tax revenue = {result.post_tax.tax_revenue}")
```

輸出：

```text
before tax: Q = 4.0, P = 6.0
after tax:  Q = 3.5
buyers pay 6.5, sellers keep 5.5
tax revenue = 3.5
```

`TaxType` 另有 `FIXED_TAX`（定額）與 `AD_VALOREM_TAX`（從價）；`TaxOn` 為 `CONSUMER` 或 `PRODUCER`。
若要把租稅畫在圖上，請使用 `MarketFigure.add_tax_transform`。

## 命令列

不寫 Python 也能求解同一個市場：

```bash
principle-viz equilibrium \
  --demand-intercept 10 --demand-slope -1 \
  --supply-intercept 2 --supply-slope 1
```

```json
{
  "q_star": 4.0,
  "p_star": 6.0,
  "is_valid_market": true,
  "notes": []
}
```

上面的租稅情境對應 `principle-viz tax`，加上 `--tax-type per_unit --amount 1 --tax-on producer`，
會以 JSON 輸出課稅前後的均衡。
