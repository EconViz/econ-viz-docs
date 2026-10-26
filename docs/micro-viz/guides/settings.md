---
seo_title: "Settings"
---

# Settings

<span id="sec-settings"></span>

`micro-viz` reads the shared `econ-viz.toml`. `mosaickit` parses and checks the file; `micro-viz` only declares what it takes, under `[micro]`.

<!-- api: micro_viz.guides_settings_1 -->

A theme loaded from an `econ-viz.toml` file. `load()` reads `path`, or `econ-viz.toml` in the working directory. `use()` makes it the default, so every figure made without an explicit `theme` uses it, and returns the config. Relative paths in the file are resolved against the file's directory.

```python
from micro_viz import Config

Config.load("econ-viz.toml").use()
```

A key left out keeps the built-in default, and without any file the output is the same as before settings existed.

```toml
base = "manual"            # shared look: black and white on white

[font]
text = "serif"
math = "texgyrepagella-math.otf"

[fonts]
serif = ["texgyrepagella-regular.otf", "texgyrepagella-italic.otf"]

[micro]
language = "en"            # en, zh-TW or zh-CN

[micro.stroke]
curve = 3.5                # points

[micro.region]
fill = true
extent = "top"
```

The figures of these pages are drawn from the files `config/econ-viz.toml`, `config/econ-viz.zh-TW.toml` and `config/econ-viz.zh-CN.toml`, which differ in the fonts and the language only.

## Shared keys

`base`, `[font]`, `[fonts]`, `background`, `axis` and `label` are shared by all EconViz packages and are documented with `mosaickit`. There is no dark theme: the background is always white.

## The `[micro]` tables

<span id="sec-micro-tables"></span>

<span id="tab-micro"></span>

| Key | Meaning | Default |
| --- | --- | --- |
| `language` | Language of built-in figure text | `en` |
| `color.<element>` | Colour of one element (see below) | the theme's |
| `stroke.curve` | Width of a main curve, in points | 3.5 |
| `stroke.dashed` | Width of a dashed curve | 2.0 |
| `stroke.guide` | Width of axes and guide lines | 1.0 |
| `stroke.after` | Width of a curve after a change (thin, solid) | 1.5 |
| `stroke.arrow` | Width of a movement arrow (solid) | 1.2 |
| `marker.diameter` | Diameter of a marked point | 6.5 |
| `brace.gap` | Gap between a shaded region and its brace | 4.0 |
| `opacity.region` | Opacity of shaded regions, above 0 and at most 1 | 0.2 |
| `region.fill` | Shade the regions of a figure (`false` keeps only braces and names) | `true` |
| `region.extent` | `top` shades up to the top of the plot, `curve` only under the curve | `top` |
| `label.<group>.<side>` | Move a label group ([Moving labels by default](labels.md#sec-nudges)) | none |

The colour elements are `axis`, `label`, `guide`, `marker`, `total`, `average`, `marginal`, `variable`, `fixed`, `price`, `region_light`, `region_mid` and `region_dark`. Each takes a theme role, so `manual` gives black and white and `default` gives colour.

A curve after a change is always thin and solid, a parallel shift is a straight arrow, and a curved arrow means rotation only; settings change widths, never these conventions.

## Themes in code

<!-- api: micro_viz.guides_settings_2 -->

`PlotTheme` holds the look of one figure: colours, line widths, marker size, region shading, fonts and the language. `shared_theme(name)` builds one from a shared `mosaickit` theme name such as `"manual"`; `default_theme()` returns the theme a figure uses without an explicit one, that of the active `Config`.

## Region fill

<span id="sec-region-fill"></span>

The marginal-return regions of the production figures can be shaded or not, shaded to the top of the plot or only under the curve, and each region can take its own colour.

```python
from dataclasses import replace

from micro_viz import shared_theme, total_product_canvas

theme = replace(shared_theme("manual"), region_extent="curve")
total_product_canvas(
    result,
    theme=theme,
    region_colors={
        "increasing": "#bbbbbb",
        "diminishing": "#dddddd",
    },
)
```

`region_colors` maps a region kind (`increasing`, `diminishing`, `negative`) to a colour; a kind left out keeps its theme shade.

<span id="fig-region-top"></span>

<figure class="ev-fig" markdown>

![Shade to the top](../../assets/micro-viz/production/total_product.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/micro-viz/production/production.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>Shade to the top</figcaption>

</figure>

<span id="fig-region-curve"></span>

<figure class="ev-fig" markdown>

![Shade under the curve](../../assets/micro-viz/production/total_product_under_curve.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/micro-viz/production/production.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>Shade under the curve</figcaption>

</figure>
