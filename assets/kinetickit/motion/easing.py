"""Six easing functions racing along parallel tracks, with GlyphKit labels.

Usage: python easing.py [font.otf]
"""

import sys

from glyphkit import FontLibrary, FontSource
from kinetickit import Animation, Bounds2D, Line2D, Point2D, Scene2D, Text2D, Vec2, ease
from kinetickit.integrations.glyphkit import GlyphKitTypography

FONT = sys.argv[1] if len(sys.argv) > 1 else "fonts/SourceSans3-Regular.ttf"

EASINGS = [
    ("linear", ease.linear),
    ("in_cubic", ease.in_cubic),
    ("out_cubic", ease.out_cubic),
    ("in_out_cubic", ease.in_out_cubic),
    ("out_expo", ease.out_expo),
    ("cubic_bezier (overshoot)", ease.cubic_bezier(0.34, 1.56, 0.64, 1)),
]

library = FontLibrary.from_sources((FontSource.path(FONT),))
typography = GlyphKitTypography(library, families=(library.faces[0].family,), size=40)

nodes = []
motion = None
for row, (name, easing) in enumerate(EASINGS):
    y = len(EASINGS) - row
    track = Line2D(id=f"track.{row}", start=Vec2(6, y), end=Vec2(11, y), width=1, color="#999999")
    label = Text2D(
        id=f"label.{row}",
        asset=typography.asset(name),
        position=Vec2(0.2, y - 0.1),
        scale=0.011,
        color="#000000",
    )
    dot = Point2D(id=f"dot.{row}", position=Vec2(6, y), size=9, color="#000000")
    nodes += [track, label, dot]
    step = dot.animate.position.to(Vec2(11, y), duration=2.0, easing=easing)
    motion = step if motion is None else motion.with_(step)

scene = Scene2D(*nodes)
scene = scene.bind({scene.camera.ref("view"): Bounds2D(Vec2(0, 0.2), Vec2(12, 6.8))})
Animation(scene, motion.then(motion.reverse(), gap=0.4)).save(
    "easing.svg", width=640, height=300, loop=True
)
