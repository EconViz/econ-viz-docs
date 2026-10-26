"""One point moving across the view, written as animated SVG.

Usage: python dot.py
"""

from kinetickit import Animation, Bounds2D, Point2D, Scene2D, Vec2, ease

dot = Point2D(id="dot", position=Vec2(1, 1), size=8, color="#e4572e")
scene = Scene2D(dot)
scene = scene.bind({scene.camera.ref("view"): Bounds2D(Vec2(0, 0), Vec2(10, 10))})

motion = dot.animate.position.to(Vec2(9, 9), duration=1.5, easing=ease.out_cubic)
animation = Animation(scene, motion)

animation.save("dot.svg", width=300, height=300, loop=True)
