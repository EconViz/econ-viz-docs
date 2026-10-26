---
seo_title: "Open economy"
---

# Open economy

<span id="sec-open-economy"></span>

The goods market with exports and imports, interest parity, floating-rate IS-LM (Mundell-Fleming) and devaluation in AS-AD. Sections follow `open_economy.py`, `mundell_fleming.py` and `open_asad.py`.

## Models

<!-- api: macro_viz.guides_open_economy_1 -->

`OpenEconomy(domestic, exports, import_propensity)` adds net exports to a `KeynesianCross`. `InterestParity` is $E = E^e - s (i - i^*)$. `OpenISLM` substitutes parity into IS-LM for floating rates; `fixed_equilibrium` is the fixed-rate case, where the interest rate is pinned at the foreign rate.

## The goods market

<span id="sec-ex-goods"></span>


<!-- api: macro_viz.guides_open_economy_2 -->

```python
from macro_viz.keynesian import ConsumptionFunction, KeynesianCross
from macro_viz.open_economy import OpenEconomy, compare
from macro_viz.visuals import open_goods_canvas

home = KeynesianCross(
    ConsumptionFunction(20, 0.6), 20, 30, 20
)
model = OpenEconomy(home, exports=25, import_propensity=0.2)
open_goods_canvas(model).save("open_goods.svg")
open_goods_canvas(compare(model, model.with_government(50))).save(
    "open_fiscal_expansion.svg"
)
```

<span id="fig-open-goods"></span>

<figure class="ev-fig" markdown>

![Demand for domestic goods, with the output at which trade is balanced](../../assets/macro-viz/open_economy/open_goods.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/macro-viz/open_economy/open_economy.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>Demand for domestic goods, with the output at which trade is balanced</figcaption>

</figure>

<span id="fig-open-fiscal-expansion"></span>

<figure class="ev-fig" markdown>

![A fiscal expansion at home](../../assets/macro-viz/open_economy/open_fiscal_expansion.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/macro-viz/open_economy/open_economy.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>A fiscal expansion at home</figcaption>

</figure>

<span id="fig-open-foreign-demand"></span>

<figure class="ev-fig" markdown>

![A rise in foreign demand](../../assets/macro-viz/open_economy/open_foreign_demand.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/macro-viz/open_economy/open_economy.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>A rise in foreign demand</figcaption>

</figure>


## Interest parity and floating-rate IS-LM

<span id="sec-ex-parity"></span>


<!-- api: macro_viz.guides_open_economy_3 -->

<!-- api: macro_viz.guides_open_economy_4 -->

```python
from macro_viz.islm import ISLM
from macro_viz.open_economy import InterestParity, OpenISLM
from macro_viz.visuals import interest_parity_canvas, open_islm_canvas

parity = InterestParity(foreign_rate=0.4, expected_rate=100, slope=40)
model = OpenISLM(ISLM(100, 25, 20, 0.5, 10), parity, exchange_effect=0.2)
interest_parity_canvas(parity).save("interest_parity.svg")
open_islm_canvas(model, fiscal=120).save("open_islm_fiscal.svg")
open_islm_canvas(model, money=35).save("open_islm_money.svg")
```

<span id="fig-interest-parity"></span>

<figure class="ev-fig" markdown>

![Interest parity: the exchange rate against the domestic rate](../../assets/macro-viz/open_economy/interest_parity.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/macro-viz/open_economy/mundell_fleming.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>Interest parity: the exchange rate against the domestic rate</figcaption>

</figure>

<span id="fig-open-islm-fiscal"></span>

<figure class="ev-fig" markdown>

![A fiscal expansion under floating rates](../../assets/macro-viz/open_economy/open_islm_fiscal.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/macro-viz/open_economy/mundell_fleming.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>A fiscal expansion under floating rates</figcaption>

</figure>

<span id="fig-open-islm-money"></span>

<figure class="ev-fig" markdown>

![A monetary expansion under floating rates](../../assets/macro-viz/open_economy/open_islm_money.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/macro-viz/open_economy/mundell_fleming.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>A monetary expansion under floating rates</figcaption>

</figure>


## Devaluation in AS-AD

<span id="sec-ex-asad"></span>



```python
from macro_viz.adas import (
    AggregateDemand,
    AggregateSupply,
    ASADModel,
    analyze_adjustment,
)
from macro_viz.open_economy import analyze_devaluation
from macro_viz.visuals import adas_adjustment_canvas, adas_canvas

supply = AggregateSupply.linear(1.0, 100, 0.6)
slump = ASADModel(supply, AggregateDemand(35, 45, 1))
shift = analyze_devaluation(slump, 0.4, exchange_effect=50)
adas_canvas(slump).save("open_asad_below_natural.svg")
adas_canvas(shift).save("open_asad_devaluation.svg")
adas_adjustment_canvas(analyze_adjustment(slump)).save(
    "open_asad_fixed_rate.svg"
)
```

<span id="fig-open-asad-below-natural"></span>

<figure class="ev-fig" markdown>

![Output below its natural level](../../assets/macro-viz/open_economy/open_asad_below_natural.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/macro-viz/open_economy/open_asad.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>Output below its natural level</figcaption>

</figure>

<span id="fig-open-asad-devaluation"></span>

<figure class="ev-fig" markdown>

![A devaluation moves AD to the right](../../assets/macro-viz/open_economy/open_asad_devaluation.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/macro-viz/open_economy/open_asad.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>A devaluation moves AD to the right</figcaption>

</figure>

<span id="fig-open-asad-fixed-rate"></span>

<figure class="ev-fig" markdown>

![Under a fixed rate the economy adjusts back by itself](../../assets/macro-viz/open_economy/open_asad_fixed_rate.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/macro-viz/open_economy/open_asad.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>Under a fixed rate the economy adjusts back by itself</figcaption>

</figure>

