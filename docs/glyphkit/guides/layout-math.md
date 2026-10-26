---
seo_title: "Text layout and mathematics"
---

# Text layout and mathematics

<span id="sec-layout-math"></span>

## Paragraphs and measurement

<!-- api: glyphkit.guides_layout_math_1 -->

Shapes every span, wraps at legal Unicode break opportunities and returns an immutable `TextLayout`. `library.layout(paragraph)` calls it with the library as its first argument.

<!-- api: glyphkit.guides_layout_math_2 -->

Summarises the logical and ink bounds, the baselines, the line count and the overflow of a layout, without drawing. `layout.measure()` returns one.

<!-- api: glyphkit.guides_layout_math_3 -->

One laid-out line with its runs, baseline, advance, bounds, source range and whether it ended at an explicit line break.

`TextStyle` carries the font families, size, weight, slant, language, direction, spacing and OpenType features. A paragraph may mix styles and scripts. Set `max_width` to wrap at Unicode line-break opportunities [{Unicode Consortium} (2026)](../project/references.md#unicode-linebreak2026), and leave it unset for one unconstrained line. [Line construction and spacing](line-layout-algorithms.md#sec-glyph-lines) explains how a line is built.

## Structured mathematics

```python
from glyphkit import FontLibrary, FontSource
from glyphkit.math import MathStyle, parse_math

library = FontLibrary.from_sources((FontSource.path("fonts/STIXTwoMath-Regular.otf"),))
formula = parse_math(r"U(x_1, x_2) = x_1^\alpha x_2^{1-\alpha}")
box = library.layout_math(formula, style=MathStyle(18, ("STIX Two Math",)))
print(box.bounds)
```

<!-- api: glyphkit.guides_layout_math_4 -->

Parses a defined LaTeX-like grammar into a tree of symbols, scripts, fractions, roots, delimiters, matrices, accents and limits. The grammar is on the [Math grammar](math-grammar.md#sec-math-grammar) page.

<!-- api: glyphkit.layout_math_layout_math -->

Lays an expression out with the OpenType MATH constants of the first font in `style.families`. The font must have a MATH table.

<!-- api: glyphkit.guides_layout_math_5 -->

Controls the math families, the size, the script level, the slant of letters, the script scales and overrides of OpenType MATH constants.

<!-- api: glyphkit.guides_layout_math_6 -->

One node of the laid-out tree. It has a `kind`, bounds, a baseline, the `origin` of each child relative to its parent, glyph layouts in `text_layout`, and drawable `rules`.

This is a defined subset of LaTeX-like input, not a TeX interpreter. The font-specific constants and glyph variants come from the OpenType MATH table [{Microsoft} (2025)](../project/references.md#opentype-math2025). `MathStyle` can override the script scales, named math constants and the slant used for letters, which helps with fonts whose MATH table is incomplete.

<span id="fig-glyph-math"></span>

<figure class="ev-fig" markdown>

![A Cobb–Douglas utility function laid out with OpenType MATH metrics and exact glyph outlines. Dashed boxes are the script nodes of the box tree.](../../assets/glyphkit/math/utility.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/glyphkit/math/utility.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>A Cobb–Douglas utility function laid out with OpenType MATH metrics and exact glyph outlines. Dashed boxes are the script nodes of the box tree.</figcaption>

</figure>

A renderer draws the tree by walking it: it adds the origin of each child to its parent's position, draws each `text_layout` with the outlines of its glyphs, and draws each rule as a line from `start` to `end` with its `thickness`. The script that draws the figure above does exactly this in about forty lines.
