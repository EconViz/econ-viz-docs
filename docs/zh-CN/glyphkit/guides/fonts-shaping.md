---
seo_title: "字体与字形处理"
---

# 字体与字形处理

<span id="sec-fonts-shaping"></span>

## 配对与后备字体

<!-- api: glyphkit.guides_fonts_shaping_1 -->

描述字体配对时偏好的字族、字重、字宽、斜体与可变字体座标。

<!-- api: glyphkit.guides_fonts_shaping_2 -->

记录一次查找的结果，包括选到的字体面与最后采用的可变字体座标。

<!-- api: glyphkit.guides_fonts_shaping_3 -->

一个可用字体面的快照，包含稳定识别、名称、度量、字符涵盖范围与字体表。

```python
from glyphkit import FontLibrary, FontSource, Paragraph, TextSpan, TextStyle

library = FontLibrary.from_sources(
    (
        FontSource.path("fonts/SourceSans3-Regular.ttf"),
        FontSource.path("fonts/NotoSansTC-Regular.otf"),
    ),
    generic_families={"sans-serif": ("Source Sans 3", "Noto Sans TC")},
)
layout = library.layout(
    Paragraph((TextSpan("效用 U(x)", TextStyle(("sans-serif",), 18)),))
)
```

示例使用 Google Fonts 提供的开源字体 Source Sans 3 与 Noto Sans TC；数学式章节则使用采开放授权的 STIX Two Math。

字体识别来自字体内容的 SHA-256 摘要与字体集合索引，不看文件名。`FontManifest` 记录重现排版所需的来源与字体。字形选取、定位与可变字体数据采用 OpenType 规格定义的结构 [{Microsoft} (2025)](../project/references.md#opentype2025)。

## Unicode 字形处理

<!-- api: glyphkit.guides_fonts_shaping_4 -->

字形处理时采用的书写系统、方向、语言、OpenType 功能与间距选项。

<!-- api: glyphkit.guides_fonts_shaping_5 -->

共用同一字体面与处理条件的一段视觉顺序字形，并保留原文范围。

<!-- api: glyphkit.guides_fonts_shaping_6 -->

一个字形编号及其字符集群、字幅、位移与字体面识别。

<!-- api: glyphkit.guides_fonts_shaping_7 -->

依明确的后备规则处理 Unicode 文本，返回不绑定绘图端的字形编号与位置。

左右方向混排时，即使视觉顺序经过重排，原文范围仍维持逻辑顺序；这里采用 Unicode 双向算法对逻辑顺序与视觉顺序的区分 [{Unicode Consortium} (2026)](../project/references.md#unicode-bidi2026)。找不到字形时会抛出 `MissingGlyphError`；GlyphKit 不会偷偷换成未设置的系统字体。

## 系统字体

<!-- api: glyphkit.guides_fonts_shaping_8 -->

主动搜索操作系统已安装的字体。需要可重现的建置时，请优先传入明确的文件或字节，并保存字体清单。
