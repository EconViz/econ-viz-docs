---
seo_title: "Change history"
---

<span id="sec-changelog"></span>

# Change history

This history lists releases that affect the use of `mosaickit` and
omits documentation-only changes. Following l3doc convention, each entry
is tagged where its feature is documented, so its page number points to
that documentation.

## 0.5.1

- Markers are drawn whole on the plot edge; markers centred outside the plot are left out [Layers and axes](../guides/layers.md)

## 0.5.0

- A dashed, dotted or dash-dot stroke dashes the shaft; the heads stay solid [Layers and axes](../guides/layers.md)
- `CanvasGrid` — `links` added [Parameters, grids and animation](../guides/parameters.md)

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

