---
seo_title: "Quick start"
---

# Quick start

<span id="sec-quickstart"></span>

A figure is two steps: build a model, then pass it to a builder from `macro_viz.visuals`.

```python
from macro_viz.keynesian import ConsumptionFunction, KeynesianCross
from macro_viz.visuals import keynesian_cross_canvas

model = KeynesianCross(ConsumptionFunction(20, 0.6), investment=20, government=30, taxes=20)
keynesian_cross_canvas(model).save("keynesian_cross.svg")
```

![The Keynesian cross](../assets/macro-viz/keynesian_cross.svg){ .ev-figure-sm }

`save()` writes PNG, SVG or PDF according to the extension. Models are immutable and answer
questions without drawing:

```python
model.equilibrium().output       # equilibrium income
model.multiplier                 # 1 / (1 - c1)
```

## Titles, labels and settings

- `title=None` draws no title, and `title="..."` sets one.
- Built-in words (axis titles, curve names, point names) are label ids of a locale table;
  `labels={"id": "text"}` replaces any of them.
- Colours, widths, fonts and sizes come from the theme and the `[macro-viz]` tables of the shared
  `econ-viz.toml`; the drawing code contains none of them.
