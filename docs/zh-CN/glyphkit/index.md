---
seo_title: "与绘图端无关的 Python 排版引擎"
description: "GlyphKit 使用明确指定的字体、处理 Unicode、排出段落与数学式、取出精确字形轮廓，并创建会检查权限的字体子集，而且不自己绘图。"
---

<h1 class="ev-visually-hidden">glyphkit：与绘图端无关的 Python 排版引擎</h1>

<p align="center"><em>返回不可变排版数据、自己不绘图的 Python 排版引擎。</em></p>

<p align="center">
  <a href="https://github.com/EconViz/glyphkit"><img alt="GitHub" src="https://img.shields.io/badge/github-EconViz%2Fglyphkit-181818?style=flat-square&labelColor=f3f3f3"></a>
  <a href="https://pypi.org/project/glyphkit/"><img alt="PyPI" src="https://img.shields.io/pypi/v/glyphkit?include_prereleases&style=flat-square&label=pypi+package&color=181818&labelColor=f3f3f3&cacheSeconds=300"></a>
  <a href="https://pypi.org/project/glyphkit/"><img alt="Python" src="https://img.shields.io/pypi/pyversions/glyphkit?style=flat-square&color=181818&labelColor=f3f3f3"></a>
</p>

!!! warning "glyphkit 1.0 为测试版"

    glyphkit 1.0.0b4 是预发行版本。预发行版本之间的每项变更都记录在[变更纪录](project/changelog.md)。

```python
from glyphkit import FontLibrary, FontSource, Paragraph, TextSpan, TextStyle

library = FontLibrary.from_sources(
    (
        FontSource.path("fonts/SourceSans3-Regular.ttf"),
        FontSource.path("fonts/NotoSansTC-Regular.otf"),
    ),
    generic_families={"sans-serif": ("Source Sans 3", "Noto Sans TC")},
)

paragraph = Paragraph(
    (TextSpan("效用 U(x₁, x₂)", TextStyle(("sans-serif",), 18)),),
    max_width=360,
)
layout = library.layout(paragraph)
print(layout.logical_bounds)
```

## 功能

<div class="grid cards" markdown>

-   :material-format-font: **字体与字形处理**

    明确的字体来源、确定的配对、设置好的后备字体、Unicode 文本系统、双向文本与 OpenType 字形处理。

    [:octicons-arrow-right-24: 字体与字形处理](guides/fonts-shaping.md)

-   :material-format-text: **段落排版**

    换行的段落，附逻辑范围与墨迹范围、基线、对齐与缩进，使用排版单位而非像素。

    [:octicons-arrow-right-24: 文本排版与数学式](guides/layout-math.md)

-   :material-sigma: **结构化数学式**

    明确定义的类 LaTeX 语法，依 TeX 的规则与字体 OpenType MATH 表的常数排版。

    [:octicons-arrow-right-24: 数学语法](guides/math-grammar.md)

-   :material-vector-curve: **精确的字形轮廓**

    以字体单位表示的移动、直线、二次、三次与封闭命令，并可依你选的容许误差自适应展平。

    [:octicons-arrow-right-24: 轮廓与嵌入](guides/outlines-embedding.md)

-   :material-shield-lock-outline: **会检查权限的字体子集**

    遵守字体嵌入权限的 SFNT 或 WOFF2 子集字节，以及有版本的纯数据串行化。

    [:octicons-arrow-right-24: 字体安全](guides/reproducibility.md)

-   :material-axis-arrow: **座标与度量**

    字体单位、缩放、字幅与墨迹的差别，以及对齐、裁切或做碰撞检查时该用哪个方框。

    [:octicons-arrow-right-24: 座标与度量](guides/coordinate-metrics.md)

</div>

## 安装

```bash
uv add --prerelease allow glyphkit
```

需要 Python 3.10 到 3.13。WOFF2 额外安装项见[安装](installation.md)。

## 示例

本文档的每张图都附上生成它的脚本。可一次下载全部。

[下载全部示例](../assets/glyphkit/glyphkit-examples.zip){ .md-button download="" }
