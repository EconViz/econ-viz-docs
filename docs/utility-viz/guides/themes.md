---
seo_title: "Themes and configuration"
---

# Themes and configuration

<span id="sec-themes"></span>

A `Theme` defines the default look of a diagram; a `Config` loads theme
overrides and font settings from a TOML file. `Canvas`, `Figure`,
`DemandDiagram`, price-effect decompositions and `EdgeworthBox` share these
style objects.

## Built-in themes

<!-- api: agora.utility_viz.guides_themes_1 -->

The Python API provides the themes below. Theme objects are immutable; to
change a field, create a new `Theme` or override the field with a
`Config`.

<span id="tab-themes"></span>

| Name | Character |
| --- | --- |
| `default` | Colour-blind-friendly default palette |
| `colorblind` | Alias with the same palette as `default` |
| `nord` | Cool theme on the Nord palette |
| `paper` | Transparent background and fine lines for print |
| `monochrome` | Black and white; layers told apart by line style and marker |
| `presentation` | Larger labels, lines and markers for projection |
| `dark` | Dark background with matching foreground colours |

The Python API and the `base` key of a configuration file accept all seven
names (Passed directly to `--theme` on the command line, only the six themes other than the `colorblind` alias are accepted.).

The default theme takes its colours from a colour-blind-friendly palette
[{thriveth} (2014)](../project/references.md#thriveth2014).

`themes.COLORBLIND_CYCLE_HEX` and `themes.COLORBLIND_CYCLE_RGB` give the
palette as hexadecimal and RGB values. Economics teaching leans heavily on
diagrams, so meaning should never rest on colour alone, or visually
impaired students cannot follow it [Kugler (1996)](../project/references.md#kugler1996).

The figures below show the same Cobb-Douglas diagram in each built-in theme except `dark`, with the manual's line weights on a white page.

```python
from dataclasses import replace

from utility_viz import Canvas, levels, solve, themes
from utility_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.5, beta=0.5)
eq = solve(model, px=2.0, py=3.0, income=30.0)

# The theme's own colours and the manual's line weights on a white page
theme = replace(
    themes.default,
    background_color="#ffffff",
    ic_linewidth=2.6,
    budget_linewidth=2.6,
    eq_markersize=5.0,
)

cvs = Canvas(
    x_max=20,
    y_max=15,
    x_label="$x$",
    y_label="$y$",
    theme=theme,
)
cvs.add_utility(model, levels=levels.around(eq.utility, n=3))
cvs.add_budget(2.0, 3.0, 30.0, fill=True)
cvs.add_equilibrium(eq)
cvs.save("theme_default.png")
```

![The `default` theme.](../../assets/utility-viz/agora/themes/default.svg){ .ev-figure-sm }

```python
from dataclasses import replace

from utility_viz import Canvas, levels, solve, themes
from utility_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.5, beta=0.5)
eq = solve(model, px=2.0, py=3.0, income=30.0)

# The theme's own colours and the manual's line weights on a white page
theme = replace(
    themes.nord,
    background_color="#ffffff",
    ic_linewidth=2.6,
    budget_linewidth=2.6,
    eq_markersize=5.0,
)

cvs = Canvas(
    x_max=20,
    y_max=15,
    x_label="$x$",
    y_label="$y$",
    theme=theme,
)
cvs.add_utility(model, levels=levels.around(eq.utility, n=3))
cvs.add_budget(2.0, 3.0, 30.0, fill=True)
cvs.add_equilibrium(eq)
cvs.save("theme_nord.png")
```

![The `nord` theme.](../../assets/utility-viz/agora/themes/nord.svg){ .ev-figure-sm }

```python
from dataclasses import replace

from utility_viz import Canvas, levels, solve, themes
from utility_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.5, beta=0.5)
eq = solve(model, px=2.0, py=3.0, income=30.0)

# The theme's own colours and the manual's line weights on a white page
theme = replace(
    themes.paper,
    background_color="#ffffff",
    ic_linewidth=2.6,
    budget_linewidth=2.6,
    eq_markersize=5.0,
)

cvs = Canvas(
    x_max=20,
    y_max=15,
    x_label="$x$",
    y_label="$y$",
    theme=theme,
)
cvs.add_utility(model, levels=levels.around(eq.utility, n=3))
cvs.add_budget(2.0, 3.0, 30.0, fill=True)
cvs.add_equilibrium(eq)
cvs.save("theme_paper.png")
```

![The `paper` theme.](../../assets/utility-viz/agora/themes/paper.svg){ .ev-figure-sm }

```python
from dataclasses import replace

from utility_viz import Canvas, levels, solve, themes
from utility_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.5, beta=0.5)
eq = solve(model, px=2.0, py=3.0, income=30.0)

# The theme's own colours and the manual's line weights on a white page
theme = replace(
    themes.monochrome,
    background_color="#ffffff",
    ic_linewidth=2.6,
    budget_linewidth=2.6,
    eq_markersize=5.0,
)

cvs = Canvas(
    x_max=20,
    y_max=15,
    x_label="$x$",
    y_label="$y$",
    theme=theme,
)
cvs.add_utility(model, levels=levels.around(eq.utility, n=3))
cvs.add_budget(2.0, 3.0, 30.0, fill=True)
cvs.add_equilibrium(eq)
cvs.save("theme_monochrome.png")
```

![The `monochrome` theme.](../../assets/utility-viz/agora/themes/monochrome.svg){ .ev-figure-sm }

```python
from dataclasses import replace

from utility_viz import Canvas, levels, solve, themes
from utility_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.5, beta=0.5)
eq = solve(model, px=2.0, py=3.0, income=30.0)

# The theme's own colours and the manual's line weights on a white page
theme = replace(
    themes.presentation,
    background_color="#ffffff",
    ic_linewidth=2.6,
    budget_linewidth=2.6,
    eq_markersize=5.0,
)

cvs = Canvas(
    x_max=20,
    y_max=15,
    x_label="$x$",
    y_label="$y$",
    theme=theme,
)
cvs.add_utility(model, levels=levels.around(eq.utility, n=3))
cvs.add_budget(2.0, 3.0, 30.0, fill=True)
cvs.add_equilibrium(eq)
cvs.save("theme_presentation.png")
```

![The `presentation` theme.](../../assets/utility-viz/agora/themes/presentation.svg){ .ev-figure-sm }

## Custom themes

<!-- api: agora.utility_viz.guides_themes_2 -->

A `Theme` holds default colours, widths and styles for diagram elements.
Fields not given keep the class defaults; style arguments passed
explicitly to a drawing method take precedence over the theme.

`Theme` also holds colours and widths for rays, kinks, compensated budget
lines and price-effect arrows. `axis_stroke`, `drop_stroke`,
`projection_stroke`, `guide_stroke` and `box_stroke` hold the defaults of
other lines; markers, labels, fills and legends come from `Marker`, `Label`,
`Fill` and `Legend` properties ([Styles](canvas.md#sec-styles)).

## Configuration files

<!-- api: agora.utility_viz.guides_themes_3 -->

`Config.load()` reads a TOML file and returns a `Config`; `use()` makes it
the default for later diagrams, and `reset()` restores the built-in
defaults.

### Tutorial: one shared style

Figures in one set of lecture notes or one paper usually share their
colours and line styles. Rather than repeating the same arguments on every
`Canvas`, write the style once in an `utility-viz.toml` at the project root,
where both Python and the command line read it.

+ *Create a template.* Run the following in the project root. It writes a
  commented `utility-viz.toml` listing the names and fields each section
  accepts:

  ```bash
  utility-viz init
  ```

  Every setting in the template starts commented out; keep only what you
  change and delete the rest.

+ *Pick a base theme.* `base` names the built-in theme to start from
  ([Built-in themes](themes.md#tab-themes)); everything else overrides it:

  ```toml
  base = "paper"
  ```

+ *Override colours and styles.* Write only the fields you change:

  ```toml
  [color]
  ic = "#1B4F72"
  eq = "#C0392B"

  [stroke.budget]
  width = 1.6
  style = "dashed"

  [marker.eq]
  size = 5

  [label.point]
  fontsize = 11
  position = "right"
  ```

  Section names map to theme properties: `ic` under `[color]` sets
  `ic_color`, and `[stroke.budget]` sets `theme.budget_stroke`. The fields
  inside a section are the arguments of `Stroke`, `Marker`, `Label`, `Fill`
  or `Legend` ([Styles](canvas.md#sec-styles)). Fonts go under `[font]` as `text` and `math`.
  Fields you leave out keep the base theme's values.

+ *Use it from Python.* Load it once, before creating any diagram:

  ```python
  from utility_viz import Config

  # reads ./utility-viz.toml by default
  Config.load().use()
  ```

  Every `Canvas`, `Figure`, `DemandDiagram` and `EdgeworthBox` created
  afterwards uses these settings; `Config.reset()` restores the defaults.

+ *Use it from the command line.* `utility-viz plot` reads
  `utility-viz.toml` from the current directory on its own; pass another
  file with `--config`:

  ```bash
  utility-viz plot --config utility-viz.toml --model cobb-douglas \
    --px 2 --py 3 --income 30 --output figure.png
  ```

Settings apply in this order, highest first: arguments passed to `Canvas`
or a drawing method, then the configuration file, then the base theme. For
example, `Canvas(theme=themes.default)` ignores the file's theme.

A mistake in the file makes `Config.load()` raise `InvalidParameterError`
with the valid names. For instance, writing `[stroke.budgt]` for
`[stroke.budget]` gives:

```text
utility-viz.toml: [stroke.budgt]: no such setting (choose: axis, box, budget, ...)
```

### This manual's settings

<span id="sec-manual-toml"></span>

Every example in this manual loads `manual.toml` first. It sets the look of the figures: grey curves, black axes and guides, black points and a white page. It leaves the font out so that it runs anywhere; the figures use TeX Gyre Pagella, and without that font you get the default typeface.

```toml
# Settings for every figure in this manual
# Grey curves and black axes and guides and black points on a white background
# Load them before drawing
#
#     Config.load("manual.toml").use()
#
# Each section maps to a Theme property as described in the Themes chapter

base = "default"

# The font is TeX Gyre Pagella and it is not set here so the file runs on any machine
# Add [font] text = "TeX Gyre Pagella" if the font is installed

[color]
background = "#ffffff"
axis = "#1a1a1a"
label = "#1a1a1a"
ic = "#8c8c8c"              # indifference curves
secondary_ic = "#b8b8b8"    # the curves beside a highlighted one
path = "#1a1a1a"            # price- and income-consumption paths
budget = "#222222"
eq = "#1a1a1a"              # equilibrium and other points
ray = "#8c8c8c"
kink = "#8c8c8c"
sub_effect = "#8c8c8c"
inc_effect = "#8c8c8c"
compensated_budget = "#1a1a1a"
subsistence = "#8c8c8c"
contract = "#8c8c8c"
core = "#1a1a1a"
price = "#8c8c8c"
walrasian = "#1a1a1a"

[stroke.axis]
width = 1.0
style = "solid"
arrow = "-|>"

[stroke.ic]
width = 2.6

[stroke.secondary_ic]
width = 1.8
opacity = 1.0

[stroke.path]
width = 1.4

[stroke.budget]
width = 2.6

[stroke.ray]
width = 0.9

[stroke.substitution]
width = 1.8

[stroke.income]
width = 1.8

[stroke.compensated_budget]
width = 1.0

[stroke.contract]
width = 2.6

[stroke.price]
width = 2.6

[stroke.drop]               # guides from a point to the axes
width = 0.8
style = "dashed"
color = "#1a1a1a"

[stroke.projection]
width = 0.8
style = "dashed"
color = "#1a1a1a"

[stroke.guide]
width = 0.8
style = "dashed"
color = "#1a1a1a"

[marker.eq]
size = 5

[marker.point]
size = 5

[label.point]               # the text beside a point such as x* at the optimum
fontsize = 14
position = "right"
offset = 10

[fill.budget]
opacity = 0.08
```

### File lookup

<span id="sec-config-lookup"></span>

<!-- api: agora.utility_viz.guides_themes_4 -->

Find and read a configuration file without failing when there is none.

`Config.load()`, `Config.discover()` and `utility-viz plot` resolve the
file in this order:

+ the path given explicitly (`Config.load("file.toml")` or `--config`),
  which must exist and is the only file read;
+ `utility-viz.toml` in the current directory (or `directory=`);
+ the legacy `econ-viz.toml`, with a deprecation warning;
+ the built-in defaults.

When both files exist, `utility-viz.toml` wins and the legacy one is ignored
with a warning. The two functions differ only when no file is found:
`Config.load()` raises `InvalidParameterError` ("config file not found"),
as in 1.x, while `Config.discover()` returns the built-in defaults.
`utility-viz init --migrate` turns a legacy file into `utility-viz.toml`
([Creating a configuration file](../getting-started/cli.md#sec-cli-init)).
