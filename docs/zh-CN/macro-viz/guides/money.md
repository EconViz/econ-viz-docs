---
seo_title: "货币市场"
---

# 货币市场

<span id="sec-money"></span>

货币需求随利率下降、随名目所得上升；中央银行决定供给。各节对应 `money.py`、`central_bank_money.py` 与 `liquidity_trap.py`。

## 模型

<!-- api: macro_viz.guides_money_1 -->

`MoneyDemand(nominal_income, liquidity, rate_max)` 是 $M^d = Y \, L(R)$，其中 `liquidity` 是利率的函数；`zero_bound=True` 让需求在利率为零处变平。`MoneyMarket` 再加上供给。`analyze_income_shift` 与 `analyze_supply_shift` 回传基准、变动后的市场，以及利率与货币的方向。

## 需求、供给与货币需求的移动

<span id="sec-ex-market"></span>


<!-- api: macro_viz.guides_money_2 -->

<!-- api: macro_viz.guides_money_3 -->

```python
from macro_viz.money import (
    MoneyDemand,
    MoneyMarket,
    analyze_income_shift,
    analyze_supply_shift,
)
from macro_viz.visuals import (
    money_demand_canvas,
    money_market_canvas,
)

demand = MoneyDemand(100, lambda r: 0.9 - 0.12 * r, 6)
market = MoneyMarket(demand, supply=60)

income = analyze_income_shift(market, nominal_income=130)
money_market_canvas(market).save("money_market.svg")
money_market_canvas(income).save("money_income_shift.svg")
money_demand_canvas(income).save("money_demand.svg")
```

<span id="fig-money-market"></span>

<figure class="ev-fig" markdown>

![货币市场：需求 $M^d$ 与供给 $M^s$](../../../assets/macro-viz/money/money_market.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/money/money.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>货币市场：需求 $M^d$ 与供给 $M^s$</figcaption>

</figure>

<span id="fig-money-income-shift"></span>

<figure class="ev-fig" markdown>

![名目所得增加使需求向右移动](../../../assets/macro-viz/money/money_income_shift.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/money/money.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>名目所得增加使需求向右移动</figcaption>

</figure>


箭头从旧均衡 A 出发，水平指向新的需求曲线。

## 货币供给的变动

<span id="sec-ex-supply"></span>



```python
supply = analyze_supply_shift(market, supply=80)
money_market_canvas(supply).save("money_supply_shift.svg")
```

<span id="fig-money-supply-shift"></span>

<figure class="ev-fig" markdown>

![货币增加使利率下降](../../../assets/macro-viz/money/money_supply_shift.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/money/money.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>货币增加使利率下降</figcaption>

</figure>


## 央行货币

<span id="sec-ex-central"></span>


<!-- api: macro_viz.guides_money_4 -->

```python
from macro_viz.money import MoneyMultiplier
from macro_viz.visuals import central_bank_money_canvas

multiplier = MoneyMultiplier(0.2, 0.1)
central_bank_money_canvas(multiplier, market).save(
    "central_bank_money.svg"
)
```

<span id="fig-central-bank-money"></span>

<figure class="ev-fig" markdown>

![央行货币市场](../../../assets/macro-viz/money/central_bank_money.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/money/central_bank_money.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>央行货币市场</figcaption>

</figure>

<span id="fig-central-bank-money-purchase"></span>

<figure class="ev-fig" markdown>

![公开市场买进](../../../assets/macro-viz/money/central_bank_money_purchase.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/money/central_bank_money.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>公开市场买进</figcaption>

</figure>


## 零利率下限

<span id="sec-ex-trap"></span>



```python
demand = MoneyDemand(
    100, lambda r: 0.9 - 0.12 * r, 6, zero_bound=True
)
market = MoneyMarket(demand, supply=130)
shift = analyze_supply_shift(market, supply=160)
money_market_canvas(shift).save("money_zero_bound.svg")
```

<span id="fig-money-zero-bound"></span>

<figure class="ev-fig" markdown>

![利率降到零之后，货币再增加也不改变利率](../../../assets/macro-viz/money/money_zero_bound.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/money/liquidity_trap.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>利率降到零之后，货币再增加也不改变利率</figcaption>

</figure>


## 动画

<span id="sec-ex-animation"></span>



<span id="fig-money-animation"></span>

<figure class="ev-fig" markdown>

![供给曲线右移、利率下降](../../../assets/macro-viz/money/money_supply_animation.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/money/money_animation.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>供给曲线右移、利率下降</figcaption>

</figure>

