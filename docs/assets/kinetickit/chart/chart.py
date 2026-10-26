"""A bar-and-line chart built from generic shapes, axes and morphs.

Usage: python chart.py
"""

from kinetickit import ease
from kinetickit.animation import Animation
from kinetickit.geometry.two_d import Bounds2D, Path2D, Vec2
from kinetickit.guides import Axis2D, Grid2D
from kinetickit.layout import Viewport, resolve_layout
from kinetickit.scene import PathNode2D, Scene2D, Shape2D

VALUES = [3.0, 5.5, 4.0, 7.5, 6.0]

bars = [
    Shape2D(id=f"bar{i}", path=Path2D.rect(i + 0.15, 0, 0.7, 0.0001), fill="#999999")
    for i, _ in enumerate(VALUES)
]
line = PathNode2D.polyline(
    "trend",
    [(i + 0.5, v) for i, v in enumerate(VALUES)],
    width=3,
    color="#000000",
    draw_progress=0.0,
)
base = Scene2D(*bars, line)
base = base.bind({base.camera.ref("view"): Bounds2D(Vec2(-0.9, -1.2), Vec2(5.9, 9))})

# Guides are compiled against the resolved layout, then added as ordinary nodes.
layout = resolve_layout(Animation(base), Viewport(280, 420))
guides = [
    Grid2D("grid", (0, 5), (0, 8)).compile(),
    Axis2D("x", "x", (0, 5)).compile(layout),
    Axis2D("y", "y", (0, 8), at=0).compile(layout),
]
scene = Scene2D(*guides, *bars, line, camera=base.camera)

motion = None
for i, (bar, value) in enumerate(zip(bars, VALUES, strict=True)):
    grow = bar.morph_to(Path2D.rect(i + 0.15, 0, 0.7, value), duration=0.8, easing=ease.out_cubic)
    motion = grow if motion is None else motion.with_(grow, offset=0.1 * i)
motion = motion.then(line.animate.draw_progress.to(1.0, duration=1.0))

Animation(scene, motion).save("chart.svg", width=280, height=420, loop=True)
