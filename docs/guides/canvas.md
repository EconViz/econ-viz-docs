---
seo_title: "Canvas: Textbook-Style Economics Diagrams"
description: "Canvas is the econ-viz drawing surface for textbook-style microeconomics diagrams: first-quadrant axes, arrow tips, LaTeX labels, budget lines, and equilibria."
---

# Canvas

`Canvas` is the central drawing surface. It manages a single matplotlib figure styled in the convention of microeconomic textbook diagrams: first-quadrant axes, arrow tips, LaTeX-rendered labels, and no numeric tick marks.

## Constructor

```python
from econ_viz import ArrowStyle, Canvas, Stroke, themes

cvs = Canvas(
    x_max=20,
    y_max=15,
    x_label="x",
    y_label="y",
    title=r"Cobb-Douglas $x^{0.5} y^{0.5}$",
    dpi=300,
    x_label_pos="right",   # "top", "right", or "bottom"
    y_label_pos="top",     # "left", "top", or "right"
    font="DejaVu Sans",
    math_font="stix",
    axis_stroke=Stroke(width=1.0, arrow=ArrowStyle.TRIANGLE),
    theme=themes.default,
)
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `x_max` | float | 10 | Upper bound of the horizontal axis |
| `y_max` | float | 10 | Upper bound of the vertical axis |
| `x_label` | str | `"X"` | Label at the tip of the horizontal axis |
| `y_label` | str | `"Y"` | Label at the tip of the vertical axis |
| `title` | str or None | None | Figure title |
| `dpi` | int | 300 | Raster export resolution (clamped to 1–1200) |
| `x_label_pos` | str or `LabelPosition` | `"right"` | Place the horizontal label above, right of, or below the arrow tip |
| `y_label_pos` | str or `LabelPosition` | `"top"` | Place the vertical label left of, above, or right of the arrow tip |
| `font` | str or sequence | None | Font family or fallback list for every text element |
| `math_font` | str | None | Matplotlib math font: `dejavusans`, `dejavuserif`, `cm`, `stix`, or `stixsans` |
| `axis_stroke` | `Stroke` | theme default | Shared width, style, colour, and arrowhead for both axes |
| `x_axis_stroke` | `Stroke` | None | Horizontal-axis override |
| `y_axis_stroke` | `Stroke` | None | Vertical-axis override |
| `theme` | Theme | `themes.default` | Colour and style theme |

## Methods

All drawing methods return `self`, so calls can be chained.

### Utility curves {#add_utility data-toc-label="Utility curves"}

Draws indifference curves for a utility model. Pass an integer to `levels` for automatically spaced curves, or a list of utility values, such as `levels.around(eq.utility, n=5)`, to place them around the optimum.

```python
cvs.add_utility(
    func,
    levels=3,          # count or list of levels
    color=None,        # default: theme.ic_color
    linewidth=None,    # default: theme.ic_linewidth
    show_rays=False,
    show_kinks=False,
    kink_radius=1.0,
    show_bliss=True,   # ★ at bliss point (Satiation)
    stroke=None,
    ray_stroke=None,
)
```

![Indifference curves drawn with add_utility](../assets/canvas/add_utility.png){ .ev-figure-sm }

### Budget line {#add_budget data-toc-label="Budget line"}

Draws the budget line $p_x x + p_y y = I$. Set `fill=True` to shade the feasible set below it.

```python
cvs.add_budget(
    px, py, income,
    color=None,
    linewidth=None,
    linestyle="-",
    label=None,        # legend label (LaTeX)
    fill=False,        # shade feasible set
    fill_alpha=None,   # default: theme.budget_fill_alpha
    stroke=None,
)
```

![Budget line with the shaded feasible set](../assets/canvas/add_budget.png){ .ev-figure-sm }

### Equilibrium {#add_equilibrium data-toc-label="Equilibrium"}

Marks the optimal bundle and drops dashed lines to both axes. Pass the result of `solve()` as `eq`; `show_ray=True` also draws the expansion path through the origin.

```python
cvs.add_equilibrium(
    eq,                # result of solve()
    color=None,
    markersize=None,
    label="x^*",
    drop_dashes=True,  # dashed lines to axes
    show_ray=False,    # expansion path
    drop_stroke=None,
    ray_stroke=None,
)
```

![Equilibrium point with dashed drop lines](../assets/canvas/add_equilibrium.png){ .ev-figure-sm }

### Ray {#add_ray data-toc-label="Ray"}

Draws a dashed ray from the origin with slope `slope` (dy/dx), often used for an expansion path or a fixed consumption ratio.

```python
cvs.add_ray(
    slope,             # dy/dx
    color=None,
    linewidth=None,
    stroke=None,
)
```

![Expansion-path ray through the optimum](../assets/canvas/add_ray.png){ .ev-figure-sm }

### Point {#add_point data-toc-label="Point"}

Marks any point, such as a bundle to compare with the optimum. `label` is rendered in LaTeX math mode, and `offset` moves the label in points.

```python
cvs.add_point(
    x, y,
    label=None,
    color=None,
    markersize=6.0,
    offset=(5, 5),     # label offset (pt)
)
```

![Labelled point A on the budget line](../assets/canvas/add_point.png){ .ev-figure-sm }

### Show and save {#show-save data-toc-label="Show and save"}

`show()` opens an interactive window. `save()` infers the format from the file extension: `.png`, `.pdf`, `.svg`, or `.tex` for TikZ. It also releases matplotlib resources, so call it last.

```python
cvs.show()               # interactive window
cvs.save("figure.png")   # .png / .pdf / .svg / .tex
```

![Complete diagram ready to save](../assets/canvas/show_save.png){ .ev-figure-sm }

## Styles

Canvas styles are divided into line styles and arrow styles. Set axis styles
directly with the `x_*` and `y_*` parameters; use `Stroke` to apply the same
controls to utility curves, budget lines, paths, and other visible lines.

### Line styles

Use `LineStyle.SOLID`, `DASHED`, `DOTTED`, or `DASHDOT` for axis lines.
The equivalent strings—`solid`, `dashed`, `dotted`, and `dashdot`—are also
accepted. Use `Stroke(style=...)` to apply the same setting to any other line.

```python
import matplotlib.pyplot as plt

