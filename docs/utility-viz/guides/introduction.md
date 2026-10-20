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
2.0.0b1.

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

| Topic | Subtopic | Description | Section |
| --- | --- | --- | --- |
| Drawing & export | Canvas & layers | Axes, curves, equilibria | [Canvas](canvas.md#sec-canvas) |
|  | Figures & demand | Panels & demand | [Figures and demand diagrams](consumer.md#sec-figures) |
|  | Themes & config | Colours, styles, config | [Themes and configuration](themes.md#sec-themes) |
|  | Output formats | Image files and TikZ | [Export](export.md#sec-export) |
| Models & analysis | Built-in models | Utility functions | [Core models](../models/index.md#sec-models) |
|  | Custom & many-good | Custom, $N$ goods, scenes | [Advanced models](../models/advanced.md#sec-advanced) |
|  | Comparative statics | Derivatives & Slutsky | [Analysis](../tools/analysis.md#sec-analysis) |
| Animation & interaction | GIF animation | Sweeps as GIFs | [Animation](animation.md#sec-animation) |
|  | Jupyter widgets | Sliders in notebooks | [Interactive widgets](interactive.md#sec-widgets) |
| Other inputs | Command line | Plots from the shell | [Command-line interface](../getting-started/cli.md#sec-cli) |
|  | LaTeX parser | Models from formulas | [LaTeX parsing](../tools/latex.md#sec-latex) |

On first use, read [Quick start](../getting-started/quickstart.md#sec-quickstart) and [Canvas](canvas.md#sec-canvas) in order. To look up a
particular API, go straight to its section or to the command index.
Users upgrading from `econ-viz` 1.x should start with
[Migrating from `econ-viz`](../getting-started/installation.md#sec-migrate).
