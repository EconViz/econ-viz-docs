"""Baseline, advance and vertical metrics of a shaped line.

Usage: python metrics.py [font.otf] [en|zh-TW|zh-CN] > metrics.svg
"""

import sys

from glyphkit import FontLibrary, FontSource, Paragraph, TextSpan, TextStyle
from glyphkit.outlines import CubicTo, LineTo, MoveTo, QuadraticTo

FONT = sys.argv[1] if len(sys.argv) > 1 else "fonts/SourceSans3-Regular.ttf"
LANG = sys.argv[2] if len(sys.argv) > 2 else "en"
WORDS = {
    "en": ("ascender", "baseline", "descender", "advance width"),
    "zh-TW": ("上伸線", "基線", "下伸線", "字幅（advance）"),
    "zh-CN": ("上伸线", "基线", "下伸线", "字幅（advance）"),
}[LANG]
SIZE = 120
TEXT = "Typography"


def outline_path(outline, scale, x0, y0):
    """SVG path data for an exact outline; font y grows up, SVG y grows down."""

    def p(point):
        return f"{x0 + point[0] * scale:.2f} {y0 - point[1] * scale:.2f}"

    parts = []
    for command in outline.commands:
        if isinstance(command, MoveTo):
            parts.append(f"M{p(command.point)}")
        elif isinstance(command, LineTo):
            parts.append(f"L{p(command.point)}")
        elif isinstance(command, QuadraticTo):
            parts.append(f"Q{p(command.control)} {p(command.point)}")
        elif isinstance(command, CubicTo):
            parts.append(f"C{p(command.control1)} {p(command.control2)} {p(command.point)}")
        else:
            parts.append("Z")
    return " ".join(parts)


library = FontLibrary.from_sources((FontSource.path(FONT),))
family = library.faces[0].family
face = library.faces[0]
layout = library.layout(Paragraph((TextSpan(TEXT, TextStyle((family,), SIZE)),)))
line = layout.lines[0]

scale = SIZE / face.metrics.units_per_em
ascender = face.metrics.ascender * scale
descender = face.metrics.descender * scale
width = line.advance

left, top = 70, 40
baseline_y = top + ascender
right = left + width
height = ascender - descender
paths = []
for run in line.runs:
    for glyph in run.glyphs:
        outline = library.outline(glyph)
        paths.append(
            outline_path(outline, SIZE / outline.units_per_em, left + glyph.x, baseline_y - glyph.y)
        )

rules = [
    (WORDS[0], baseline_y - ascender),
    (WORDS[1], baseline_y),
    (WORDS[2], baseline_y - descender),
]
svg = [
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width + 190:.0f} {height + 100:.0f}"'
    ' font-family="Helvetica, Arial, \'PingFang TC\', \'Noto Sans TC\', sans-serif" font-size="13">',
    '<rect width="100%" height="100%" fill="#fff"/>',
    f'<rect x="{left}" y="{top}" width="{width:.2f}" height="{height:.2f}" fill="none"'
    ' stroke="#000" stroke-width="1"/>',
]
for name, y in rules:
    dash = "" if name == WORDS[1] else ' stroke-dasharray="5 4"'
    svg.append(
        f'<line x1="{left - 30}" y1="{y:.2f}" x2="{right + 30:.2f}" y2="{y:.2f}"'
        f' stroke="#000" stroke-width="1"{dash}/>'
    )
    svg.append(f'<text x="{right + 36:.2f}" y="{y + 4:.2f}" fill="#000">{name}</text>')
svg.append(f'<path d="{" ".join(paths)}" fill="#000"/>')
bottom = top + height + 28
svg.append(
    f'<line x1="{left}" y1="{bottom:.2f}" x2="{right:.2f}" y2="{bottom:.2f}" stroke="#000"/>'
    f'<line x1="{left}" y1="{bottom - 5:.2f}" x2="{left}" y2="{bottom + 5:.2f}" stroke="#000"/>'
    f'<line x1="{right:.2f}" y1="{bottom - 5:.2f}" x2="{right:.2f}" y2="{bottom + 5:.2f}" stroke="#000"/>'
    f'<text x="{(left + right) / 2:.2f}" y="{bottom + 20:.2f}" text-anchor="middle">'
    f"{WORDS[3]}</text>"
)
svg.append("</svg>")
print("\n".join(svg))
