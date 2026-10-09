---
seo_title: "Introduction"
---

# Introduction

<span id="sec-intro"></span>

The `mosaickit` package assembles two-dimensional diagrams from small,
immutable pieces. A scene is an ordered list of layers (paths, filled regions,
markers, text, arrows, labels, braces). Each layer names a semantic role, a
theme maps roles to styles, and a renderer produces PNG, SVG, PDF, GIF or MP4.
The package is domain-neutral. Domain packages such as `principle-viz`
and `utility-viz` define their own models and role names, then pass
`mosaickit` the layers to draw. Curve construction and TikZ export
belong to geometry packages such as `bezierkit`.

## Design

Four ideas run through the package.

/ Immutable values: Layers, scenes, styles, themes and specifications
  are frozen dataclasses. A `Canvas` is a fluent builder around an immutable
  `Scene`; `snapshot()`, `copy()` and `bind()` never change a scene another
  object holds.
/ Sparse styles: Every style field may be `None`, meaning inherit.
  A layer's explicit style sits on top of canvas overrides, configuration
  overrides, the theme and the primitive defaults ([Themes and configuration](themes.md#sec-themes)).
/ Roles, not colors: Layers name what they are (`"primary"`,
  `"axes.note"`, `"mypkg.boundary"`); themes decide how that looks, and
  colors are palette names resolved when a canvas renders ([Styles and colors](styles.md#sec-styles)).
/ Placement that covers nothing: Region labels, point labels, braces
  and axis annotations are placed after everything else is drawn, by pure
  geometry in display pixels, so that text touches no line, marker, region
  or other text ([Layout geometry](geometry.md#sec-geometry), [Region and point labels](labels.md#sec-labels)).

## Mathematics and proofs

Automatic placement uses several computational-geometry routines. An
orientation test determines which side of a directed line contains a point,
and the even-odd rule classifies a point by counting ray crossings of a
boundary. The package also measures distance to a polygon's boundary and
uses best-first search, always examining the candidate region with the
largest upper bound first, to find the point deepest inside a region. Axis
text is arranged without overlap while minimizing the sum of squared
displacements. The chapters state what each routine guarantees
as numbered definitions, lemmas, propositions and theorems; the proofs are
collected in [Proofs](../project/proofs.md#app-proofs), so the chapters can be read for the API alone. The
manual also states and proves the corresponding results for style and theme
algebra (sparse merging and role resolution) and for parameter binding. The
standard references are
[{de Berg} (2008)](../project/references.md#deberg2008) for the geometry and [Barlow (1972)](../project/references.md#barlow1972) for the
order-restricted least squares behind [Spreading is optimal](annotations.md#thm-spread).

## Reading guide

<span id="tab-guide"></span>

| Topic | Contents | Section |
| --- | --- | --- |
| Canvases, specifications, scenes | [Canvases and scenes](canvas.md#sec-canvas) | Paths, fills, markers, text, axes |
| [Layers and axes](layers.md#sec-layers) | Axis marks, notes and braces | [Axis annotations](annotations.md#sec-annotations) |
| Layout geometry | [Layout geometry](geometry.md#sec-geometry) | Region and point labels |
| [Region and point labels](labels.md#sec-labels) | Styles, colors, palettes | [Styles and colors](styles.md#sec-styles) |
| Themes, roles, configuration | [Themes and configuration](themes.md#sec-themes) | Parameters, grids, animation |
| [Parameters, grids and animation](parameters.md#sec-parameters) | Renderers, caches, saving | [Rendering](rendering.md#sec-rendering) |

Start with [Quick start](../quickstart.md#sec-quickstart), [Canvases and scenes](canvas.md#sec-canvas) and [Layers and axes](layers.md#sec-layers). Every
figure in this manual is `mosaickit` output, drawn by the canvas or
grid it illustrates and saved as PDF at the printed size.
