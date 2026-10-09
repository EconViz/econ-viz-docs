---
seo_title: "劳动与可贷资金"
---

# 劳动与可贷资金

<span id="sec-factor"></span>

## 最低工资

<!-- api: agora.principle_viz.guides_factor_markets_1 -->

设有工资下限的竞争劳动市场。`MinimumWageResult` 包含 `equilibrium`、`minimum_wage`、`is_binding`、`labor_demanded`、`labor_supplied`、`employment`（两者中较小者）、`unemployment`（两者之差）与 `wage_bill`。

```python
from principle_viz import analyze_minimum_wage

labor_demand = line_from_inverse(12, -1)
labor_supply = line_from_inverse(2, 1)
labor = analyze_minimum_wage(
    labor_demand,
    labor_supply,
    minimum_wage=9,
)
# 3.0 4.0
print(labor.employment, labor.unemployment)
```

<!-- api: agora.principle_viz.guides_factor_markets_2 -->

以价格下限的方式绘制工资下限（详见[价格管制](controls.md#sec-controls)）："Minimum wage" 线、工资轴上的 $w_{\min}$，有约束时另标出 $L_d$ 与 $L_s$ 及 "Unemployment" 括号。坐标轴命名为 $L$ 与 $w$，曲线命名为 $D_L$ 与 $S_L$（参见[有约束的最低工资。](factor-markets.md#fig-minimum-wage)）：

```python
fig = MarketFigure(x_max=11, y_max=14, x_label="L", y_label="w")
fig.add_curves(
    labor_demand,
    labor_supply,
    q_max=10,
    demand_label="$D_L$",
    supply_label="$S_L$",
)
fig.add_minimum_wage(labor)
```

<span id="fig-minimum-wage"></span>

![有约束的最低工资。](../../../assets/principle-viz/agora/factor/minimum_wage.svg){ .ev-figure-sm }

`labor_demanded` 为 3，`labor_supplied` 为 7，`employment` 为 3，`unemployment` 为 4。

## 可贷资金

<!-- api: agora.principle_viz.guides_factor_markets_3 -->

储蓄（供给）与投资（需求）以数量衡量的水平移动。政府借款（不得为负）加入可贷资金的需求。

<!-- api: agora.principle_viz.guides_factor_markets_4 -->

移动前后的可贷资金市场：`baseline_equilibrium`、`shifted_equilibrium`、`shifted_savings`、`shifted_investment_demand`、`private_investment_after`、`interest_rate_change`，以及 `crowding_out`，即利率上升所挤出的民间投资。

```python
from principle_viz import (
    LoanableFundsScenario,
    analyze_loanable_funds,
)

savings = line_from_inverse(2, 0.5)
investment = line_from_inverse(12, -0.5)
scenario = LoanableFundsScenario(government_borrowing=4)
funds = analyze_loanable_funds(savings, investment, scenario)
# 1.0 2.0
print(funds.interest_rate_change, funds.crowding_out)
```

`interest_rate_change` 为 1.0，`crowding_out` 为 2.0。

<!-- api: agora.principle_viz.guides_factor_markets_5 -->

画出移动后的曲线并命名为 $D_1$ 或 $S_1$，以及两个均衡点与其间的移动。价格轴命名为 $r$（参见[政府借款挤出民间投资。](factor-markets.md#fig-loanable-funds)）。

<span id="fig-loanable-funds"></span>

![政府借款挤出民间投资。](../../../assets/principle-viz/agora/factor/loanable_funds.svg){ .ev-figure-sm }
