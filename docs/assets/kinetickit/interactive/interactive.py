"""Declarative interactions and accessibility metadata on a small generic scene.

Usage: python interactive.py        (needs kinetickit[interactive])
"""

from kinetickit.accessibility import AccessibilityInfo, Semantics
from kinetickit.animation import Animation
from kinetickit.geometry.two_d import Bounds2D, Vec2
from kinetickit.interaction import Binding, Event, InteractionSpec, PlayRange, Select, SetProperty
from kinetickit.scene import Point2D, Scene2D

a = Point2D(
    id="a",
    position=Vec2(1, 1),
    size=9,
    semantics=Semantics(
        role="graphics-symbol",
        label="Start",
        description="Where the motion begins",
        reading_order=1,
    ),
)
b = Point2D(
    id="b",
    position=Vec2(8, 8),
    size=9,
    semantics=Semantics(role="graphics-symbol", label="Goal", reading_order=2),
)
scene = Scene2D(a, b)
scene = scene.bind({scene.camera.ref("view"): Bounds2D(Vec2(0, 0), Vec2(10, 10))})
motion = a.animate.position.to(Vec2(8, 8), duration=2.0).mark("arrived", 2.0)

interactions = InteractionSpec(
    (
        Binding(Event.CLICK, (PlayRange("run"),), "a"),
        Binding(Event.CLICK, (Select(mode="toggle"), SetProperty(None, "opacity", 0.6)), "b"),
    ),
    {"run": (0.0, 2.0)},
)
info = AccessibilityInfo(
    title="Reaching the goal",
    description="A dot travels to a target",
    long_description="A dot starts at the lower left and moves to the upper right.",
)
animation = Animation(scene, motion, interactions=interactions, accessibility=info)

animation.save("interactive.html", width=480, height=480, autoplay=False)
animation.save("interactive.svg", width=480, height=480, loop=True)
