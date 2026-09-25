---
seo_title: "繪製個體經濟學圖形的 Python 套件"
description: "開源 Python 套件，繪製出版品質的個體經濟學圖形：無異曲線、預算限制、消費者均衡，並可匯出 TikZ。"
---

<h1 class="ev-visually-hidden">Econ-Viz：繪製個體經濟學圖形的 Python 套件</h1>

<p align="center">
  <img src="../assets/banner.svg" alt="Econ-Viz" style="max-width: 480px; width: 100%; margin: 2rem 0 1rem;">
</p>

<p align="center"><em>用 Python 繪製高品質的個體經濟學圖形。</em></p>

<p align="center">
  <a href="https://github.com/EconViz/econ-viz/actions"><img alt="Publish" src="https://img.shields.io/github/actions/workflow/status/EconViz/econ-viz/publish.yml?style=flat-square&label=publish&color=181818&labelColor=f3f3f3"></a>
  <img alt="Coverage" src="https://img.shields.io/badge/coverage-99%25-181818?style=flat-square&color=181818&labelColor=f3f3f3">
  <a href="https://pypi.org/project/econ-viz/"><img alt="PyPI" src="https://img.shields.io/pypi/v/econ-viz?style=flat-square&label=pypi+package&color=181818&labelColor=f3f3f3"></a>
  <a href="https://pypi.org/project/econ-viz/"><img alt="Python" src="https://img.shields.io/pypi/pyversions/econ-viz?style=flat-square&color=181818&labelColor=f3f3f3"></a>
</p>

---

:fontawesome-brands-github: **原始碼：** [https://github.com/EconViz/econ-viz](https://github.com/EconViz/econ-viz)

:fontawesome-solid-envelope: **聯絡我們：** [contact@econ-viz.org](mailto:contact@econ-viz.org)

---

```python
from econ_viz import Canvas, levels, solve
from econ_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.5, beta=0.5)
eq    = solve(model, px=2.0, py=3.0, income=30.0)
lvls  = levels.around(eq.utility, n=5)

cvs = Canvas(x_max=20, y_max=15, title=r"Cobb-Douglas $x^{0.5} y^{0.5}$")
cvs.add_utility(model, levels=lvls)
cvs.add_budget(2.0, 3.0, 30.0, fill=True)
cvs.add_equilibrium(eq, show_ray=True)
cvs.save("cobb_douglas.png")
```

## 功能特色

<div class="grid cards" markdown>

-   :material-shape-outline: **八種內建效用模型**

    涵蓋 Cobb-Douglas、完全互補、CES 等教科書常見的效用函數，從完全替代到飽和偏好都能直接畫

    [:octicons-arrow-right-24: 模型目錄](models/index.md)

-   :material-function: **自動求解均衡**

    給定價格與所得，自動找出消費者的最適組合。無論是內部解、拗折點或是角解，均毋需自己推導

    [:octicons-arrow-right-24: 快速開始](getting-started/quickstart.md)

-   :material-view-dashboard-outline: **多面板教學圖**

    將多張圖並排、上下堆疊或排成網格，適合呈現價格變動前後的比較、效果分解，或是直接放進課堂簡報中使用

    [:octicons-arrow-right-24: 多面板圖與需求圖](guides/consumer.md)

-   :material-chart-bell-curve-cumulative: **需求路徑圖**

    讓價格或所得逐步變動，畫出價格消費曲線與所得消費曲線，並把每個最適點連結到下方的 Marshall 需求曲線

    [:octicons-arrow-right-24: 多面板圖與需求圖](guides/consumer.md)

-   :material-math-integral: **LaTeX 解析器**

    直接貼上講義或論文裡的 LaTeX 效用函數，就能自動辨識函數形式與參數，建立對應的模型，馬上開始畫圖

    [:octicons-arrow-right-24: LaTeX 解析](tools/latex.md)

-   :material-export: **出版品質的匯出**

    一行程式就能存成 PNG、PDF 或 SVG，向量格式放大也不會失真，可以直接放進論文、簡報與網頁中使用

    [:octicons-arrow-right-24: 匯出格式](guides/export.md)

-   :material-play-box-multiple-outline: **GIF 動畫**

    將參數、價格或所得的變動做成 GIF 動畫，可實際看見均衡點如何隨預算線移動，適合放進簡報或網頁

    [:octicons-arrow-right-24: 動畫](guides/animation.md)

-   :material-tune: **筆記本互動元件**

    在 Jupyter 中用滑桿或輸入數值即時調整參數，圖形會跟著更新，學生可以自己動手探索不同情境下的均衡

    [:octicons-arrow-right-24: 互動元件](guides/interactive.md)

-   :material-chart-line: **分析工具**

    計算比較靜態與 Slutsky 矩陣，並檢查效用函數的齊次性與位似性，把圖形背後的數學性質也一併驗證清楚

    [:octicons-arrow-right-24: 分析工具](tools/analysis.md)

-   :material-code-braces: **進階模型**

    把任何自訂函數包裝成效用函數，或把多種商品的偏好固定其餘變數、投影到平面上，畫出教科書以外的情境

    [:octicons-arrow-right-24: 進階模型](models/advanced.md)

-   :material-console: **命令列工具**

    不寫 Python 也能直接在終端機產生圖形，還能輸出 Marshall 需求的封閉解公式，方便貼進 LaTeX 講義

    [:octicons-arrow-right-24: 命令列工具說明](getting-started/cli.md)

</div>

## 安裝

```bash
uv add econ-viz
```

需要 Python 3.10 以上。
