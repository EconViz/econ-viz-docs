---
seo_title: "快速開始"
---

# 快速開始

<span id="sec-quickstart"></span>

一個點在視野中移動，同一段動畫寫成三種格式。

```python
from kinetickit import Animation, Bounds2D, Point2D, Scene2D, Vec2, ease

dot = Point2D(id="dot", position=Vec2(1, 1), size=8, color="#e4572e")
scene = Scene2D(dot)
scene = scene.bind({scene.camera.ref("view"): Bounds2D(Vec2(0, 0), Vec2(10, 10))})

motion = dot.animate.position.to(Vec2(9, 9), duration=1.5, easing=ease.out_cubic)
animation = Animation(scene, motion)

animation.save("dot.svg", width=400, height=400)  # 原生動態 SVG
animation.save("dot.gif", width=400, height=400, fps=30)  # 需要 kinetickit[raster]
animation.save("dot.html", width=400, height=440)  # 需要 kinetickit[interactive]
```

<span id="fig-kinetic-dot"></span>

<figure class="ev-fig" markdown>

![點用三次 ease-out 從 (1, 1) 移到 (9, 9)。](../../assets/kinetickit/quickstart/dot.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/kinetickit/quickstart/dot.py" download aria-label="下載生圖原始檔"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下載生圖原始檔</span></a></div>

<figcaption markdown>點用三次 ease-out 從 (1, 1) 移到 (9, 9)。</figcaption>

</figure>

<!-- api: kinetickit.quickstart_1 -->

把不可變場景與動作接在一起的門面。`frames()` 會逐張產生快照，`sample(t)` 回傳某個時間點的場景，`save()` 依目的檔的副檔名選擇匯出器。

<!-- api: kinetickit.quickstart_save -->

寫出動畫並回傳 `ExportManifest`。寫檔是原子操作：匯出失敗時不會留下半個檔案。

<!-- api: kinetickit.quickstart_2 -->

由 2D 節點與一個相機組成的不可變集合。`bind()` 會回傳設好相機視野的新場景，不會修改原來的場景。

<!-- api: kinetickit.quickstart_3 -->

一個圓形的 2D 標記，有穩定編號、位置、大小、顏色與透明度。這些屬性都能透過 `node.animate` 製作動畫。

<!-- api: kinetickit.quickstart_4 -->

與座標軸平行的矩形，用於相機視野、裁切、版面與範圍。

<!-- api: kinetickit.quickstart_5 -->

不可變的二維向量，用來表示位置、方向與大小。

<!-- api: kinetickit.quickstart_6 -->

緩動函式的命名空間。[時間與緩動](guides/time-easing.md#sec-kinetic-time)列出所有函式。

## 讀出某個時間的場景

場景加上時間，一定得到相同的狀態，所以不必播放動畫，就能問任何一個時刻的樣子。

```python
print(animation.duration)  # 1.5
print(animation.sample(0.0).get("dot").position)  # Vec2(x=1.0, y=1.0)
print(animation.sample(0.75).get("dot").position)  # Vec2(x=8.0, y=8.0)
print(animation.sample(1.5).get("dot").position)  # Vec2(x=9.0, y=9.0)
```

0.75 秒時進度是 0.5，三次 ease-out 走完 $1 - (1 - 0.5)^3 = 0.875$，所以點在 $1 + 8 \times 0.875 = 8$。

## 組合動作

動作是一個值。用 `then`、`with_`、`delay`、`repeat`、`yoyo`、`reverse` 與 `trim` 把動作組合起來，並用 `mark` 替某個時刻命名。

```python
from kinetickit import Animation, Bounds2D, Point2D, Scene2D, Vec2

a = Point2D(id="a", position=Vec2(0, 0), size=8)
b = Point2D(id="b", position=Vec2(0, 5), size=8, opacity=0.0)
c = Point2D(id="c", position=Vec2(5, 5), size=4)
scene = Scene2D(a, b, c)
scene = scene.bind({scene.camera.ref("view"): Bounds2D(Vec2(-1, -1), Vec2(11, 11))})

motion = (
    a.animate.position.to(Vec2(5, 5), duration=1.0)
    .then(b.animate.opacity.to(1.0, duration=0.5).with_(c.animate.size.to(9, duration=0.5)))
    .mark("settled")
)
print(Animation(scene, motion).duration)  # 1.5
```

GIF 與 HTML 那兩行需要對應的額外安裝項。能力檢查會在開啟目的檔之前執行，所以不支援的組合會拋出 `CapabilityError`，而且不會留下半個檔案（參見[輸出格式](guides/outputs.md#sec-outputs)）。
