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

-   :material-chart-bell-curve-cumulative: **macro-viz**

    總體經濟學模型與圖形：凱因斯十字、貨幣市場、AS-AD、IS-LM、梭羅成長、開放經濟與連動面板。

    ```bash
    uv add "macro-viz @ git+https://github.com/EconViz/macro-viz"
    ```

    開發版，尚未上架 PyPI。

    [:octicons-arrow-right-24: macro-viz](macro-viz/index.md)

-   :material-factory: **micro-viz**

    廠商與市場的個體經濟學模型與圖形：生產、成本、競爭、獨占、定價、不確定性與資訊。

    ```bash
    uv add "micro-viz @ git+https://github.com/EconViz/micro-viz"
    ```

    開發版，尚未上架 PyPI。

    [:octicons-arrow-right-24: micro-viz](micro-viz/index.md)

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

    目前的穩定版本為 1.1.0。

    [:octicons-arrow-right-24: bezierkit](bezierkit/index.md)

</div>

### 動畫與字型

兩個各自獨立的引擎：KineticKit 負責動畫，GlyphKit 負責排版。兩者都不依賴經濟學套件。

<div class="grid cards ev-package-cards" markdown>

-   :material-animation-play: **kinetickit**

    確定性的 2D 與 3D 動畫，可輸出動態 SVG、串流 GIF 或互動 HTML。

    ```bash
    uv add --prerelease allow kinetickit
    ```

    預發行版本：1.0.0b2。

    [:octicons-arrow-right-24: kinetickit](kinetickit/index.md)

-   :material-format-font: **glyphkit**

    與繪圖端無關的排版：字型、字形處理、段落與數學式排版、精確輪廓與字型子集。

    ```bash
    uv add --prerelease allow glyphkit
    ```

    預發行版本：1.0.0b4。

    [:octicons-arrow-right-24: glyphkit](glyphkit/index.md)

</div>
