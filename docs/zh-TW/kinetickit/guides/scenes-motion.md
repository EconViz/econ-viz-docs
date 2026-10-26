---
seo_title: "場景與動作"
---

# 場景與動作

<span id="sec-scenes-motion"></span>

場景是不可變的節點集合，節點有穩定的編號，另外還有一個相機。動作則是讓節點的屬性隨時間變化。兩者都不知道繪圖端的存在。

## 2D 場景

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

![路徑逐段畫出，圖形淡入，整個群組移動；接著動作倒著播放。](../../../assets/kinetickit/scenes/scene2d.svg){ .ev-figure-lg }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/kinetickit/scenes/scene2d.py" download aria-label="下載生圖原始檔"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下載生圖原始檔</span></a></div>

<figcaption markdown>路徑逐段畫出，圖形淡入，整個群組移動；接著動作倒著播放。</figcaption>

</figure>

每種節點都能查到哪些屬性可以製作動畫：`Point2D.animatable_properties()` 回傳屬性名稱與數值型別，`node.animate.<屬性>` 則為其中一個屬性建立動作。顏色、向量、角度與變換各依自己的規則插補（參見[插補與變換](interpolation-transforms.md#sec-kinetic-interpolation)）。

<!-- api: kinetickit.guides_scenes_motion_1 -->

兩點之間的描邊線段。端點、顏色、線寬、虛線樣式與繪製進度都能製作動畫。

<!-- api: kinetickit.guides_scenes_motion_2 -->

開放或封閉的描邊 `Path2D`。它保留直線與 Bézier 命令，並支援路徑變形。`PathNode2D.polyline(id, points)` 是畫直線折線的捷徑。

<!-- api: kinetickit.guides_scenes_motion_3 -->

填色的路徑，可另外加描邊。用於區域、封閉輪廓與複合圖形。

<!-- api: kinetickit.guides_scenes_motion_4 -->

對一串有順序的子節點，統一套用變換、透明度與裁切的節點。

<!-- api: kinetickit.guides_scenes_motion_5 -->

由排版轉接器產生、已定位的 `TextAsset`，縮放、變換與透明度都能製作動畫（參見[文字排版](typography.md#sec-typography)）。

<!-- api: kinetickit.guides_scenes_motion_6 -->

定義 2D 世界中可見的矩形，以及它如何對應到輸出視窗。用 `scene.bind({scene.camera.ref("view"): Bounds2D(...)})` 設定。視野會維持長寬比，所以輸出尺寸的比例不同時，會出現留白。

## 3D 場景

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

![相機繞著打光的高度場曲面轉動。](../../../assets/kinetickit/surface/surface.gif){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/kinetickit/surface/surface.py" download aria-label="下載生圖原始檔"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下載生圖原始檔</span></a></div>

<figcaption markdown>相機繞著打光的高度場曲面轉動。</figcaption>

</figure>

<!-- api: kinetickit.guides_scenes_motion_7 -->

不可變的 3D 場景，包含幾何、光源、群組與一個相機。

<!-- api: kinetickit.guides_scenes_motion_8 -->

3D 空間中的點標記，位置、大小、顏色與透明度都能製作動畫。

<!-- api: kinetickit.guides_scenes_motion_9 -->

單一 3D 線段，由目前的相機投影。

<!-- api: kinetickit.guides_scenes_motion_10 -->

由有順序的 3D 點組成的折線，畫成相連的線段。

<!-- api: kinetickit.guides_scenes_motion_11 -->

帶索引的頂點與面，拓撲會經過驗證，可選用每個面的顏色與材質設定。

<!-- api: kinetickit.guides_scenes_motion_12 -->

由 $x,y$ 網格與高度值建立的規則高度場曲面。常用的建構方式是 `Surface3D.height_field(id, xs, ys, zs)`。

<!-- api: kinetickit.guides_scenes_motion_13 -->

一組有順序的 3D 節點，共用同一個變換與透明度。

<!-- api: kinetickit.guides_scenes_motion_14 -->

透視或正交相機，有位置、目標、裁切平面與投影設定。它的屬性和一般節點一樣可以製作動畫，所以繞行只是一個 `position` 動作。

<!-- api: kinetickit.scenes_vec3 -->

3D 的點或方向。

<!-- api: kinetickit.scenes_colorscale -->

透過有序的色標，把數值對應到顏色。

<!-- api: kinetickit.scenes_material -->

表面的環境光、漫射與鏡面反應。

<!-- api: kinetickit.scenes_light -->

朝單一方向照射的光源，像太陽那樣。

## 組合時間

<!-- api: kinetickit.guides_scenes_motion_15 -->

不可變的變化描述。動作可以依序、重疊、延遲、重複、反轉或裁切。

<!-- api: kinetickit.guides_scenes_motion_16 -->

動作樹編譯後的形式，可以直接求出任意有效時間的屬性值。

<!-- api: kinetickit.guides_scenes_motion_17 -->

某個時間點的屬性值，也可指定通往下一個區間的緩動規則。`hold=True` 會讓這個值維持到下一個關鍵影格。

<!-- api: kinetickit.guides_scenes_motion_18 -->

同一屬性的關鍵影格序列，會檢查端點與時間順序是否合法。

```python
motion = (
    a.animate.position.to(Vec2(5, 5), duration=1.0)
    .then(b.animate.opacity.to(1.0, duration=0.5))
    .with_(c.animate.size.to(9, duration=0.5), offset=1.0)
    .mark("settled")
)
```

`then` 在前一段結束時開始下一段。`with_` 則在前一段內部的某個偏移時間開始。兩者的總長度見[時間與緩動](time-easing.md#sec-kinetic-time)。

## 場景之間的轉場

<!-- api: kinetickit.guides_scenes_motion_19 -->

為兩個場景建立動作。編號相同的節點會配成一對，並對相容的屬性做插補。

<!-- api: kinetickit.guides_scenes_motion_20 -->

決定沒有對象或結構不相容的節點要如何進場、退場、交叉淡化或報錯。

路徑、網格與曲面都有專用的變形工具。自動正規化推不出你要的拓撲時，請明確提供對應方式（參見[變形](morphing.md#sec-kinetic-morphing)）。
