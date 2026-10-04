---
seo_title: "principle-viz：用 Python 绘制经济学原理的市场图形"
description: "principle-viz 是用于经济学原理市场分析与绘图的 Python 包：均衡、税收、价格管制、福利分析等，以线性需求与供给为基础。"
---

# principle-viz

`principle-viz` 是用于经济学原理市场分析与绘图的 Python 包，聚焦于**线性需求与供给**模型，
并把求解、政策、福利分解与绘图拆成各自独立的模块。

![用 principle-viz 绘制的基本市场均衡图](../../assets/principle-viz/basic_equilibrium.png){ width="360" }

| | |
|---|---|
| 本文档对应版本 | 0.10.0 |
| Python | 3.10 以上 |
| 依赖 | [mosaickit](../mosaickit/index.md)（`>=0.5.1,<0.6.0`） |
| 命令行 | `principle-viz` |
| 源代码 | [github.com/EconViz/principle-viz](https://github.com/EconViz/principle-viz) |
| 许可证 | MIT |

## 功能范围

- 由线性需求与供给，或离散的单位表求解市场均衡
- 比较静态分析：需求或供给移动，以及从旧均衡到新均衡的变化
- 税收（定额、从量、从价；征在买方或卖方）与补贴
- 价格上限、价格下限与最低工资
- 福利分解：消费者剩余、生产者剩余、税收与无谓损失
- 国际贸易（自由贸易、关税、配额）、外部性、共有资源、公共品、可贷资金、生产可能曲线与弹性
- 把个别曲线或个别需求表水平加总成市场需求与供给
- 以 [mosaickit](../mosaickit/index.md) 为基础的教科书风格图形
- 支持 JSON 输出的命令行工具

## 接下来

<div class="grid cards" markdown>

-   :material-download: **安装**

    用 pip 或 uv 安装包。

    [:octicons-arrow-right-24: 安装](installation.md)

-   :material-rocket-launch-outline: **快速开始**

    求解市场、比较税收效果，并画出图形。

    [:octicons-arrow-right-24: 快速开始](quickstart.md)

</div>
