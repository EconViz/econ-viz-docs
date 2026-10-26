---
seo_title: "相容性"
---

# 相容性

<span id="sec-compatibility"></span>

## 支援的平台

- Python 3.10、3.11、3.12 與 3.13。
- 基本安裝包含 NumPy 與 GlyphKit。`raster` 與 `interactive` 是選用的額外安裝項，它們的第三方引擎屬於私有的實作細節。

## 穩定的介面（1.0）

| 介面 | 匯入路徑 |
| --- | --- |
| 時間軸、補間、關鍵影格、排程器 | `kinetickit.timeline`、`.tween`、`.keyframes`、`.scheduler`、`.easing`、`.interpolation` |
| 2D 與 3D 場景契約 | `kinetickit.scene`、`.geometry`、`.styles` |
| 變形與轉場 | `kinetickit.morph`、`.transitions` |
| 繪圖端與匯出器協定 | `kinetickit.renderers`（`Renderer`、`RendererCapabilities`、`register_renderer`）、`kinetickit.exporters`（`Destination`、`ExportManifest`、`register_exporter`） |
| 互動與無障礙 | `kinetickit.interaction`、`.accessibility` |
| 排版埠與文字素材 | `kinetickit.typography` |
| 一致性測試資料 | `kinetickit.conformance` |

公開套件 `__all__` 匯出的一切都是公開的。以底線開頭的名稱，以及名稱以底線開頭的模組（`_matplotlib`、`_plotly`、`_gif_stream`）裡的一切，都是私有的，隨時可能改變。視覺化的語意不在範圍內。

## 版本

KineticKit 從 1.0 起遵循語意化版本。預發行版本（`1.0.0bN`、`1.0.0rcN`）可能在版本之間改變公開契約，每項變更都會記錄在變更紀錄中。

## 棄用

1. 被棄用的公開名稱至少再維持一個次要版本。
2. 它會發出 `DeprecationWarning`，指出替代名稱與移除的版本。
3. 移除會記錄在變更紀錄中。
4. 被棄用的名稱只會在主要版本移除。

輸出格式遵守同樣的規則。會改變既有成品的變更（例如 SVG 的結構）會出現在變更紀錄中，並在同一次提交更新黃金檔案。
