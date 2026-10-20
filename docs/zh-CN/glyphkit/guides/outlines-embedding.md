---
seo_title: "字形轮廓、字体子集与可移植数据"
---

# 字形轮廓、字体子集与可移植数据

<span id="sec-outlines-embedding"></span>

## 字形几何

<!-- api: agora.glyphkit.guides_outlines_embedding_1 -->

精确的字形轮廓，包含按顺序排列的路径命令、范围与每 em 单位数。

<!-- api: agora.glyphkit.guides_outlines_embedding_2 -->

把当前位置移动到指定的字体坐标，开始一条新轮廓。

<!-- api: agora.glyphkit.guides_outlines_embedding_3 -->

从当前位置绘制一条直线到指定端点。

<!-- api: agora.glyphkit.guides_outlines_embedding_4 -->

加入一段具有一个控制点与一个端点的二次 Bézier 曲线。

<!-- api: agora.glyphkit.guides_outlines_embedding_5 -->

加入一段具有两个控制点与一个端点的三次 Bézier 曲线。

<!-- api: agora.glyphkit.guides_outlines_embedding_6 -->

把当前轮廓连接回起点并闭合。

<!-- api: agora.glyphkit.guides_outlines_embedding_7 -->

按照调用方指定的允许误差，用线段近似轮廓中的曲线命令。

<!-- api: agora.glyphkit.guides_outlines_embedding_8 -->

曲线细分后得到的一条开放或闭合折线。

```python
glyph = layout.lines[0].runs[0].glyphs[0]
outline = library.outline(glyph)
```

## 检查权限的字体子集

<!-- api: agora.glyphkit.guides_outlines_embedding_9 -->

声明字体子集的嵌入用途，让 GlyphKit 能够根据该用途检查字体权限。

<!-- api: agora.glyphkit.guides_outlines_embedding_10 -->

选择返回的字体容器，例如 OpenType 或 WOFF2。

<!-- api: agora.glyphkit.guides_outlines_embedding_11 -->

完整的字体子集结果，包括可移植字体、来源映射、警告与元数据。

<!-- api: agora.glyphkit.guides_outlines_embedding_12 -->

一份已经检查权限的字体数据，包含字体族、格式、字节、覆盖字形与嵌入信息。

```python
from glyphkit.embedding import EmbeddingUse, FontContainer

bundle = library.subset(
    layout,
    embedding_use=EmbeddingUse.WEB,
    container=FontContainer.WOFF2,
)
```

禁止嵌入的字体会直接被拒绝。权限不明确时也会拒绝，除非调用方明确覆盖并自行记录这项决定。GlyphKit 只返回字节与元数据；是否写入文件、写到哪里，都由使用方决定。

## 序列化

<!-- api: agora.glyphkit.guides_outlines_embedding_13 -->

把支持的公开不可变对象转换成带有版本、适合 JSON 类存储方式的一般数据。

<!-- api: agora.glyphkit.guides_outlines_embedding_14 -->

验证带版本的数据，并在设置的限制内还原成对应的公开对象。

<span id="fig-glyph-outline"></span>

<figure class="ev-fig" markdown>

![完成字形处理后的精确 Bézier 轮廓与部分控制多边形](../../../assets/glyphkit/agora/outlines/glyph-g.svg){ .ev-figure-sm }

<figcaption markdown>完成字形处理后的精确 Bézier 轮廓与部分控制多边形</figcaption>

</figure>
