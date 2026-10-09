---
seo_title: "价格管制"
---

# 价格管制

<span id="sec-controls"></span>

低于均衡价格的价格上限，或高于均衡价格的价格下限，会*产生约束*：市场无法结清，成交量等于管制价格下需求量与供给量中较小者。

<!-- api: agora.principle_viz.guides_controls_1 -->

位于 `control_price` 的上限（`CEILING`）或下限（`FLOOR`），位于 `principle_viz.core.controls`。

<!-- api: agora.principle_viz.guides_controls_2 -->

管制下的市场，返回 `PriceControlResult`：

```python
from principle_viz import evaluate_price_control
from principle_viz.core.controls import (
    PriceControlScenario,
    PriceControlType,
)

scenario = PriceControlScenario(PriceControlType.CEILING, 4.0)
ceiling = evaluate_price_control(demand, supply, scenario)
print(
    ceiling.is_binding,
    ceiling.traded_quantity,
    ceiling.shortage,
)
# True 2.0 4.0
```

上限高于均衡价格（例如 7）时，`is_binding` 为 `False`。

<!-- api: agora.principle_viz.guides_controls_3 -->

画出管制线并命名为 "Price ceiling" 或 "Price floor"，在价格轴上标出 $p_c$。有约束时另标出 $Q_d$ 与 $Q_s$，并以括号标示差额：上限下方为 "Shortage"，下限上方为 "Surplus"。`gap_brace="axis"` 改在数量轴下方标示（参见[有约束的价格上限。](controls.md#fig-ceiling)、[有约束的价格下限。](controls.md#fig-floor)）。

<span id="fig-ceiling"></span>

![有约束的价格上限。](../../../assets/principle-viz/agora/controls/ceiling.svg){ .ev-figure-sm }

<span id="fig-floor"></span>

![有约束的价格下限。](../../../assets/principle-viz/agora/controls/floor.svg){ .ev-figure-sm }

`outcome_from_control()` 将结果转为市场结果，可交给[福利](welfare.md#sec-welfare)的福利函数（参见[上限为 3.5 时的福利。](controls.md#fig-ceiling-welfare)）：

```python
from principle_viz.welfare.surplus import (
    compare_surplus,
    outcome_from_control,
    outcome_from_equilibrium,
)

eq = solve_equilibrium(demand, supply)
baseline = outcome_from_equilibrium(eq)
controlled = outcome_from_control(ceiling)
delta = compare_surplus(demand, supply, baseline, controlled)
fig.add_price_control(ceiling)
fig.add_welfare(delta.policy)
```

<span id="fig-ceiling-welfare"></span>

![上限为 3.5 时的福利。](../../../assets/principle-viz/agora/controls/ceiling_welfare.svg){ .ev-figure-sm }

价格上限下，无谓损失为未成交的交易利益；部分剩余由卖方转移给买方。
