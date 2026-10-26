---
seo_title: "Introduction"
---

# Introduction

<span id="sec-intro"></span>

`kinetickit` is a domain-neutral animation engine. It owns scenes, motions, deterministic frame scheduling, renderer capabilities, interactions, accessibility metadata and file export. Economics packages and other applications translate their own objects into ordinary KineticKit nodes.

One immutable scene and one motion can drive three outputs: animated SVG, streamed GIF and self-contained interactive HTML. The same scene and time always give the same snapshot. Wall-clock time and the choice of renderer do not enter the model.

KineticKit does not import `mosaickit`, `utility-viz` or any other domain package. Font processing belongs to `glyphkit` and reaches the scene through one adapter, described in [Typography](typography.md#sec-typography).

## Layers

| Layer | May know | Must not know |
| --- | --- | --- |
| Motion core (`easing`, `interpolation`, `timeline`, `tween`, `keyframes`) | time, values, protocols | scenes, renderers |
| Scene model (`geometry`, `scene`, `styles`, `morph`, `transitions`) | geometry, styles, object ids | backend objects |
| Renderers (`renderers.vector`, `.raster`, `.interactive`) | scene snapshots, capabilities | consumer domain models |
| Exporters (`exporters`) | frames, artifacts, destinations | visualization logic |

Import-linter contracts and tests that read the syntax tree enforce these boundaries. Matplotlib, Plotly and Pillow live only in private `_*` modules.

## A short tour

1. [Quick start](../quickstart.md) moves one point and writes it to three formats.
2. [Scenes and motion](scenes-motion.md) lists the nodes and shows how motions compose.
3. [Output formats](outputs.md) explains capabilities, fallbacks and what each format keeps.
4. [Examples](examples.md) runs a chart, an adapter and a 3D surface.
