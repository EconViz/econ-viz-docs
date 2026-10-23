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

| Name | Character and use |
| --- | --- |
| `manual` | The black and white of the EconViz manuals and the playground: white page, black axes and points, grey curves. For print and handouts |
| `default` | Colour-blind-friendly palette on a transparent background. The everyday choice |
| `colorblind` | The colours of `default` under an explicit name |
| `nord` | Cool colours of the Nord palette, for screens and slides |
| `paper` | Muted colours and finer lines on a transparent background, for papers |
| `monochrome` | Black only; layers told apart by line style and marker, for black-and-white printing |
| `presentation` | Brighter colours, with lines 1.5, markers 1.3 and labels 1.25 times as large, for projection |

The Python API, the `base` key of a configuration file and `--theme` on
the command line accept all seven names. The same name gives the same
look in every EconViz package: each theme gives a colour to a role (ink,
primary, constraint, accent, ...), and utility-viz decides which role each
element takes (`utility_viz.core.themes.roles`). Indifference curves take
primary, the budget line constraint, the equilibrium and other points
accent, and the axes and labels ink. Line widths and point sizes are
utility-viz's own; a theme only scales them.

There is no dark theme. `themes.dark`, `base = "dark"` and `--theme dark`
emit a `UtilityVizDeprecationWarning` and use `default` throughout 2.x;
set `background` under `[color]` for an opaque backdrop.

