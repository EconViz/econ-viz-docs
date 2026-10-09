---
seo_title: "principle-viz：用 Python 繪製經濟學原理的市場圖形"
description: "principle-viz 是用於經濟學原理市場分析與繪圖的 Python 套件：均衡、租稅、價格管制、福利分析等，以線性需求與供給為基礎。"
---

<h1 class="ev-visually-hidden">principle-viz：用 Python 繪製經濟學原理的市場圖形</h1>

<p align="center">
  <img src="../../assets/principle-viz/banner.svg" alt="principle-viz" style="max-width: 480px; width: 100%; margin: 2rem 0 1rem;">
</p>

<p align="center"><em>用 Python 進行經濟學原理的市場分析與繪圖。</em></p>

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

-   :material-scale-balance: **市場均衡**

    由線性需求與供給，或離散的單位表求解均衡。

-   :material-chart-line: **比較靜態分析**

    移動需求或供給，呈現從舊均衡到新均衡的變化。

-   :material-percent-outline: **租稅與補貼**

    定額、從量與從價租稅，法定歸宿可設在買方或賣方。

-   :material-lock-outline: **價格管制**

    價格上限、價格下限與最低工資，並標示短缺、過剩或失業。

-   :material-chart-areaspline: **福利分解**

    消費者剩餘、生產者剩餘、稅收與無謂損失。

-   :material-earth: **貿易、外部性與更多**

    關稅與配額、外部性、共有資源、公共財、可貸資金、生產可能曲線與彈性。

-   :material-sigma: **市場加總**

    把個別曲線或需求表水平加總成市場需求與供給。

-   :material-console: **命令列工具**

    在終端機執行均衡、租稅、補貼與貿易分析，並輸出 JSON。

</div>

## 安裝

```bash
uv add principle-viz
```

!!! info "系統需求"

    - Python 3.10 以上。
    - [mosaickit](../mosaickit/index.md)，uv 會自動一併安裝。

開發環境請見[安裝](installation.md)，或直接看[快速入門](quickstart.md)。

<!-- agora-navigation -->

## 文件導覽

以下章節涵蓋 principle-viz 0.10.1。

- [簡介](guides/introduction.md)
- [安裝](installation.md)
- [快速開始](quickstart.md)
- [線性市場](guides/markets.md)
- [離散市場](guides/discrete.md)
- [由個人加總市場曲線](guides/aggregation.md)
- [彈性與總收益](guides/elasticity.md)
- [福利](guides/welfare.md)
- [租稅與補貼](guides/taxes.md)
- [價格管制](guides/controls.md)
- [國際貿易](guides/trade.md)
- [市場失靈](guides/failures.md)
- [勞動與可貸資金](guides/factor-markets.md)
- [生產可能曲線](guides/ppf.md)
- [圖形](guides/figures.md)
- [命令列介面](cli.md)
- [更新紀錄](changelog.md)

<!-- /agora-navigation -->
