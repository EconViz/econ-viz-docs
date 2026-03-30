---
hide:
  - navigation
  - toc
---

<p align="center">
  <img src="assets/banner.svg" alt="Econ-Viz" style="max-width: 480px; width: 100%; margin: 2rem 0 1rem;">
</p>

<p align="center"><em>A Python toolkit for producing publication-quality microeconomics diagrams.</em></p>

<p align="center">
  <a href="https://github.com/EconViz/econ-viz/actions"><img alt="Publish" src="https://img.shields.io/github/actions/workflow/status/EconViz/econ-viz/publish.yml?style=flat-square&label=publish&color=181818&labelColor=f3f3f3"></a>
  <img alt="Coverage" src="https://img.shields.io/badge/coverage-99%25-181818?style=flat-square&color=181818&labelColor=f3f3f3">
  <a href="https://pypi.org/project/econ-viz/"><img alt="PyPI" src="https://img.shields.io/pypi/v/econ-viz?style=flat-square&label=pypi+package&color=181818&labelColor=f3f3f3"></a>
  <a href="https://pypi.org/project/econ-viz/"><img alt="Python" src="https://img.shields.io/pypi/pyversions/econ-viz?style=flat-square&color=181818&labelColor=f3f3f3"></a>
</p>

---

**Documentation:** [https://econ-viz.org](https://econ-viz.org)

**Source Code:** [https://github.com/EconViz/econ-viz](https://github.com/EconViz/econ-viz)

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

    Cobb-Douglas, Leontief, Perfect Substitutes, CES, Translog, Satiation, Quasi-Linear, and Stone-Geary — covering the full range of standard microeconomic preferences.

    [:octicons-arrow-right-24: Model catalogue](models/index.md)

-   :material-function: **Automatic equilibrium solving**

    Interior solutions, kinked optima (Leontief), and corner solutions — all handled via SLSQP with no manual setup required.

    [:octicons-arrow-right-24: Quick Start](quickstart.md)

-   :material-math-integral: **LaTeX parser**

    Pass a LaTeX expression like `x^{0.4} y^{0.6}` directly and get back a fully-configured model instance.

    [:octicons-arrow-right-24: LaTeX parsing](latex.md)

-   :material-export: **Publication-ready export**

    Save as PNG, PDF, or SVG for presentations, papers, and the web.

    [:octicons-arrow-right-24: Export formats](export.md)

-   :material-chart-line: **Analysis helpers**

    Compute comparative statics and inspect homogeneity, Euler's theorem, homotheticity, and demand degree-0 behaviour.

    [:octicons-arrow-right-24: Analysis tools](analysis.md)

-   :material-code-braces: **Advanced models**

    Wrap any callable as a utility function, or extend to N goods with 2-D projection via `MultiGoodCD.freeze()`.

    [:octicons-arrow-right-24: Advanced models](models/advanced.md)

-   :material-console: **CLI**

    Generate diagrams from the terminal without writing a single line of Python.

    [:octicons-arrow-right-24: CLI reference](cli.md)

</div>

## Install

```bash
pip install econ-viz
```

Requires Python 3.10 or later.
