# econ-viz

A Python toolkit for producing publication-quality microeconomics diagrams.

Define utility functions declaratively, solve for consumer equilibria, and export figures as raster images or LaTeX/TikZ source — all in a few lines of code.

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

- **Six utility models** — Cobb-Douglas, Leontief, Perfect Substitutes, CES, Satiation, Quasi-Linear
- **Advanced models** — custom callables and multi-good Cobb-Douglas with 2-D projection
- **Automatic equilibrium solving** — interior, kink, and corner solutions via SLSQP
- **LaTeX parser** — turn `x^{0.4} y^{0.6}` directly into a model instance
- **Themes** — built-in Default and Nord palettes
- **Export** — PNG / PDF / SVG raster and TikZ/PGFPlots source for LaTeX documents
- **CLI** — generate diagrams from the terminal without writing Python

## Quick links

- [Installation](installation.md)
- [Quick Start](quickstart.md)
- [CLI reference](cli.md)
- [Model catalogue](models/index.md)
- [GitHub](https://github.com/EconViz/econ-viz)
- [PyPI](https://pypi.org/project/econ-viz/)
