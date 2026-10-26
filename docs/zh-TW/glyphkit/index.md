---
seo_title: "與繪圖端無關的 Python 排版引擎"
description: "GlyphKit 使用明確指定的字型、處理 Unicode、排出段落與數學式、取出精確字形輪廓，並建立會檢查權限的字型子集，而且不自己繪圖。"
---

<h1 class="ev-visually-hidden">glyphkit：與繪圖端無關的 Python 排版引擎</h1>

<p align="center"><em>回傳不可變排版資料、自己不繪圖的 Python 排版引擎。</em></p>

<p align="center">
  <a href="https://github.com/EconViz/glyphkit"><img alt="GitHub" src="https://img.shields.io/badge/github-EconViz%2Fglyphkit-181818?style=flat-square&labelColor=f3f3f3"></a>
  <a href="https://pypi.org/project/glyphkit/"><img alt="PyPI" src="https://img.shields.io/pypi/v/glyphkit?include_prereleases&style=flat-square&label=pypi+package&color=181818&labelColor=f3f3f3&cacheSeconds=300"></a>
  <a href="https://pypi.org/project/glyphkit/"><img alt="Python" src="https://img.shields.io/pypi/pyversions/glyphkit?style=flat-square&color=181818&labelColor=f3f3f3"></a>
</p>

!!! warning "glyphkit 1.0 為測試版"

    glyphkit 1.0.0b4 是預發行版本。預發行版本之間的每項變更都記錄在[變更紀錄](project/changelog.md)。

```python
from glyphkit import FontLibrary, FontSource, Paragraph, TextSpan, TextStyle

library = FontLibrary.from_sources(
    (
        FontSource.path("fonts/SourceSans3-Regular.ttf"),
        FontSource.path("fonts/NotoSansTC-Regular.otf"),
    ),
    generic_families={"sans-serif": ("Source Sans 3", "Noto Sans TC")},
)

paragraph = Paragraph(
    (TextSpan("效用 U(x₁, x₂)", TextStyle(("sans-serif",), 18)),),
    max_width=360,
)
layout = library.layout(paragraph)
print(layout.logical_bounds)
```

## 功能

<div class="grid cards" markdown>

-   :material-format-font: **字型與字形處理**

    明確的字型來源、確定的配對、設定好的後備字型、Unicode 文字系統、雙向文字與 OpenType 字形處理。

    [:octicons-arrow-right-24: 字型與字形處理](guides/fonts-shaping.md)

-   :material-format-text: **段落排版**

    換行的段落，附邏輯範圍與墨跡範圍、基線、對齊與縮排，使用排版單位而非像素。

    [:octicons-arrow-right-24: 文字排版與數學式](guides/layout-math.md)

-   :material-sigma: **結構化數學式**

    明確定義的類 LaTeX 語法，依 TeX 的規則與字型 OpenType MATH 表的常數排版。

    [:octicons-arrow-right-24: 數學語法](guides/math-grammar.md)

-   :material-vector-curve: **精確的字形輪廓**

    以字型單位表示的移動、直線、二次、三次與封閉命令，並可依你選的容許誤差自適應展平。

    [:octicons-arrow-right-24: 輪廓與嵌入](guides/outlines-embedding.md)

-   :material-shield-lock-outline: **會檢查權限的字型子集**

    遵守字型嵌入權限的 SFNT 或 WOFF2 子集位元組，以及有版本的純資料序列化。

    [:octicons-arrow-right-24: 字型安全](guides/reproducibility.md)

-   :material-axis-arrow: **座標與度量**

    字型單位、縮放、字幅與墨跡的差別，以及對齊、裁切或做碰撞檢查時該用哪個方框。

    [:octicons-arrow-right-24: 座標與度量](guides/coordinate-metrics.md)

</div>

## 安裝

```bash
uv add --prerelease allow glyphkit
```

需要 Python 3.10 到 3.13。WOFF2 額外安裝項見[安裝](installation.md)。

## 範例

本文件的每張圖都附上生成它的腳本。可一次下載全部。

[下載全部範例](../assets/glyphkit/glyphkit-examples.zip){ .md-button download="" }
