---
seo_title: "Interactive widgets"
---

# Interactive widgets

<span id="sec-widgets"></span>

`WidgetViewer` provides sliders and numeric input boxes in Jupyter and
redraws the figure when a parameter changes. It needs the `interactive`
extra ([Optional dependencies](../getting-started/installation.md#sec-extras)). Import it from `utility_viz.core.interactive`;
it was `econ_viz.interactive` in 1.x.

<!-- api: agora.utility_viz.guides_interactive_1 -->

Pass a drawing function `draw` and give each parameter's range as
`(min, max, step)`. Each parameter gets a linked `FloatSlider` and
`FloatText`; when a value changes, `draw` is called again and its figure
replaces the old one in the cell.

`draw` follows the same contract as for `Animator` ([Animation](animation.md#sec-animation)), but may
take several parameters. Starting from the price-sweep example there, let
`draw()` also take `alpha`:

```python
from utility_viz.core.interactive import WidgetViewer

def draw(alpha: float, px: float) -> Canvas:
    model = CobbDouglas(alpha=alpha, beta=1.0 - alpha)
    ...  # rest as in the animation example

WidgetViewer(
    draw,
    alpha=(0.2, 0.8, 0.05),
    px=(1.0, 6.0, 0.25),
).show()
```

## Notebook setup

In a fresh Jupyter or Colab runtime, run the steps in this order (The Playground notebook in the `utility-viz` repository, `notebook/econ-viz Playground.ipynb` (which keeps its historical name), follows this flow; open it in Jupyter, VS Code or Colab. It does not reinstall when `utility-viz` is already present.):

+ Run the install cell.
+ If the install upgraded `ipywidgets`, `traitlets` or
  `IPython`, restart the runtime.
+ After the restart, continue from the import cell without reinstalling.

## Widgets or GIFs

Use `WidgetViewer` when users should adjust the parameters themselves; use
`Animator` to export a GIF when a fixed sweep should play in slides or on a
web page ([Animation](animation.md#sec-animation)).
