---
seo_title: "Adding a figure"
---

# Adding a figure

<span id="sec-adding"></span>

Which figures exist is decided by the issues and milestones of the repository. Statistics charts and accounting boxes are not drawn. A new figure follows five steps.

+ *Model.* Put the equations in a frozen dataclass in `macro_viz/<topic>/models.py`. Check the inputs and raise `ValidationError`. No renderer is imported.
+ *Comparison.* Add an `analyze_*` function in `analysis.py` that returns both models and the direction of each change.
+ *Builder.* Write `macro_viz/visuals/<topic>.py` with the helpers of `_theory.py`. Never write display text in it.
+ *Text.* Add every word to `locale/labels.json` in all three languages under a stable id (`islm.curve.is`).
+ *Export, example and tests.* Add the names to `visuals/__init__.py`, write `examples/scripts/<topic>.py` that reads its numbers from `examples/examples.toml`, test the model, that a changed parameter changes the figure, that `title=None` draws no title, and that no label overlaps a line.

```python
from macro_viz.i18n import Labels
from macro_viz.visuals._theory import (
    curve,
    drop_lines,
    marked_point,
    point_name,
    theory_canvas,
    trim,
)


def demand_canvas(intercept, slope, x_max, *, title=None):
    text = Labels()
    y_max = intercept
    canvas = theory_canvas(
        x_max,
        y_max,
        labels=text,
        x_label_id="keynesian.axis.income",
        y_label_id="keynesian.axis.demand",
        title=title,
    )
    line = [(0.0, intercept), (x_max, intercept - slope * x_max)]
    canvas.extend(
        curve(
            trim(line, x_max, y_max),
            layer_id="macro.demo.demand",
            role="macro.curve.primary",
            label=text("keynesian.curve.demand"),
        )
    )
    return canvas
```

## The theory kit

<span id="sec-kit"></span>

The helpers of `macro_viz.visuals._theory` draw the parts every figure shares, each with a stable id and a theme role.

<!-- api: macro_viz.guides_adding_figure_1 -->

A canvas with arrowed axes from the origin, symbol axis titles and an optional title. `x_max` and `y_max` are the axis lengths.

<!-- api: macro_viz.guides_adding_figure_2 -->

A curve through `points` with its name at the right-hand end. The role says what it is: `macro.curve.primary` or `secondary` is a heavy curve, and the same role ending in `.shifted` is the thin solid curve after a change. The canvas puts the name at the first free diagonal off the end: lower-right, upper-left, lower-left, upper-right.

<!-- api: macro_viz.guides_adding_figure_3 -->

A straight, solid, thin arrow for a parallel shift. It starts at the old equilibrium and ends on the new curve, so it is horizontal for a sideways shift and vertical for a shift up or down.

<!-- api: macro_viz.guides_adding_figure_4 -->

The only curved arrow, for a change of slope: gentle curvature, concave side down. Its bulge is a theme-independent parameter, `BULGE`, as a share of the arrow's length.

## Conventions

- A changed curve is thin and solid, never dashed; a parallel shift is a straight arrow; a curved arrow means rotation only.
- Dotted guides join a point to the axes and the marks on the axes name its values.
- Only the price `p` is lowercase; other variables are uppercase italic. Acronyms and point names keep their case.
- Nothing is hard-coded: text comes from the locale table, numbers from arguments, and colours, widths and fonts from the theme.
- The theme is always on white. The examples use `manual`.

## Checks

```bash
uv run ruff check . && uv run ruff format --check .
uv run mypy
uv run pytest
```
