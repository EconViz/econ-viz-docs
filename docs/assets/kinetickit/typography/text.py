"""Text from a caller-provided font, laid out by GlyphKit and animated by KineticKit.

Usage: python text.py [font.otf]
"""

import sys

from glyphkit import FontLibrary, FontSource
from kinetickit import Animation, Bounds2D, Scene2D, Text2D, Vec2
from kinetickit.integrations.glyphkit import GlyphKitTypography

FONT = sys.argv[1] if len(sys.argv) > 1 else "fonts/SourceSans3-Regular.ttf"

library = FontLibrary.from_sources((FontSource.path(FONT),))
typography = GlyphKitTypography(library, families=(library.faces[0].family,), size=48)

title = Text2D(
    id="title",
    asset=typography.asset("Marginal utility"),
    position=Vec2(0.4, 0.6),
    scale=0.022,
    color="#000000",
)
scene = Scene2D(title)
scene = scene.bind({scene.camera.ref("view"): Bounds2D(Vec2(0, 0), Vec2(10, 4))})
motion = title.animate.position.to(Vec2(1.4, 2.8), duration=1.5)

Animation(scene, motion).save("text.svg", width=480, height=192, loop=True)
