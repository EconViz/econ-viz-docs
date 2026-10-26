---
seo_title: "簡介"
---

# 簡介

<span id="sec-intro"></span>

`kinetickit` 是不綁定特定用途的動畫引擎。它負責場景、動作、可重現的影格排程、繪圖端能力、互動、無障礙中繼資料與檔案匯出。經濟學套件和其他應用程式只要把自己的物件轉成一般 KineticKit 節點即可。

同一個不可變場景和一段動作，可以輸出成動態 SVG、串流 GIF 與單檔互動 HTML。同一場景在同一時間一定得到相同快照，系統時間與繪圖端的選擇都不會進入模型。

KineticKit 不會匯入 `mosaickit`、`utility-viz` 或其他特定用途的套件。字型處理由 `glyphkit` 負責，並透過一個轉接器接入場景，詳見[文字排版](typography.md#sec-typography)。

## 分層

| 層 | 可以知道 | 不可以知道 |
| --- | --- | --- |
| 動作核心（`easing`、`interpolation`、`timeline`、`tween`、`keyframes`） | 時間、數值、協定 | 場景、繪圖端 |
| 場景模型（`geometry`、`scene`、`styles`、`morph`、`transitions`） | 幾何、樣式、物件編號 | 後端物件 |
| 繪圖端（`renderers.vector`、`.raster`、`.interactive`） | 場景快照、能力 | 使用端的領域模型 |
| 匯出器（`exporters`） | 影格、成品、輸出目標 | 視覺化邏輯 |

這些界線由 import-linter 規則與讀取語法樹的測試把關。Matplotlib、Plotly 與 Pillow 只出現在私有的 `_*` 模組裡。

## 簡短導覽

1. [快速開始](../quickstart.md)移動一個點，並寫成三種格式。
2. [場景與動作](scenes-motion.md)列出各種節點，並說明動作如何組合。
3. [輸出格式](outputs.md)說明能力、替代方案，以及各格式保留什麼。
4. [範例](examples.md)執行一張圖表、一個轉接器與一個 3D 曲面。
