---
seo_title: "Change history"
---

<span id="sec-changelog"></span>

# Change history

Release history of `mosaickit`. Documentation-only changes are not
listed; each entry is tagged where the feature it describes is documented,
following l3doc convention, so the page number is the real page.

## 1.0.0rc6

- Packages declare an `econ_toml.Schema` and mosaickit parses `econ-viz.toml` for them; shared themes (`mosaickit.themes`) and label nudges (`Nudge`) added [Introduction](../guides/introduction.md)
- `Nudge` — Added [Region and point labels](../guides/labels.md)
- `Schema` — Added; packages declare their keys and mosaickit parses the file [Themes and configuration](../guides/themes.md)
- `get_tokens` — Added [Themes and configuration](../guides/themes.md)

## 1.0.0rc5

- New `mosaickit.econ_toml` reads the sections of `econ-viz.toml` that every EconViz package shares [Introduction](../guides/introduction.md)

## 1.0.0rc4

- Parsed fonts are shared across symbolic links; a configured title keeps the baseline Matplotlib gives it [Introduction](../guides/introduction.md)

## 1.0.0rc3

- Titles and text that mixes words with `$...$` math are set in the configured text fonts, so Chinese no longer comes out as boxes [Introduction](../guides/introduction.md)

## 1.0.0rc2

- Faster drawing with identical output: label placement, point validation and Matplotlib's mathtext parsing use arrays and caches scoped to one draw or save [Introduction](../guides/introduction.md)

## 1.0.0rc1

- Removed the deprecated `Animation` and `TextStyle.family` (see the chapters on parameters and styles) [Introduction](../guides/introduction.md)
- `TextStyle` — Removed `family`; choose `font` and replace the files with `TextFonts`. Pass the fields by name; a scene document that holds `"family": null` still loads, one that names a family is refused [Styles and colors](../guides/styles.md)
- `Animation` — Removed `Animation`, `Animation.sweep()` and the Matplotlib playback helper, deprecated in 0.6.0; `kinetickit` animates scenes, and `CanvasGrid.sweep()` and `canvas.bind()` still draw one frame per value [Parameters and grids](../guides/parameters.md)

## 0.9.2

- `TikZ` — `font` maps to the TeX font families [Styles and colors](../guides/styles.md)

## 0.9.1

- `TextStyle` — New `font` field; `family` is deprecated [Styles and colors](../guides/styles.md)
- `TextFonts` — `serif` and `mono` slots; defaults to DejaVu [Styles and colors](../guides/styles.md)

## 0.9.0

- `TextStyle` — `weight` is no longer deprecated [Styles and colors](../guides/styles.md)
- `TextFonts` — Added; one list of files for sans [Styles and colors](../guides/styles.md)
- `Config` — `Config.math_font` and `Config.fonts` added [Themes and configuration](../guides/themes.md)

## 0.8.0

- `DashStyle` — `DashStyle` and `ArrowStyle` accept short forms, so a package can use them as its own line and arrow style enums [Styles and colors](../guides/styles.md)

## 0.5.1

- Markers are drawn whole on the plot edge; markers centred outside the plot are left out [Layers and axes](../guides/layers.md)

## 0.5.0

- A dashed, dotted or dash-dot stroke dashes the shaft; the heads stay solid [Layers and axes](../guides/layers.md)
- `CanvasGrid` — `links` added [Parameters and grids](../guides/parameters.md)

## 0.4.0

- Inside brace labels move out on a leader when nothing past the tip is free (they used to overlap and warn) [Axis annotations](../guides/annotations.md)

## 0.3.2

- A region counts as the point's own only when the point is strictly inside it; a point on a region's edge keeps its label outside [Region and point labels](../guides/labels.md)

## 0.3.1

- A point label may sit inside a filled region that contains its point [Region and point labels](../guides/labels.md)

## 0.3.0

- Axis titles are placed past the arrow tips instead of centred on them [Layers and axes](../guides/layers.md)
- `mosaickit` — Text outside an axis is laid out in columns: marks, then outside braces (one column per lane), then notes; marks and notes are spread so none overlap [Axis annotations](../guides/annotations.md)
- The default theme gains the `axes.note` role [Axis annotations](../guides/annotations.md)
- `mosaickit` — Point labels are placed before region labels, so region callouts avoid them; label text is measured with its rotation [Region and point labels](../guides/labels.md)
- `Placement.leader` may be `None` [Region and point labels](../guides/labels.md)
- `place_point_label` and `place_beside` added [Region and point labels](../guides/labels.md)
- `Palette` — Themes and styles refer to colors by palette name, resolved against `Config.palette` when the render plan is built; an unknown name raises `ConfigurationError` naming the role, field and palette [Styles and colors](../guides/styles.md)
- `Config.palette` added, defaulting to `DEFAULT_PALETTE` [Themes and configuration](../guides/themes.md)
- `Config.load` — TOML accepts a `[palette]` table, and style colors may be palette names, checked when the file is loaded [Themes and configuration](../guides/themes.md)
- `expand` added (default `True`) [Rendering](../guides/rendering.md)

## 0.2.0

- `mosaickit` — Built-in renderers are loaded by name on first use; the core no longer imports the Matplotlib backend [Installation](../installation.md)
- `LayoutWarning` — Added, emitted when no callout position avoids every obstacle [Canvases and scenes](../guides/canvas.md)
- `clip` added (default `True`); arrowheads no longer redraw a solid shaft over the end of the path, so dashed arrows stay dashed [Layers and axes](../guides/layers.md)
- `anchor` accepts the four corners `top-left`, `top-right`, `bottom-left`, `bottom-right` [Layers and axes](../guides/layers.md)
- Arrowheads are no longer clipped to the axes [Layers and axes](../guides/layers.md)
- Axis presets draw filled triangle arrowheads; axis lines are not clipped, so they keep their full width on the plot edge [Layers and axes](../guides/layers.md)
- `mosaickit.layout` — Added: the pure geometry behind label placement [Layout geometry](../guides/geometry.md)
- `DEFAULT_PALETTE` — Added: a grey ramp, `white`, `blue`, `red` and `teal`; the default theme takes its colors from it, so `primary`, `secondary` and `accent` become blue, red and teal [Styles and colors](../guides/styles.md)
- `resolve` — `themes.resolve` accepts `overrides`, applied in order after the theme [Themes and configuration](../guides/themes.md)
- `Layer` — Layers declare `style_slots`; Matplotlib drawing is driven by a per-type registry [Rendering](../guides/rendering.md)

## 0.1.1

- Package metadata on PyPI links the homepage, repository, issue tracker, changelog and release notes [Introduction](../guides/introduction.md)

## 0.1.0

- First release: immutable scenes and layers, sparse styles, namespaced themes, canvases, spanning grids, parameter expressions, animation, Matplotlib rendering with job-scoped caches, and strict TOML configuration [Introduction](../guides/introduction.md)

