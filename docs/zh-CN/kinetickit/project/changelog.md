---
seo_title: "变更纪录"
---

# 变更纪录

<span id="sec-changelog"></span>

本文档涵盖的 `kinetickit` 版本。

## 1.0.0b2（2026-10-19）

- GlyphKit（`>=1.0.0b2,<2`）随 KineticKit 一起安装，并负责所有字体处理。`kinetickit.integrations.glyphkit` 适配器仍是唯一的导入界线，内核导入维持延迟加载，中性的文本契约也没有改变（参见[文本排版](../guides/typography.md#sec-typography)）。
- 添加 `export_png_frames(...)`，把已编码的 PNG 帧串流写成 GIF，并精确分配百分之一秒的误差（参见[输出格式](../guides/outputs.md#sec-outputs)）。

## 1.0.0b1（2026-10-13）

- 第一个 1.0 测试版。[兼容性](../compatibility.md)中的动作、场景、绘图端、导出器与成品契约都打算保持稳定，但在预发行版本之间仍可能改变。
- 可重现的时间轴、标准与三次 Bézier 缓动、关键帧与流畅的动作树（参见[时间与缓动](../guides/time-easing.md#sec-kinetic-time)）。
- 2D 与 3D 场景、路径、网格与曲面变形，以及依稳定编号配对的场景转场（参见[场景与动作](../guides/scenes-motion.md#sec-scenes-motion)）。
- 动态 SVG、串流 GIF 与交互 HTML 输出，写档前先做能力检查（参见[输出格式](../guides/outputs.md#sec-outputs)）。
- 交互、无障碍中继数据与一致性测试软件包（参见[无障碍与交互](../guides/accessibility.md#sec-accessibility)）。

测试版已知的限制列在[输出格式](../guides/outputs.md#sec-outputs)。
