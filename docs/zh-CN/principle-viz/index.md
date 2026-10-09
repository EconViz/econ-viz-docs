---
seo_title: "principle-viz：用 Python 绘制经济学原理的市场图形"
description: "principle-viz 是用于经济学原理市场分析与绘图的 Python 包：均衡、税收、价格管制、福利分析等，以线性需求与供给为基础。"
---

<h1 class="ev-visually-hidden">principle-viz：用 Python 绘制经济学原理的市场图形</h1>

<p align="center">
  <img src="../../assets/principle-viz/banner.svg" alt="principle-viz" style="max-width: 480px; width: 100%; margin: 2rem 0 1rem;">
</p>

<p align="center"><em>用 Python 进行经济学原理的市场分析与绘图。</em></p>

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

## 功能特色

<div class="grid cards" markdown>

-   :material-scale-balance: **市场均衡**

    由线性需求与供给，或离散的单位表求解均衡。

-   :material-chart-line: **比较静态分析**

    移动需求或供给，呈现从旧均衡到新均衡的变化。

-   :material-percent-outline: **税收与补贴**

    定额、从量与从价税，法定归宿可设在买方或卖方。

-   :material-lock-outline: **价格管制**

    价格上限、价格下限与最低工资，并标示短缺、过剩或失业。

-   :material-chart-areaspline: **福利分解**

    消费者剩余、生产者剩余、税收与无谓损失。

-   :material-earth: **贸易、外部性与更多**

    关税与配额、外部性、公共资源、公共品、可贷资金、生产可能性曲线与弹性。

-   :material-sigma: **市场加总**

    把个别曲线或需求表水平加总成市场需求与供给。

-   :material-console: **命令行工具**

    在终端运行均衡、税收、补贴与贸易分析，并输出 JSON。

</div>

## 安装

```bash
uv add principle-viz
```

!!! info "环境要求"

    - Python 3.10 以上。
    - [mosaickit](../mosaickit/index.md)，uv 会自动一并安装。

开发环境请见[安装](installation.md)，或直接看[快速入门](quickstart.md)。

<!-- agora-navigation -->

## 文档导航

以下章节涵盖 principle-viz 0.10.1。

- [简介](guides/introduction.md)
- [安装](installation.md)
- [快速开始](quickstart.md)
- [线性市场](guides/markets.md)
- [离散市场](guides/discrete.md)
- [由个人加总市场曲线](guides/aggregation.md)
- [弹性与总收益](guides/elasticity.md)
- [福利](guides/welfare.md)
- [税收与补贴](guides/taxes.md)
- [价格管制](guides/controls.md)
- [国际贸易](guides/trade.md)
- [市场失灵](guides/failures.md)
- [劳动与可贷资金](guides/factor-markets.md)
- [生产可能性曲线](guides/ppf.md)
- [图形](guides/figures.md)
- [命令行界面](cli.md)
- [更新纪录](changelog.md)

<!-- /agora-navigation -->
