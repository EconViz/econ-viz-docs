---
seo_title: "Model and figure"
---

# Model and figure

<span id="sec-model-figure"></span>

## Model first, figure second

Every topic has two layers.

- A *model* is a frozen dataclass with checked inputs and methods that answer questions: `CubicCost.marginal_cost`, `Monopolist.solve`, `IndustrySupply.quantity`. Models never import a renderer and raise their own errors (`CostError`, `CompetitionError`, `UncertaintyError`) on bad input.
- A *builder* in `micro_viz.visuals` turns a model result into a `mosaickit` `Canvas`: `unit_cost_canvas(analysis)`, `monopoly_canvas(outcome, analysis)`. A builder has no equations in it; it places what the model computed.

```python
from micro_viz import (
    CubicCost,
    LinearDemand,
    Monopolist,
    analyze_costs,
    monopoly_canvas,
)

demand = LinearDemand(intercept=30, slope=2)
cost = CubicCost(20, 6, -1.5, 0.15)
outcome = Monopolist(demand, cost).solve()
analysis = analyze_costs(cost, output_range=(1, 10))

monopoly_canvas(outcome, analysis, profit=True).save(
    "monopoly.svg"
)
```

## Common options

<span id="sec-options"></span>

Every builder returns a `Canvas` and accepts the same keyword options. In the signatures on these pages they are written `**options`.

<!-- api: micro_viz.guides_model_figure_1 -->

Builders that draw several panels take `titles` (one per panel) instead of `title`.

## Package layout

<span id="tab-layout"></span>

| Where | What |
| --- | --- |
| `micro_viz/<topic>.py`, `micro_viz/<topic>/` | Models and solvers, renderer-free |
| `micro_viz/visuals/` | Builders that return a `Canvas`; `plane.py` is a small kit (`Plane`) for plane diagrams |
| `micro_viz/locale/labels.json` | Every built-in word, by id and language |
| `micro_viz/theme.py`, `config.py` | The theme and the `[micro]` settings schema |
| `micro_viz/animation/` | Optional animation over a parameter |
| `examples/scripts/<topic>/` | Scripts, one folder per topic; the figures of these pages |

## Layer ids

A builder gives every layer a stable id of the form `micro.<prefix>.<kind>.<n>`, such as `micro.cost.avc.label`. The ids are what the per-figure label table of the settings file addresses ([Labels and placement](labels.md#sec-labels)) and what an animation matches between frames ([Animation](animation.md#sec-animation)).

## Multi-panel figures

Figures with several panels (market and firm, multiplant monopoly, industry supply) use a `mosaickit` `CanvasGrid`. A dashed line that runs across the gap between panels is a `GridLink` from a point in one cell to a point in the next, so the price or marginal-cost level stays one continuous line.

## Relationship to the other packages

- `mosaickit` draws everything: scenes, layers, themes, label placement, grids and rendering. `micro-viz` depends on it and on nothing else at run time.
- `bezierkit` supplies curve geometry. `micro-viz` does not import it directly; it joins the dependencies when a figure needs its public geometry API.
- `kinetickit` animates figures and arrives only with the `animation` extra ([Animation](animation.md#sec-animation)).
- `utility-viz` and `principle-viz` own consumer theory and introductory market diagrams. Their objects can be used alongside; `micro-viz` does not rewrite them.
