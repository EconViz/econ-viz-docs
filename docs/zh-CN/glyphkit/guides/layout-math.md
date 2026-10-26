---
seo_title: "文本排版与数学式"
---

# 文本排版与数学式

<span id="sec-layout-math"></span>

## 段落与测量

<!-- api: glyphkit.guides_layout_math_1 -->

处理每个片段的字形，在合法的 Unicode 断行位置换行，并返回不可变的 `TextLayout`。`library.layout(paragraph)` 会把字体库当成第一个参数来调用它。

<!-- api: glyphkit.guides_layout_math_2 -->

汇整排版结果的逻辑范围与墨迹范围、基线、行数与溢出，不绘制任何东西。`layout.measure()` 会返回这样一份。

<!-- api: glyphkit.guides_layout_math_3 -->

排好的一行，包含字形组、基线、字幅、范围、原文范围，以及这一行是否在明确的换行处结束。

`TextStyle` 带着字族、字级、字重、斜体、语言、方向、间距与 OpenType 功能。一个段落可以混用多种样式与文本系统。设置 `max_width` 会在 Unicode 断行位置换行 [{Unicode Consortium} (2026)](../project/references.md#unicode-linebreak2026)；不设置则排成不受限制的一行。一行如何组成，见[行的组成与间距](line-layout-algorithms.md#sec-glyph-lines)。

## 结构化数学式

```python
from glyphkit import FontLibrary, FontSource
from glyphkit.math import MathStyle, parse_math

library = FontLibrary.from_sources((FontSource.path("fonts/STIXTwoMath-Regular.otf"),))
formula = parse_math(r"U(x_1, x_2) = x_1^\alpha x_2^{1-\alpha}")
box = library.layout_math(formula, style=MathStyle(18, ("STIX Two Math",)))
print(box.bounds)
```

<!-- api: glyphkit.guides_layout_math_4 -->

把一套明确定义、类 LaTeX 的语法解析成由符号、上下标、分数、根号、括号、矩阵、重音符号与上下限组成的树。语法列在[数学语法](math-grammar.md#sec-math-grammar)。

<!-- api: glyphkit.layout_math_layout_math -->

用 `style.families` 里第一个字体的 OpenType MATH 常数排出算式。这个字体必须有 MATH 表。

<!-- api: glyphkit.guides_layout_math_5 -->

控制数学字族、大小、上下标层级、字母的倾斜、上下标缩放比例，以及 OpenType MATH 常数的覆写值。

<!-- api: glyphkit.guides_layout_math_6 -->

排好的树的一个节点。它有 `kind`、范围、基线、每个子节点相对于父节点的 `origin`、放在 `text_layout` 里的字形排版，以及可绘制的 `rules`。

这是一套明确定义的类 LaTeX 子集，不是 TeX 解释器。与字体相关的常数与字形变体来自 OpenType MATH 表 [{Microsoft} (2025)](../project/references.md#opentype-math2025)。`MathStyle` 可以覆写上下标缩放比例、具名的数学常数与字母使用的倾斜，这对 MATH 表不完整的字体很有用。

<span id="fig-glyph-math"></span>

<figure class="ev-fig" markdown>

![以 OpenType MATH 度量与精确字形轮廓排出的 Cobb–Douglas 效用函数。虚线方框是方框树中的上下标节点。](../../../assets/glyphkit/math/utility.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/glyphkit/math/utility.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>以 OpenType MATH 度量与精确字形轮廓排出的 Cobb–Douglas 效用函数。虚线方框是方框树中的上下标节点。</figcaption>

</figure>

绘图端只要走访这棵树：把每个子节点的原点加到父节点的位置上，用字形轮廓画出每个 `text_layout`，并把每条 rule 画成从 `start` 到 `end`、粗细为 `thickness` 的线。画出上图的脚本就是这样做的，大约四十行。
