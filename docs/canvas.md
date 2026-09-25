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
    x_label_pos="right",   # "right" (axis tip) or "bottom"
    y_label_pos="top",     # "top" (axis tip) or "left"
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

### Add utility curves: `add_utility` {#add_utility data-toc-label="Add utility curves"}

```python
cvs.add_utility(
    func,
    levels=3,          # int (auto-spaced) or explicit list of floats
    color=None,        # falls back to theme.ic_color
    linewidth=None,    # falls back to theme.ic_linewidth
    show_rays=False,
    show_kinks=False,
    kink_radius=1.0,
    show_bliss=True,   # draw ★ at bliss point (Satiation models only)
)
```

![Indifference curves drawn with add_utility](assets/canvas/add_utility.png){ .ev-figure-sm }

### Add a budget line: `add_budget` {#add_budget data-toc-label="Add a budget line"}

```python
cvs.add_budget(
    px, py, income,
    color=None,
    linewidth=None,
    linestyle="-",
    label=None,        # legend label (LaTeX math mode)
    fill=False,        # shade the feasible set
    fill_alpha=None,   # falls back to theme.budget_fill_alpha
)
```

![Budget line with the shaded feasible set](assets/canvas/add_budget.png){ .ev-figure-sm }

### Add the equilibrium: `add_equilibrium` {#add_equilibrium data-toc-label="Add the equilibrium"}

```python
cvs.add_equilibrium(
    eq,                # Equilibrium namedtuple from solve()
    color=None,
    markersize=None,
    label="x^*",
    drop_dashes=True,  # dashed perpendicular lines to both axes
    show_ray=False,    # expansion-path ray from origin
)
```

![Equilibrium point with dashed drop lines](assets/canvas/add_equilibrium.png){ .ev-figure-sm }

### Add a ray: `add_ray` {#add_ray data-toc-label="Add a ray"}

```python
cvs.add_ray(
    slope,             # dy/dx
    color=None,
    linewidth=None,
)
```

![Expansion-path ray through the optimum](assets/canvas/add_ray.png){ .ev-figure-sm }

### Add a point: `add_point` {#add_point data-toc-label="Add a point"}

```python
cvs.add_point(
    x, y,
    label=None,
    color=None,
    markersize=6.0,
    offset=(5, 5),     # text offset in points
)
```

![Labelled point A on the budget line](assets/canvas/add_point.png){ .ev-figure-sm }

### Show and save: `show` / `save` {#show-save data-toc-label="Show and save"}

```python
cvs.show()               # interactive window
cvs.save("figure.png")   # raster (.png, .pdf, .svg)
```

![Complete diagram ready to save](assets/canvas/show_save.png){ .ev-figure-sm }

## Method chaining

```python
Canvas(x_max=20, y_max=15) \
    .add_utility(model, levels=lvls) \
    .add_budget(2.0, 3.0, 30.0, fill=True) \
    .add_equilibrium(eq, show_ray=True) \
    .save("figure.png")
```
