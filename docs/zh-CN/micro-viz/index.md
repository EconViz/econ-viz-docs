---
seo_title: "绘制厂商与市场图形的 Python 软件包"
description: "开源 Python 软件包，绘制教科书的厂商与市场图形：生产、成本、竞争、独占、寡占、要素市场与不确定性。"
---

<h1 class="ev-visually-hidden">micro-viz：绘制厂商与市场图形的 Python 软件包</h1>

<p align="center">
  <img src="../../assets/micro-viz/banner.svg" alt="micro-viz" style="max-width: 480px; width: 100%; margin: 2rem 0 1rem;">
</p>

<p align="center"><em>用 Python 绘制厂商与市场的教科书图形。</em></p>

<p align="center">
  <a href="https://github.com/EconViz/micro-viz"><img alt="GitHub" src="https://img.shields.io/badge/github-EconViz%2Fmicro--viz-181818?style=flat-square&labelColor=f3f3f3"></a>
  <img alt="Python" src="https://img.shields.io/badge/python-3.10%2B-181818?style=flat-square&labelColor=f3f3f3">
  <img alt="Status" src="https://img.shields.io/badge/status-0.2.0.dev0-181818?style=flat-square&labelColor=f3f3f3">
</p>

!!! warning "micro-viz 开发中"

    micro-viz 0.2.0.dev0 尚未发布到 PyPI，请从 GitHub 安装；第一版发布前 API 仍可能变动。

```python
from micro_viz import (
    Config,
    CubicCost,
    LinearDemand,
    Monopolist,
    analyze_costs,
    monopoly_canvas,
)

Config.load("econ-viz.toml").use()

demand = LinearDemand(intercept=30, slope=2)
cost = CubicCost(fixed_cost=20, linear=6, quadratic=-1.5, cubic=0.15)
outcome = Monopolist(demand, cost).solve()
analysis = analyze_costs(cost, output_range=(2, 10))

canvas = monopoly_canvas(outcome, analysis, profit=True)
canvas.save("monopoly.png")
```

## 功能

<div class="grid cards" markdown>

-   :material-chart-bell-curve: **生产与成本**

    短期总产量、平均产量与边际产量、成本函数，以及阶梯与折点成本。

    [:octicons-arrow-right-24: 生产与成本](guides/production-costs.md)

-   :material-store-outline: **竞争**

    价格接受者厂商、产业供给、长期成本、进入与经济租。

    [:octicons-arrow-right-24: 竞争](guides/competition.md)

-   :material-crown-outline: **独占与定价**

    独占、管制、价格歧视、两部定价、搭售与广告。

    [:octicons-arrow-right-24: 独占与定价](guides/monopoly.md)

-   :material-account-group-outline: **寡占与垂直关系**

    古诺、史塔克柏格与柏川双占、拗折需求、支配厂商与双重加成。

    [:octicons-arrow-right-24: 寡占与垂直关系](guides/oligopoly.md)

-   :material-factory: **投入与技术**

    等产量线、成本最小化、要素市场、买方独占与工会。

    [:octicons-arrow-right-24: 投入与技术](guides/inputs.md)

-   :material-dice-multiple-outline: **不确定性与信息**

    期望效用、风险、拍卖、柠檬市场、信号与道德风险。

    [:octicons-arrow-right-24: 不确定性与信息](guides/uncertainty.md)

-   :material-label-outline: **标签与位置**

    取代任何内置文本、移动标签群组，并让文本避开线条。

    [:octicons-arrow-right-24: 标签与位置](guides/labels.md)

-   :material-tune: **设置**

    由共用的 econ-viz.toml 设置颜色、线宽、字体与区域底色。

    [:octicons-arrow-right-24: 设置](guides/settings.md)

-   :material-play-box-multiple-outline: **动画**

    把价格、产量或移动的变化做成 SVG 或 GIF 动画。

    [:octicons-arrow-right-24: 动画](guides/animation.md)

</div>

## 安装

```bash
uv add --prerelease allow "micro-viz @ git+https://github.com/EconViz/micro-viz"
```

需要 Python 3.10 以上。uv 与选用依赖请见[安装](installation.md)。

## 示例

文档里每张图都附有画出它的脚本，已依主题分文件夹。一次下载全部，内含脚本加载的设置档 `econ-viz.toml`（`base = "manual"`）。

[下载全部示例](../../assets/micro-viz/micro-viz-examples.zip){ .md-button download="" }
