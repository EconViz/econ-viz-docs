---
seo_title: "Settings File"
description: "Keep econ-viz diagram styles in an econ-viz.toml file and load them once with Config."
---

# Settings File

Keep your colours, lines, labels, and legend settings in an `econ-viz.toml`
file and load them once, instead of passing the same arguments to every
method.

## Format

Section names match Theme properties, and fields match the arguments of the
style objects. Anything left out keeps the built-in default.

```toml
# econ-viz.toml
base = "default"                 # default or nord

[font]
text = "TeX Gyre Pagella"
math = "stix"

[color]
ic = "#2E86AB"
budget = "#6C3483"
equilibrium = "#C0392B"

[stroke.budget]                  # theme.budget_stroke
width = 1.5
style = "solid"

[stroke.ic]                      # theme.ic_stroke
width = 1.8
opacity = 0.9

[marker.equilibrium]             # theme.eq_marker
size = 5

[label.point]                    # theme.point_label
fontsize = 12
position = "top-right"

[label.origin]
visible = false

[fill.budget]                    # theme.budget_fill
color = "lightgrey"
opacity = 0.3

[legend]                         # theme.legend
position = "auto"
fontsize = 10
```

| Section | Sets | Fields |
|---------|------|--------|
| `base` | Built-in theme to start from | `"default"`, `"nord"` |
| `[font]` | Text and math font | `text`, `math` |
| `[color]` | Theme colours, e.g. `ic` → `ic_color` | colour strings |
| `[stroke.<name>]` | `theme.<name>_stroke` | `width`, `style`, `color`, `arrow`, `opacity` |
| `[marker.<name>]` | `theme.<name>_marker` | `color`, `size`, `shape`, `opacity` |
| `[label.<name>]` | `theme.<name>_label` | `position`, `offset`, `color`, `fontsize`, `visible`, `opacity` |
| `[fill.<name>]` | `theme.<name>_fill` | `color`, `opacity` |
| `[legend]` | `theme.legend` | `position`, `fontsize`, `frame`, `columns`, `visible`, `opacity` |

`equilibrium` is accepted for `eq` (`[marker.equilibrium]`,
`[color] equilibrium`). A wrong section, name, or field raises an error that
lists the valid choices.

## Loading

```python
from econ_viz import Canvas, Config

Config.load("econ-viz.toml").use()     # diagrams created from now on
Canvas(x_max=20, y_max=15)             # uses the file's settings

theme = Config.load("econ-viz.toml").theme
Canvas(theme=theme)                    # or one diagram only

Config.reset()                         # back to the built-in defaults
```

Arguments passed to a method still win over the file: with the settings above,
`add_budget(..., stroke=Stroke(width=1))` draws a 1 pt line in the file's style.

## Command line

`econ-viz init` writes a commented template that lists every setting name,
and `econ-viz plot` reads the same file with `--config`:

```bash
uv run econ-viz init                       # writes econ-viz.toml
uv run econ-viz plot --model cobb-douglas --px 2 --py 3 --income 30 \
    --config econ-viz.toml --output cd.png
```
