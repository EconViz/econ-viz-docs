---
seo_title: "輪廓、字型子集與可攜資料"
---

# 輪廓、字型子集與可攜資料

<span id="sec-outlines-embedding"></span>

## 字形幾何

```python
glyph = layout.lines[0].runs[0].glyphs[0]
outline = library.outline(glyph)
print(outline.units_per_em, outline.bounds, outline.commands[:3])
```

<!-- api: glyphkit.outlines_outline -->

回傳已定位字形的精確輪廓。輪廓使用字型單位，所以要乘上該字形組的 `size / outline.units_per_em`，再加上字形的位置。

<!-- api: glyphkit.guides_outlines_embedding_1 -->

精確的字形輪廓：依序排列的路徑命令、範圍與每 em 的單位數。

<!-- api: glyphkit.guides_outlines_embedding_2 -->

在字型空間的指定點開始一條新的輪廓線。

<!-- api: glyphkit.guides_outlines_embedding_3 -->

從目前的點畫一條直線到終點。

<!-- api: glyphkit.guides_outlines_embedding_4 -->

加入一段二次 Bézier 曲線，有一個控制點與一個終點。

<!-- api: glyphkit.guides_outlines_embedding_5 -->

加入一段三次 Bézier 曲線，有兩個控制點與一個終點。

<!-- api: glyphkit.guides_outlines_embedding_6 -->

把目前的輪廓線連回起點並封閉。

<!-- api: glyphkit.guides_outlines_embedding_7 -->

依你選的容許誤差（字型單位），把曲線命令近似成線段。

<!-- api: glyphkit.guides_outlines_embedding_8 -->

曲線展平後回傳的一串開放或封閉的點。

<span id="fig-glyph-outline"></span>

<figure class="ev-fig" markdown>

![一個字形的精確輪廓。方塊是曲線上的點，圓圈是控制點，虛線是控制多邊形。](../../../assets/glyphkit/outlines/glyph.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/glyphkit/outlines/glyph.py" download aria-label="下載生圖原始檔"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下載生圖原始檔</span></a></div>

<figcaption markdown>一個字形的精確輪廓。方塊是曲線上的點，圓圈是控制點，虛線是控制多邊形。</figcaption>

</figure>

## 會檢查權限的字型子集

<!-- api: glyphkit.outlines_subset -->

建立涵蓋某個排版結果的字型子集，並回傳位元組與中繼資料。它不會寫出標記或檔案。

<!-- api: glyphkit.guides_outlines_embedding_9 -->

宣告子集要用在哪裡，字型的權限才能針對那個用途來檢查。

<!-- api: glyphkit.guides_outlines_embedding_10 -->

選擇回傳字型的容器：SFNT（OpenType）或 WOFF2。

<!-- api: glyphkit.guides_outlines_embedding_11 -->

完整的子集化結果：可攜式字型、診斷訊息與中繼資料。

<!-- api: glyphkit.guides_outlines_embedding_12 -->

一份通過權限檢查的字型資料，含字族、子集標籤、字形編號、權限與位元組。

```python
from glyphkit.embedding import EmbeddingUse, FontContainer

bundle = library.subset(layout, embedding_use=EmbeddingUse.WEB, container=FontContainer.WOFF2)
```

WOFF2 需要 `portable` 額外安裝項。權限規則見[可重現性與字型安全](reproducibility.md#sec-font-safety)。

## 序列化

<!-- api: glyphkit.guides_outlines_embedding_13 -->

把支援的不可變公開值轉成有版本的純資料，可直接存成類 JSON 的格式。

<!-- api: glyphkit.guides_outlines_embedding_14 -->

驗證有版本的資料，並在設定的限制內重建公開值。
