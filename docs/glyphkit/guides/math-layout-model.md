---
seo_title: "OpenType mathematics layout"
---

# OpenType mathematics layout

<span id="sec-glyph-math-model"></span>

## Semantic box tree

GlyphKit parses a small semantic language and lays it out as a `MathBox` tree. The tree keeps glyph layouts, child origins, bounds, baselines and rules apart, so a backend can draw [A Cobb–Douglas utility function laid out with OpenType MATH metrics and exact glyph outlines](layout-math.md#fig-glyph-math) without implementing TeX.

A node's `kind` says what it is: `text` (glyphs), `sequence` (children side by side), `script`, `shifted`, `fraction`, `root`, `limits`, `operator`, `delimited`, `matrix`, `hat` and `overline` (accents and rules), and `space`. The `origin` of a child is its position relative to its parent, in layout units with y up, and `baseline` and `bounds` are in the node's own frame.

```python
def walk(node, depth=0):
    print("  " * depth, node.kind, node.origin)
    for child in node.children:
        walk(child, depth + 1)


walk(box)
```

## Script scaling

If the display size is $s$ and `ScriptPercentScaleDown` is $r$ percent, the script size is $s_1 = s r / 100$. At the next level the `ScriptScriptPercentScaleDown` constant applies in the same way, and both are taken from the whole expression's size. `MathStyle.script_scale` and `script_script_scale` replace the font's values.

## Constants come from the font

Shifts, gaps, rule thicknesses and the sizes of operators come from the font's MATH table: for example `SuperscriptShiftUp`, `SubscriptShiftDown`, `AxisHeight`, `FractionRuleThickness`, `RadicalVerticalGap` and `DisplayOperatorMinHeight`. [Math grammar](math-grammar.md#how-a-formula-is-set) describes how each construct uses them. A constant that the font does not supply falls back to a value in points. It is not scaled a second time.

## Style and constant overrides

<!-- api: glyphkit.guides_math_layout_model_1 -->

Controls the size, the family, the level, the slant of letters, overrides of the script scales, and overrides of other OpenType constants by name. Override values are fractions of an em, and values from the font table are scaled from font units.