The default theme takes its colours from a colour-blind-friendly palette
[{thriveth} (2014)](../project/references.md#thriveth2014).

`themes.COLORBLIND_CYCLE_HEX` and `themes.COLORBLIND_CYCLE_RGB` give the
palette as hexadecimal and RGB values. Economics teaching leans heavily on
diagrams, so meaning should never rest on colour alone, or visually
impaired students cannot follow it [Kugler (1996)](../project/references.md#kugler1996).

The figures below show the same Cobb-Douglas diagram in five built-in themes, with the manual's line weights on a white page. `manual` is the look of every other figure in this manual, and `colorblind` has the colours of `default`.

```python
from dataclasses import replace

from utility_viz import Canvas, levels, solve, themes
from utility_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.5, beta=0.5)
eq = solve(model, px=2.0, py=3.0, income=30.0)

# theme colours with manual line weights
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

<figure class="ev-fig" markdown>

![The `default` theme](../../assets/utility-viz/agora/themes/default.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/utility-viz/agora/themes/default.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>The `default` theme</figcaption>

</figure>

```python
from dataclasses import replace

from utility_viz import Canvas, levels, solve, themes
from utility_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.5, beta=0.5)
eq = solve(model, px=2.0, py=3.0, income=30.0)

# theme colours with manual line weights
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

<figure class="ev-fig" markdown>

![The `nord` theme](../../assets/utility-viz/agora/themes/nord.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/utility-viz/agora/themes/nord.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>The `nord` theme</figcaption>

</figure>

```python
from dataclasses import replace

from utility_viz import Canvas, levels, solve, themes
from utility_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.5, beta=0.5)
eq = solve(model, px=2.0, py=3.0, income=30.0)

# theme colours with manual line weights
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

<figure class="ev-fig" markdown>

![The `paper` theme](../../assets/utility-viz/agora/themes/paper.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/utility-viz/agora/themes/paper.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>The `paper` theme</figcaption>

</figure>

```python
from dataclasses import replace

from utility_viz import Canvas, levels, solve, themes
from utility_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.5, beta=0.5)
eq = solve(model, px=2.0, py=3.0, income=30.0)

# theme colours with manual line weights
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

<figure class="ev-fig" markdown>

![The `monochrome` theme](../../assets/utility-viz/agora/themes/monochrome.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/utility-viz/agora/themes/monochrome.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>The `monochrome` theme</figcaption>

</figure>

```python
from dataclasses import replace

from utility_viz import Canvas, levels, solve, themes
from utility_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.5, beta=0.5)
eq = solve(model, px=2.0, py=3.0, income=30.0)

# theme colours with manual line weights
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

<figure class="ev-fig" markdown>

![The `presentation` theme](../../assets/utility-viz/agora/themes/presentation.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/utility-viz/agora/themes/presentation.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>The `presentation` theme</figcaption>

</figure>

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
`Canvas`, write the style once in an `econ-viz.toml` at the project root.
Python, the command line and every other EconViz package read the same file;
`mosaickit` parses it for all of them.

The top level of the file holds what every package shares: `base`, `[font]`,
`[fonts]` and the `background`, `axis` and `label` colours in `[color]`.
utility-viz keeps its own settings under `[utility]`; other packages keep
theirs in their own table, such as `[principle]`, which utility-viz skips.

+ *Create a template.* Run the following in the project root. It writes a
  commented `econ-viz.toml` listing the names and fields each table
  accepts:

  ```bash
  utility-viz init
  ```

  Every setting in the template starts commented out; keep only what you
  change and delete the rest.

+ *Pick a base theme.* `base` names the shared theme to start from
  ([Built-in themes](themes.md#tab-themes)); everything else overrides it. `base = "manual"` gives the
  black-and-white look of the manuals, so colours and widths need not be
  spelled out:

  ```toml
  base = "manual"
  ```

+ *Set the shared fonts and colours.* Fonts go under `[font]` as `text`
  (`"sans"`, `"serif"` or `"mono"`) and `math` (the path of a math font),
  and font files under `[fonts]` as `sans`, `serif` and `mono`, each a file
  or a list of files. A relative path is read from the folder of the TOML
  file:

  ```toml
  [font]
  text = "serif"
  math = "fonts/texgyrepagella-math.otf"

  [fonts]
  serif = ["fonts/texgyrepagella-regular.otf", "fonts/texgyrepagella-bold.otf"]

  [color]
  background = "#ffffff"
  ```

+ *Override utility-viz's elements.* Write only the fields you change,
  under `[utility]`:

  ```toml
  [utility.color]
  ic = "#1B4F72"
  eq = "#C0392B"

  [utility.stroke.budget]
  width = 1.6
  style = "dashed"

  [utility.marker.eq]
  size = 5

  [utility.label.point]
  fontsize = 11
  position = "right"
  top = "2pt"
  ```

  Table names map to theme properties: `ic` under `[utility.color]` sets
  `ic_color`, and `[utility.stroke.budget]` sets `theme.budget_stroke`. The
  fields inside a table are the arguments of `Stroke`, `Marker`, `Label`,
  `Fill` or `Legend` ([Styles](canvas.md#sec-styles)); `top`, `bottom`, `left` and `right` in
  `[utility.label.<name>]` nudge every label of that kind by a length in
  pt, mm, cm or in. Fields you leave out keep the base theme's values.

+ *Use it from Python.* Load it once, before creating any diagram:

  ```python
  from utility_viz import Config

  Config.load("econ-viz.toml").use()
  ```

  Every `Canvas`, `Figure`, `DemandDiagram` and `EdgeworthBox` created
  afterwards uses these settings; `Config.reset()` restores the defaults.
  `mosaickit.econ_toml.use("econ-viz.toml")` loads the file for every
  installed EconViz package at once.

+ *Use it from the command line.* `utility-viz plot` reads
  `econ-viz.toml` from the current directory on its own; pass another
  file with `--config`:

  ```bash
  utility-viz plot --config econ-viz.toml --model cobb-douglas \
    --px 2 --py 3 --income 30 --output figure.png
  ```

Settings apply in this order, highest first: arguments passed to `Canvas`
or a drawing method, then the configuration file, then the base theme. For
example, `Canvas(theme=themes.default)` ignores the file's theme.

A mistake in the file makes `Config.load()` raise `InvalidParameterError`
naming the file and the table, with the closest name when one is close. For
instance, writing `[utility.stroke.budgt]` for `[utility.stroke.budget]`
gives:

```text
econ-viz.toml: [utility.stroke.budgt] no such setting; did you mean 'budget'? (choose: axis, box, budget, ...)
```

### File lookup

<span id="sec-config-lookup"></span>

<!-- api: agora.utility_viz.guides_themes_4 -->

Find and read a configuration file without failing when there is none.

`Config.load()`, `Config.discover()` and `utility-viz plot` resolve the
file in this order:

+ the path given explicitly (`Config.load("file.toml")` or `--config`),
  which must exist and is the only file read;
+ `econ-viz.toml` in the current directory (or `directory=`);
+ `utility-viz.toml`, the name the 2.0 betas used up to 2.0.0b6, with a
  deprecation warning;
+ the built-in defaults.

When both files exist, `econ-viz.toml` wins and `utility-viz.toml` is
ignored with a warning. The two functions differ only when no file is found:
`Config.load()` raises `InvalidParameterError` ("config file not found"),
as in 1.x, while `Config.discover()` returns the built-in defaults.

Files written for 2.0.0b7 and earlier keep utility-viz's tables at the top
level (`[color] ic`, `[stroke.budget]`, `[legend]`, ...). They are still
read until 3.0, with one `UtilityVizDeprecationWarning` per load naming
the new place of each table; a key under `[utility]` wins over the same key
at the top level. `utility-viz init --migrate` moves the tables under
`[utility]` and keeps the comments ([Creating a configuration file](../getting-started/cli.md#sec-cli-init)).
