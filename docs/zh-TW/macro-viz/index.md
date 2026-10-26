---
seo_title: "繪製總體經濟學圖形的 Python 套件"
description: "開源 Python 套件，繪製教科書的總體經濟學圖形：凱因斯十字、貨幣市場、AS-AD、IS-LM、梭羅成長、工資與價格設定、開放經濟與連動面板。"
---

<h1 class="ev-visually-hidden">macro-viz：繪製總體經濟學圖形的 Python 套件</h1>

<p align="center">
  <img src="../../assets/macro-viz/banner.svg" alt="macro-viz" style="max-width: 480px; width: 100%; margin: 2rem 0 1rem;">
</p>

<p align="center"><em>用 Python 繪製教科書的總體經濟學圖形。</em></p>

<p align="center">
  <a href="https://github.com/EconViz/macro-viz/actions"><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/EconViz/macro-viz/ci.yml?style=flat-square&label=ci&color=181818&labelColor=f3f3f3"></a>
  <a href="https://github.com/EconViz/macro-viz"><img alt="GitHub" src="https://img.shields.io/badge/github-EconViz%2Fmacro--viz-181818?style=flat-square&labelColor=f3f3f3"></a>
  <img alt="Python" src="https://img.shields.io/badge/python-3.10%2B-181818?style=flat-square&labelColor=f3f3f3">
</p>

!!! warning "macro-viz 目前為開發版"

    macro-viz 0.2.0.dev0 尚未上架 PyPI，第一次發行前 API 可能變動。請從 GitHub 安裝。

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

-   :material-cursor-default-click-outline: **凱因斯商品市場**

    消費函數、凱因斯十字與乘數，並含彎曲需求的變形

    [:octicons-arrow-right-24: 凱因斯商品市場](guides/keynesian.md)

-   :material-cash-multiple: **貨幣市場**

    貨幣需求與供給、央行貨幣與零利率下限

    [:octicons-arrow-right-24: 貨幣市場](guides/money.md)

-   :material-chart-line: **總合供給與需求**

    AS-AD 均衡、需求與供給衝擊，以及到中期的調整

    [:octicons-arrow-right-24: 總合供給與需求](guides/adas.md)

-   :material-vector-intersection: **IS-LM**

    財政與貨幣政策、排擠效果、平坦與陡峭的曲線、流動性陷阱與預期通膨

    [:octicons-arrow-right-24: IS-LM](guides/islm.md)

-   :material-earth: **開放經濟**

    淨出口、利率平價、浮動匯率的 IS-LM，以及 AS-AD 中的貶值

    [:octicons-arrow-right-24: 開放經濟](guides/open-economy.md)

-   :material-trending-up: **梭羅成長**

    穩定狀態、黃金法則，以及水準、對數與成長率的轉換路徑

    [:octicons-arrow-right-24: 梭羅成長](guides/growth.md)

-   :material-account-hard-hat-outline: **自然失業率**

    工資設定與價格設定，以及給付、加成與生產力造成的移動

    [:octicons-arrow-right-24: 自然失業率](guides/labor.md)

-   :material-view-dashboard-outline: **連動面板**

    四面板與五面板的推導，面板間共用的值只有一個數字，並可指定曲線移動

    [:octicons-arrow-right-24: 連動面板](guides/panels.md)

-   :material-play-box-multiple-outline: **動畫**

    以 KineticKit 把移動或調整做成 GIF 或動畫 SVG

    [:octicons-arrow-right-24: 動畫](guides/animation.md)

-   :material-tune: **設定**

    從共用的 econ-viz.toml 設定顏色、線寬、字型、語言與標籤微調

    [:octicons-arrow-right-24: 設定](guides/settings.md)

</div>

## 安裝

```bash
uv add "macro-viz @ git+https://github.com/EconViz/macro-viz"
```

需要 Python 3.10 以上。`--prerelease allow`、字型與選用的動畫套件請見[安裝](installation.md)。

## 範例

文件裡每張圖都附有畫出它的腳本，已依主題分資料夾。一次下載全部，內含腳本載入的設定檔 `econ-viz.toml`（`base = "manual"`）。

[下載全部範例](../../assets/macro-viz/macro-viz-examples.zip){ .md-button download="" }