from econ_viz import Canvas, LineStyle

styles = [
    LineStyle.SOLID,
    LineStyle.DASHED,
    LineStyle.DOTTED,
    LineStyle.DASHDOT,
]

fig, axes = plt.subplots(2, 2, figsize=(7, 7))
for ax, style in zip(axes.flat, styles):
    Canvas(
        title=style.value,
        x_line_style=style,
        y_line_style=style,
        fig=fig,
        ax=ax,
    )

fig.tight_layout()
fig.savefig("line_styles.png", dpi=160, transparent=True)
```

![Available line styles](../assets/canvas/line_styles.png)

### Arrow styles

Use `ArrowStyle.SIMPLE`, `TRIANGLE`, `FANCY`, or `WEDGE` for axis arrowheads.
Use `Stroke(arrow=...)` to add the same arrowhead to another visible line.

```python
import matplotlib.pyplot as plt

from econ_viz import ArrowStyle, Canvas

styles = [
    ArrowStyle.SIMPLE,
    ArrowStyle.TRIANGLE,
    ArrowStyle.FANCY,
    ArrowStyle.WEDGE,
]

fig, axes = plt.subplots(2, 2, figsize=(7, 7))
for ax, style in zip(axes.flat, styles):
    Canvas(
        title=style.name.title(),
        x_arrow_style=style,
        y_arrow_style=style,
        fig=fig,
        ax=ax,
    )

fig.tight_layout()
fig.savefig("arrow_styles.png", dpi=160, transparent=True)
```

![Available arrow styles](../assets/canvas/arrow_styles.png)

`Stroke` is also available for paths, decomposition diagrams,
`DemandDiagram`, `Figure`, and `EdgeworthBox`. Fields left as `None` inherit
from the active theme.

## Method chaining

```python
Canvas(x_max=20, y_max=15) \
    .add_utility(model, levels=lvls) \
    .add_budget(2.0, 3.0, 30.0, fill=True) \
    .add_equilibrium(eq, show_ray=True) \
    .save("figure.png")
```
