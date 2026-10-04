---
seo_title: "Python Packages for Economics Diagrams"
description: "EconViz is a family of open-source Python packages for economics diagrams: utility-viz, principle-viz, mosaickit and bezierkit."
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

EconViz is made of four packages. Two draw economics diagrams, and two are general-purpose building blocks they share.

<div class="grid cards" markdown>

-   :material-chart-bell-curve-cumulative: **utility-viz**

    Publication-quality microeconomics diagrams: indifference curves, budget constraints, consumer equilibria and
    TikZ export.

    ```bash
    pip install --pre utility-viz
    ```

    Version 2.0 is in beta.

    [:octicons-arrow-right-24: utility-viz](utility-viz/index.md)

-   :material-scale-balance: **principle-viz**

    Principles of Economics market analysis and diagrams: equilibrium, taxes, price controls, welfare and trade, built
    on linear demand and supply.

    ```bash
    pip install principle-viz
    ```

    [:octicons-arrow-right-24: principle-viz](principle-viz/index.md)

-   :material-view-grid-outline: **mosaickit**

    A domain-neutral toolkit for assembling two-dimensional diagrams from scenes, layers, styles, parameters and
    renderers.

    ```bash
    pip install mosaickit
    ```

    [:octicons-arrow-right-24: mosaickit](mosaickit/index.md)

-   :material-vector-bezier: **bezierkit**

    A small mathematical toolkit for constructing, analyzing and exporting Bézier curves, with native SVG and TikZ
    output.

    ```bash
    pip install --pre bezierkit
    ```

    Currently a release candidate (0.5.0rc1).

    [:octicons-arrow-right-24: bezierkit](bezierkit/index.md)

</div>

## How the packages fit together

Each arrow reads "depends on", taken from the packages' declared dependencies:

```text
utility-viz   ──>  mosaickit
utility-viz   ──>  bezierkit
principle-viz ──>  mosaickit
```

- **utility-viz** and **principle-viz** render their diagrams with **mosaickit**.
- **utility-viz** also uses **bezierkit** for curves and TikZ output.
- **mosaickit** does not depend on bezierkit or on any domain package.

## Coming from econ-viz?

`econ-viz` was renamed to **utility-viz** in 2.0. See [Migrating from econ-viz](utility-viz/migrating.md).
