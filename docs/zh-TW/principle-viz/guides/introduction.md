---
seo_title: "簡介"
---

# 簡介

<span id="sec-intro"></span>

`principle-viz` 是經濟學原理的繪圖套件，涵蓋供給與需求、均衡及其移動、租稅與補貼、價格管制、福利、國際貿易、市場失靈、要素市場與生產可能曲線。每個主題都有計算與圖形兩個部分：計算回傳數值，圖形依教科書慣例繪製。

圖形的曲線名稱標在末端而不放進圖例，面積名稱寫在區塊內，數值標在座標軸上，所有文字都不遮住線、點或其他文字。輸出格式包括 PNG、SVG 與 PDF；命令列工具則以 JSON 輸出計算結果。

`principle-viz` 屬於 EconViz 系列套件，繪圖使用與領域無關的場景與繪製函式庫 `mosaickit`。同系列的 `utility-viz` 是個體經濟學繪圖套件，涵蓋效用模型、最適消費組合求解，以及無異曲線、預算線、消費者均衡、需求曲線與 Edgeworth 箱形圖；本套件不包含這些功能。

## 功能範圍

`principle-viz` 處理線性市場，功能分為市場、政策、應用與工具四個部分。計算與圖形可分開使用；同一個結果可以印出、輸出為 JSON，也可以交給 `MarketFigure` 繪製。

## 閱讀指引

本手冊依主題分成市場、政策、應用與工具四個部分（參見[章節主題](introduction.md#tab-guide)）：

<span id="tab-guide"></span>

| 主題 | 子主題 | 說明 | 章節 |
| --- | --- | --- | --- |
| 線性市場 | 直線、均衡與曲線移動 | [線性市場](markets.md#sec-markets) | 離散市場 |
| 逐單位的需求與供給表 | [離散市場](discrete.md#sec-discrete) | 市場曲線加總 | 個人曲線的水平加總 |
| [由個人加總市場曲線](aggregation.md#sec-aggregation) | 彈性與總收益 | 點彈性、弧彈性與總收益曲線 | [彈性與總收益](elasticity.md#sec-elasticity) |
| 福利 | 消費者剩餘、生產者剩餘與無謂損失 | [福利](welfare.md#sec-welfare) | 租稅與補貼 |
| 稅負楔差與補貼成本 | [租稅與補貼](taxes.md#sec-taxes) | 價格管制 | 價格上限、價格下限與短缺 |
| [價格管制](controls.md#sec-controls) | 國際貿易 | 自由貿易、關稅與進口配額 | [國際貿易](trade.md#sec-trade) |
| 市場失靈 | 外部性、共有資源與公共財 | [市場失靈](failures.md#sec-failures) | 勞動與可貸資金 |
| 最低工資與政府借款 | [勞動與可貸資金](factor-markets.md#sec-factor) | 生產可能曲線 | 機會成本、成長與比較利益 |
| [生產可能曲線](ppf.md#sec-ppf) | 圖形 | 標籤、圖層與配色 | [圖形](figures.md#sec-figures) |
| 命令列介面 | 以 JSON 輸出計算結果 | [命令列介面](../cli.md#sec-cli) |

初次使用時，依序閱讀[快速開始](../quickstart.md#sec-quickstart)、[線性市場](markets.md#sec-markets)與[圖形](figures.md#sec-figures)。之後每章說明一個主題，先介紹計算，再介紹圖形。查詢特定指令的選項時，可直接前往[命令列介面](../cli.md#sec-cli)。
