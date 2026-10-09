---
seo_title: "Market curves from individuals"
---

# Market curves from individuals

<span id="sec-aggregation"></span>

A market curve is the horizontal sum of the individual curves: at each price,
market quantity is the sum of the quantities every buyer (or seller) chooses
at that price. A buyer buys nothing above the choke price and a seller sells
nothing below the minimum price. The market curve of linear individuals is
piecewise linear, with a kink where each additional individual enters.

## Summing linear curves

<!-- api: agora.principle_viz.guides_aggregation_1 -->

Sum downward-sloping (demand) or upward-sloping (supply) individual lines.
The supply sum runs from the lowest minimum price up to `p_max`. Curves of
the wrong slope raise `AggregationError`.

<!-- api: agora.principle_viz.guides_aggregation_2 -->

A demand or supply curve through `points` $(Q, p)$, ordered by quantity.
If the first point has $Q = 0$, quantity is zero at prices beyond it.

```python
from principle_viz import (
    line_from_inverse,
    market_demand,
    market_supply,
)

# p = 10 - 2Q
a = line_from_inverse(10, -2)
# p = 6 - 0.5Q
b = line_from_inverse(6, -0.5)
demand = market_demand((a, b))
# ((0.0, 10.0), (2.0, 6.0), (17.0, 0.0))
print(demand.points)
# 7.0 = Q_A + Q_B = 3 + 4
print(demand.q_at(4))
```

Buyer B enters at a price of 6, giving the kink $(2, 6)$. At a price of 4,
$Q_A = 3$ and $Q_B = 4$, so market demand is 7.

<!-- api: agora.principle_viz.guides_aggregation_3 -->

The exact market equilibrium, solved segment by segment, and the consumer
and producer surplus at it, integrated along price.

```python
from principle_viz import (
    piecewise_surplus,
    solve_piecewise_equilibrium,
)

c = line_from_inverse(2, 1)
d = line_from_inverse(5, 0.5)
supply = market_supply((c, d), p_max=10)
eq = solve_piecewise_equilibrium(demand, supply)
# 3.818 5.273
print(round(eq.q_star, 3), round(eq.p_star, 3))
cs, ps = piecewise_surplus(demand, supply, eq)
```

`piecewise_surplus()` returns the consumer and producer surplus integrated
along price.

## Summing discrete schedules

`DiscreteDemand.combine(*schedules)` merges every buyer's reservation prices
into one market schedule, highest first; `DiscreteSupply.combine()` merges
unit costs, lowest first. Equal values remain separate units, and the result
works with `solve_discrete_equilibrium()` ([Discrete markets](discrete.md#sec-discrete)). The output is
shown in [Combining two discrete demand schedules.](aggregation.md#fig-discrete-market-demand).

```python
from principle_viz import DiscreteDemand

first = DiscreteDemand((10, 7, 4))
second = DiscreteDemand((8, 5, 2))
market = DiscreteDemand.combine(first, second)
print(market.values)
# (10.0, 8.0, 7.0, 5.0, 4.0, 2.0)
```

## Aggregation figures

<!-- api: agora.principle_viz.guides_aggregation_4 -->

One panel per individual, then the market, side by side and sharing the
price axis. `individuals` maps each name to a curve or schedule; the
curves are named $D_A$, $D_B$, ... and $D$ (or $S_A$, ..., $S$). Dashed
guides at `price` mark $Q_A$, $Q_B$ and $Q_A + Q_B = Q$.
`supply_aggregation_figure()` also needs `p_max`.

The returned `AggregationFigure` has `save()`, `hide()`, `show()`,
`configure_label()`, `layer_ids` and `label_ids`, like `MarketFigure`.

```python
from principle_viz import demand_aggregation_figure

fig = demand_aggregation_figure(
    {"A": a, "B": b},
    price=4,
    link_price=True,
)
fig.save("market_demand.png")
```

The output of `demand_aggregation_figure()` is shown in [Market demand as the horizontal sum.](aggregation.md#fig-market-demand).

<span id="fig-market-demand"></span>

![Market demand as the horizontal sum.](../../assets/principle-viz/agora/aggregation/market_demand.svg){ .ev-figure-sm }

<span id="fig-discrete-market-demand"></span>

![Combining two discrete demand schedules.](../../assets/principle-viz/agora/aggregation/discrete_market_demand.svg){ .ev-figure-sm }
