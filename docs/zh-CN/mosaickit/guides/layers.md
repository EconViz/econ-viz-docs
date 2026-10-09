---
seo_title: "图层与坐标轴"
---

# 图层与坐标轴

<span id="sec-layers"></span>

## 共同字段

<!-- api: agora.mosaickit.guides_layers_1 -->

所有图层共用的不可变基类。各种图层在自身的位置参数之后，都接受以下仅限关键字使用的字段。

坐标可以是有限实数对（数据单位），也可以是参数表达式（详见[参数、网格与动画](parameters.md#sec-parameters)）。无效的几何会在创建图层时引发 `ConfigurationError`，而不是等到绘制时才报错。

## 基本图层

<span id="tab-layers"></span>

| 图层 | 默认角色 | 绘制内容 |
| --- | --- | --- |
| `PathLayer(path, stroke)` | `primary` | 通过至少两点的折线 |
| `FillLayer(boundary, fill, stroke)` | `region` | 至少三点的多边形，含填色与外框 |
| `MarkerLayer(points, marker)` | `point` | 每个点上的标记，至少一点 |
| `TextLayer(position, text)` | `text` | 某点上的文字 |
| `ArrowLayer(start, end, stroke)` | `annotation` | 直线箭头，可加标签 |
| `LegendLayer(entries, style)` | `legend` | 有标签图层的图例 |
| `GroupLayer(children)` | `primary` | 本身不画任何东西，只将图层分组 |

<!-- api: agora.mosaickit.guides_layers_2 -->

以直线段连接各点。如果解析后的线条样式设有 `arrow`，便会在 `START`、`END` 或 `BOTH` 端画出与该端线段对齐的箭头。`clip=False` 可让线条以完整宽度越过绘图区边缘，坐标轴默认便采用此设置。

<!-- api: agora.mosaickit.guides_layers_3 -->

以 `fill` 填色、以 `stroke` 描边的闭合多边形。`RegionLabelLayer` 以它的 id 引用它。

<!-- api: agora.mosaickit.guides_layers_4 -->

在每个点绘制一个标记。标记一律完整画出：中心位于绘图区边缘的标记（例如坐标轴上的点）不会被切半，中心落在绘图区外的则会略过。

<!-- api: agora.mosaickit.guides_layers_5 -->

在 `position` 放置文字，并偏移 `offset` pt。`anchor` 指定文字框的哪一点要对准该位置：`center`、`left`、`right`、`top`、`bottom`、`top-left`、`top-right`、`bottom-left` 或 `bottom-right`。`math=True` 时，文字会以数学式排版（`"a_1"` 成为 $a_1$）。

<!-- api: agora.mosaickit.guides_layers_6 -->

从 `start` 指向 `end` 的直线箭头。除非线条样式指定其他 `ArrowStyle`，否则使用开放式箭头；`label` 写在中点。虚线、点线或点划线只应用在箭身，箭头维持实线。箭头不受绘图区裁切。

<!-- api: agora.mosaickit.guides_layers_7 -->

列出 `entries` 中各 id 所指定的图层；`entries` 为空时，则列出所有带有 `legend` 标签的图层。如果 id 不存在或对应图层没有标签，便会引发 `RenderError`。`LegendStyle(visible=False)` 可隐藏图例。

<!-- api: agora.mosaickit.guides_layers_8 -->

由其他图层组成的图层。子图层的绘制方式如同直接加入场景，但其 `z_index` 会再加上群组的值；隐藏群组也会隐藏其中所有子图层。

## 坐标轴

<!-- api: agora.mosaickit.guides_layers_9 -->

`build_axes` 将两个坐标轴规格转换为角色为 `axes` 的一般图层。两个规格都没有 `arrow` 时，结果是围住范围的闭合框；否则，各轴会沿 $y = 0$ 或 $x = 0$ 画成直线，并按指定的 `ArrowPlacement` 画出实心三角箭头。标题位于箭头尖端之外 6 pt：x 轴标题在右侧，y 轴标题在上方。

<!-- api: agora.mosaickit.guides_layers_10 -->

三种默认依次为：从原点出发、远端带箭头的两轴；穿过原点、两端带箭头的两轴；以及不带箭头的外框。

每条坐标轴都由 `PathLayer` 与 `TextLayer` 组成，因此可通过 `axes` 角色改变样式、以 id（`axes.x`、`axes.y`、`axes.frame`、`axes.x.label`、`axes.y.label`）移除，或改用自行创建的图层。
