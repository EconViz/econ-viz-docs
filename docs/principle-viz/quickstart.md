---
seo_title: "principle-viz Quick Start"
description: "Solve a linear market equilibrium, compare a per-unit tax, and draw a supply and demand figure with principle-viz."
---

# Quick Start

Every output below comes from running the code with principle-viz 0.10.0.

## Solve and draw a market

Demand is `P = 10 - Q` and supply is `P = 2 + Q`. `Line.from_inverse(intercept, slope)` builds a line from its
inverse form `P = intercept + slope * Q`.

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

Output:

```text
EquilibriumResult(q_star=4.0, p_star=6.0, is_valid_market=True, notes=())
```

![Basic equilibrium figure](../assets/principle-viz/basic_equilibrium.png){ width="360" }

## Compare a tax

`compare_tax_scenario` solves the market before and after the tax. This one is a per-unit tax of 1 on producers.

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

Output:

```text
before tax: Q = 4.0, P = 6.0
after tax:  Q = 3.5
buyers pay 6.5, sellers keep 5.5
tax revenue = 3.5
```

`TaxType` also offers `FIXED_TAX` and `AD_VALOREM_TAX`; `TaxOn` is `CONSUMER` or `PRODUCER`. To draw the tax on a
figure, use `MarketFigure.add_tax_transform`.

## From the command line

The same market, solved without writing Python:

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

The tax scenario above is `principle-viz tax` with `--tax-type per_unit --amount 1 --tax-on producer`; it prints
the baseline and post-tax equilibrium as JSON.
