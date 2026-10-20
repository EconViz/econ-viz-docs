---
seo_title: "OpenType mathematics layout"
---

# OpenType mathematics layout

<span id="sec-glyph-math-model"></span>

## Semantic box tree

GlyphKit parses a small semantic language and lays it out as a `MathBox` tree. The tree separates glyph layouts, child origins, bounds, baselines, and rules. A backend can therefore draw [A Cobb–Douglas utility function laid out with OpenType MATH metrics and exact glyph outlines](layout-math.md#fig-glyph-math) without implementing TeX.

## Script scaling and placement

If the display size is $s$ and `ScriptPercentScaleDown` is $r$ percent, the script size is $s_1 = s r / 100$. At the next level, `ScriptScriptPercentScaleDown` is applied. Scripts begin after the base width plus its italic correction $k$:

$$
x_{\text{script}} = w_{\text{base}} + k.
$$

Vertical offsets come from `SuperscriptShiftUp` and `SubscriptShiftDown`.

## Fractions

For numerator width $w_n$ and denominator width $w_d$, GlyphKit assigns $w = \max(w_n, w_d) + 0.2 s$ and centres both children. The rule lies at `AxisHeight`, has at least $s/1000$ thickness, and otherwise follows `FractionRuleThickness`. Display and inline styles may select different shifts.

## Roots, limits, and accents

The radicand begins after the radical glyph. Its overbar is placed at the ink top plus `RadicalVerticalGap`; thickness and indexed-root kern also come from the MATH table. Limits use minimum rise and drop constants. Accent attachment uses per-glyph data when present and otherwise falls back to the horizontal centre.

## Style and constant overrides

<!-- api: agora.glyphkit.guides_math_layout_model_1 -->

Controls size, family, level, alphabetic slant, script-scale overrides, and documented OpenType constant overrides. Override values are em fractions; font-table values are scaled from font units.
