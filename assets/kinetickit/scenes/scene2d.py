"""Lines, a path, a shape and a group: a 2D scene with three motions.

Usage: python scene2d.py
"""

from kinetickit import (
    Animation,
    Bounds2D,
    Group2D,
    Line2D,
    Path2D,
    PathNode2D,
    Scene2D,
    Shape2D,
    Transform2D,
    Vec2,
    ease,
)

x_axis = Line2D(id="x-axis", start=Vec2(0, 0), end=Vec2(10, 0), width=1.5, color="#000000")
y_axis = Line2D(id="y-axis", start=Vec2(0, 0), end=Vec2(0, 8), width=1.5, color="#000000")
curve = PathNode2D.polyline(
    "curve", [(0, 7), (2, 4.5), (4, 3), (7, 1.6), (10, 1)], width=3, color="#000000", draw_progress=0.0
)
area = Shape2D(id="area", path=Path2D.rect(0, 0, 4, 3), fill="#bbbbbb", opacity=0.0)
plot = Group2D(id="plot", children=(x_axis, y_axis, area, curve))

scene = Scene2D(plot)
scene = scene.bind({scene.camera.ref("view"): Bounds2D(Vec2(-1, -1), Vec2(12, 9))})

draw = curve.animate.draw_progress.to(1.0, duration=1.5, easing=ease.in_out_cubic)
fade = area.animate.opacity.to(1.0, duration=0.8)
motion = draw.then(fade).then(
    plot.animate.transform.to(Transform2D(translate=Vec2(1, 0.6)), duration=0.8)
)

Animation(scene, motion.then(motion.reverse(), gap=0.5)).save(
    "scene2d.svg", width=455, height=315, loop=True
)
