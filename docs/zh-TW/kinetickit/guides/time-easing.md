---
seo_title: "時間、緩動與動作組合"
---

# 時間、緩動與動作組合

<span id="sec-kinetic-time"></span>

## 把區段時間換成 0 到 1

屬性在區間 $[t_0, t_0 + D]$ 變化。KineticKit 先把時間換成 0 到 1 之間的進度

$$
u = \text{clamp}((t - t_0) / D, 0, 1),
$$

再計算緩動 $e(u)$，最後把進度 $e(u)$ 交給該屬性的插補器。

## 緩動函式族

`ease.linear` 是 $e(u) = u$。名稱裡的 `quad`、`cubic`、`quart`、`quint` 分別對應 $n = 2, 3, 4, 5$ 次方：

| 名稱 | 公式 |
| --- | --- |
| `in_*` | $u^n$ |
| `out_*` | $1-(1-u)^n$ |
| `in_out_*` | $u < \tfrac12$ 時為 $\tfrac12 (2u)^n$，否則為 $1 - \tfrac12 (2(1-u))^n$ |

正弦族是 `in_sine` $= 1-\cos(\pi u/2)$、`out_sine` $= \sin(\pi u/2)$ 與 `in_out_sine` $= \tfrac12 (1-\cos \pi u)$。指數族是 `in_expo` $= (2^{10u}-1)/1023$，`out_expo` 與 `in_out_expo` 用同樣的方式由它組出。每個函式都精確滿足 $e(0)=0$ 與 $e(1)=1$。字典 `ease.STANDARD` 把每個名稱對應到函式。

<!-- api: kinetickit.guides_time_easing_1 -->

緩動的命名空間：上面各族函式、用於 CSS 風格時間曲線的 `cubic_bezier(x1, y1, x2, y2)`，以及 `STANDARD`。會超越的曲線在區段中間可以離開 $[0,1]$，區段兩端仍然精確回傳屬性端值。

```python
from kinetickit import ease

print(ease.out_cubic(0.5))  # 0.875
spring = ease.cubic_bezier(0.34, 1.56, 0.64, 1)
print(round(spring(0.5), 4))  # 1.0874，超過終點值
```

<span id="fig-kinetic-motion"></span>

<figure class="ev-fig" markdown>

![六種緩動函式，各自在兩秒內把一個點從軌道一端移到另一端。最後一條曲線會超越終點。](../../../assets/kinetickit/motion/easing.svg){ .ev-figure-lg }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/kinetickit/motion/easing.py" download aria-label="下載生圖原始檔"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下載生圖原始檔</span></a></div>

<figcaption markdown>六種緩動函式，各自在兩秒內把一個點從軌道一端移到另一端。最後一條曲線會超越終點。</figcaption>

</figure>

## 三次 Bézier 時間曲線

控制點為 $(x_1,y_1)$ 與 $(x_2,y_2)$ 的三次 Bézier 時間曲線是

$$
B(t) = (1-t)^3(0,0) + 3(1-t)^2t(x_1,y_1) + 3(1-t) t^2(x_2,y_2) + t^3(1,1).
$$

給定時間 $u$ 時，先解出橫座標為 $u$ 的參數，再取縱座標。兩個 $x$ 控制點必須落在 $[0,1]$，因此 $x$ 單調、解是唯一的；$y$ 控制點則沒有限制，上圖最後一條軌道就是靠這點超越終點。

## 動作組合

`a.then(b, gap=g)` 的長度為 $D_a + g + D_b$；`a.with_(b, offset=o)` 為 $\max(D_a, o + D_b)$。重複會把長度乘上次數，反轉以 $D - t$ 取樣，裁切則把新區間映回子動作。這些操作在編譯之前，都只是在建立不可變的動作樹。

```python
forward = dot.animate.position.to(Vec2(9, 9), duration=1.0)
motion = forward.then(forward.reverse(), gap=0.4)  # D + 0.4 + D
```

上圖就是這樣組出來的：六段動作用 `with_` 同時進行，整段動作再接上它自己的 `reverse()`。

## 關鍵影格與標記

`Keyframes` 動作為單一屬性列出各時間的值。每個 `Keyframe` 可以帶著後面那個區間的緩動，`hold=True` 則讓值維持到下一個關鍵影格。`mark("名稱", at=0.0)` 可以替任何動作上的一個時刻命名，互動可以跳到那個時刻（參見[無障礙與互動](accessibility.md#sec-interaction)）。

```python
from kinetickit import Keyframe, Keyframes, Point2D, Vec2, ease

p = Point2D(id="p", position=Vec2(0, 0))
fade = Keyframes(
    p.ref("opacity"),
    (Keyframe(0.0, 0.0), Keyframe(1.0, 1.0, easing=ease.out_quad), Keyframe(2.0, 0.2)),
)
print(fade.duration)  # 2.0
```
