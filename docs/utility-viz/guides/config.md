---
seo_title: "Settings File"
description: "Keep utility-viz diagram styles in an utility-viz.toml file and load them once with Config."
---

# Settings File

Keep your colours, lines, labels, and legend settings in an `utility-viz.toml`
file and load them once, instead of passing the same arguments to every
method.

## Format

Section names match Theme properties, and fields match the arguments of the
style objects. Anything left out keeps the built-in default.

```toml
# utility-viz.toml
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

`Config` bundles a theme with the font choices. Read it from a file, then make it the default for every diagram or hand its theme to one `Canvas`.

### Reading a file {#config_load data-toc-label="Reading a file"}

Reads one TOML file into a `Config`.

<!-- api: config.load -->

??? example "View example"

    ```python
    from utility_viz import Config

    config = Config.load("utility-viz.toml")
    theme = config.theme
    ```

### Finding the file {#config_discover data-toc-label="Finding the file"}

Looks for the file in order: the explicit path, then `utility-viz.toml`, then the built-in defaults. Unlike `Config.load`, it never fails when no file exists.

<!-- api: config.discover -->

??? example "View example"

    ```python
    from utility_viz import Config

    # falls back to the built-in defaults
    config = Config.discover()
    ```

### Applying it {#config_use data-toc-label="Applying it"}

Makes this `Config` the default for diagrams created from now on, and returns it. To affect a single diagram only, pass its `theme` to `Canvas(theme=...)`.

<!-- api: config.use -->

??? example "View example"

    ```python
    from utility_viz import Canvas, Config

    # diagrams created from now on
    Config.load("utility-viz.toml").use()
    # uses the file's settings
    Canvas(x_max=20, y_max=15)

    theme = Config.load("utility-viz.toml").theme
    # or one diagram only
    Canvas(theme=theme)
    ```

### Going back {#config_reset data-toc-label="Going back"}

Returns to the built-in defaults. `Config.active()` tells which `Config` is in use.

<!-- api: config.reset -->

<!-- api: config.active -->

??? example "View example"

    ```python
    from utility_viz import Config

    # back to the built-in defaults
    Config.reset()
    ```

Arguments passed to a method still win over the file: with the settings above,
`add_budget(..., stroke=Stroke(width=1))` draws a 1 pt line in the file's style.

## Command line

`utility-viz init` writes a commented template that lists every setting name,
and `utility-viz plot` reads the same file with `--config`:

```bash
uv run utility-viz init                       # writes utility-viz.toml
uv run utility-viz plot --model cobb-douglas --px 2 --py 3 --income 30 \
    --config utility-viz.toml --output cd.png
```
