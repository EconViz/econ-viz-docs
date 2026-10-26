---
seo_title: "总合供给与需求"
---

# 总合供给与需求

<span id="sec-adas"></span>

总合供给通过产出等于自然水准、价格等于预期价格的点；总合需求随物价水准下降。各节对应 `adas.py` 与 `adas_adjustment.py`。

## 模型

<!-- api: macro_viz.guides_adas_1 -->

`AggregateSupply.linear(expected_price, natural_output, slope)` 是 $p = p^e (1 + s (Y / Y_n - 1))$，其中 `0 < slope < 1`。`AggregateDemand(autonomous, money, multiplier)` 是由 IS-LM 推出的需求。`ASADModel` 解出两者的交点并分类缺口（`Gap`）。冲击函数回传 `ASADShift`，含产出与价格的方向。

## 总合供给

<span id="sec-ex-supply"></span>


<!-- api: macro_viz.guides_adas_2 -->

```python
from macro_viz.adas import AggregateSupply
from macro_viz.visuals import aggregate_supply_canvas

supply = AggregateSupply.linear(1.0, 100, 0.6)
aggregate_supply_canvas(supply).save("aggregate_supply.svg")
aggregate_supply_canvas(
    supply, shifted=supply.with_expected_price(1.2)
).save("aggregate_supply_shift.svg")
```

<span id="fig-aggregate-supply"></span>

<figure class="ev-fig" markdown>

![通过 A 的总合供给](../../../assets/macro-viz/adas/aggregate_supply.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/adas/adas.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>通过 A 的总合供给</figcaption>

</figure>

<span id="fig-aggregate-supply-shift"></span>

<figure class="ev-fig" markdown>

![预期价格上升使 AS 上移到 AS'](../../../assets/macro-viz/adas/aggregate_supply_shift.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/adas/adas.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>预期价格上升使 AS 上移到 AS'</figcaption>

</figure>


## 总合需求

<span id="sec-ex-demand"></span>


<!-- api: macro_viz.guides_adas_3 -->

```python
from macro_viz.adas import AggregateDemand
from macro_viz.visuals import aggregate_demand_canvas

demand = AggregateDemand(80, 45, 1)
aggregate_demand_canvas(
    demand,
    [demand.with_autonomous(100), demand.with_money(30)],
    captions=["Increase in government spending", "Decrease in nominal money"],
    x_max=240,
    y_max=2.2,
).save("aggregate_demand_shifts.svg")
```

<span id="fig-aggregate-demand-shifts"></span>

<figure class="ev-fig" markdown>

![同一物价水准下，需求向右或向左移动](../../../assets/macro-viz/adas/aggregate_demand_shifts.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/adas/adas.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>同一物价水准下，需求向右或向左移动</figcaption>

</figure>


## 均衡与冲击

<span id="sec-ex-equilibrium"></span>


<!-- api: macro_viz.guides_adas_4 -->

```python
from macro_viz.adas import (
    ASADModel,
    analyze_demand_shock,
    analyze_supply_shock,
)
from macro_viz.visuals import adas_canvas

model = ASADModel(supply, demand)
adas_canvas(model).save("adas_equilibrium.svg")
adas_canvas(model, productivity=1.0).save("adas_employment.svg")

oil = analyze_supply_shock(model, scale=0.75)
adas_canvas(oil, ambiguous_demand=True).save("adas_productivity.svg")

boom = analyze_demand_shock(model, autonomous=115)
adas_canvas(boom).save("adas_demand_shock.svg")
```

<span id="fig-adas-equilibrium"></span>

<figure class="ev-fig" markdown>

![短期均衡 A，附自然产出 $Y_n$ 与预期价格](../../../assets/macro-viz/adas/adas_equilibrium.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/adas/adas.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>短期均衡 A，附自然产出 $Y_n$ 与预期价格</figcaption>

</figure>

<span id="fig-adas-employment"></span>

<figure class="ev-fig" markdown>

![由产出读出就业](../../../assets/macro-viz/adas/adas_employment.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/adas/adas.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>由产出读出就业</figcaption>

</figure>

<span id="fig-adas-productivity"></span>

<figure class="ev-fig" markdown>

![供给冲击：需求的反应方向不确定](../../../assets/macro-viz/adas/adas_productivity.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/adas/adas.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>供给冲击：需求的反应方向不确定</figcaption>

</figure>

<span id="fig-adas-demand-shock"></span>

<figure class="ev-fig" markdown>

![需求冲击使 AD 移到 AD'](../../../assets/macro-viz/adas/adas_demand_shock.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/adas/adas.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>需求冲击使 AD 移到 AD'</figcaption>

</figure>


`ambiguous_demand=True` 会画出左右两支各标问号的箭头，表示需求可能往任一方向移动。

## 调整到中期

<span id="sec-ex-adjustment"></span>


<!-- api: macro_viz.guides_adas_5 -->

```python
from macro_viz.adas import analyze_adjustment
from macro_viz.visuals import adas_adjustment_canvas

money_up = analyze_demand_shock(model, money=70)
path = analyze_adjustment(money_up)
adas_adjustment_canvas(path).save("adjustment_money.svg")
```

<span id="fig-adjustment-money"></span>

<figure class="ev-fig" markdown>

![货币扩张后预期跟上，产出回到 $Y_n$](../../../assets/macro-viz/adas/adjustment_money.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/adas/adas_adjustment.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>货币扩张后预期跟上，产出回到 $Y_n$</figcaption>

</figure>

<span id="fig-adjustment-deficit"></span>

<figure class="ev-fig" markdown>

![削减赤字](../../../assets/macro-viz/adas/adjustment_deficit.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/adas/adas_adjustment.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>削减赤字</figcaption>

</figure>

<span id="fig-adjustment-oil"></span>

<figure class="ev-fig" markdown>

![油价冲击](../../../assets/macro-viz/adas/adjustment_oil.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/adas/adas_adjustment.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>油价冲击</figcaption>

</figure>

<span id="fig-adjustment-expectations"></span>

<figure class="ev-fig" markdown>

![预期逐步调整](../../../assets/macro-viz/adas/adjustment_expectations.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/adas/adas_adjustment.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>预期逐步调整</figcaption>

</figure>


均衡 A、A'、A''、……以直线实线箭头相连，沿着总合需求滑动，最后停在自然产出垂直线上的中期均衡。

## 动画

<span id="sec-ex-animation"></span>



<span id="fig-adas-animation"></span>

<figure class="ev-fig" markdown>

![AD 曲线移动，经济沿 AS 滑动](../../../assets/macro-viz/adas/adas_animation.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/adas/adas_animation.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>AD 曲线移动，经济沿 AS 滑动</figcaption>

</figure>

