---
seo_title: "國際貿易"
---

# 國際貿易

<span id="sec-trade"></span>

小型開放經濟體接受既定的世界價格 $p_w$。世界價格低於自給自足價格時，進口國內需求與供給的差額；高於自給自足價格時則出口。關稅或進口配額會提高國內價格並減少進口。

<!-- api: agora.principle_viz.guides_trade_1 -->

世界價格與至多一項政策：每單位 `tariff` 或 `import_quota`，兩者不可同時設定（`PolicyError`）。

<!-- api: agora.principle_viz.guides_trade_2 -->

比較自給自足、自由貿易與政策三種情況。`TradeComparisonResult` 包含三個 `TradeOutcome`（`autarky`、`free_trade`、`policy`），以及政策相對於自由貿易的 `deadweight_loss`。

```python
from principle_viz import TradeScenario, analyze_trade

# autarky price 7
demand = line_from_inverse(12.0, -1.0)
scenario = TradeScenario(world_price=4, tariff=2)
result = analyze_trade(demand, supply, scenario)
print(result.free_trade.imports, result.policy.imports)
# 6.0 2.0
print(result.policy.government_revenue, result.deadweight_loss)
# 4.0 4.0
```

關稅 2 時，國內價格為 6，政府收入為 $2 \times 2 = 4$。配額 2 單位時價格同為 6，配額租 4 歸 `quota_rent_recipient` 指定的一方。

<!-- api: agora.principle_viz.guides_trade_3 -->

畫出世界價格線並命名為 $p_w$，標出政策價格（$p_w + t$ 或 $p_q$），在數量軸上標 $Q_s$ 與 $Q_d$ 並於下方加上 "Imports" 或 "Exports" 括號，再以命名的矩形表示關稅收入或配額租（參見[自由貿易下的進口。](trade.md#fig-free-trade)、[進口關稅。](trade.md#fig-tariff)、[有約束的進口配額。](trade.md#fig-quota)）。

<span id="fig-free-trade"></span>

![自由貿易下的進口。](../../../assets/principle-viz/agora/trade/free_trade_import.svg){ .ev-figure-sm }

<span id="fig-tariff"></span>

![進口關稅。](../../../assets/principle-viz/agora/trade/tariff.svg){ .ev-figure-sm }

<span id="fig-quota"></span>

![有約束的進口配額。](../../../assets/principle-viz/agora/trade/quota.svg){ .ev-figure-sm }
