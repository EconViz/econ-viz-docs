---
seo_title: "简介"
---

# 简介

<span id="sec-intro"></span>

`utility-viz` 是微观经济学绘图软件包，涵盖效用模型、最优消费组合求解与可视化。Python API 与命令行工具均可生成无差异曲线、预算线、消费者均衡、需求曲线及 Edgeworth 箱形图。

图形默认显示第一象限，坐标轴以箭头表示并隐藏数字刻度，标签支持 TeX 数学语法。输出格式包括 PNG、PDF、SVG、TikZ 与 GIF。

本软件包在 1.12 版以前名为 `econ-viz`，2.0.0 起更名为 `utility-viz`；变更内容与旧代码的兼容方式详见[从 `econ-viz` 迁移](../getting-started/installation.md#sec-migrate)。本手册说明预览版 2.0.0b8。

`utility-viz` 属于 EconViz 系列软件包：绘图通过与领域无关的场景与渲染库 `mosaickit`，曲线则以 `bezierkit` 描绘。经济学原理图形由同系列的 `principle-viz` 负责。

每张图的图说都链接到画出它的脚本；全部脚本按主题分文件夹，可一次下载：[utility-viz-examples-zh-CN.zip](https://econ-viz.org/assets/utility-viz/agora/utility-viz-examples-zh-CN.zip)。

## 功能范围

`utility-viz` 的功能分为效用模型、均衡求解、效用水平、图层与导出格式五个部分。模型与求解结果可分开使用；同一模型也可交由画布、多面板图、需求图或分析 API 处理。

## 阅读指引

本手册按主题分成四个部分（参见[章节主题](introduction.md#tab-guide)）：

<span id="tab-guide"></span>

| 主题 | 子主题 | 说明 |
| --- | --- | --- |
| 绘图与导出 | [画布与图层](canvas.md#sec-canvas) | 坐标轴、曲线与均衡点 |
|  | [多面板图与需求图](consumer.md#sec-figures) | 并排比较与需求曲线 |
|  | [主题与配置文件](themes.md#sec-themes) | 配色、样式与配置文件 |
|  | [输出格式](export.md#sec-export) | 导出图像与 TikZ |
| 模型与分析 | [内置模型](../models/index.md#sec-models) | 常见效用函数 |
|  | [自定义与多商品模型](../models/advanced.md#sec-advanced) | 自定义函数与多商品、场景 |
|  | [比较静态与 Slutsky 矩阵](../tools/analysis.md#sec-analysis) | 需求导数与齐次性 |
| 动画与交互 | [GIF 动画](animation.md#sec-animation) | 参数变动的 GIF |
|  | [Jupyter 交互组件](interactive.md#sec-widgets) | 笔记本滑块调参数 |
| 其他输入方式 | [命令行工具](../getting-started/cli.md#sec-cli) | 使用命令行出图 |
|  | [LaTeX 效用函数解析](../tools/latex.md#sec-latex) | 从算式创建模型 |

初次使用时，依次阅读[快速开始](../getting-started/quickstart.md#sec-quickstart)与[Canvas 画布](canvas.md#sec-canvas)。查询特定 API 时，可直接前往对应章节或命令索引。从 `econ-viz` 1.x 升级时，请先阅读[从 `econ-viz` 迁移](../getting-started/installation.md#sec-migrate)。
