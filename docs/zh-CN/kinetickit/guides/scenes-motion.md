---
seo_title: "场景与动作"
---

# 场景与动作

<span id="sec-scenes-motion"></span>

场景是不可变的节点集合，节点有稳定的编号，另外还有一个相机。动作则是让节点的属性随时间变化。两者都不知道绘图端的存在。

## 2D 场景

```python
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
move = plot.animate.transform.to(Transform2D(translate=Vec2(1, 0.6)), duration=0.8)

Animation(scene, draw.then(fade).then(move)).save("scene2d.svg", width=455, height=315)
```

<span id="fig-kinetic-scene2d"></span>

<figure class="ev-fig" markdown>

![路径逐段画出，图形淡入，整个群组移动；接着动作倒着播放。](../../../assets/kinetickit/scenes/scene2d.svg){ .ev-figure-lg }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/kinetickit/scenes/scene2d.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>路径逐段画出，图形淡入，整个群组移动；接着动作倒着播放。</figcaption>

</figure>

每种节点都能查到哪些属性可以制作动画：`Point2D.animatable_properties()` 返回属性名称与数值类型，`node.animate.<属性>` 则为其中一个属性创建动作。颜色、矢量、角度与变换各依自己的规则插值（参见[插值与变换](interpolation-transforms.md#sec-kinetic-interpolation)）。

<!-- api: kinetickit.guides_scenes_motion_1 -->

两点之间的描边线段。端点、颜色、线宽、虚线样式与绘制进度都能制作动画。

<!-- api: kinetickit.guides_scenes_motion_2 -->

开放或封闭的描边 `Path2D`。它保留直线与 Bézier 命令，并支持路径变形。`PathNode2D.polyline(id, points)` 是画直线折线的捷径。

<!-- api: kinetickit.guides_scenes_motion_3 -->

填色的路径，可另外加描边。用于区域、封闭轮廓与复合图形。

<!-- api: kinetickit.guides_scenes_motion_4 -->

对一串有顺序的子节点，统一套用变换、透明度与裁切的节点。

<!-- api: kinetickit.guides_scenes_motion_5 -->

由排版适配器产生、已定位的 `TextAsset`，缩放、变换与透明度都能制作动画（参见[文本排版](typography.md#sec-typography)）。

<!-- api: kinetickit.guides_scenes_motion_6 -->

定义 2D 世界中可见的矩形，以及它如何对应到输出窗口。用 `scene.bind({scene.camera.ref("view"): Bounds2D(...)})` 设置。视野会维持长宽比，所以输出尺寸的比例不同时，会出现留白。

## 3D 场景

```python
import numpy as np

from kinetickit import Animation, Camera3D, DirectionalLight3D, Point3D, Scene3D, Surface3D, Vec3
from kinetickit.styles import ColorScale, Material

xs = ys = np.linspace(-2, 2, 28)
X, Y = np.meshgrid(xs, ys)
Z = np.sin(np.hypot(X, Y) * 2.2) / (1 + np.hypot(X, Y))
surface = Surface3D.height_field(
    "surface", xs, ys, Z, colorscale=ColorScale.viridis_like(), material=Material(0.4, 0.6, 0.2, 24)
)
scene = Scene3D(
    surface,
    Point3D(id="peak", position=Vec3(0, 0, 1.0), size=6, color="#d62728"),
    DirectionalLight3D(id="sun"),
    camera=Camera3D(position=Vec3(5.5, -6.5, 4.2), target=Vec3(0, 0, 0.2)),
)
orbit = scene.camera.animate.position.to(Vec3(-6, -5.5, 4.2), duration=2.0)
Animation(scene, orbit).save("surface.gif", width=320, height=240, fps=10)
```

<span id="fig-kinetic-surface"></span>

<figure class="ev-fig" markdown>

![相机绕着打光的高度场曲面转动。](../../../assets/kinetickit/surface/surface.gif){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/kinetickit/surface/surface.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>相机绕着打光的高度场曲面转动。</figcaption>

</figure>

<!-- api: kinetickit.guides_scenes_motion_7 -->

不可变的 3D 场景，包含几何、光源、群组与一个相机。

<!-- api: kinetickit.guides_scenes_motion_8 -->

3D 空间中的点标记，位置、大小、颜色与透明度都能制作动画。

<!-- api: kinetickit.guides_scenes_motion_9 -->

单一 3D 线段，由目前的相机投影。

<!-- api: kinetickit.guides_scenes_motion_10 -->

由有顺序的 3D 点组成的折线，画成相连的线段。

<!-- api: kinetickit.guides_scenes_motion_11 -->

带索引的顶点与面，拓扑会经过验证，可选用每个面的颜色与材质设置。

<!-- api: kinetickit.guides_scenes_motion_12 -->

由 $x,y$ 网格与高度值创建的规则高度场曲面。常用的建构方式是 `Surface3D.height_field(id, xs, ys, zs)`。

<!-- api: kinetickit.guides_scenes_motion_13 -->

一组有顺序的 3D 节点，共用同一个变换与透明度。

<!-- api: kinetickit.guides_scenes_motion_14 -->

透视或正交相机，有位置、目标、裁切平面与投影设置。它的属性和一般节点一样可以制作动画，所以绕行只是一个 `position` 动作。

<!-- api: kinetickit.scenes_vec3 -->

3D 的点或方向。

<!-- api: kinetickit.scenes_colorscale -->

通过有序的色标，把数值对应到颜色。

<!-- api: kinetickit.scenes_material -->

表面的环境光、漫射与镜面反应。

<!-- api: kinetickit.scenes_light -->

朝单一方向照射的光源，像太阳那样。

## 组合时间

<!-- api: kinetickit.guides_scenes_motion_15 -->

不可变的变化描述。动作可以依序、重叠、延迟、重复、反转或裁切。

<!-- api: kinetickit.guides_scenes_motion_16 -->

动作树编译后的形式，可以直接求出任意有效时间的属性值。

<!-- api: kinetickit.guides_scenes_motion_17 -->

某个时间点的属性值，也可指定通往下一个区间的缓动规则。`hold=True` 会让这个值维持到下一个关键帧。

<!-- api: kinetickit.guides_scenes_motion_18 -->

同一属性的关键帧串行，会检查端点与时间顺序是否合法。

```python
motion = (
    a.animate.position.to(Vec2(5, 5), duration=1.0)
    .then(b.animate.opacity.to(1.0, duration=0.5))
    .with_(c.animate.size.to(9, duration=0.5), offset=1.0)
    .mark("settled")
)
```

`then` 在前一段结束时开始下一段。`with_` 则在前一段内部的某个偏移时间开始。两者的总长度见[时间与缓动](time-easing.md#sec-kinetic-time)。

## 场景之间的转场

<!-- api: kinetickit.guides_scenes_motion_19 -->

为两个场景创建动作。编号相同的节点会配成一对，并对兼容的属性做插值。

<!-- api: kinetickit.guides_scenes_motion_20 -->

决定没有对象或结构不兼容的节点要如何进场、退场、交叉淡化或报错。

路径、网格与曲面都有专用的变形工具。自动范式推不出你要的拓扑时，请明确提供对应方式（参见[变形](morphing.md#sec-kinetic-morphing)）。
