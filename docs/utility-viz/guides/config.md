---
seo_title: "Settings File"
description: "Keep utility-viz diagram styles in econ-viz.toml, the settings file every EconViz package shares, and load them once with Config."
---

# Settings File

Keep your colours, lines, labels, and legend settings in an `econ-viz.toml`
file and load them once, instead of passing the same arguments to every
method. Every EconViz package reads the same file, and mosaickit parses and
checks it for all of them.

## Format

The top level holds what every EconViz package shares: `base`, `[font]`,
`[fonts]` and the `background`, `axis` and `label` colours in `[color]`.
utility-viz keeps its own settings under `[utility]`; other packages keep
theirs in their own table, such as `[principle]`, which utility-viz skips.
Table names match Theme properties, and fields match the arguments of the
style objects. Anything left out keeps the built-in default.

```toml
# econ-viz.toml
base = "manual"                  # a shared theme (see below)

[font]
text = "serif"
math = "fonts/texgyrepagella-math.otf"

[fonts]
serif = ["fonts/texgyrepagella-regular.otf", "fonts/texgyrepagella-bold.otf"]

[color]                          # shared by every package
background = "#ffffff"
axis = "#1a1a1a"
label = "#1a1a1a"

[utility.color]
ic = "#2E86AB"
budget = "#6C3483"
equilibrium = "#C0392B"

[utility.stroke.budget]          # theme.budget_stroke
width = 1.5
style = "solid"

[utility.stroke.ic]              # theme.ic_stroke
width = 1.8
opacity = 0.9

[utility.marker.equilibrium]     # theme.eq_marker
size = 5

[utility.label.point]            # theme.point_label
fontsize = 12
position = "top-right"
top = "2pt"

[utility.label.origin]
visible = false

[utility.fill.budget]            # theme.budget_fill
color = "lightgrey"
opacity = 0.3

[utility.legend]                 # theme.legend
position = "auto"
fontsize = 10

[principle]                      # read by principle-viz, skipped here
language = "en"
```

| Table | Sets | Fields |
|-------|------|--------|
| `base` | Shared theme to start from | `"manual"`, `"default"`, `"colorblind"`, `"monochrome"`, `"nord"`, `"paper"`, `"presentation"` |
| `[font]` | Text and math font, shared | `text` (`"sans"`, `"serif"`, `"mono"`), `math` (a math font file) |
| `[fonts]` | Font files, shared | `sans`, `serif`, `mono`: a file or a list of files |
| `[color]` | Shared colours | `background`, `axis`, `label` |
| `[utility.color]` | Theme colours, e.g. `ic` → `ic_color` | colour strings |
| `[utility.stroke.<name>]` | `theme.<name>_stroke` | `width`, `style`, `color`, `arrow`, `opacity` |
| `[utility.marker.<name>]` | `theme.<name>_marker` | `color`, `size`, `shape`, `opacity` |
| `[utility.label.<name>]` | `theme.<name>_label` | `text`, `position`, `offset`, `color`, `fontsize`, `visible`, `opacity`, `top`, `bottom`, `left`, `right` |
| `[utility.fill.<name>]` | `theme.<name>_fill` | `color`, `opacity` |
| `[utility.legend]` | `theme.legend` | `position`, `fontsize`, `frame`, `columns`, `visible`, `opacity` |

`equilibrium` is accepted for `eq` (`[utility.marker.equilibrium]`,
`[utility.color] equilibrium`). Relative paths are read from the folder of
the file. A mistake names the file and the table and suggests the closest
name:

```text
econ-viz.toml: [utility.stroke.budgt] no such setting; did you mean 'budget'? (choose: axis, box, budget, ...)
```

## Themes

`base` picks one of the seven shared EconViz themes. The same name gives the
same look in utility-viz, principle-viz and the other packages, because each
theme gives a colour to a role and each package decides which role its
elements take. `[utility.*]` tables still change single elements on top.

| `base` | Look | Use |
|--------|------|-----|
| `manual` | White page, black axes and points, grey curves | The black-and-white look of the manuals and the playground; print and handouts |
| `default` | Colour-blind-friendly palette, transparent background | Everyday figures |
| `colorblind` | The colours of `default` | When the name should say it |
| `monochrome` | Black only; line style and marker tell layers apart | Black-and-white printing |
| `nord` | Cool Nord colours | Screens and slides |
| `paper` | Muted colours, finer lines | Papers |
| `presentation` | Brighter colours; lines 1.5, markers 1.3 and labels 1.25 times as large | Projection |

There is no dark theme: `base = "dark"` warns and uses `default`. Set
`[color] background` for an opaque backdrop. With `base = "manual"` the
manuals' colours and widths need not be spelled out:

```toml
base = "manual"

[font]
text = "serif"
```

## Label nudges

`top`, `bottom`, `left` and `right` move a label after automatic placement,
so the package still picks the spot and you only fine-tune it. In the file
they set a default for every label of one kind, in pt, mm, cm or in:

```toml
[utility.label.point]
top = "2pt"
```

In code, a `Label` moves one label by a number of points or a string such
as `"10pt"`, `"0.5em"` (the label's font size) or `"2mm"`; it replaces the
file's value for that direction:

```python
from utility_viz import Label

cvs.add_equilibrium(eq, label=Label(top="10pt"))
cvs.add_point(5, 3, label=Label(text="A", left="6pt"))
```

principle-viz takes the same nudges, for example
`MarketFigure(labels={"market.equilibrium": Label(top="4pt")})`.

## Older files

Files written for utility-viz 2.0.0b7 and earlier keep utility-viz's tables
at the top level (`[color] ic`, `[stroke.budget]`, `[legend]`, ...). They
are still read, with one deprecation warning per load naming the new place
of each table, until 3.0; a key under `[utility]` wins over the same key at
the top level. A `utility-viz.toml`, the name the 2.0 betas used up to
2.0.0b6, is also still read with a warning. `utility-viz init --migrate`
moves the tables under `[utility]` and keeps your comments:

```bash
uv run utility-viz init --migrate
```

It rewrites `utility-viz.toml` into `econ-viz.toml` and keeps the old file,
or, without one, rewrites an old-layout `econ-viz.toml` in place.

## Loading

`Config` bundles a theme with the font choices. Read it from a file, then make it the default for every diagram or hand its theme to one `Canvas`.

### Reading a file {#config_load data-toc-label="Reading a file"}

Reads one TOML file into a `Config`.

<!-- api: config.load -->

??? example "View example"

    ```python
    from utility_viz import Config

    config = Config.load("econ-viz.toml")
    theme = config.theme
    ```

### Finding the file {#config_discover data-toc-label="Finding the file"}

Looks for the file in order: the explicit path, then `econ-viz.toml`, then the older `utility-viz.toml` (with a warning), then the built-in defaults. Unlike `Config.load`, it never fails when no file exists.

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
    Config.load("econ-viz.toml").use()
    # uses the file's settings
    Canvas(x_max=20, y_max=15)

    theme = Config.load("econ-viz.toml").theme
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
uv run utility-viz init                       # writes econ-viz.toml
uv run utility-viz plot --model cobb-douglas --px 2 --py 3 --income 30 \
    --config econ-viz.toml --output cd.png
```

`mosaickit.econ_toml.use("econ-viz.toml")` loads the file for every installed EconViz package at once.
