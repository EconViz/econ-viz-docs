# Interactive Widgets

`WidgetViewer` renders an `econ-viz` figure inside a notebook cell and redraws it whenever a control changes. In `v1.4.0`, every parameter gets both a slider and a numeric input box, so users can drag for intuition or type exact values for teaching and demos.

## Install

```bash
pip install "econ-viz[interactive]"
```

If you also want GIF export:

```bash
pip install "econ-viz[all]"
```

## Basic usage

```python
from econ_viz import Canvas, levels, solve
from econ_viz.interactive import WidgetViewer
from econ_viz.models import CobbDouglas

def draw(alpha: float, px: float) -> Canvas:
    model = CobbDouglas(alpha=alpha, beta=1.0 - alpha)
    eq = solve(model, px=px, py=2.0, income=20.0)

    return (
        Canvas(x_max=14, y_max=12, x_label="X_1", y_label="X_2", title="Interactive equilibrium")
        .add_utility(model, levels=levels.around(eq.utility, n=5))
        .add_budget(px=px, py=2.0, income=20.0, fill=True)
        .add_equilibrium(eq, show_ray=True, drop_dashes=True)
    )

WidgetViewer(
    draw,
    alpha=(0.2, 0.8, 0.05),
    px=(1.0, 6.0, 0.25),
).show()
```

## What the widget layer does

- Builds one `FloatSlider` per parameter.
- Builds one linked `FloatText` input per parameter.
- Keeps slider and typed values in sync.
- Clears the old figure before redrawing, so notebook cells do not accumulate a stack of stale plots.

## Colab and Jupyter notes

For fresh notebook runtimes, especially in Colab:

1. Run the install cell once.
2. Restart the runtime once if `ipywidgets`, `traitlets`, or `IPython` were upgraded.
3. Skip the install cell after restart and continue from the import cell.

The packaged Playground notebook now follows this flow and avoids reinstalling when `econ-viz 1.4.0` is already present.

## When to use widgets vs GIFs

- Use `WidgetViewer` when students need to type or drag parameters and inspect one state at a time.
- Use `Animator` when you want a fixed, repeatable narrative sweep for slides, docs, or the project website.
