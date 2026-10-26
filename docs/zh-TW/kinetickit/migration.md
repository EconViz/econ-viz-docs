---
seo_title: "移植動畫程式碼"
---

# 移植動畫程式碼

<span id="sec-migration"></span>

KineticKit 是全新而且獨立的引擎。它不會匯入 MosaicKit 或任何 `*-viz` 套件，也沒有相容層。移植的意思，是透過一個小轉接器，把你的物件描述成 KineticKit 節點。已移除的 MosaicKit 與 utility-viz 動畫 API 不會被重新匯出。

## 從參數掃描移植

MosaicKit 的 `Animation.sweep(canvas, values)` 會產生不可變的場景影格。把每個圖層描繪成以圖層編號為鍵的 KineticKit 節點，再交給 KineticKit 在影格之間插補。

1. 替每個來源圖層指定穩定的編號。
2. 寫一個描繪函式，把一個圖層轉成節點。
3. 用 `kinetickit.adapters.transition` 把相鄰的影格轉成轉場，並用 `then()` 接起它們的動作。
4. 用 `Animation.save()` 匯出。

```python
from kinetickit import Animation
from kinetickit.adapters import transition


def depict(layer):  # 只使用 MosaicKit 的公開欄位
    ...  # PathLayer -> PathNode2D(id=layer.id, ...)，依此類推


frames = list(sweep.frames())
steps = [transition(a.layers, b.layers, depict, duration=1.0) for a, b in zip(frames, frames[1:])]
motion = steps[0].motion
for step in steps[1:]:
    motion = motion.then(step.motion)
animation = Animation(steps[0].scene, motion)
```

<!-- api: kinetickit.examples_transition -->

依編號配對兩個狀態的節點，回傳把前者帶到後者的場景與動作。

圖層的編號在各影格之間必須保持不變。沒有配對到的編號會淡入或淡出，結構改變則會交叉淡化，並把診斷訊息放在 `Transition.diagnostics`。轉接器應該放在使用端的套件裡，因為只有那裡懂得領域物件。

## 從工廠式動畫器移植

用描繪函式取代工廠，直接建立動畫。

1. 用 `adapt(objects, depict)` 把每個領域物件轉成節點。
2. 用 `node.animate.<屬性>.to(...)` 或 `SceneTransition.between()` 表達變化。
3. 用 `animation.save(path)` 匯出。檔案路徑、影格率、DPI 與替代方案都由匯出器負責。

## 字型

把特定繪圖端的字型路徑，換成由呼叫端持有的 `FontSource` 與 `FontLibrary`，並透過 `GlyphKitTypography` 轉換排版結果（參見[文字排版](guides/typography.md#sec-typography)）。不要讓場景模型或選用的繪圖端去尋找字型。

現有使用 `Text2D`、`TextAsset`、`GlyphShape`、`FontResource` 與排版協定的程式，契約不變。
