---
seo_title: "繪製廠商與市場圖形的 Python 套件"
description: "開源 Python 套件，繪製教科書的廠商與市場圖形：生產、成本、競爭、獨占、寡占、要素市場與不確定性。"
---

<h1 class="ev-visually-hidden">micro-viz：繪製廠商與市場圖形的 Python 套件</h1>

<p align="center">
  <img src="../../assets/micro-viz/banner.svg" alt="micro-viz" style="max-width: 480px; width: 100%; margin: 2rem 0 1rem;">
</p>

<p align="center"><em>用 Python 繪製廠商與市場的教科書圖形。</em></p>

<p align="center">
  <a href="https://github.com/EconViz/micro-viz"><img alt="GitHub" src="https://img.shields.io/badge/github-EconViz%2Fmicro--viz-181818?style=flat-square&labelColor=f3f3f3"></a>
  <img alt="Python" src="https://img.shields.io/badge/python-3.10%2B-181818?style=flat-square&labelColor=f3f3f3">
  <img alt="Status" src="https://img.shields.io/badge/status-0.2.0.dev0-181818?style=flat-square&labelColor=f3f3f3">
</p>

!!! warning "micro-viz 開發中"

    micro-viz 0.2.0.dev0 尚未發布到 PyPI，請從 GitHub 安裝；第一版發布前 API 仍可能變動。

```python
from micro_viz import (
    ShortRunProductionFunction,
    analyze_production,
    total_product_canvas,
)

production = ShortRunProductionFunction(
    linear=6, quadratic=3, cubic=-0.5
)
result = analyze_production(production, input_range=(0, 6))

total_product_canvas(result).save("total_product.svg")
```

![總產量](../../assets/micro-viz/production/total_product.zh-TW.svg){ .ev-figure-sm }

## 功能

<div class="grid cards" markdown>

-   :material-chart-bell-curve: **生產與成本**

    短期總產量、平均產量與邊際產量、成本函式，以及階梯與折點成本。

    [:octicons-arrow-right-24: 生產與成本](guides/production-costs.md)

-   :material-store-outline: **競爭**

    價格接受者廠商、產業供給、長期成本、進入與經濟租。

    [:octicons-arrow-right-24: 競爭](guides/competition.md)

-   :material-crown-outline: **獨占與定價**

    獨占、管制、價格歧視、兩部定價、搭售與廣告。

    [:octicons-arrow-right-24: 獨占與定價](guides/monopoly.md)

-   :material-account-group-outline: **寡占與垂直關係**

    古諾、史塔克柏格與柏川雙占、拗折需求、支配廠商與雙重加成。

    [:octicons-arrow-right-24: 寡占與垂直關係](guides/oligopoly.md)

-   :material-factory: **投入與技術**

    等產量線、成本最小化、要素市場、買方獨佔與工會。

    [:octicons-arrow-right-24: 投入與技術](guides/inputs.md)

-   :material-dice-multiple-outline: **不確定性與資訊**

    期望效用、風險、拍賣、檸檬市場、訊號與道德風險。

    [:octicons-arrow-right-24: 不確定性與資訊](guides/uncertainty.md)

-   :material-label-outline: **標籤與位置**

    取代任何內建文字、移動標籤群組，並讓文字避開線條。

    [:octicons-arrow-right-24: 標籤與位置](guides/labels.md)

-   :material-tune: **設定**

    由共用的 econ-viz.toml 設定顏色、線寬、字型與區域底色。

    [:octicons-arrow-right-24: 設定](guides/settings.md)

-   :material-play-box-multiple-outline: **動畫**

    把價格、產量或移動的變化做成 SVG 或 GIF 動畫。

    [:octicons-arrow-right-24: 動畫](guides/animation.md)

</div>

## 安裝

```bash
uv add --prerelease allow "micro-viz @ git+https://github.com/EconViz/micro-viz"
```

需要 Python 3.10 以上。uv 與選用依賴請見[安裝](installation.md)。

## 範例

文件裡每張圖都附有畫出它的腳本，已依主題分資料夾。一次下載全部，內含腳本載入的設定檔 `econ-viz.toml`（`base = "manual"`）。

[下載全部範例](../../assets/micro-viz/micro-viz-examples.zip){ .md-button download="" }
