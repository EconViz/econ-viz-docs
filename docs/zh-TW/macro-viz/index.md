---
seo_title: "macro-viz：用 Python 繪製總體經濟學圖形"
description: "macro-viz 用 Python 繪製教科書的總體經濟學模型：凱因斯十字、貨幣市場、AS-AD、IS-LM、梭羅成長、工資與價格設定、開放經濟與連動面板。"
---

<h1 class="ev-visually-hidden">macro-viz：用 Python 繪製總體經濟學圖形</h1>

<p align="center">
  <img src="../../assets/macro-viz/banner.svg" alt="macro-viz" style="max-width: 480px; width: 100%; margin: 2rem 0 1rem;">
</p>

<p align="center"><em>教科書總體經濟學分析與圖形的 Python 套件。</em></p>

`macro-viz` 用於已給定方程式、需要分析或繪圖的初級與中級總體經濟學模型。每個模型是不知道如何繪圖的型別化物件；每張圖是由模型建出的 `mosaickit` 畫布。統計資料圖與會計方塊圖不在範圍內。

```python
from macro_viz.keynesian import (
    ConsumptionFunction,
    KeynesianCross,
    analyze_autonomous_shift,
)
from macro_viz.visuals import multiplier_canvas

model = KeynesianCross(
    ConsumptionFunction(20, 0.6),
    investment=20,
    government=30,
    taxes=20,
)
shift = analyze_autonomous_shift(model, change=30)

multiplier_canvas(shift).save("multiplier.svg")
```

<span id="fig-index-multiplier"></span>

<figure class="ev-fig" markdown>

![自發性支出增加](../../assets/macro-viz/keynesian/multiplier.zh-TW.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/macro-viz/keynesian/keynesian.py" download aria-label="下載生圖原始檔"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下載生圖原始檔</span></a></div>

<figcaption markdown>自發性支出增加</figcaption>

</figure>

## 模型與圖形

| 模型 | 模組 | 圖形 |
| --- | --- | --- |
| 消費函數、凱因斯十字、乘數 | `keynesian` | [凱因斯商品市場](guides/keynesian.md) |
| 貨幣需求與供給、央行貨幣、零下限 | `money` | [貨幣市場](guides/money.md) |
| 總合供給與需求、衝擊、中期調整 | `adas` | [總合供給與需求](guides/adas.md) |
| IS-LM、財政與貨幣政策、排擠效果、預期通膨 | `islm` | [IS-LM](guides/islm.md) |
| 梭羅成長、黃金法則、轉換路徑 | `growth` | [梭羅成長](guides/growth.md) |
| 工資設定、價格設定、自然失業率 | `labor` | [自然失業率](guides/labor.md) |
| 開放經濟商品市場、利率平價、Mundell-Fleming、貶值 | `open_economy` | [開放經濟](guides/open-economy.md) |
| 連動的四面板與五面板推導 | `panels` | [連動面板](guides/panels.md) |

每個繪圖函式都回傳 `mosaickit` 的 `Canvas`，並使用穩定的 `macro.*` 圖層編號。文字來自英文、繁體中文與簡體中文的語系表，任何一個都可以用 `labels=` 取代。尺寸、線寬、顏色與字型來自主題與共用的 `econ-viz.toml`，繪圖程式碼中沒有這些數值。

!!! note "狀態"

    `macro-viz` 版本為 `0.2.0.dev0`，尚未發布到 PyPI；請從 GitHub 安裝（參見 [安裝](installation.md#sec-install)）。

## 圖形的風格

- 白底黑線，如同印刷教科書；沒有深色主題。
- 只有價格 `p` 用小寫；其他變數（$Y$、$R$、$W$、$N$、$K$）一律用大寫斜體。
- 變動後的曲線是細實線，名稱加上撇號（`IS'`）。平行移動畫成由舊點指向新曲線的直線箭頭；彎曲的箭頭只代表轉動，也就是斜率改變。
- 曲線名稱放在線的末端，沒有任何文字蓋到線或其他文字。

## 範圍

- `macro-viz` 負責封閉與開放經濟的短期模型與成長模型。
- 消費者理論與一般均衡屬於 [utility-viz](../utility-viz/index.md)。
- 廠商與市場屬於 [micro-viz](../micro-viz/index.md)。
- 統計圖（真實資料散布圖、實證時間序列）與會計方塊不繪製。
