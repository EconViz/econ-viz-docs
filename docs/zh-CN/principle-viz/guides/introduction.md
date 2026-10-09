---
seo_title: "简介"
---

# 简介

<span id="sec-intro"></span>

  "0.10.0",
)[由 `principle-econ` 更名为 `principle-viz`，加入 EconViz 系列；Python 软件包名称改为 `principle_viz`]

`principle-viz` 是经济学原理的绘图软件包，涵盖供给与需求、均衡及其移动、税收与补贴、价格管制、福利、国际贸易、市场失灵、要素市场与生产可能性曲线。每个主题都有计算与图形两个部分：计算返回数值，图形依教科书惯例绘制。

图形的曲线名称标在末端而不放进图例，面积名称写在区块内，数值标在坐标轴上，所有文字都不遮住线、点或其他文字。输出格式包括 PNG、SVG 与 PDF；命令行工具则以 JSON 输出计算结果。

`principle-viz` 属于 EconViz 系列软件包，绘图使用与领域无关的场景与绘制函数库 `mosaickit`。同系列的 `utility-viz` 是个体经济学绘图软件包，涵盖效用模型、最优消费组合求解，以及无异曲线、预算线、消费者均衡、需求曲线与 Edgeworth 箱形图；本软件包不包含这些功能。

## 功能范围

`principle-viz` 处理线性市场，功能分为市场、政策、应用与工具四个部分。计算与图形可分开使用；同一个结果可以打印、输出为 JSON，也可以交给 `MarketFigure` 绘制。

## 阅读指引

本手册依主题分成市场、政策、应用与工具四个部分（参见[章节主题](introduction.md#tab-guide)）：

<span id="tab-guide"></span>

| 主题 | 子主题 | 说明 | 章节 |
| --- | --- | --- | --- |
| 线性市场 | 直线、均衡与曲线移动 | [线性市场](markets.md#sec-markets) | 离散市场 |
| 逐单位的需求与供给表 | [离散市场](discrete.md#sec-discrete) | 市场曲线加总 | 个人曲线的水平加总 |
| [由个人加总市场曲线](aggregation.md#sec-aggregation) | 弹性与总收益 | 点弹性、弧弹性与总收益曲线 | [弹性与总收益](elasticity.md#sec-elasticity) |
| 福利 | 消费者剩余、生产者剩余与无谓损失 | [福利](welfare.md#sec-welfare) | 税收与补贴 |
| 税负楔子与补贴成本 | [税收与补贴](taxes.md#sec-taxes) | 价格管制 | 价格上限、价格下限与短缺 |
| [价格管制](controls.md#sec-controls) | 国际贸易 | 自由贸易、关税与进口配额 | [国际贸易](trade.md#sec-trade) |
| 市场失灵 | 外部性、公共资源与公共物品 | [市场失灵](failures.md#sec-failures) | 劳动与可贷资金 |
| 最低工资与政府借款 | [劳动与可贷资金](factor-markets.md#sec-factor) | 生产可能性曲线 | 机会成本、成长与比较优势 |
| [生产可能性曲线](ppf.md#sec-ppf) | 图形 | 标签、图层与配色 | [图形](figures.md#sec-figures) |
| 命令行接口 | 以 JSON 输出计算结果 | [命令行界面](../cli.md#sec-cli) |

初次使用时，依序阅读[快速开始](../quickstart.md#sec-quickstart)、[线性市场](markets.md#sec-markets)与[图形](figures.md#sec-figures)。之后每章说明一个主题，先介绍计算，再介绍图形。查找特定命令的选项时，可直接前往[命令行界面](../cli.md#sec-cli)。
