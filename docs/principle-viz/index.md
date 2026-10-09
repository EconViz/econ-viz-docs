---
seo_title: "principle-viz: Principles of Economics Market Diagrams in Python"
description: "principle-viz is a Python package for Principles of Economics market analysis and diagrams: equilibrium, taxes, price controls, welfare and more, built on linear demand and supply."
---

<h1 class="ev-visually-hidden">principle-viz: Principles of Economics market diagrams in Python</h1>

<p align="center">
  <img src="../assets/principle-viz/banner.svg" alt="principle-viz" style="max-width: 480px; width: 100%; margin: 2rem 0 1rem;">
</p>

<p align="center"><em>Python package for Principles of Economics market analysis and diagrams.</em></p>

<p align="center">
  <a href="https://pypi.org/project/principle-viz/"><img alt="PyPI" src="https://img.shields.io/pypi/v/principle-viz?style=flat-square&label=pypi+package&color=181818&labelColor=f3f3f3&cacheSeconds=300"></a>
  <a href="https://pypi.org/project/principle-viz/"><img alt="Python" src="https://img.shields.io/pypi/pyversions/principle-viz?style=flat-square&color=181818&labelColor=f3f3f3"></a>
  <a href="https://opensource.org/licenses/MIT"><img alt="License" src="https://img.shields.io/badge/License-MIT-181818?style=flat-square&color=181818&labelColor=f3f3f3"></a>
</p>

```python
from principle_viz.core.equilibrium import solve_equilibrium
from principle_viz.core.line import Line
from principle_viz.plot.figure import MarketFigure

# P = 10 - Q
demand = Line.from_inverse(10.0, -1.0)
# P = 2 + Q
supply = Line.from_inverse(2.0, 1.0)
# Q* = 4, P* = 6
eq = solve_equilibrium(demand, supply)

fig = MarketFigure(
    x_max=12, y_max=12, title="Basic Equilibrium"
)
fig.add_curves(demand, supply, q_max=10)
fig.add_equilibrium(eq)
fig.finalize()
fig.save("basic_equilibrium.png")
fig.close()
```

## Features

<div class="grid cards" markdown>

-   :material-scale-balance: **Market equilibrium**

    Solve equilibrium from linear demand and supply, or from discrete unit schedules.

-   :material-chart-line: **Comparative statics**

    Shift demand or supply and see the move from the old equilibrium to the new one.

-   :material-percent-outline: **Taxes and subsidies**

    Fixed, per-unit and ad valorem taxes, with legal incidence on buyers or sellers.

-   :material-lock-outline: **Price controls**

    Price ceilings, price floors and the minimum wage, with the shortage, surplus or unemployment marked.

-   :material-chart-areaspline: **Welfare decomposition**

    Consumer and producer surplus, tax revenue and deadweight loss.

-   :material-earth: **Trade, externalities and more**

    Tariffs and quotas, externalities, common resources, public goods, loanable funds, the PPF and elasticity.

-   :material-sigma: **Market aggregation**

    Sum individual curves or schedules horizontally into market demand and supply.

-   :material-console: **CLI**

    Run equilibrium, tax, subsidy and trade analyses from the terminal, with JSON output.

</div>

## Install

```bash
uv add principle-viz
```

!!! info "Requirements"

    - Python 3.10 or later.
    - [mosaickit](../mosaickit/index.md), which uv installs automatically.

See [Installation](installation.md) for the development setup, or go straight to the [Quick start](quickstart.md).

<!-- agora-navigation -->

## Documentation

The following chapters cover principle-viz 0.10.1.

- [Introduction](guides/introduction.md)
- [Installation](installation.md)
- [Quick start](quickstart.md)
- [Linear markets](guides/markets.md)
- [Discrete markets](guides/discrete.md)
- [Market curves from individuals](guides/aggregation.md)
- [Elasticity and total revenue](guides/elasticity.md)
- [Welfare](guides/welfare.md)
- [Taxes and subsidies](guides/taxes.md)
- [Price controls](guides/controls.md)
- [International trade](guides/trade.md)
- [Market failures](guides/failures.md)
- [Labor and loanable funds](guides/factor-markets.md)
- [Production possibilities](guides/ppf.md)
- [Figures](guides/figures.md)
- [Command-line interface](cli.md)
- [Change history](changelog.md)

<!-- /agora-navigation -->
