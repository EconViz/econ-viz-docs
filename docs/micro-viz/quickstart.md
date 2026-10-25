---
seo_title: "Quick start"
---

# Quick start

<span id="sec-quickstart"></span>

A figure takes two steps: build a model, then pass its result to a builder from `micro_viz`.

```python
from micro_viz import CubicCost, analyze_costs, unit_cost_canvas

cost = CubicCost(
    fixed_cost=50, linear=36, quadratic=-8, cubic=0.6
)
analysis = analyze_costs(cost, output_range=(1, 11))

unit_cost_canvas(analysis).save("unit_cost.svg")
```

<span id="fig-quick-unit-cost"></span>

<figure class="ev-fig" markdown>

![Unit costs](../assets/micro-viz/agora/costs/unit_cost.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../assets/micro-viz/agora/costs/costs.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>Unit costs</figcaption>

</figure>

`save()` writes PNG, SVG or PDF according to the extension. Models are immutable and answer questions without drawing:

```python
# lowest ATC and its output
analysis.minimum_average_total_cost
# MC at one output
cost.marginal_cost(5.0)
```

## Titles, labels and settings

- `title=None` draws no title, and `title="..."` sets one.
- Built-in words (axis titles, curve names, point names) are label ids of a locale table; `labels={"id": "text"}` replaces any of them ([Labels and placement](guides/labels.md#sec-labels)).
- Colours, widths, fonts and sizes come from the theme and the `[micro]` tables of the shared `econ-viz.toml` ([Settings](guides/settings.md#sec-settings)); the drawing code contains none of them.
- Numbers such as ranges, output marks and sample counts are arguments of the builder.
