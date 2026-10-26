---
seo_title: "Python Library for Macroeconomics Diagrams"
description: "Open-source Python library for textbook macroeconomics diagrams: the Keynesian cross, money market, AS-AD, IS-LM, Solow growth, wage and price setting, the open economy and linked panels."
---

<h1 class="ev-visually-hidden">macro-viz: Python library for macroeconomics diagrams</h1>

<p align="center">
  <img src="../assets/macro-viz/banner.svg" alt="macro-viz" style="max-width: 480px; width: 100%; margin: 2rem 0 1rem;">
</p>

<p align="center"><em>A Python toolkit for producing textbook macroeconomics diagrams.</em></p>

<p align="center">
  <a href="https://github.com/EconViz/macro-viz/actions"><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/EconViz/macro-viz/ci.yml?style=flat-square&label=ci&color=181818&labelColor=f3f3f3"></a>
  <a href="https://github.com/EconViz/macro-viz"><img alt="GitHub" src="https://img.shields.io/badge/github-EconViz%2Fmacro--viz-181818?style=flat-square&labelColor=f3f3f3"></a>
  <img alt="Python" src="https://img.shields.io/badge/python-3.10%2B-181818?style=flat-square&labelColor=f3f3f3">
</p>

!!! warning "macro-viz is a development version"

    macro-viz 0.2.0.dev0 is not on PyPI yet and its API may change before the first release. Install it from GitHub.

```python
from macro_viz import Config
from macro_viz.panels import (
    IsLm,
    LinearFunction,
    MacroEconomy,
    QuadraticProduction,
    Scenario,
    Shock,
    Step,
)
from macro_viz.visuals import four_panel_canvas

Config.load("econ-viz.toml").use()

economy = MacroEconomy(
    QuadraticProduction(3.0, 0.2, 1.0),
    LinearFunction(0.4, 0.25),
    capital=1.0,
    expected_price=1.0,
    islm=IsLm(0.0, 1.0, 2.0, 0.25, 1.0),
).calibrated(2.0)

scenario = Scenario(
    economy, (Step("A"), Step("B", Shock(money=1.4)))
)
cvs = four_panel_canvas(scenario, steps=["A", "B"], extent=1.5)
cvs.save("four_panel.png")
```

## Features

<div class="grid cards" markdown>

-   :material-cursor-default-click-outline: **Keynesian goods market**

    Consumption function, the Keynesian cross and the multiplier, with a curved-demand variant.

    [:octicons-arrow-right-24: Keynesian goods market](guides/keynesian.md)

-   :material-cash-multiple: **Money market**

    Money demand and supply, central-bank money and the zero lower bound.

    [:octicons-arrow-right-24: Money market](guides/money.md)

-   :material-chart-line: **Aggregate supply and demand**

    AS-AD equilibrium, demand and supply shocks and the adjustment to the medium run.

    [:octicons-arrow-right-24: Aggregate supply and demand](guides/adas.md)

-   :material-vector-intersection: **IS-LM**

    Fiscal and monetary policy, crowding out, flat and steep curves, the liquidity trap and expected inflation.

    [:octicons-arrow-right-24: IS-LM](guides/islm.md)

-   :material-earth: **Open economy**

    Net exports, interest parity, floating-rate IS-LM and devaluation in AS-AD.

    [:octicons-arrow-right-24: Open economy](guides/open-economy.md)

-   :material-trending-up: **Solow growth**

    Steady state, golden rule and transition paths in levels, logs and growth rates.

    [:octicons-arrow-right-24: Solow growth](guides/growth.md)

-   :material-account-hard-hat-outline: **Natural rate of unemployment**

    Wage setting and price setting, with shifts from benefits, markup and productivity.

    [:octicons-arrow-right-24: Natural rate of unemployment](guides/labor.md)

-   :material-view-dashboard-outline: **Linked panels**

    Four- and five-panel derivations that share one value across panels, with typed curve movements.

    [:octicons-arrow-right-24: Linked panels](guides/panels.md)

-   :material-play-box-multiple-outline: **Animation**

    Turn a shift or an adjustment into a GIF or an animated SVG with KineticKit.

    [:octicons-arrow-right-24: Animation](guides/animation.md)

-   :material-tune: **Settings**

    Colours, line widths, fonts, language and label nudges from the shared econ-viz.toml.

    [:octicons-arrow-right-24: Settings](guides/settings.md)

</div>

## Install

```bash
uv add "macro-viz @ git+https://github.com/EconViz/macro-viz"
```

Requires Python 3.10 or later. See [Installation](installation.md) for `--prerelease allow`, fonts and the optional animation extra.

## Examples

Every figure in this documentation comes with the script that draws it, sorted into folders by topic. Download them all in one file, with `econ-viz.toml`, the settings the scripts load (`base = "manual"`).

[Download all examples](../assets/macro-viz/macro-viz-examples.zip){ .md-button download="" }
