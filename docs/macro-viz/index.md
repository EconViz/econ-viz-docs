---
seo_title: "macro-viz: Macroeconomics Diagrams in Python"
description: "macro-viz draws textbook macroeconomic models in Python: the Keynesian cross, money market, AS-AD, IS-LM, Solow growth, wage and price setting, and linked-panel diagrams."
---

<h1 class="ev-visually-hidden">macro-viz: macroeconomics diagrams in Python</h1>

<p align="center"><em>Python package for textbook macroeconomic analysis and diagrams.</em></p>

`macro-viz` is for introductory and intermediate macroeconomics models whose equations are given
and need to be analysed or drawn. Each model is a typed, renderer-free object; each figure is a
`mosaickit` canvas built from it. Statistics-style data charts and accounting box diagrams are
out of scope.

```python
from macro_viz.keynesian import ConsumptionFunction, KeynesianCross, analyze_autonomous_shift
from macro_viz.visuals import multiplier_canvas

model = KeynesianCross(ConsumptionFunction(20, 0.6), investment=20, government=30, taxes=20)
shift = analyze_autonomous_shift(model, change=30)

multiplier_canvas(shift, title="A rise in autonomous spending").save("multiplier.svg")
```

![A rise in autonomous spending](../assets/macro-viz/multiplier.svg){ .ev-figure-sm }

## Models

| Model | Module | Chapter |
| --- | --- | --- |
| Consumption function, Keynesian cross, multiplier | `macro_viz.keynesian` | [Keynesian goods market](guides/keynesian.md) |
| Money demand, money market, central-bank money | `macro_viz.money` | [Money market](guides/money.md) |
| Aggregate supply and demand, adjustment | `macro_viz.adas` | [Aggregate supply and demand](guides/adas.md) |
| IS-LM, fiscal and monetary policy | `macro_viz.islm` | [IS-LM](guides/islm.md) |
| Solow growth | `macro_viz.growth` | [Solow growth](guides/growth.md) |
| Wage setting and price setting | `macro_viz.labor` | [Natural rate of unemployment](guides/labor.md) |
| Four- and five-panel linked quadrants | `macro_viz.panels` | [Linked panels](guides/panels.md) |

Every builder accepts `title=None`, returns a `mosaickit` `Canvas` and emits stable `macro.*`
layer ids. Words come from a locale table in English, Traditional Chinese and Simplified Chinese,
and any of them can be replaced with `labels=`. Sizes, widths, colours and fonts come from the
theme and the shared `econ-viz.toml`, never from the drawing code.

!!! note "Status"

    `macro-viz` is at `0.2.0.dev0` and is not on PyPI yet; install it from GitHub
    ([Installation](installation.md#sec-install)).
