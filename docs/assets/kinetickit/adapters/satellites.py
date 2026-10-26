"""Animate any object model: plain Python satellites, no visualization package.

Usage: python satellites.py
"""

import math
from dataclasses import dataclass

from kinetickit.adapters import adapt, transition
from kinetickit.animation import Animation
from kinetickit.geometry.two_d import Bounds2D, Vec2
from kinetickit.scene import Line2D, Point2D


@dataclass(frozen=True)
class Satellite:
    """A domain object that KineticKit knows nothing about."""

    name: str
    angle: float
    radius: float
    tint: str


def depict(satellite: Satellite):
    """Translate one object into ordinary nodes with stable ids."""
    position = Vec2(
        satellite.radius * math.cos(satellite.angle),
        satellite.radius * math.sin(satellite.angle),
    )
    return [
        Point2D(id=f"{satellite.name}.body", position=position, size=7, color=satellite.tint),
        Line2D(
            id=f"{satellite.name}.tether",
            start=Vec2(0, 0),
            end=position,
            width=1.5,
            color="#999999",
        ),
    ]


before = [Satellite("alpha", 0.0, 3.0, "#000000"), Satellite("beta", 2.0, 5.0, "#666666")]
after = [
    Satellite("alpha", 1.5, 4.0, "#000000"),
    Satellite("beta", 4.0, 5.0, "#666666"),
    Satellite("gamma", 5.5, 2.0, "#999999"),
]

step = transition(before, after, depict, duration=1.5)
scene = step.scene
scene = scene.bind({scene.camera.ref("view"): Bounds2D(Vec2(-6, -6), Vec2(6, 6))})
Animation(scene, step.motion).save("satellites.svg", width=360, height=360, loop=True)
