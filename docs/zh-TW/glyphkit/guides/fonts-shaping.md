---
seo_title: "字型與字形處理"
---

# 字型與字形處理

<span id="sec-fonts-shaping"></span>

## 配對與後備字體

<!-- api: glyphkit.guides_fonts_shaping_1 -->

描述字型配對時偏好的字族、字重、字寬、斜體與可變字型座標。

<!-- api: glyphkit.guides_fonts_shaping_2 -->

記錄一次查詢的結果，包括選到的字型面與最後採用的可變字型座標。

<!-- api: glyphkit.guides_fonts_shaping_3 -->

一個可用字型面的快照，包含穩定識別、名稱、度量、字元涵蓋範圍與字型表。

```python
from glyphkit import FontLibrary, FontSource, Paragraph, TextSpan, TextStyle

library = FontLibrary.from_sources(
    (
        FontSource.path("fonts/SourceSans3-Regular.ttf"),
        FontSource.path("fonts/NotoSansTC-Regular.otf"),
    ),
    generic_families={"sans-serif": ("Source Sans 3", "Noto Sans TC")},
)
layout = library.layout(
    Paragraph((TextSpan("效用 U(x)", TextStyle(("sans-serif",), 18)),))
)
```

範例使用 Google Fonts 提供的開源字型 Source Sans 3 與 Noto Sans TC；數學式章節則使用採開放授權的 STIX Two Math。

字型識別來自字型內容的 SHA-256 摘要與字型集合索引，不看檔名。`FontManifest` 記錄重現排版所需的來源與字型。字形選取、定位與可變字型資料採用 OpenType 規格定義的結構 [{Microsoft} (2025)](../project/references.md#opentype2025)。

## Unicode 字形處理

<!-- api: glyphkit.guides_fonts_shaping_4 -->

字形處理時採用的書寫系統、方向、語言、OpenType 功能與間距選項。

<!-- api: glyphkit.guides_fonts_shaping_5 -->

共用同一字型面與處理條件的一段視覺順序字形，並保留原文範圍。

<!-- api: glyphkit.guides_fonts_shaping_6 -->

一個字形編號及其字元叢集、字幅、位移與字型面識別。

<!-- api: glyphkit.guides_fonts_shaping_7 -->

依明確的後備規則處理 Unicode 文字，回傳不綁定繪圖端的字形編號與位置。

左右方向混排時，即使視覺順序經過重排，原文範圍仍維持邏輯順序；這裡採用 Unicode 雙向演算法對邏輯順序與視覺順序的區分 [{Unicode Consortium} (2026)](../project/references.md#unicode-bidi2026)。找不到字形時會拋出 `MissingGlyphError`；GlyphKit 不會偷偷換成未設定的系統字體。

## 系統字體

<!-- api: glyphkit.guides_fonts_shaping_8 -->

主動搜尋作業系統已安裝的字型。需要可重現的建置時，請優先傳入明確的檔案或位元組，並保存字型清單。
