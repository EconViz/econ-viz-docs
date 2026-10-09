---
seo_title: "mosaickit: Domain-Neutral Diagram Scenes and Rendering"
description: "mosaickit is a domain-neutral Python toolkit for assembling two-dimensional diagrams from scenes, layers, styles, parameters and renderers."
---

<h1 class="ev-visually-hidden">mosaickit: domain-neutral diagram scenes and rendering</h1>

<p align="center">
  <img src="../assets/mosaickit/banner.svg" alt="mosaickit" style="max-width: 480px; width: 100%; margin: 2rem 0 1rem;">
</p>

<p align="center"><em>A domain-neutral Python toolkit for assembling two-dimensional diagrams.</em></p>

<p align="center">
  <a href="https://pypi.org/project/mosaickit/"><img alt="PyPI" src="https://img.shields.io/pypi/v/mosaickit?style=flat-square&label=pypi+package&color=181818&labelColor=f3f3f3&cacheSeconds=300"></a>
  <a href="https://pypi.org/project/mosaickit/"><img alt="Python" src="https://img.shields.io/pypi/pyversions/mosaickit?style=flat-square&color=181818&labelColor=f3f3f3"></a>
  <a href="https://opensource.org/licenses/MIT"><img alt="License" src="https://img.shields.io/badge/License-MIT-181818?style=flat-square&color=181818&labelColor=f3f3f3"></a>
</p>

```python
from mosaickit import (
    Canvas,
    Fill,
    FillLayer,
    MarkerLayer,
    PathLayer,
    Stroke,
    TextLayer,
    quadrant_axes,
)

canvas = Canvas().extend(quadrant_axes(10, 10))
canvas.add(
    FillLayer(
        [(1, 1), (1, 7), (8, 1)],
        fill=Fill(color="#377EB8", opacity=0.12),
        z_index=-1,
    )
)
canvas.add(
    PathLayer(
        [(1, 8), (2, 5), (4, 3), (7, 1.5), (9, 1)],
        stroke=Stroke(color="#984EA3", width=2),
    )
)
canvas.add(MarkerLayer([(4, 3)]))
canvas.add(TextLayer((4, 3), "A", offset=(8, 8)))
canvas.save("diagram.svg")
```

## Features

<div class="grid cards" markdown>

-   :material-layers-outline: **Small scene graph**

    `PathLayer`, `FillLayer`, `MarkerLayer`, `TextLayer`, `ArrowLayer`, `LegendLayer` and `GroupLayer`.

-   :material-label-outline: **Labels that cover nothing**

    `RegionLabelLayer` and `PointLabelLayer` place labels clear of the drawing, with axis marks, notes and braces.

-   :material-axis-arrow: **Axes helpers**

    `quadrant_axes()`, `crosshair_axes()` and `box_frame()` set up common frames.

-   :material-palette-outline: **Styles and themes**

    Styles, themes and palettes, with colours that can be given by name.

-   :material-view-grid-outline: **Parameters and grids**

    Parameters and expressions, `CanvasGrid` layouts and `Animation` sweeps.

-   :material-file-image-outline: **Pluggable rendering**

    A built-in Matplotlib renderer for PNG, SVG and PDF, and a `Renderer` protocol for other backends.

</div>

## Scope

mosaickit owns domain-neutral scene composition, styles, themes, parameter binding, grid layout, animation frames,
renderer contracts and static or animated output. Domain semantics belong to the packages built on it. Curve
construction and native TikZ path generation belong to geometry packages such as
[bezierkit](../bezierkit/index.md).

## Install

```bash
uv add mosaickit
```

Requires Python 3.10 or later. See [Installation](installation.md) for extras and the development setup, or go straight to the [Quick start](quickstart.md).

<!-- agora-navigation -->

## Documentation

The following chapters cover mosaickit 0.5.1.

- [Introduction](guides/introduction.md)
- [Installation](installation.md)
- [Quick start](quickstart.md)
- [Canvases and scenes](guides/canvas.md)
- [Layers and axes](guides/layers.md)
- [Axis annotations](guides/annotations.md)
- [Layout geometry](guides/geometry.md)
- [Region and point labels](guides/labels.md)
- [Styles and colors](guides/styles.md)
- [Themes and configuration](guides/themes.md)
- [Parameters, grids and animation](guides/parameters.md)
- [Rendering](guides/rendering.md)
- [Proofs](project/proofs.md)
- [Change history](project/changelog.md)

<!-- /agora-navigation -->
