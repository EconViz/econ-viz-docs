---
seo_title: "繪製經濟學圖形的 Python 套件"
description: "EconViz 是一組開源 Python 套件，用來繪製經濟學圖形：utility-viz、principle-viz、mosaickit 與 bezierkit。"
---

<h1 class="ev-visually-hidden">EconViz：繪製經濟學圖形的 Python 套件</h1>

<p align="center">
  <img src="../assets/banner.svg" alt="EconViz" style="max-width: 480px; width: 100%; margin: 2rem 0 1rem;">
</p>

<p align="center"><em>用 Python 繪製經濟學圖形的開源套件。</em></p>

---

:fontawesome-brands-github: **原始碼：** [https://github.com/EconViz](https://github.com/EconViz)

:fontawesome-solid-envelope: **聯絡我們：** [contact@econ-viz.org](mailto:contact@econ-viz.org)

---

## 模組

EconViz 由四個套件組成：兩個負責繪製經濟學圖形，另外兩個是它們共用的通用元件。

### 經濟學套件

兩個負責繪製經濟學圖形的套件。

<div class="grid cards ev-package-cards" markdown>

-   :material-chart-bell-curve-cumulative: **utility-viz**

    繪製出版品質的個體經濟學圖形：無異曲線、預算限制、消費者均衡，並可匯出 TikZ。

    ```bash
    uv add --prerelease allow utility-viz
    ```

    2.0 版目前為 Beta。

    [:octicons-arrow-right-24: utility-viz](utility-viz/index.md)

-   :material-scale-balance: **principle-viz**

    經濟學原理的市場分析與圖形：均衡、租稅、價格管制、福利與貿易，以線性需求與供給為基礎。

    ```bash
    uv add principle-viz
    ```

    [:octicons-arrow-right-24: principle-viz](principle-viz/index.md)

</div>

### 底層套件

兩個通用的基礎元件，由經濟學套件共用。

<div class="grid cards ev-package-cards" markdown>

-   :material-view-grid-outline: **mosaickit**

    與領域無關的工具組，用場景、圖層、樣式、參數與渲染器組合出二維圖形。

    ```bash
    uv add mosaickit
    ```

    [:octicons-arrow-right-24: mosaickit](mosaickit/index.md)

-   :material-vector-bezier: **bezierkit**

    小巧的數學工具組，用來建構、分析與匯出貝茲曲線，並原生支援 SVG 與 TikZ 輸出。

    ```bash
    uv add bezierkit
    ```

    目前的穩定版本為 1.0.1。

    [:octicons-arrow-right-24: bezierkit](bezierkit/index.md)

</div>
