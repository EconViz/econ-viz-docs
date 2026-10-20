---
seo_title: "畫布與場景"
---

# 畫布與場景

<span id="sec-canvas"></span>

## 畫布規格

<!-- api: agora.mosaickit.guides_canvas_1 -->

圖形的實體尺寸與座標範圍。`x_range` 與 `y_range` 是顯示的資料範圍；`width` 與 `height` 是以英寸計算的圖形尺寸；`dpi` 是 $[1, 1200]$ 內的整數。屬性 `x_min`、`x_max`、`y_min`、`y_max` 可讀取範圍，`replace(**changes)` 則回傳只修改指定欄位的副本。範圍必須有限且 `lo < hi`，尺寸必須是有限正數，否則會引發 `ConfigurationError`。

<!-- api: agora.mosaickit.guides_canvas_2 -->

有限的遞增區間，`lo < hi`，供規格與座標軸共用。

## 畫布

<!-- api: agora.mosaickit.guides_canvas_3 -->

封裝不可變場景的流暢建構器。若引數為 `None`，便採用建立畫布當下生效的設定（詳見[設定](themes.md#sec-config)），分別是其中的 `canvas_spec`、`theme` 與 `renderer`。`role_overrides` 將角色名稱對應至 `StyleBundle`，並套用在主題與設定之上（參見[解析順序](themes.md#thm-resolution)）。

建構方法會修改畫布，但不會就地改動場景：每次呼叫都以新場景取代畫布中的場景，因此先前取得的快照、副本或綁定後的畫布都會維持原有內容。

```python
from mosaickit import Canvas, PathLayer

canvas = Canvas()
before = canvas.snapshot()
canvas.add(PathLayer([(0, 0), (1, 1)], id="line"))
# the old snapshot is unchanged
assert before.layers == ()
assert canvas.snapshot().layers[0].id == "line"
```

## 場景

<!-- api: agora.mosaickit.guides_canvas_4 -->

具持久性且有序的圖層集合，也就是每次操作都會保留舊版本。`add()`、`extend()`、`remove()` 與 `clear()` 都會回傳新場景；`Scene.empty()` 是空場景。圖層 id 在整個場景（包括群組）中必須唯一，若有重複便引發 `ConfigurationError`。`ordered_layers` 依 `z_index` 排序頂層圖層；值相同時維持加入順序，而這個順序就是繪製順序。

## 錯誤與警告

| 類別 | 引發或發出的時機 |
| --- | --- |
| `MosaicKitError` | 以下三個錯誤的基礎類別 |
| `ConfigurationError` | 模型、樣式、主題、規格或設定值無效 |
| `BindingError` | 參數缺少值、型別錯誤，或運算式無法求值 |
| `RenderError` | 繪製器無法完成要求：未知的格式或繪製器、缺少的圖例項目 |
| `LayoutWarning` | 自動配置無法避開所有障礙物（詳見[區域標籤與點標籤](labels.md#sec-labels)） |
| `CacheBypassWarning` | 圖層的模型無法雜湊，因此不經快取繪製 |
