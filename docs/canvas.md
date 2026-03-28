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

### `add_utility`

```python
cvs.add_utility(
    func,
    levels=3,          # int (auto-spaced) or explicit list of floats
    color=None,        # falls back to theme.ic_color
    linewidth=None,    # falls back to theme.ic_linewidth
    show_rays=False,
    show_kinks=False,
    kink_radius=1.0,
)
```

### `add_budget`

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

### `add_equilibrium`

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

### `add_ray`

```python
cvs.add_ray(
    slope,             # dy/dx
    color=None,
    linewidth=None,
)
```

### `add_point`

```python
cvs.add_point(
    x, y,
    label=None,
    color=None,
    markersize=6.0,
    offset=(5, 5),     # text offset in points
)
```

### `show` / `save`

```python
cvs.show()               # interactive window
cvs.save("figure.png")   # raster (.png, .pdf, .svg)
cvs.save("figure.tex")   # TikZ/PGFPlots source
```

## Method chaining

```python
Canvas(x_max=20, y_max=15) \
    .add_utility(model, levels=lvls) \
    .add_budget(2.0, 3.0, 30.0, fill=True) \
    .add_equilibrium(eq, show_ray=True) \
    .save("figure.png")
```
