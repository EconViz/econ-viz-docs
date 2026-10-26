"""A Cobb-Douglas utility function laid out with OpenType MATH metrics.

Usage: python utility.py [math-font.otf] > utility.svg
"""

import sys

from glyphkit import FontLibrary, FontSource
from glyphkit.math import MathStyle, parse_math
from glyphkit.outlines import CubicTo, LineTo, MoveTo, QuadraticTo

FONT = sys.argv[1] if len(sys.argv) > 1 else "fonts/STIXTwoMath-Regular.otf"
SIZE = 56


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
box = library.layout_math(
    parse_math(r"U(x_1, x_2) = x_1^{\alpha} x_2^{1-\alpha}"),
    style=MathStyle(SIZE, (family,)),
)

paths = []
boxes = []
rules = []


def walk(node, x, y):
    """Visit the box tree; children carry their origin relative to the parent."""
    ox, oy = x + node.origin[0], y - node.origin[1]  # origins are y-up
    if node.kind == "text" and node.text_layout is not None:
        for line in node.text_layout.lines:
            for run in line.runs:
                for glyph in run.glyphs:
                    outline = library.outline(glyph)
                    if outline.commands:
                        paths.append(
                            outline_path(
                                outline,
                                run.size / outline.units_per_em,
                                ox + glyph.x,
                                oy - glyph.y,
                            )
                        )
    elif node.kind in ("script",):
        b = node.bounds
        boxes.append((ox + b.x_min, oy - b.y_max, b.width, b.height))
    for rule in node.rules:
        (x1, y1), (x2, y2) = rule.start, rule.end
        rules.append((ox + x1, oy - y1, ox + x2, oy - y2, rule.thickness))
    for child in node.children:
        walk(child, ox, oy)


left, top = 30, 24
b = box.bounds
baseline = top + b.y_max
walk(box, left, baseline)
width = b.width + 2 * left
height = b.height + 2 * top
svg = [
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:.0f} {height:.0f}">',
    '<rect width="100%" height="100%" fill="#fff"/>',
]
for x, y, w, h in boxes:
    svg.append(
        f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" fill="none"'
        ' stroke="#000" stroke-width="0.6" stroke-dasharray="3 3"/>'
    )
svg.append(
    f'<line x1="{left - 10}" y1="{baseline:.2f}" x2="{left + b.width + 10:.2f}" y2="{baseline:.2f}"'
    ' stroke="#000" stroke-width="0.6"/>'
)
for x1, y1, x2, y2, thickness in rules:
    svg.append(
        f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}"'
        f' stroke="#000" stroke-width="{thickness:.2f}"/>'
    )
svg.append(f'<path d="{" ".join(paths)}" fill="#000"/>')
svg.append("</svg>")
print("\n".join(svg))
