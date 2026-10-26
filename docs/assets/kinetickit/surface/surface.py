"""A lit 3D surface with an orbiting camera, written as a GIF.

Usage: python surface.py        (needs kinetickit[raster])
"""

import numpy as np

from kinetickit.animation import Animation
from kinetickit.geometry.three_d import Vec3
from kinetickit.scene import Camera3D, DirectionalLight3D, Point3D, Scene3D, Surface3D
from kinetickit.styles import ColorScale, Material

xs = ys = np.linspace(-2, 2, 28)
X, Y = np.meshgrid(xs, ys)
Z = np.sin(np.hypot(X, Y) * 2.2) / (1 + np.hypot(X, Y))
surface = Surface3D.height_field(
    "surface",
    xs,
    ys,
    Z,
    colorscale=ColorScale.viridis_like(),
    material=Material(0.4, 0.6, 0.2, 24),
)
marker = Point3D(id="peak", position=Vec3(0, 0, 1.0), size=6, color="#d62728")
scene = Scene3D(
    surface,
    marker,
    DirectionalLight3D(id="sun"),
    camera=Camera3D(position=Vec3(5.5, -6.5, 4.2), target=Vec3(0, 0, 0.2)),
)
orbit = scene.camera.animate.position.to(Vec3(-6, -5.5, 4.2), duration=2.0)

Animation(scene, orbit).save("surface.gif", width=320, height=240, fps=10)
