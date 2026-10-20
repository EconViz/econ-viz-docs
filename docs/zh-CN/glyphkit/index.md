---
seo_title: "GlyphKit：与绘图端无关的 Python 字体排版工具"
description: "GlyphKit 负责明确的字体选择、Unicode 塑形、段落与数学式排版、字形轮廓，以及检查嵌入权限的字体子集，本身不绑定绘图端。"
---

<h1 class="ev-visually-hidden">GlyphKit：与绘图端无关的 Python 字体排版工具</h1>

<p align="center">
  <img src="../../assets/glyphkit/banner.svg" alt="glyphkit" style="max-width: 480px; width: 100%; margin: 2rem 0 1rem;">
</p>

GlyphKit 把调用方提供的字体与文本转换成不可变的排版数据。它负责字体匹配、Unicode 塑形、段落与数学公式排版、精确字形轮廓，以及检查嵌入权限的字体子集；本身不绘图，也不写入文件。

```bash
uv add --prerelease allow glyphkit
```

```python
from glyphkit import (
    FontLibrary,
    FontSource,
    Paragraph,
    TextSpan,
    TextStyle,
)

library = FontLibrary.from_sources(
    (FontSource.path("fonts/SourceSans3-Regular.ttf"),)
)
family = library.faces[0].family
layout = library.layout(
    Paragraph(
        (TextSpan("效用 U(x₁, x₂)", TextStyle((family,), 18)),)
    )
)
```

## GlyphKit 负责什么

<div class="grid cards" markdown>

-   :material-format-font: **字体与塑形**

    明确的字体来源、可重现的匹配、已配置的备用字体、Unicode 书写系统、双向文本与 OpenType 塑形。

    [:octicons-arrow-right-24: 字体与塑形](guides/fonts-shaping.md)

-   :material-format-text: **文字与数学式排版**

    段落换行、逻辑与墨迹边界，以及按明确的类 LaTeX 语法建立的 OpenType MATH 排版。

    [:octicons-arrow-right-24: 文字与数学式排版](guides/layout-math.md)

-   :material-vector-curve: **可移植的几何与字体**

    精确字形路径、可控的折线近似、带版本的通用数据，以及检查嵌入权限的字体子集。

    [:octicons-arrow-right-24: 字形轮廓与嵌入](guides/outlines-embedding.md)

</div>

GlyphKit 不依赖渲染器或动画包。KineticKit 通过单一适配器使用它的公开数据；GlyphKit 不会反向导入 KineticKit。

<!-- agora-navigation -->

## 文件导览

- [简介](guides/introduction.md)
- [安装](installation.md)
- [快速开始](quickstart.md)
- [字体与文字塑形](guides/fonts-shaping.md)
- [文字与数学式排版](guides/layout-math.md)
- [字形轮廓、字体子集与可移植数据](guides/outlines-embedding.md)
- [坐标、度量与边界](guides/coordinate-metrics.md)
- [Bézier 字形轮廓](guides/bezier-geometry.md)
- [OpenType 数学排版模型](guides/math-layout-model.md)
- [行构造与间距算法](guides/line-layout-algorithms.md)
- [可重现性与绘图端契约](guides/reproducibility.md)
- [更新记录](project/changelog.md)

<!-- /agora-navigation -->
