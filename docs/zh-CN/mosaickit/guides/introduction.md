---
seo_title: "简介"
---

# 简介

<span id="sec-intro"></span>

`mosaickit` 软件包以小型且不可变的组件组装二维图形：场景是一份有序的图层列表（路径、填色区域、标记、文字、箭头、标签、大括号）；每个图层标明一个语义角色，主题将角色转换为样式，渲染器再将结果输出为 PNG、SVG、PDF、GIF 或 MP4。它不包含任何特定领域的知识。`principle-viz`、`utility-viz` 等领域软件包自行定义模型与角色名称，再将要绘制的图层交给 `mosaickit`；曲线构造与 TikZ 导出则由 `bezierkit` 等几何软件包负责。

## 设计

软件包设计遵循四项原则。

/ 不可变的值: 图层、场景、样式、主题与规格都是冻结的 dataclass。`Canvas` 是封装不可变 `Scene` 的流式构建器；`snapshot()`、`copy()` 与 `bind()` 不会改动其他对象持有的场景。
/ 稀疏样式: 每个样式字段都可以是 `None`，表示继承。图层自带的样式位于画布覆盖、配置覆盖、主题与基本默认值之上（详见[主题与配置](themes.md#sec-themes)）。
/ 角色而非颜色: 图层只说明自己是什么（`"primary"`、`"axes.note"`、`"mypkg.boundary"`），外观由主题决定，而颜色是画布绘制时才解析的调色板名称（详见[样式与颜色](styles.md#sec-styles)）。
/ 避让所有内容的布局: 区域标签、点标签、大括号与坐标轴注释会等其他内容绘制完毕后再放置。布局仅依据显示像素进行几何计算，使文字不碰到任何线、标记、区域或其他文字（详见[布局几何](geometry.md#sec-geometry)、[区域标签与点标签](labels.md#sec-labels)）。

## 数学与证明

自动布局以多种计算几何方法为基础。方向测试用于判断点位于有向直线的哪一侧，奇偶规则则依据射线穿越边界的次数判断内外；此外还会计算到多边形边界的距离，并以每次优先检查上界最高候选区域的最佳优先搜索找出区域最深处。坐标轴文字则会排列到互不重叠且位移平方和最小的位置。各章以编号的定义、引理、命题与定理说明每个程序的保证，证明集中在[证明](../project/proofs.md#app-proofs)；如果只想查阅 API，可以略过。样式与主题的代数（稀疏合并、角色解析）以及参数绑定也采用相同的处理方式。几何部分的标准参考书为 [{de Berg} (2008)](../project/references.md#deberg2008)，[分散为最佳解](annotations.md#thm-spread)背后的保序最小二乘问题则参见 [Barlow (1972)](../project/references.md#barlow1972)。

## 阅读指引

<span id="tab-guide"></span>

| 主题 | 内容 | 章节 |
| --- | --- | --- |
| 画布、规格、场景 | [画布与场景](canvas.md#sec-canvas) | 路径、填色、标记、文字、坐标轴 |
| [图层与坐标轴](layers.md#sec-layers) | 坐标轴标记、注释与大括号 | [坐标轴注释](annotations.md#sec-annotations) |
| 布局几何 | [布局几何](geometry.md#sec-geometry) | 区域标签与点标签 |
| [区域标签与点标签](labels.md#sec-labels) | 样式、颜色、调色板 | [样式与颜色](styles.md#sec-styles) |
| 主题、角色、配置 | [主题与配置](themes.md#sec-themes) | 参数、网格、动画 |
| [参数、网格与动画](parameters.md#sec-parameters) | 渲染器、缓存、保存 | [绘制](rendering.md#sec-rendering) |

初次使用请先读[快速入门](../quickstart.md#sec-quickstart)、[画布与场景](canvas.md#sec-canvas)与[图层与坐标轴](layers.md#sec-layers)。本手册的图都是 `mosaickit` 自己的输出：每张图由它所示范的画布或网格绘制，并以印在此处的尺寸存成 PDF。
