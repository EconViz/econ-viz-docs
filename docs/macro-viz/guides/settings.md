---
seo_title: "Settings"
---

# Settings

<span id="sec-settings"></span>

`macro-viz` reads the shared `econ-viz.toml`. `mosaickit` parses and checks the file; `macro-viz` only declares what it takes, under `[macro]`.

<!-- api: macro_viz.guides_settings_1 -->

A key left out keeps the built-in default, and without any file the figures use the built-in colours.

```python
from macro_viz import Config

Config.load("econ-viz.toml").use()
```

```toml
base = "manual"            # shared look: black and white on white

[font]
text = "serif"
math = "texgyrepagella-math.otf"

[fonts]
serif = ["texgyrepagella-regular.otf", "texgyrepagella-italic.otf"]

[macro]
language = "en"            # en, zh-TW or zh-CN

[macro.stroke]
curve = 3.5                # points

[macro.text]
scale = 1.5                # multiplies every text size
```

The figures of these pages are drawn from the files `config/econ-viz.toml`, `config/econ-viz.zh-TW.toml` and `config/econ-viz.zh-CN.toml` ([download the examples](#sec-download)), which differ in the fonts and the language only.

## Shared keys

`base`, `[font]`, `[fonts]`, `background`, `axis` and `label` are shared by all EconViz packages and are documented with `mosaickit`. There is no dark theme: the background is always white.

## The `[macro]` tables

<span id="sec-macro-tables"></span>

<span id="tab-macro"></span>

| Key | Meaning | Default |
| --- | --- | --- |
| `palette` | Colour model for macro-viz only; wins over `base` | the base's |
| `language` | Language of built-in figure text: `en`, `zh-TW` or `zh-CN` | `en` |
| `color.<role>` | Colour of a role: `background`, `axis`, `label`, `primary`, `secondary`, `tertiary` | the theme's |
| `stroke.curve` | Width of a heavy theory curve, in points | 3.5 |
| `stroke.shifted` | Width of a curve after a change (thin, solid) | 1.0 |
| `stroke.arrow` | Width of a movement arrow (solid, thinner than a curve) | 1.0 |
| `stroke.guide` | Width of a dotted guide | 1.0 |
| `stroke.line45` | Width of the 45-degree line of a single-panel figure | 0.8 |
| `stroke.diagonal` | Width of the 45-degree line of linked panels | 0.6 |
| `stroke.link` | Width of a dashed projection link between linked panels | 0.7 |
| `marker.point` | Diameter of an equilibrium dot, in points | 6.5 |
| `text.scale` | Multiplies every text size | 1.0 |
| `label.<group>.<side>` | Move a label group ([Moving labels by default](labels.md#sec-nudges)) | none |

Colours name a role of the theme, so `manual` gives black and white and the colour themes give colour. A curve after a change is always thin and solid, a parallel shift is a straight arrow and a curved arrow means rotation only; settings change widths, never these conventions.

## Themes in code

<!-- api: macro_viz.guides_settings_2 -->

`get_theme(name)` builds the `mosaickit` theme of a shared theme name such as `"manual"`, with the macro roles (`macro.curve.primary`, `macro.curve.primary.shifted`, `macro.movement`, `macro.point`, `macro.guide`, ...). `list_themes()` lists the names. `MANUAL_THEME` is the black-and-white one.

```python
from macro_viz.themes import MANUAL_THEME, list_themes

list_themes()
MANUAL_THEME.resolve("macro.movement", fallback_category="path").stroke
```

<span id="sec-download"></span>

## The examples

The examples archive holds `examples/scripts/*.py`, the sample numbers `examples.toml` and the three settings files. Every script takes `--output`, `--config`, `--data` and `--suffix`; `--help` lists them. Nothing is written into the scripts: the numbers come from `examples.toml`.

<div class="ev-downloads"><a class="ev-download" href="../../assets/macro-viz/macro-viz-examples.zip" download aria-label="Download the examples"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the examples</span></a></div>

```bash
uv run python examples/scripts/islm.py --output out --config examples/econ-viz.toml
```
