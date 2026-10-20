---
seo_title: "Python Packages for Economics Diagrams"
description: "EconViz is a family of open-source Python packages for economics diagrams, geometry, typography, and animation."
---

<h1 class="ev-visually-hidden">EconViz: Python packages for economics diagrams</h1>

<p align="center">
  <img src="assets/banner.svg" alt="EconViz" style="max-width: 480px; width: 100%; margin: 2rem 0 1rem;">
</p>

<p align="center"><em>Open-source Python packages for economics diagrams.</em></p>

---

:fontawesome-brands-github: **Source Code:** [https://github.com/EconViz](https://github.com/EconViz)

:fontawesome-solid-envelope: **Contact:** [contact@econ-viz.org](mailto:contact@econ-viz.org)

---

## Modules

EconViz is made of six packages. Two draw economics diagrams; four provide the geometry, scene, typography, and animation layers they share.

### Economics packages

Two packages draw economics diagrams.

<div class="grid cards ev-package-cards" markdown>

-   :material-chart-bell-curve-cumulative: **utility-viz**

    Publication-quality microeconomics diagrams: indifference curves, budget constraints and equilibria.

    ```bash
    uv add --prerelease allow utility-viz
    ```

    Version 2.0 is in beta.

    [:octicons-arrow-right-24: utility-viz](utility-viz/index.md)

-   :material-scale-balance: **principle-viz**

    Market analysis and diagrams for Principles of Economics: taxes, price controls, welfare and trade.

    ```bash
    uv add principle-viz
    ```

    [:octicons-arrow-right-24: principle-viz](principle-viz/index.md)

</div>

### Foundation packages

Four general-purpose building blocks that the economics packages share.

<div class="grid cards ev-package-cards" markdown>

-   :material-view-grid-outline: **mosaickit**

    A domain-neutral toolkit for assembling two-dimensional diagrams from layers, styles and renderers.

    ```bash
    uv add mosaickit
    ```

    [:octicons-arrow-right-24: mosaickit](mosaickit/index.md)

-   :material-vector-bezier: **bezierkit**

    A small toolkit for constructing, analyzing and exporting Bézier curves, with SVG and TikZ output.

    ```bash
    uv add bezierkit
    ```

    Current stable release: 1.0.1.

    [:octicons-arrow-right-24: bezierkit](bezierkit/index.md)

-   :material-format-font: **glyphkit**

    Renderer-independent font selection, Unicode shaping, text and math layout, glyph outlines, and portable font subsets.

    ```bash
    uv add --prerelease allow glyphkit
    ```

    [:octicons-arrow-right-24: glyphkit](glyphkit/index.md)

-   :material-animation-play: **kinetickit**

    Deterministic 2D and 3D animation with animated SVG, streamed GIF, and interactive HTML output.

    ```bash
    uv add --prerelease allow "kinetickit[studio]"
    ```

    [:octicons-arrow-right-24: kinetickit](kinetickit/index.md)

</div>
