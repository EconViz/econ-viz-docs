---
seo_title: "Python Library for Microeconomics Diagrams"
description: "Open-source Python library for publication-quality microeconomics diagrams: indifference curves, budget constraints, consumer equilibria, and TikZ export."
---

<h1 class="ev-visually-hidden">Econ-Viz: Python library for microeconomics diagrams</h1>

<p align="center">
  <img src="assets/banner.svg" alt="Econ-Viz" style="max-width: 480px; width: 100%; margin: 2rem 0 1rem;">
</p>

<p align="center"><em>A Python toolkit for producing publication-quality microeconomics diagrams.</em></p>

<p align="center">
  <a href="https://github.com/EconViz/econ-viz/actions"><img alt="Publish" src="https://img.shields.io/github/actions/workflow/status/EconViz/econ-viz/publish.yml?style=flat-square&label=publish&color=181818&labelColor=f3f3f3"></a>
  <img alt="Coverage" src="https://img.shields.io/badge/coverage-92.63%25-181818?style=flat-square&color=181818&labelColor=f3f3f3">
  <a href="https://pypi.org/project/econ-viz/"><img alt="PyPI" src="https://img.shields.io/pypi/v/econ-viz?style=flat-square&label=pypi+package&color=181818&labelColor=f3f3f3&cacheSeconds=300"></a>
  <a href="https://pypi.org/project/econ-viz/"><img alt="Python" src="https://img.shields.io/pypi/pyversions/econ-viz?style=flat-square&color=181818&labelColor=f3f3f3"></a>
</p>

---

:fontawesome-brands-github: **Source Code:** [https://github.com/EconViz/econ-viz](https://github.com/EconViz/econ-viz)

:fontawesome-solid-envelope: **Contact:** [contact@econ-viz.org](mailto:contact@econ-viz.org)

---

```python
from econ_viz import Canvas, levels, solve
from econ_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.5, beta=0.5)
eq    = solve(model, px=2.0, py=3.0, income=30.0)
lvls  = levels.around(eq.utility, n=5)

cvs = Canvas(x_max=20, y_max=15, title=r"Cobb-Douglas $x^{0.5} y^{0.5}$")
cvs.add_utility(model, levels=lvls)
cvs.add_budget(2.0, 3.0, 30.0, fill=True)
cvs.add_equilibrium(eq, show_ray=True)
cvs.save("cobb_douglas.png")
```

## Features

<div class="grid cards" markdown>

-   :material-shape-outline: **Eight built-in utility models**

    Cobb-Douglas, Leontief, CES, and other textbook utility functions, from perfect substitutes to satiation, ready to plot.

    [:octicons-arrow-right-24: Model catalogue](models/index.md)

-   :material-function: **Automatic equilibrium solving**

    Give prices and income and get the consumer's optimal bundle. Interior, kinked, and corner solutions need no manual setup.

    [:octicons-arrow-right-24: Quick Start](getting-started/quickstart.md)

-   :material-view-dashboard-outline: **Multi-panel teaching figures**

    Place diagrams side by side, stacked, or in a grid for before-and-after comparisons, decompositions, or lecture slides.

    [:octicons-arrow-right-24: Figures & demand diagrams](guides/consumer.md)

-   :material-chart-bell-curve-cumulative: **Demand-path diagrams**

    Sweep a price or income to trace price- and income-consumption curves, linked to the Marshallian demand curve below.

    [:octicons-arrow-right-24: Figures & demand diagrams](guides/consumer.md)

-   :material-math-integral: **LaTeX parser**

    Paste a utility function written in LaTeX and get a ready-to-plot model with its functional form and parameters detected.

    [:octicons-arrow-right-24: LaTeX parsing](tools/latex.md)

-   :material-export: **Publication-ready export**

    Save to PNG, PDF, or SVG in one line. Vector output stays sharp at any size for papers, slides, and the web.

    [:octicons-arrow-right-24: Export formats](guides/export.md)

-   :material-play-box-multiple-outline: **Animated GIF sweeps**

    Turn parameter, price, or income changes into GIFs so students can watch the equilibrium move with the budget line.

    [:octicons-arrow-right-24: Animation](guides/animation.md)

-   :material-tune: **Notebook widgets**

    Tune parameters in Jupyter with sliders or typed values and watch the diagram update as students explore on their own.

    [:octicons-arrow-right-24: Interactive widgets](guides/interactive.md)

-   :material-chart-line: **Analysis helpers**

    Compute comparative statics and Slutsky matrices, and check the homogeneity and homotheticity behind every diagram.

    [:octicons-arrow-right-24: Analysis tools](tools/analysis.md)

-   :material-code-braces: **Advanced models**

    Wrap any function as a utility model, or project many-good preferences onto a plane to go beyond the textbook cases.

    [:octicons-arrow-right-24: Advanced models](models/advanced.md)

-   :material-console: **CLI**

    Generate diagrams from the terminal without writing Python, and print closed-form Marshallian demand ready for LaTeX.

    [:octicons-arrow-right-24: CLI reference](getting-started/cli.md)

</div>

## Install

```bash
uv add econ-viz
```

Requires Python 3.10 or later.
