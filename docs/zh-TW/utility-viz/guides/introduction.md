---
seo_title: "簡介"
---

# 簡介

<span id="sec-intro"></span>

`utility-viz` 是個體經濟學繪圖套件，涵蓋效用模型、最適消費組合求解與視覺化。Python API 與命令列工具均可產生無異曲線、預算線、消費者均衡、需求曲線及 Edgeworth 箱形圖。

圖形預設顯示第一象限，座標軸以箭頭表示並隱藏數字刻度，標籤支援 TeX 數學語法。輸出格式包括 PNG、PDF、SVG、TikZ 與 GIF。

本套件在 1.12 版以前名為 `econ-viz`，2.0.0 起更名為 `utility-viz`；變更內容與舊程式碼的相容方式詳見[從 `econ-viz` 遷移](../getting-started/installation.md#sec-migrate)。本手冊說明預覽版 2.0.0b1。

`utility-viz` 屬於 EconViz 系列套件：繪圖透過與領域無關的場景與繪製函式庫 `mosaickit`，曲線則以 `bezierkit` 描繪。經濟學原理圖形由同系列的 `principle-viz` 負責。

## 功能範圍

`utility-viz` 的功能分為效用模型、均衡求解、效用水準、圖層與匯出格式五個部分。模型與求解結果可分開使用；同一模型也可交由畫布、多面板圖、需求圖或分析 API 處理。

## 閱讀指引

本手冊依主題分成四個部分（參見[章節主題](introduction.md#tab-guide)）：

<span id="tab-guide"></span>

| 主題 | 子主題 | 說明 | 章節 |
| --- | --- | --- | --- |
| 繪圖與匯出 | 畫布與圖層 | 座標軸、曲線與均衡點 | [Canvas 畫布](canvas.md#sec-canvas) |
|  | 多面板圖與需求圖 | 並排比較與需求曲線 | [多面板圖與需求圖](consumer.md#sec-figures) |
|  | 主題與設定檔 | 配色、樣式與設定檔 | [主題與設定](themes.md#sec-themes) |
|  | 輸出格式 | 匯出圖檔與 TikZ | [匯出](export.md#sec-export) |
| 模型與分析 | 內建模型 | 常見效用函數 | [核心模型](../models/index.md#sec-models) |
|  | 自訂與多商品模型 | 自訂函數與多商品、場景 | [進階模型](../models/advanced.md#sec-advanced) |
|  | 比較靜態與 Slutsky 矩陣 | 需求導數與齊次性 | [分析](../tools/analysis.md#sec-analysis) |
| 動畫與互動 | GIF 動畫 | 參數變動的 GIF | [動畫](animation.md#sec-animation) |
|  | Jupyter 互動元件 | 筆記本滑桿調參數 | [互動元件](interactive.md#sec-widgets) |
| 其他輸入方式 | 命令列工具 | 使用命令列產圖 | [命令列工具](../getting-started/cli.md#sec-cli) |
|  | LaTeX 效用函數解析 | 從算式建立模型 | [LaTeX 解析](../tools/latex.md#sec-latex) |

初次使用時，依序閱讀[快速開始](../getting-started/quickstart.md#sec-quickstart)與[Canvas 畫布](canvas.md#sec-canvas)。查詢特定 API 時，可直接前往對應章節或指令索引。從 `econ-viz` 1.x 升級時，請先閱讀[從 `econ-viz` 遷移](../getting-started/installation.md#sec-migrate)。
