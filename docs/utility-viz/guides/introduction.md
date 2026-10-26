---
seo_title: "Introduction"
---

# Introduction

<span id="sec-intro"></span>

The `utility-viz` package is a Python toolkit for producing
publication-quality microeconomics diagrams: indifference curves, budget
constraints, consumer equilibria, demand curves and exchange economies. It
draws in the conventions of textbook figures---first-quadrant axes with
arrow tips, LaTeX;-style labels and no numeric ticks---and exports to PNG,
PDF, SVG, TikZ or animated GIF.

Up to version 1.12 the package was called `econ-viz`. It was
renamed `utility-viz` in 2.0.0; [Migrating from `econ-viz`](../getting-started/installation.md#sec-migrate) describes what changed
and how existing code keeps working. This manual describes the pre-release
2.0.0b8.

`utility-viz` belongs to the EconViz family of packages. It
draws through `mosaickit`, a domain-neutral scene and rendering
library, and traces curves with `bezierkit`. The sibling package
`principle-viz` covers principles-of-economics diagrams.

The script behind every figure is linked from its caption, and all of them, sorted into folders by topic, come as one zip: [utility-viz-examples-en.zip](https://econ-viz.org/assets/utility-viz/agora/utility-viz-examples-en.zip).

## Scope

`utility-viz` is organised in five parts: utility models, equilibrium solving, utility levels, drawing layers, and output formats. Models and solutions remain usable on their own, and the same model can be passed to a canvas, multi-panel figure, demand diagram, or analysis API.

## Reading guide

The manual is organised in four parts ([Chapter guide](introduction.md#tab-guide)):

<span id="tab-guide"></span>

| Topic | Subtopic | Description |
| --- | --- | --- |
| Drawing & export | [Canvas & layers](canvas.md#sec-canvas) | Axes, curves, equilibria |
|  | [Figures & demand](consumer.md#sec-figures) | Panels & demand |
|  | [Themes & config](themes.md#sec-themes) | Colours, styles, config |
|  | [Output formats](export.md#sec-export) | Image files and TikZ |
| Models & analysis | [Built-in models](../models/index.md#sec-models) | Utility functions |
|  | [Custom & many-good](../models/advanced.md#sec-advanced) | Custom, $N$ goods, scenes |
|  | [Comparative statics](../tools/analysis.md#sec-analysis) | Derivatives & Slutsky |
| Animation & interaction | [GIF animation](animation.md#sec-animation) | Sweeps as GIFs |
|  | [Jupyter widgets](interactive.md#sec-widgets) | Sliders in notebooks |
| Other inputs | [Command line](../getting-started/cli.md#sec-cli) | Plots from the shell |
|  | [LaTeX parser](../tools/latex.md#sec-latex) | Models from formulas |

On first use, read [Quick start](../getting-started/quickstart.md#sec-quickstart) and [Canvas](canvas.md#sec-canvas) in order. To look up a
particular API, go straight to its section or to the command index.
Users upgrading from `econ-viz` 1.x should start with
[Migrating from `econ-viz`](../getting-started/installation.md#sec-migrate).
