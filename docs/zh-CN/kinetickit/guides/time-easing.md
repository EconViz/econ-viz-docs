---
seo_title: "时间、缓动与动作组合"
---

# 时间、缓动与动作组合

<span id="sec-kinetic-time"></span>

## 把区段时间换成 0 到 1

属性在区间 $[t_0, t_0 + D]$ 变化。KineticKit 先把时间换成 0 到 1 之间的进度

$$
u = \text{clamp}((t - t_0) / D, 0, 1),
$$

再计算缓动 $e(u)$，最后把进度 $e(u)$ 交给该属性的插值器。

## 缓动函数族

`ease.linear` 是 $e(u) = u$。名称里的 `quad`、`cubic`、`quart`、`quint` 分别对应 $n = 2, 3, 4, 5$ 次方：

| 名称 | 公式 |
| --- | --- |
| `in_*` | $u^n$ |
| `out_*` | $1-(1-u)^n$ |
| `in_out_*` | $u < \tfrac12$ 时为 $\tfrac12 (2u)^n$，否则为 $1 - \tfrac12 (2(1-u))^n$ |

正弦族是 `in_sine` $= 1-\cos(\pi u/2)$、`out_sine` $= \sin(\pi u/2)$ 与 `in_out_sine` $= \tfrac12 (1-\cos \pi u)$。指数族是 `in_expo` $= (2^{10u}-1)/1023$，`out_expo` 与 `in_out_expo` 用同样的方式由它组出。每个函数都精确满足 $e(0)=0$ 与 $e(1)=1$。字典 `ease.STANDARD` 把每个名称对应到函数。

<!-- api: kinetickit.guides_time_easing_1 -->

缓动的命名空间：上面各族函数、用于 CSS 风格时间曲线的 `cubic_bezier(x1, y1, x2, y2)`，以及 `STANDARD`。会超越的曲线在区段中间可以离开 $[0,1]$，区段两端仍然精确返回属性端值。

```python
from kinetickit import ease

print(ease.out_cubic(0.5))  # 0.875
spring = ease.cubic_bezier(0.34, 1.56, 0.64, 1)
print(round(spring(0.5), 4))  # 1.0874，超过终点值
```

<span id="fig-kinetic-motion"></span>

<figure class="ev-fig" markdown>

![六种缓动函数，各自在两秒内把一个点从轨道一端移到另一端。最后一条曲线会超越终点。](../../../assets/kinetickit/motion/easing.svg){ .ev-figure-lg }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/kinetickit/motion/easing.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>六种缓动函数，各自在两秒内把一个点从轨道一端移到另一端。最后一条曲线会超越终点。</figcaption>

</figure>

## 三次 Bézier 时间曲线

控制点为 $(x_1,y_1)$ 与 $(x_2,y_2)$ 的三次 Bézier 时间曲线是

$$
B(t) = (1-t)^3(0,0) + 3(1-t)^2t(x_1,y_1) + 3(1-t) t^2(x_2,y_2) + t^3(1,1).
$$

给定时间 $u$ 时，先解出横坐标为 $u$ 的参数，再取纵坐标。两个 $x$ 控制点必须落在 $[0,1]$，因此 $x$ 单调、解是唯一的；$y$ 控制点则没有限制，上图最后一条轨道就是靠这点超越终点。

## 动作组合

`a.then(b, gap=g)` 的长度为 $D_a + g + D_b$；`a.with_(b, offset=o)` 为 $\max(D_a, o + D_b)$。重复会把长度乘上次数，反转以 $D - t$ 采样，裁切则把新区间映回子动作。这些操作在编译之前，都只是在创建不可变的动作树。

```python
forward = dot.animate.position.to(Vec2(9, 9), duration=1.0)
motion = forward.then(forward.reverse(), gap=0.4)  # D + 0.4 + D
```

上图就是这样组出来的：六段动作用 `with_` 同时进行，整段动作再接上它自己的 `reverse()`。

## 关键帧与标记

`Keyframes` 动作为单一属性列出各时间的值。每个 `Keyframe` 可以带着后面那个区间的缓动，`hold=True` 则让值维持到下一个关键帧。`mark("名称", at=0.0)` 可以替任何动作上的一个时刻命名，交互可以跳到那个时刻（参见[无障碍与交互](accessibility.md#sec-interaction)）。

```python
from kinetickit import Keyframe, Keyframes, Point2D, Vec2, ease

p = Point2D(id="p", position=Vec2(0, 0))
fade = Keyframes(
    p.ref("opacity"),
    (Keyframe(0.0, 0.0), Keyframe(1.0, 1.0, easing=ease.out_quad), Keyframe(2.0, 0.2)),
)
print(fade.duration)  # 2.0
```
