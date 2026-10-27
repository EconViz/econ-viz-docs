---
seo_title: "绘制经济学图形的 Python 包"
description: "EconViz 是一组开源 Python 包，用来绘制经济学图形：utility-viz、principle-viz、mosaickit 与 bezierkit。"
---

<h1 class="ev-visually-hidden">EconViz：绘制经济学图形的 Python 包</h1>

<p align="center">
  <img src="../assets/banner.svg" alt="EconViz" style="max-width: 480px; width: 100%; margin: 2rem 0 1rem;">
</p>

<p align="center"><em>用 Python 绘制经济学图形的开源包。</em></p>

---

:fontawesome-brands-github: **源代码：** [https://github.com/EconViz](https://github.com/EconViz)

:fontawesome-solid-envelope: **联系我们：** [contact@econ-viz.org](mailto:contact@econ-viz.org)

---

## 模块

EconViz 由四个包组成：两个负责绘制经济学图形，另外两个是它们共用的通用组件。

### 经济学包

两个负责绘制经济学图形的包。

<div class="grid cards ev-package-cards" markdown>

-   :material-chart-bell-curve-cumulative: **utility-viz**

    绘制出版质量的微观经济学图形：无差异曲线、预算约束、消费者均衡，并可导出 TikZ。

    ```bash
    uv add --prerelease allow utility-viz
    ```

    2.0 版目前处于 Beta 阶段。

    [:octicons-arrow-right-24: utility-viz](utility-viz/index.md)

-   :material-scale-balance: **principle-viz**

    经济学原理的市场分析与图形：均衡、税收、价格管制、福利与贸易，以线性需求与供给为基础。

    ```bash
    uv add principle-viz
    ```

    [:octicons-arrow-right-24: principle-viz](principle-viz/index.md)

-   :material-factory: **micro-viz**

    厂商与市场的微观经济学模型与图形：生产、成本、竞争、垄断、定价、不确定性与信息。

    ```bash
    uv add "micro-viz @ git+https://github.com/EconViz/micro-viz"
    ```

    开发版，尚未上架 PyPI。

    [:octicons-arrow-right-24: micro-viz](micro-viz/index.md)

</div>

### 底层包

两个通用的基础组件，由经济学包共用。

<div class="grid cards ev-package-cards" markdown>

-   :material-view-grid-outline: **mosaickit**

    与领域无关的工具包，用场景、图层、样式、参数与渲染器组合出二维图形。

    ```bash
    uv add mosaickit
    ```

    [:octicons-arrow-right-24: mosaickit](mosaickit/index.md)

-   :material-vector-bezier: **bezierkit**

    小巧的数学工具包，用来构造、分析与导出贝塞尔曲线，并原生支持 SVG 与 TikZ 输出。

    ```bash
    uv add bezierkit
    ```

    当前稳定版本为 1.1.0。

    [:octicons-arrow-right-24: bezierkit](bezierkit/index.md)

</div>

### 动画与字体

两个各自独立的引擎：KineticKit 负责动画，GlyphKit 负责排版。两者都不依赖经济学软件包。

<div class="grid cards ev-package-cards" markdown>

-   :material-animation-play: **kinetickit**

    确定性的 2D 与 3D 动画，可输出动态 SVG、流式 GIF 或交互 HTML。

    ```bash
    uv add --prerelease allow kinetickit
    ```

    预发布版本：1.0.0b2。

    [:octicons-arrow-right-24: kinetickit](kinetickit/index.md)

-   :material-format-font: **glyphkit**

    与绘图端无关的排版：字体、字形处理、段落与数学式排版、精确轮廓与字体子集。

    ```bash
    uv add --prerelease allow glyphkit
    ```

    预发布版本：1.0.0b4。

    [:octicons-arrow-right-24: glyphkit](glyphkit/index.md)

</div>
