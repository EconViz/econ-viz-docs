---
seo_title: "Canvas: Textbook-Style Economics Diagrams"
description: "Canvas is the econ-viz drawing surface for textbook-style microeconomics diagrams: first-quadrant axes, arrow tips, LaTeX labels, budget lines, and equilibria."
---

# Canvas

`Canvas` is the central drawing surface. It manages a single matplotlib figure styled in the convention of microeconomic textbook diagrams: first-quadrant axes, arrow tips, LaTeX-rendered labels, and no numeric tick marks.

## Constructor

```python
from econ_viz import Canvas

cvs = Canvas(
    x_max=20,
    y_max=15,
    x_label="x",
    y_label="y",
    title=r"Cobb-Douglas $x^{0.5} y^{0.5}$",
    dpi=300,
    x_label_pos="right",   # "right" or "bottom"
    y_label_pos="top",     # "top" or "left"
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
| `x_label_pos` | str | `"right"` | `"right"` places label at axis tip; `"bottom"` uses standard xlabel |
| `y_label_pos` | str | `"top"` | `"top"` places label at axis tip; `"left"` uses standard ylabel |
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

## Method chaining

```python
Canvas(x_max=20, y_max=15) \
    .add_utility(model, levels=lvls) \
    .add_budget(2.0, 3.0, 30.0, fill=True) \
    .add_equilibrium(eq, show_ray=True) \
    .save("figure.png")
```
