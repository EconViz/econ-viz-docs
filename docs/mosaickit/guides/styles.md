---
seo_title: "Styles and colors"
---

# Styles and colors

<span id="sec-styles"></span>

## Sparse styles

Every style is a frozen dataclass whose fields may all be `None`. `None`
means inherit: the value comes from a style below it ([Themes and configuration](themes.md#sec-themes)). Falsy
values are not `None`, so `opacity=0`, `width=0` and
`LegendStyle(visible=False)` are explicit overrides.

<span id="def-merge"></span>

!!! abstract "Definition · Sparse merge"

    Let $a$ and $b$ be styles of the same type with fields $F$. The style
    $a \triangleright b$ (`a.merged_over(b)`) has, for each $\phi \in F$,

    $$
    (a \triangleright b)_\phi = \begin{cases}\begin{aligned}a_\phi & \text{if} a_\phi \ne \text{None}\end{aligned} \\\ \begin{aligned}b_\phi & \text{otherwise}.\end{aligned}\end{cases}
    $$

    The empty style $\epsilon$ has every field `None`. For style bundles the
    merge is taken slot by slot, a `None` slot acting as $\epsilon$.

<span id="prop-monoid"></span>

!!! abstract "Proposition · Merging is a monoid"

    For styles $a, b, c$ of one type,
    (i) $(a \triangleright b) \triangleright c = a \triangleright (b \triangleright c)$;
    (ii) $\epsilon \triangleright a = a \triangleright \epsilon = a$;
    (iii) $a \triangleright a = a$.
    Field by field, $a_1 \triangleright \cdots \triangleright a_n$ takes the first
    value that is not `None`.

A stack of styles can therefore be merged in any grouping. The result acts
as a priority list: the first source that sets a field wins.

<!-- api: agora.mosaickit.guides_styles_1 -->

The merge of [Sparse merge](styles.md#def-merge). Styles of different types raise `TypeError`.

## Style types

<!-- api: agora.mosaickit.guides_styles_2 -->

Line styles. `width` is in points; `dash` is a `DashStyle` (`SOLID`,
`DASHED`, `DOTTED`, `DASHDOT`); `arrow` is an `ArrowStyle` (`OPEN`,
`TRIANGLE`, `FANCY`, `WEDGE`) drawn at the layer's `ArrowPlacement`
(`START`, `END`, `BOTH`).

<!-- api: agora.mosaickit.guides_styles_3 -->

Styles for region interiors. `hatch` is a Matplotlib hatch pattern such as
`"//"`; `""` means no hatch.

<!-- api: agora.mosaickit.guides_styles_4 -->

Point-marker styles. As in Matplotlib's `scatter`, `size` is the area in
square points (36 is a 6 pt disc). `shape` is a Matplotlib marker such as
`"o"`, `"s"` or `"X"`.

<!-- api: agora.mosaickit.guides_styles_5 -->

Text styles. `size` is in points, `family` is a font-family name, `weight`
may be a value such as `"bold"`, and `rotation` is in degrees
counter-clockwise.

<!-- api: agora.mosaickit.guides_styles_6 -->

Legend styles, including a Matplotlib location such as `"best"` or
`"upper right"`, a frame setting and the font size.

Sizes, widths and opacities are checked when a style is created: sizes must
be finite and non-negative, opacities in $[0, 1]$, rotation finite.

<span id="tab-primitive"></span>

| Style | Values |
| --- | --- |
| `Stroke` | `grey-800`, width 1.5, solid, opacity 1 |
| `Fill` | `grey-200`, opacity 0.3, no hatch |
| `Marker` | `grey-800`, size 36, `"o"`, opacity 1, edge `grey-800` of width 0 |
| `TextStyle` | `grey-900`, 12 pt, DejaVu Sans, normal weight, opacity 1, no rotation |
| `LegendStyle` | visible, location `"best"`, no frame, 10 pt |

## Colors

<!-- api: agora.mosaickit.guides_styles_7 -->

An immutable RGBA color with channels in $[0, 1]$. `channels` returns the
four values, `from_channels()` builds one, and
`to_hex(include_alpha=None)` writes `#RRGGBB`, adding `AA` when
`include_alpha` is true, or by default when alpha is not 1.
`TRANSPARENT` is `Color(0, 0, 0, 0)`.

<span id="prop-hex"></span>

!!! abstract "Proposition · Hex round trip"

    For every string $h$ of the form `#RRGGBB` or `#RRGGBBAA` in hexadecimal
    digits, `Color.from_hex(h).to_hex(include_alpha=len(h) == 9)` equals $h$
    in upper case. A three-digit `#RGB` is read as `#RRGGBB`.

A style `color` or `edge_color` takes a `Color`, a `"#hex"` string (parsed
at once) or any other string, which is kept as a _palette name_.

## Palettes

<!-- api: agora.mosaickit.guides_styles_8 -->

A named table of colors. Values may be `Color`s or hex strings.
`palette[name]` looks up a color and raises `ConfigurationError`, naming
the palette, when the name is unknown. `name in palette` tests whether a
name exists.

<span id="tab-palette"></span>

| Name | Value | Used by the default theme for |
| --- | --- | --- |
| `grey-900` | `#222222` | Text |
| `grey-800` | `#333333` | Lines, markers, axes |
| `grey-600` | `#666666` | Axis notes |
| `grey-400` | `#999999` | Guides |
| `grey-200` | `#CCCCCC` | Fills |
| `grey-100` | `#E6E6E6` |  |
| `white` | `#FFFFFF` | The canvas background |
| `blue` | `#01A2D9` | `primary` |
| `red` | `#E3120B` | `secondary` |
| `teal` | `#00887D` | `accent` |

Themes and styles name their colors, and the names are looked up in the
active palette (`Config.palette`) when a canvas builds its render plan, so
renderers only ever see concrete colors. Changing a palette entry recolors
every role that names it. A missing name raises
`ConfigurationError` at render time, naming the role, the style field and
the palette. A Python `Palette` replaces the default palette, so build it
from `DEFAULT_PALETTE.colors` to keep the names the built-in theme uses:

```python
from mosaickit import (
    DEFAULT_PALETTE,
    Canvas,
    Config,
    Palette,
    use_config,
)

brand = Palette(
    "brand", {**DEFAULT_PALETTE.colors, "blue": "#0072B2"}
)
with use_config(Config(palette=brand)):
    # primary now draws in #0072B2
    canvas = Canvas()
```
