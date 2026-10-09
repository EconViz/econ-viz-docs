---
seo_title: "Price controls"
---

# Price controls

<span id="sec-controls"></span>

A price ceiling below the equilibrium price, or a floor above it, binds: the
market does not clear, and the quantity traded is the smaller of the
quantities demanded and supplied at the controlled price.

<!-- api: agora.principle_viz.guides_controls_1 -->

A `CEILING` or `FLOOR` at `control_price`, from
`principle_viz.core.controls`.

<!-- api: agora.principle_viz.guides_controls_2 -->

The controlled market, as a `PriceControlResult`:

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

A ceiling above the equilibrium price (for example 7) leaves `is_binding`
`False`.

<!-- api: agora.principle_viz.guides_controls_3 -->

Draw the control line, named "Price ceiling" or "Price floor", with $p_c$
on the price axis. A binding control also marks $Q_d$ and $Q_s$ and
braces the gap: "Shortage" below a ceiling, "Surplus" above a floor.
`gap_brace="axis"` braces it under the quantity axis instead (see
[A binding price ceiling.](controls.md#fig-ceiling) and [A binding price floor.](controls.md#fig-floor)).

<span id="fig-ceiling"></span>

![A binding price ceiling.](../../assets/principle-viz/agora/controls/ceiling.svg){ .ev-figure-sm }

<span id="fig-floor"></span>

![A binding price floor.](../../assets/principle-viz/agora/controls/floor.svg){ .ev-figure-sm }

`outcome_from_control()` turns the result into a market outcome for the
welfare functions of [Welfare](welfare.md#sec-welfare) (see [Welfare under a price ceiling of 3.5.](controls.md#fig-ceiling-welfare)):

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

![Welfare under a price ceiling of 3.5.](../../assets/principle-viz/agora/controls/ceiling_welfare.svg){ .ev-figure-sm }

Under a price ceiling, the deadweight loss is the surplus of the units that
are no longer traded, and part of the remaining surplus transfers from
sellers to buyers.
