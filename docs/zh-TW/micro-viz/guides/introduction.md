---
seo_title: "簡介"
---

# 簡介

<span id="sec-intro"></span>

`micro-viz` 是個體經濟學廠商端的 Python 套件：生產、成本、完全競爭、獨占與定價、寡占、要素市場、不確定性與資訊。每個主題都有一個*模型*，以數字回答問題，也有一張依教科書慣例由模型畫出的*圖形*。

圖形可輸出為 PNG、SVG 或 PDF。統計資料圖與方塊加箭頭的流程圖不在套件範圍內。

`micro-viz` 屬於 EconViz 套件家族，以 `mosaickit` 繪圖；`mosaickit` 是與領域無關的場景與繪圖函式庫。消費者理論與一般均衡屬於 `utility-viz`，入門的供需圖屬於 `principle-viz`，賽局理論不在本套件範圍內。

## 範圍

本套件涵蓋六組主題，各有一章（參見 [章節指引](introduction.md#tab-guide)）。模型不引入任何繪圖器，因此結果可以不畫圖直接使用；繪圖函式只負責安置模型算出的內容。

## 閱讀指引

<span id="tab-guide"></span>

| 主題 | 說明 |
| --- | --- |
| [模型與圖形](model-figure.md#sec-model-figure) | 模型、繪圖函式、圖層編號與多欄圖如何配合 |
| [生產與成本](production-costs.md#sec-production-costs) | 短期生產、成本函式、階梯與折點成本 |
| [競爭](competition.md#sec-competition) | 價格接受者廠商、產業供給、長期成本、進入 |
| [獨占與定價](monopoly.md#sec-monopoly) | 獨占、獨占性競爭、管制、價格歧視、兩部定價、搭售、廣告、可耗竭資源 |
| [寡占](oligopoly.md#sec-oligopoly) | 雙占、拗折需求、支配廠商、垂直關係 |
| [投入與技術](inputs.md#sec-inputs) | 等產量線、成本最小化、學習與範疇、要素市場、買方獨佔與工會 |
| [不確定性與資訊](uncertainty.md#sec-uncertainty) | 期望效用、風險、拍賣、逆選擇、訊號、道德風險 |
| [設定](settings.md#sec-settings) | `econ-viz.toml` 的 `[micro]` 表 |
| [標籤與位置](labels.md#sec-labels) | 語系表、取代文字、移動標籤 |
| [新增圖形](adding-figure.md#sec-adding) | 模型、繪圖函式、文字、匯出、測試 |
| [動畫](animation.md#sec-animation) | 讓圖形隨參數變化 |

初次使用時，依序閱讀 [快速開始](../quickstart.md#sec-quickstart) 與 [模型與圖形](model-figure.md#sec-model-figure)。

所有圖形的繪製腳本依主題整理成一個壓縮檔：[micro-viz-examples.zip](https://econ-viz.org/assets/micro-viz/micro-viz-examples.zip)。
