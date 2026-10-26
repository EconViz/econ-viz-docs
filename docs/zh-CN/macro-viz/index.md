---
seo_title: "绘制总体经济学图形的 Python 套件"
description: "开源 Python 套件，绘制教科书的总体经济学图形：凯因斯十字、货币市场、AS-AD、IS-LM、梭罗成长、工资与价格设置、开放经济与连动面板。"
---

<h1 class="ev-visually-hidden">macro-viz：绘制总体经济学图形的 Python 套件</h1>

<p align="center">
  <img src="../../assets/macro-viz/banner.svg" alt="macro-viz" style="max-width: 480px; width: 100%; margin: 2rem 0 1rem;">
</p>

<p align="center"><em>用 Python 绘制教科书的总体经济学图形。</em></p>

<p align="center">
  <a href="https://github.com/EconViz/macro-viz/actions"><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/EconViz/macro-viz/ci.yml?style=flat-square&label=ci&color=181818&labelColor=f3f3f3"></a>
  <a href="https://github.com/EconViz/macro-viz"><img alt="GitHub" src="https://img.shields.io/badge/github-EconViz%2Fmacro--viz-181818?style=flat-square&labelColor=f3f3f3"></a>
  <img alt="Python" src="https://img.shields.io/badge/python-3.10%2B-181818?style=flat-square&labelColor=f3f3f3">
</p>

!!! warning "macro-viz 目前为开发版"

    macro-viz 0.2.0.dev0 尚未上架 PyPI，第一次发行前 API 可能变动。请从 GitHub 安装。

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

## 功能特色

<div class="grid cards" markdown>

-   :material-cursor-default-click-outline: **凯因斯商品市场**

    消费函数、凯因斯十字与乘数，并含弯曲需求的变形

    [:octicons-arrow-right-24: 凯因斯商品市场](guides/keynesian.md)

-   :material-cash-multiple: **货币市场**

    货币需求与供给、央行货币与零利率下限

    [:octicons-arrow-right-24: 货币市场](guides/money.md)

-   :material-chart-line: **总合供给与需求**

    AS-AD 均衡、需求与供给冲击，以及到中期的调整

    [:octicons-arrow-right-24: 总合供给与需求](guides/adas.md)

-   :material-vector-intersection: **IS-LM**

    财政与货币政策、排挤效果、平坦与陡峭的曲线、流动性陷阱与预期通膨

    [:octicons-arrow-right-24: IS-LM](guides/islm.md)

-   :material-earth: **开放经济**

    净出口、利率平价、浮动汇率的 IS-LM，以及 AS-AD 中的贬值

    [:octicons-arrow-right-24: 开放经济](guides/open-economy.md)

-   :material-trending-up: **梭罗成长**

    稳定状态、黄金法则，以及水准、对数与成长率的转换路径

    [:octicons-arrow-right-24: 梭罗成长](guides/growth.md)

-   :material-account-hard-hat-outline: **自然失业率**

    工资设置与价格设置，以及给付、加成与生产力造成的移动

    [:octicons-arrow-right-24: 自然失业率](guides/labor.md)

-   :material-view-dashboard-outline: **连动面板**

    四面板与五面板的推导，面板间共用的值只有一个数字，并可指定曲线移动

    [:octicons-arrow-right-24: 连动面板](guides/panels.md)

-   :material-play-box-multiple-outline: **动画**

    以 KineticKit 把移动或调整做成 GIF 或动画 SVG

    [:octicons-arrow-right-24: 动画](guides/animation.md)

-   :material-tune: **设置**

    从共用的 econ-viz.toml 设置颜色、线宽、字体、语言与标签微调

    [:octicons-arrow-right-24: 设置](guides/settings.md)

</div>

## 安装

```bash
uv add "macro-viz @ git+https://github.com/EconViz/macro-viz"
```

需要 Python 3.10 以上。`--prerelease allow`、字体与选用的动画套件请见[安装](installation.md)。

## 范例

文档里每张图都附有画出它的脚本，已依主题分文件夹。一次下载全部，内含脚本加载的设置档 `econ-viz.toml`（`base = "manual"`）。

[下载全部范例](../../assets/macro-viz/macro-viz-examples.zip){ .md-button download="" }
