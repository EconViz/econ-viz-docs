---
seo_title: "简介"
---

# 简介

<span id="sec-intro"></span>

`micro-viz` 是个体经济学厂商端的 Python 软件包：生产、成本、完全竞争、独占与定价、寡占、要素市场、不确定性与信息。每个主题都有一个*模型*，以数字回答问题，也有一张依教科书惯例由模型画出的*图形*。

图形可输出为 PNG、SVG 或 PDF。统计数据图与方块加箭头的流程图不在软件包范围内。

`micro-viz` 属于 EconViz 软件包家族，以 `mosaickit` 绘图；`mosaickit` 是与领域无关的场景与绘图函数库。消费者理论与一般均衡属于 `utility-viz`，入门的供需图属于 `principle-viz`，赛局理论不在本软件包范围内。

## 范围

本软件包涵盖六组主题，各有一章（参见 [章节指引](introduction.md#tab-guide)）。模型不引入任何绘图器，因此结果可以不画图直接使用；绘图函数只负责安置模型算出的内容。

## 阅读指引

<span id="tab-guide"></span>

| 主题 | 说明 |
| --- | --- |
| [模型与图形](model-figure.md#sec-model-figure) | 模型、绘图函数、图层 ID 与多栏图如何配合 |
| [生产与成本](production-costs.md#sec-production-costs) | 短期生产、成本函数、阶梯与折点成本 |
| [竞争](competition.md#sec-competition) | 价格接受者厂商、产业供给、长期成本、进入 |
| [独占与定价](monopoly.md#sec-monopoly) | 独占、独占性竞争、管制、价格歧视、两部定价、搭售、广告、可耗竭资源 |
| [寡占](oligopoly.md#sec-oligopoly) | 双占、拗折需求、支配厂商、垂直关系 |
| [投入与技术](inputs.md#sec-inputs) | 等产量线、成本最小化、学习与范畴、要素市场、买方独占与工会 |
| [不确定性与信息](uncertainty.md#sec-uncertainty) | 期望效用、风险、拍卖、逆选择、信号、道德风险 |
| [设置](settings.md#sec-settings) | `econ-viz.toml` 的 `[micro]` 表 |
| [标签与位置](labels.md#sec-labels) | 语言表、取代文本、移动标签 |
| [添加图形](adding-figure.md#sec-adding) | 模型、绘图函数、文本、导出、测试 |
| [动画](animation.md#sec-animation) | 让图形随参数变化 |

初次使用时，依序阅读 [快速开始](../quickstart.md#sec-quickstart) 与 [模型与图形](model-figure.md#sec-model-figure)。

所有图形的绘制脚本依主题整理成一个压缩包：[micro-viz-examples.zip](https://econ-viz.org/assets/micro-viz/micro-viz-examples.zip)。
