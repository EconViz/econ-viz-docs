---
seo_title: "由个人加总市场曲线"
---

# 由个人加总市场曲线

<span id="sec-aggregation"></span>

市场曲线是个人曲线的水平加总：在每个价格下，市场数量等于所有买方（或卖方）在该价格下选择的数量之和。买方在阻绝价格以上不购买，卖方在最低价格以下不销售。线性个人曲线加总后的市场曲线是分段线性的，每多一人进入市场出现一个折点。

## 加总线性曲线

<!-- api: agora.principle_viz.guides_aggregation_1 -->

加总负斜率（需求）或正斜率（供给）的个人直线。供给加总由最低的最低价格延伸到 `p_max`。斜率方向不符时抛出 `AggregationError`。

<!-- api: agora.principle_viz.guides_aggregation_2 -->

通过 `points` $(Q, p)$ 的需求或供给曲线，点依数量排序。若第一点的 $Q = 0$，超出该点的价格下数量为零。

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

买方 B 在价格 6 进入市场，折点为 $(2, 6)$。价格为 4 时，$Q_A = 3$、$Q_B = 4$，市场需求量为 7。

<!-- api: agora.principle_viz.guides_aggregation_3 -->

逐段精确求解的市场均衡，以及沿价格积分得到的消费者剩余与生产者剩余。

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

`piecewise_surplus()` 返回沿价格积分得到的消费者剩余与生产者剩余。

## 加总离散表

`DiscreteDemand.combine(*schedules)` 将所有买方的保留价格合并为一张市场表，由高到低排列；`DiscreteSupply.combine()` 合并单位成本，由低到高排列。相同的数值保留为不同单位，合并结果可直接交给 `solve_discrete_equilibrium()`（详见[离散市场](discrete.md#sec-discrete)）。输出参见[合并两张离散需求表。](aggregation.md#fig-discrete-market-demand)。

```python
from principle_viz import DiscreteDemand

first = DiscreteDemand((10, 7, 4))
second = DiscreteDemand((8, 5, 2))
market = DiscreteDemand.combine(first, second)
print(market.values)
# (10.0, 8.0, 7.0, 5.0, 4.0, 2.0)
```

## 加总图

<!-- api: agora.principle_viz.guides_aggregation_4 -->

每位个人一个面板，最后是市场面板，左右并排并共用价格轴。`individuals` 将名称对应到曲线或逐单位表；曲线命名为 $D_A$、$D_B$……与 $D$（或 $S_A$……与 $S$）。在 `price` 处以虚线标出 $Q_A$、$Q_B$ 与 $Q_A + Q_B = Q$。`supply_aggregation_figure()` 另需 `p_max`。

返回的 `AggregationFigure` 与 `MarketFigure` 一样提供 `save()`、`hide()`、`show()`、`configure_label()`、`layer_ids` 与 `label_ids`。

```python
from principle_viz import demand_aggregation_figure

fig = demand_aggregation_figure(
    {"A": a, "B": b},
    price=4,
    link_price=True,
)
fig.save("market_demand.png")
```

`demand_aggregation_figure()` 的输出参见[水平加总的市场需求。](aggregation.md#fig-market-demand)。

<span id="fig-market-demand"></span>

![水平加总的市场需求。](../../../assets/principle-viz/agora/aggregation/market_demand.svg){ .ev-figure-sm }

<span id="fig-discrete-market-demand"></span>

![合并两张离散需求表。](../../../assets/principle-viz/agora/aggregation/discrete_market_demand.svg){ .ev-figure-sm }
