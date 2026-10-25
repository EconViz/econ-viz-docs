---
seo_title: "micro-viz: Microeconomics Diagrams in Python"
description: "micro-viz draws textbook microeconomic models in Python: production, costs, competition, monopoly, pricing, oligopoly, factor markets, uncertainty and information."
---

<h1 class="ev-visually-hidden">micro-viz: microeconomics diagrams in Python</h1>

<p align="center">
  <img src="../assets/micro-viz/banner.svg" alt="micro-viz" style="max-width: 480px; width: 100%; margin: 2rem 0 1rem;">
</p>

<p align="center"><em>Python package for textbook analysis and diagrams of firms and markets.</em></p>

`micro-viz` covers the firm side of microeconomics: production, costs, market structure, pricing,
factor markets, uncertainty and information. Each model is a typed object that does not know how
to draw; each figure is a `mosaickit` canvas built from it. Statistics-style data charts and
box-and-arrow flowcharts are out of scope.

```python
from micro_viz import (
    ShortRunProductionFunction,
    analyze_production,
    total_product_canvas,
)

production = ShortRunProductionFunction(
    linear=6, quadratic=3, cubic=-0.5
)
result = analyze_production(production, input_range=(0, 6))

total_product_canvas(result).save("total_product.svg")
```

![Total product](../assets/micro-viz/production/total_product.svg){ .ev-figure-sm }

## Models and figures

| Models | Modules | Figures |
| --- | --- | --- |
| Short-run production, cost functions, stepped cost | `production`, `costs` | [Production and costs](guides/production-costs.md) |
| Isoquants, cost minimization, learning and scope, factor markets, monopsony and unions | `isoquant`, `production.extras`, `factors` | [Inputs and technology](guides/inputs.md) |
| Perfect competition, entry and exit, long-run costs | `competition`, `entry`, `longrun` | [Competition and the long run](guides/competition.md) |
| Monopoly, monopolistic competition, regulation, price discrimination, tariffs, bundling, advertising, exhaustible resources | `monopoly`, `monopolistic`, `regulation`, `discrimination`, `pricing`, `bundling`, `advertising`, `capital` | [Monopoly and pricing](guides/monopoly.md) |
| Duopoly, kinked demand, dominant firm, vertical chains | `oligopoly`, `vertical` | [Oligopoly and vertical chains](guides/oligopoly.md) |
| Expected utility, risk, auctions, adverse selection, signaling, moral hazard | `uncertainty`, `auctions`, `information` | [Uncertainty and information](guides/uncertainty.md) |

Every builder accepts `title=None`, returns a `mosaickit` `Canvas` and emits stable `micro.*`
layer ids. Words come from a locale table in English, Traditional Chinese and Simplified Chinese,
and any of them can be replaced with `labels=`. Sizes, widths, colours and fonts come from the
theme and the shared `econ-viz.toml`, never from the drawing code.

!!! note "Status"

    `micro-viz` is at `0.2.0.dev0` and is not on PyPI yet; install it from GitHub
    ([Installation](installation.md#sec-install)).

## Scope

- `micro-viz` owns producer theory, market structure, factor markets, uncertainty and information.
- Consumer theory and general equilibrium belong to [utility-viz](../utility-viz/index.md).
- Introductory supply-and-demand policy diagrams belong to [principle-viz](../principle-viz/index.md).
- Game theory is outside the package.
