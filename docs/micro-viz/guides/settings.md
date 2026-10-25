---
seo_title: "Settings"
---

# Settings

<span id="sec-settings"></span>

`micro-viz` reads the shared `econ-viz.toml`. `mosaickit` parses and checks the file; `micro-viz`
only declares what it takes, under `[micro]`. Load the file once and every figure made without an
explicit `theme` uses it:

```python
from micro_viz import Config

Config.load("econ-viz.toml").use()
```

Relative paths are resolved against the file's directory. A key left out keeps the built-in
default, and without any file the output is the same as before settings existed.

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

## Shared keys

`base`, `[font]`, `[fonts]`, `background`, `axis` and `label` are shared by all EconViz packages
and documented in [Themes and configuration](../../mosaickit/guides/themes.md). There is no dark
theme: the background is always white.

## The `[micro]` tables

| Key | Meaning | Default |
| --- | --- | --- |
| `language` | Language of built-in figure text | `en` |
| `color.<element>` | Colour of one element (below) | the theme's |
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
| `label.<group>.<side>` | Move a label group, see [Labels and placement](labels.md#sec-nudges) | none |

The colour elements are `axis`, `label`, `guide`, `marker`, `total`, `average`, `marginal`,
`variable`, `fixed`, `price`, `region_light`, `region_mid` and `region_dark`. Each takes a theme
role, so `manual` gives black and white and `default` gives colour.

A curve after a change is always thin and solid, a parallel shift is a straight arrow, and a
curved arrow means rotation only; settings change widths, never these conventions.

## Region fill

The marginal-return regions of the production figures can be shaded or not, shaded to the top of
the plot or only under the curve, and each region can take its own colour.

```python
from dataclasses import replace

from micro_viz import shared_theme, total_product_canvas

theme = replace(shared_theme("manual"), region_extent="curve")
total_product_canvas(
    result, theme=theme, region_colors={"increasing": "#bbbbbb", "diminishing": "#dddddd"}
)
```

`region_colors` maps a region kind (`increasing`, `diminishing`, `negative`) to a colour; a kind
left out keeps its theme shade.

![Shade to the top](../../assets/micro-viz/en/production/total_product.svg){ .ev-figure-sm }

![Shade under the curve](../../assets/micro-viz/en/production/total_product_under_curve.svg){ .ev-figure-sm }
