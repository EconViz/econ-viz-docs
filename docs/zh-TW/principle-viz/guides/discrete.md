---
seo_title: "離散市場"
---

# 離散市場

<span id="sec-discrete"></span>

離散市場逐一列出每個單位：買方對多一單位的願付價格，以及賣方多生產一單位的成本。需求與供給都是階梯函數；均衡是整數個單位，並由一段價格區間支持。

## 逐單位表

<!-- api: agora.principle_viz.guides_discrete_1 -->

需求表存放邊際願付價格，由第一單位到最後一單位弱遞減；供給表存放邊際成本，弱遞增。順序不符時拋出 `DiscreteMarketError`。

## 均衡

<!-- api: agora.principle_viz.guides_discrete_2 -->

交易所有價值不低於成本的單位，並找出恰好使該數量成交的價格區間。結果包含下列欄位：

`solve_discrete_market(demand_values, supply_values)` 直接由 tuple 建立兩張表並求解。需求表的值由高到低、供給表的值由低到高，各單位的價值與成本才能依序配對。

```python
from principle_viz import (
    DiscreteDemand,
    DiscreteSupply,
    solve_discrete_equilibrium,
)

demand = DiscreteDemand((11, 9, 7, 5, 3))
supply = DiscreteSupply((1, 3, 5, 8, 10))
eq = solve_discrete_equilibrium(demand, supply)
print(eq.q_star, eq.price_low, eq.price_high, eq.price)
# 3 5.0 7.0 6.0
print(eq.gains_from_trade)
# (10.0, 6.0, 2.0)
```

成交 3 單位，價格區間為 5 到 7，中點規則回報 6。交易利得合計 $10 + 6 + 2 = 18$。

<!-- api: agora.principle_viz.guides_discrete_3 -->

所選價格下的消費者剩餘與生產者剩餘，包含總額與逐單位數值（`consumer_surplus_by_unit`、`producer_surplus_by_unit`）。上例價格為 6 時，兩者皆為 $5 + 3 + 1 = 9$。

## 圖形

<!-- api: agora.principle_viz.guides_discrete_4 -->

每個單位畫成區間 $[q, q + 1)$ 的一階：起點為實心點（包含），終點為空心點（不包含），並以虛線連到下一階。可只傳入其中一張表。均衡在座標軸上標出 $Q^*$ 與價格區間。

```python
fig = MarketFigure(
    x_max=5.5,
    y_max=12,
    title="Discrete Demand and Supply",
)
fig.add_discrete_curves(demand, supply)
fig.add_discrete_equilibrium(eq)
fig.finalize()
```

上例的圖形參見[離散需求與供給。](discrete.md#fig-discrete)。

<span id="fig-discrete"></span>

![離散需求與供給。](../../../assets/principle-viz/agora/discrete/market.svg){ .ev-figure-sm }
