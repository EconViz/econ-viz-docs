"""A mixed-script paragraph wrapped at a maximum width, one box per line.

Usage: python paragraph.py [latin.otf cjk.otf] > paragraph.svg
"""

import sys

from glyphkit import FontLibrary, FontSource, Paragraph, TextSpan, TextStyle
from glyphkit.outlines import CubicTo, LineTo, MoveTo, QuadraticTo

LATIN = sys.argv[1] if len(sys.argv) > 1 else "fonts/SourceSans3-Regular.ttf"
CJK = sys.argv[2] if len(sys.argv) > 2 else "fonts/NotoSansTC-Regular.otf"
SIZE = 28
MAX_WIDTH = 330


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


library = FontLibrary.from_sources((FontSource.path(LATIN), FontSource.path(CJK)))
families = tuple(face.family for face in library.faces)
text = "Utility U(x) measures satisfaction. 效用函數描述偏好，數字大小只代表順序。"
layout = library.layout(
    Paragraph((TextSpan(text, TextStyle(families, SIZE)),), max_width=MAX_WIDTH, line_height=SIZE * 1.5)
)

left, top = 40, 30
top_edge = layout.logical_bounds.y_max
width = MAX_WIDTH + 2 * left
height = layout.logical_bounds.height + 2 * top
svg = [
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:.0f} {height:.0f}"'
    ' font-family="Helvetica, Arial, sans-serif" font-size="12">',
    '<rect width="100%" height="100%" fill="#fff"/>',
    f'<line x1="{left + MAX_WIDTH}" y1="{top - 12}" x2="{left + MAX_WIDTH}" y2="{height - top + 12:.0f}"'
    ' stroke="#000" stroke-dasharray="5 4"/>',
]
paths = []
for line in layout.lines:
    y_base = top + top_edge - line.baseline
    box = line.logical_bounds
    svg.append(
        f'<rect x="{left + box.x_min:.2f}" y="{top + top_edge - box.y_max:.2f}"'
        f' width="{box.width:.2f}" height="{box.height:.2f}" fill="none" stroke="#000" stroke-width="0.8"/>'
    )
    svg.append(
        f'<line x1="{left + box.x_min:.2f}" y1="{y_base:.2f}" x2="{left + box.x_max:.2f}" y2="{y_base:.2f}"'
        ' stroke="#000" stroke-width="0.6" stroke-dasharray="2 3"/>'
    )
    for run in line.runs:
        for glyph in run.glyphs:
            outline = library.outline(glyph)
            if outline.commands:
                paths.append(
                    outline_path(
                        outline,
                        run.size / outline.units_per_em,
                        left + glyph.x,
                        top + top_edge - glyph.y,
                    )
                )
svg.append(f'<path d="{" ".join(paths)}" fill="#000"/>')
svg.append(
    f'<text x="{left + MAX_WIDTH - 6}" y="{top - 16}" text-anchor="end">max_width</text>'
)
svg.append("</svg>")
print("\n".join(svg))
