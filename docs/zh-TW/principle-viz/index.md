---
seo_title: "principle-viz：用 Python 繪製經濟學原理的市場圖形"
description: "principle-viz 是用於經濟學原理市場分析與繪圖的 Python 套件：均衡、租稅、價格管制、福利分析等，以線性需求與供給為基礎。"
---

# principle-viz

`principle-viz` 是用於經濟學原理市場分析與繪圖的 Python 套件，聚焦於**線性需求與供給**模型，
並把求解、政策、福利分解與繪圖拆成各自獨立的模組。

![用 principle-viz 繪製的基本市場均衡圖](../../assets/principle-viz/basic_equilibrium.png){ width="360" }

| | |
|---|---|
| 本文件對應版本 | 0.10.0 |
| Python | 3.10 以上 |
| 依賴 | [mosaickit](../mosaickit/index.md)（`>=0.5.1,<0.6.0`） |
| 命令列 | `principle-viz` |
| 原始碼 | [github.com/EconViz/principle-viz](https://github.com/EconViz/principle-viz) |
| 授權 | MIT |

## 功能範圍

- 由線性需求與供給，或離散的單位表求解市場均衡
- 比較靜態分析：需求或供給移動，以及從舊均衡到新均衡的變化
- 租稅（定額、從量、從價；課在買方或賣方）與補貼
- 價格上限、價格下限與最低工資
- 福利分解：消費者剩餘、生產者剩餘、稅收與無謂損失
- 國際貿易（自由貿易、關稅、配額）、外部性、共有資源、公共財、可貸資金、生產可能曲線與彈性
- 把個別曲線或個別需求表水平加總成市場需求與供給
- 以 [mosaickit](../mosaickit/index.md) 為基礎的教科書風格圖形
- 支援 JSON 輸出的命令列工具

## 接下來

<div class="grid cards" markdown>

-   :material-download: **安裝**

    用 pip 或 uv 安裝套件。

    [:octicons-arrow-right-24: 安裝](installation.md)

-   :material-rocket-launch-outline: **快速開始**

    求解市場、比較租稅效果，並畫出圖形。

    [:octicons-arrow-right-24: 快速開始](quickstart.md)

</div>
