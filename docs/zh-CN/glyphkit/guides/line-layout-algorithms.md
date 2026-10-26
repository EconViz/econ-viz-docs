---
seo_title: "行构造与间距算法"
---

# 行构造与间距算法

<span id="sec-glyph-lines"></span>

## 字符集群与换行位置

段落先取得 Unicode 提供的换行位置，但绝不拆开已完成字形处理的字符集群（cluster）。同一字符集群的字形会组成不可分割的排版单位。若各单位的字幅为 $a_i$、缩进为 $h$，候选行宽是 $W = h + \sum_i a_i$；加入下一个单位会超过 `max_width` 时，便回到最近的合法换行位置。

## 定位点与缩进

位置 $x$ 的 Tab 字符会前进到第一个大于 $x$ 的指定定位点。没有可用定位点时，以缺省间距 $T$ 计算 $\Delta x = T - (x \mod T)$。首行与后续行分别使用 `first_line_indent` 与 `hanging_indent`。

## 对齐与左右齐行

可用宽度 $M$、行宽 $W$ 时，起始、置中、末端的位移为 $0,(M-W)/2,M-W$。非末行的左右对齐把剩余宽度平均分给 $N_{\text{space}}$ 个可调空白：

$$
\delta=(M-W)/N_{\text{space}}.
$$

增加的是字幅，不会改动字形轮廓。

<!-- api: glyphkit.guides_line_layout_algorithms_1 -->

保存带样式的文本片段，以及算法使用的宽高、缩进、对齐、定位点与行距限制。

<!-- api: glyphkit.guides_line_layout_algorithms_2 -->

记录一行的字形列、字幅、逻辑与墨迹范围、基线、原文范围及结束方式。

<!-- api: glyphkit.guides_line_layout_algorithms_3 -->

汇整整个段落的范围、基线、行数、阅读顺序与水平／垂直溢出。

## 垂直排版与溢出

有明确行高 $H$ 时，相邻基线相差 $H$；否则 GlyphKit 依该行最大的文本样式推导行高。`max_height` 限制可接受的行数，未容纳的高度记入 `vertical_overflow`，不会改写既有字形数据。
