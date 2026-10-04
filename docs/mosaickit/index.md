---
seo_title: "mosaickit: Domain-Neutral Diagram Scenes and Rendering"
description: "mosaickit is a domain-neutral Python toolkit for assembling two-dimensional diagrams from scenes, layers, styles, parameters and renderers."
---

# mosaickit

`mosaickit` is a domain-neutral toolkit for assembling two-dimensional diagrams from reusable scenes, layers,
styles, parameters and renderers.

Domain libraries define their own models and semantic roles; mosaickit composes their visual layers and renders the
result. It knows nothing about any domain and does not depend on a model package or a curve-fitting library.

![A diagram built from mosaickit layers](../assets/mosaickit/diagram.svg){ width="360" }

| | |
|---|---|
| Documented version | 0.5.1 |
| Python | 3.10 or later (the project supports 3.10 to 3.13) |
| Dependencies | numpy, matplotlib (and tomli on Python 3.10) |
| Used by | [utility-viz](../utility-viz/index.md), [principle-viz](../principle-viz/index.md) |
| Source | [github.com/EconViz/mosaickit](https://github.com/EconViz/mosaickit) |
| License | MIT |

## What it covers

- A small scene graph: `PathLayer`, `FillLayer`, `MarkerLayer`, `TextLayer`, `ArrowLayer`, `LegendLayer` and
  `GroupLayer`
- Labels placed so they cover nothing (`RegionLabelLayer`, `PointLabelLayer`) and annotations on an axis
  (`AxisMarkLayer`, `AxisNoteLayer`, `BraceLayer`, `SpanBraceLayer`)
- Axes helpers such as `quadrant_axes()`, `crosshair_axes()` and `box_frame()`
- Styles, themes and palettes, with colours that can be given by name
- Parameters and expressions, `CanvasGrid` layouts and `Animation` sweeps
- A built-in Matplotlib renderer for PNG, SVG and PDF, and a `Renderer` protocol for other backends

## Scope

mosaickit owns domain-neutral scene composition, styles, themes, parameter binding, grid layout, animation frames,
renderer contracts and static or animated output. Domain semantics belong to the packages built on it. Curve
construction and native TikZ path generation belong to geometry packages such as
[bezierkit](../bezierkit/index.md).

## Next steps

<div class="grid cards" markdown>

-   :material-download: **Installation**

    Install the package with pip or uv.

    [:octicons-arrow-right-24: Installation](installation.md)

-   :material-rocket-launch-outline: **Quick start**

    Build a canvas from layers and save it as SVG.

    [:octicons-arrow-right-24: Quick start](quickstart.md)

</div>
