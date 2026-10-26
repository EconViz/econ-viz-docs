"""The exact outline of one glyph, with its on-curve points and control polygons.

Usage: python glyph.py [font.otf] [character] > glyph.svg
"""

import sys

from glyphkit import FontLibrary, FontSource, Paragraph, TextSpan, TextStyle
from glyphkit.outlines import ClosePath, CubicTo, LineTo, MoveTo, QuadraticTo

FONT = sys.argv[1] if len(sys.argv) > 1 else "fonts/SourceSans3-Regular.ttf"
CHARACTER = sys.argv[2] if len(sys.argv) > 2 else "g"
SCALE = 0.62  # SVG units per font unit


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
layout = library.layout(Paragraph((TextSpan(CHARACTER, TextStyle((family,), 100)),)))
glyph = layout.lines[0].runs[0].glyphs[0]
outline = library.outline(glyph)

bounds = outline.bounds
left, top, margin = 40, 40, 40
width = bounds.width * SCALE + 2 * margin
height = bounds.height * SCALE + 2 * margin
x0 = margin - bounds.x_min * SCALE
y0 = margin + bounds.y_max * SCALE


def point(p):
    return x0 + p[0] * SCALE, y0 - p[1] * SCALE


svg = [
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:.0f} {height:.0f}">',
    '<rect width="100%" height="100%" fill="#fff"/>',
    f'<line x1="0" y1="{y0:.2f}" x2="{width:.0f}" y2="{y0:.2f}" stroke="#000"'
    ' stroke-width="0.6" stroke-dasharray="5 4"/>',
    f'<path d="{outline_path(outline, SCALE, x0, y0)}" fill="#e6e6e6" stroke="#000" stroke-width="1.6"/>',
]
current = (0.0, 0.0)
start = current
for command in outline.commands:
    if isinstance(command, MoveTo):
        current = start = command.point
    elif isinstance(command, LineTo):
        current = command.point
    elif isinstance(command, QuadraticTo):
        a, b, c = point(current), point(command.control), point(command.point)
        svg.append(
            f'<polyline points="{a[0]:.2f},{a[1]:.2f} {b[0]:.2f},{b[1]:.2f} {c[0]:.2f},{c[1]:.2f}"'
            ' fill="none" stroke="#000" stroke-width="0.8" stroke-dasharray="3 3"/>'
        )
        svg.append(f'<circle cx="{b[0]:.2f}" cy="{b[1]:.2f}" r="3" fill="#fff" stroke="#000"/>')
        current = command.point
    elif isinstance(command, CubicTo):
        a, b, c, d = (point(current), point(command.control1), point(command.control2), point(command.point))
        svg.append(
            f'<polyline points="{a[0]:.2f},{a[1]:.2f} {b[0]:.2f},{b[1]:.2f} {c[0]:.2f},{c[1]:.2f} {d[0]:.2f},{d[1]:.2f}"'
            ' fill="none" stroke="#000" stroke-width="0.8" stroke-dasharray="3 3"/>'
        )
        for control in (b, c):
            svg.append(f'<circle cx="{control[0]:.2f}" cy="{control[1]:.2f}" r="3" fill="#fff" stroke="#000"/>')
        current = command.point
    elif isinstance(command, ClosePath):
        current = start
for command in outline.commands:
    if not isinstance(command, ClosePath):
        x, y = point(command.point)
        svg.append(f'<rect x="{x - 3:.2f}" y="{y - 3:.2f}" width="6" height="6" fill="#000"/>')
svg.append("</svg>")
print("\n".join(svg))
