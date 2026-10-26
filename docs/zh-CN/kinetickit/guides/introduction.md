---
seo_title: "简介"
---

# 简介

<span id="sec-intro"></span>

`kinetickit` 是不绑定特定用途的动画引擎。它负责场景、动作、可重现的帧调度、绘图端能力、交互、无障碍中继数据与文件导出。经济学软件包和其他应用程序只要把自己的对象转成一般 KineticKit 节点即可。

同一个不可变场景和一段动作，可以输出成动态 SVG、串流 GIF 与单档交互 HTML。同一场景在同一时间一定得到相同快照，系统时间与绘图端的选择都不会进入模型。

KineticKit 不会导入 `mosaickit`、`utility-viz` 或其他特定用途的软件包。字体处理由 `glyphkit` 负责，并通过一个适配器接入场景，详见[文本排版](typography.md#sec-typography)。

## 分层

| 层 | 可以知道 | 不可以知道 |
| --- | --- | --- |
| 动作内核（`easing`、`interpolation`、`timeline`、`tween`、`keyframes`） | 时间、数值、协定 | 场景、绘图端 |
| 场景模型（`geometry`、`scene`、`styles`、`morph`、`transitions`） | 几何、样式、对象编号 | 后端对象 |
| 绘图端（`renderers.vector`、`.raster`、`.interactive`） | 场景快照、能力 | 使用端的领域模型 |
| 导出器（`exporters`） | 帧、成品、输出目标 | 可视化逻辑 |

这些界线由 import-linter 规则与读取语法树的测试把关。Matplotlib、Plotly 与 Pillow 只出现在私有的 `_*` 模块里。

## 简短导览

1. [快速开始](../quickstart.md)移动一个点，并写成三种格式。
2. [场景与动作](scenes-motion.md)列出各种节点，并说明动作如何组合。
3. [输出格式](outputs.md)说明能力、替代方案，以及各格式保留什么。
4. [示例](examples.md)运行一张图表、一个适配器与一个 3D 曲面。
