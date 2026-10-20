---
seo_title: "简介"
---

# 简介

<span id="sec-intro"></span>

`kinetickit` 是不绑定特定用途的动画引擎。它负责场景、动作、可重现的帧调度、渲染器能力、交互、无障碍元数据与文件导出。经济学软件包和其他应用程序只需把自己的对象转换成普通的 KineticKit 节点。

同一个不可变场景和一段动作，可以输出为动态 SVG、流式 GIF 与单文件交互式 HTML。同一场景在同一时刻一定得到相同快照，不受系统时间或特定渲染器影响。

KineticKit 不会导入 `mosaickit`、`utility-viz` 或其他特定用途的软件包。字体处理由 `glyphkit` 负责，并通过[字体与无障碍信息](typography-accessibility.md#sec-typography-accessibility)介绍的单一适配器接入。
