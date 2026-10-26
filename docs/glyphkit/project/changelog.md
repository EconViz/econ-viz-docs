---
seo_title: "Change history"
---

# Change history

<span id="sec-changelog"></span>

Releases of `glyphkit` covered by this documentation.

## 1.0.0b4 (2026-10-22)

- A font is parsed once and kept (the eight most recently used), instead of once per glyph outline and once per math layout. Outlines and layouts are identical. The parsed font is shared under a lock, so concurrent reads stay deterministic ([Outlines](../guides/outlines-embedding.md#sec-outlines-embedding)).

## 1.0.0b3 (2026-10-21)

- Math layout follows TeX's rules with the font's MATH constants: fractions, scripts, large operators and limits, stretched radicals and delimiters, accents, and rules for `\overline` and `\underline` ([Math grammar](../guides/math-grammar.md#sec-math-grammar)).
- Atoms are spaced by TeX's table. A binary operator with no left operand is ordinary, and `-` is drawn as U+2212 when the font has it.
- `MathStyle.level` accepts `"text"` and `"scriptscript"` besides `"display"` and `"script"`.
- More commands: the whole Greek alphabet, symbols and relations, functions, `\mathrm`, `\text`, `\operatorname`, spaces and integrals. `Symbol.role` classifies atoms, and there is a new `Space` node.

## 1.0.0b2 (2026-10-13)

- `MathStyle` accepts `script_scale` and `script_script_scale`, and `constants` and `letter_slant` ([Text layout and mathematics](../guides/layout-math.md#sec-layout-math)).

## 1.0.0b1 (2026-10-12)

- First integration beta of the public typography contract: explicit font sources, matching, fallback and manifests, Unicode segmentation, bidi-aware shaping, paragraph layout and outlines, OpenType MATH layout, permission-aware subsets, versioned serialization ([Introduction](../guides/introduction.md#sec-intro)).
