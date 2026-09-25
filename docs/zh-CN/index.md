---
seo_title: "绘制微观经济学图形的 Python 包"
description: "开源 Python 包，绘制出版质量的微观经济学图形：无差异曲线、预算约束、消费者均衡，并可导出 TikZ。"
---

<h1 class="ev-visually-hidden">Econ-Viz：绘制微观经济学图形的 Python 包</h1>

<p align="center">
  <img src="../assets/banner.svg" alt="Econ-Viz" style="max-width: 480px; width: 100%; margin: 2rem 0 1rem;">
</p>

<p align="center"><em>用 Python 绘制出版质量的微观经济学图形。</em></p>

<p align="center">
  <a href="https://github.com/EconViz/econ-viz/actions"><img alt="Publish" src="https://img.shields.io/github/actions/workflow/status/EconViz/econ-viz/publish.yml?style=flat-square&label=publish&color=181818&labelColor=f3f3f3"></a>
  <img alt="Coverage" src="https://img.shields.io/badge/coverage-92.63%25-181818?style=flat-square&color=181818&labelColor=f3f3f3">
  <a href="https://pypi.org/project/econ-viz/"><img alt="PyPI" src="https://img.shields.io/pypi/v/econ-viz?style=flat-square&label=pypi+package&color=181818&labelColor=f3f3f3&cacheSeconds=300"></a>
  <a href="https://pypi.org/project/econ-viz/"><img alt="Python" src="https://img.shields.io/pypi/pyversions/econ-viz?style=flat-square&color=181818&labelColor=f3f3f3"></a>
</p>

---

:fontawesome-brands-github: **源代码：** [https://github.com/EconViz/econ-viz](https://github.com/EconViz/econ-viz)

:fontawesome-solid-envelope: **联系我们：** [contact@econ-viz.org](mailto:contact@econ-viz.org)

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

-   :material-shape-outline: **八种内置效用模型**

    涵盖 Cobb-Douglas、完全互补、CES 等教科书常见的效用函数，从完全替代到饱和偏好都能直接画

    [:octicons-arrow-right-24: 模型目录](models/index.md)

-   :material-function: **自动求解均衡**

    给定价格与收入，自动找出消费者的最优组合。无论是内点解、折点还是角点解，都不需要自己推导

    [:octicons-arrow-right-24: 快速开始](getting-started/quickstart.md)

-   :material-view-dashboard-outline: **多面板教学图**

    把多张图并排、上下堆叠或排成网格，适合呈现价格变动前后的比较、效应分解，或是直接放进课堂幻灯片中使用

    [:octicons-arrow-right-24: 多面板图与需求图](guides/consumer.md)

-   :material-chart-bell-curve-cumulative: **需求路径图**

    让价格或收入逐步变动，画出价格消费曲线与收入消费曲线，并把每个最优点连接到下方的 Marshall 需求曲线

    [:octicons-arrow-right-24: 多面板图与需求图](guides/consumer.md)

-   :material-math-integral: **LaTeX 解析器**

    直接粘贴讲义或论文里的 LaTeX 效用函数，就能自动识别函数形式与参数，创建对应的模型，马上开始画图

    [:octicons-arrow-right-24: LaTeX 解析](tools/latex.md)

-   :material-export: **出版质量的导出**

    一行代码就能保存为 PNG、PDF 或 SVG，矢量格式放大也不会失真，可以直接放进论文、幻灯片与网页中使用

    [:octicons-arrow-right-24: 导出格式](guides/export.md)

-   :material-play-box-multiple-outline: **GIF 动画**

    把参数、价格或收入的变动做成 GIF 动画，让学生亲眼看见均衡点如何随预算线移动，适合放进幻灯片或网页

    [:octicons-arrow-right-24: 动画](guides/animation.md)

-   :material-tune: **笔记本交互组件**

    在 Jupyter 中用滑块或输入数值实时调整参数，图形会跟着更新，学生可以自己动手探索不同情境下的均衡

    [:octicons-arrow-right-24: 交互组件](guides/interactive.md)

-   :material-chart-line: **分析工具**

    计算比较静态与 Slutsky 矩阵，并检查效用函数的齐次性与位似性，把图形背后的数学性质也一并验证清楚

    [:octicons-arrow-right-24: 分析工具](tools/analysis.md)

-   :material-code-braces: **高级模型**

    把任何自定义函数包装成效用函数，或把多种商品的偏好固定其余变量、投影到平面上，画出教科书以外的情境

    [:octicons-arrow-right-24: 高级模型](models/advanced.md)

-   :material-console: **命令行工具**

    不写 Python 也能直接在终端生成图形，还能输出 Marshall 需求的闭式解公式，方便贴进 LaTeX 讲义

    [:octicons-arrow-right-24: 命令行工具说明](getting-started/cli.md)

</div>

## 安装

```bash
uv add econ-viz
```

需要 Python 3.10 以上。
