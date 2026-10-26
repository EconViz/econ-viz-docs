---
seo_title: "文字排版"
---

# 文字排版

<span id="sec-typography"></span>

KineticKit 場景裡的文字是中性的 `TextAsset`：已定位的字形路徑、度量與選用的字型資料。KineticKit 自己沒有字型載入器。排版交給隨它一起安裝的 GlyphKit，用你提供的字型完成。

## 接上 GlyphKit

```python
from glyphkit import FontLibrary, FontSource
from kinetickit import Animation, Bounds2D, Scene2D, Text2D, Vec2
from kinetickit.integrations.glyphkit import GlyphKitTypography

library = FontLibrary.from_sources((FontSource.path("fonts/SourceSans3-Regular.ttf"),))
typography = GlyphKitTypography(library, families=(library.faces[0].family,), size=48)

title = Text2D(
    id="title",
    asset=typography.asset("Marginal utility"),
    position=Vec2(0.4, 0.6),
    scale=0.022,
    color="#000000",
)
scene = Scene2D(title)
scene = scene.bind({scene.camera.ref("view"): Bounds2D(Vec2(0, 0), Vec2(10, 4))})
motion = title.animate.position.to(Vec2(1.4, 2.8), duration=1.5)
Animation(scene, motion).save("text.svg", width=480, height=192)
```

<span id="fig-kinetic-type"></span>

<figure class="ev-fig" markdown>

![呼叫端提供的字型經 GlyphKit 取得輪廓，再由 KineticKit 移動。](../../../assets/kinetickit/typography/text.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/kinetickit/typography/text.py" download aria-label="下載生圖原始檔"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下載生圖原始檔</span></a></div>

<figcaption markdown>呼叫端提供的字型經 GlyphKit 取得輪廓，再由 KineticKit 移動。</figcaption>

</figure>

<!-- api: kinetickit.guides_typography_1 -->

設定好的轉接器。`asset(text)` 回傳 `TextAsset`，`layout(text)` 回傳 GlyphKit 的 `TextLayout`，`math(latex)` 回傳算式的素材。

<!-- api: kinetickit.guides_typography_2 -->

把你已經有的 GlyphKit `TextLayout` 轉成已定位的路徑、度量與選用的可攜式字型資料。

<!-- api: kinetickit.guides_typography_3 -->

把 GlyphKit 的數學排版結果（含字形與橫線）轉成文字素材。算式語法由 GlyphKit 定義（參見[數學語法](../../glyphkit/guides/math-grammar.md)）。

素材沿用 GlyphKit 的單位：y 軸向上，第一條基線在 `y = 0`，單位與 `size` 相同。這就是上面的 `Text2D` 要用很小的 `scale` 的原因：`size=48` 讓字形約 30 個單位高，而場景只有 10 個單位寬。

## 各種輸出怎麼處理文字

| 輸出 | 文字 |
| --- | --- |
| SVG | 字形路徑；`embed=True` 時另以 `@font-face` 嵌入通過權限檢查的字型子集 |
| HTML | 透過內嵌的 SVG |
| GIF | 畫進像素 |

只有在 GlyphKit 的權限檢查允許宣告的 `embedding_use`（預設是 `EmbeddingUse.WEB`）時，才會嵌入字型。受限的字型會被拒絕；權限不明的字型也會被拒絕，除非你傳入 `allow_unknown=True`，而這個決定會被記錄下來。

安裝 KineticKit 會一併安裝相容的 GlyphKit。KineticKit 核心的匯入保持延遲載入：只有 `kinetickit.integrations.glyphkit` 會匯入 GlyphKit，GlyphKit 也絕不匯入 KineticKit。需要文字的輔助線（例如座標軸）在沒有排版引擎時會拋出 `TypographyUnavailableError`，不會自己猜一個字型。
