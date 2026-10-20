---
seo_title: "Text layout and mathematics"
---

# Text layout and mathematics

<span id="sec-layout-math"></span>

## Paragraphs and measurement

<!-- api: agora.glyphkit.guides_layout_math_1 -->

Shapes every span, wraps at legal Unicode break opportunities, and returns an immutable `TextLayout`.

<!-- api: agora.glyphkit.guides_layout_math_2 -->

Summarises logical and ink bounds, baselines, line count, and overflow without drawing.

<!-- api: agora.glyphkit.guides_layout_math_3 -->

One laid-out line with its runs, baseline, advance, bounds, source range, and explicit-ending status.

`TextStyle` carries the font families, size, weight, slant, language, direction, spacing, and OpenType features. A paragraph may mix styles and scripts. Set `max_width` to wrap at Unicode line-break opportunities [{Unicode Consortium} (2026)](../project/references.md#unicode-linebreak2026); leave it unset for one unconstrained line.

## Structured mathematics

```python
from glyphkit import FontLibrary, FontSource
from glyphkit.math import MathStyle, parse_math

library = FontLibrary.from_sources(
    (FontSource.path("fonts/STIXTwoMath-Regular.otf"),)
)
formula = parse_math(r"U(x_1, x_2) = x_1^\alpha x_2^{1-\alpha}")
box = library.layout_math(formula, style=MathStyle(18, ("STIX Two Math",)))
print(box.bounds)
```

<!-- api: agora.glyphkit.guides_layout_math_4 -->

Parses the supported LaTeX-like subset into a structured tree of symbols, scripts, fractions, roots, delimiters, matrices, accents, and limits.

<!-- api: agora.glyphkit.guides_layout_math_5 -->

Controls math families, size, script level, alphabetic slant, script scales, and OpenType MATH constant overrides.

<!-- api: agora.glyphkit.guides_layout_math_6 -->

One node in the laid-out math tree, containing bounds, baseline, child origins, glyph layouts, and drawable rules.

This is a defined subset of LaTeX-like input, not a TeX interpreter. Its font-specific constants and glyph variants come from the OpenType MATH table [{Microsoft} (2025)](../project/references.md#opentype-math2025). Unknown commands and malformed groups raise `MathSyntaxError`. In 1.0.0b2, `MathStyle` can override script scales, named math constants, and the slant used for alphabetic symbols.

<span id="fig-glyph-math"></span>

<figure class="ev-fig" markdown>

![A Cobb–Douglas utility function laid out with OpenType MATH metrics and exact glyph outlines](../../assets/glyphkit/agora/math/utility.svg){ .ev-figure-sm }

<figcaption markdown>A Cobb–Douglas utility function laid out with OpenType MATH metrics and exact glyph outlines</figcaption>

</figure>
