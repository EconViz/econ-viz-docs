---
seo_title: "圖層與座標軸"
---

# 圖層與座標軸

<span id="sec-layers"></span>

## 共同欄位

<!-- api: agora.mosaickit.guides_layers_1 -->

所有圖層共用的不可變基礎類別。各種圖層在自身的位置引數之後，都接受以下僅限關鍵字使用的欄位。

座標可以是有限實數對（資料單位），也可以是參數運算式（詳見[參數、網格與動畫](parameters.md#sec-parameters)）。無效的幾何會在建立圖層時引發 `ConfigurationError`，而不是等到繪製時才報錯。

## 基本圖層

<span id="tab-layers"></span>

| 圖層 | 預設角色 | 繪製內容 |
| --- | --- | --- |
| `PathLayer(path, stroke)` | `primary` | 通過至少兩點的折線 |
| `FillLayer(boundary, fill, stroke)` | `region` | 至少三點的多邊形，含填色與外框 |
| `MarkerLayer(points, marker)` | `point` | 每個點上的標記，至少一點 |
| `TextLayer(position, text)` | `text` | 某點上的文字 |
| `ArrowLayer(start, end, stroke)` | `annotation` | 直線箭頭，可加標籤 |
| `LegendLayer(entries, style)` | `legend` | 有標籤圖層的圖例 |
| `GroupLayer(children)` | `primary` | 本身不畫任何東西，只將圖層分組 |

<!-- api: agora.mosaickit.guides_layers_2 -->

以直線段連接各點。若解析後的線條樣式設有 `arrow`，便會在 `START`、`END` 或 `BOTH` 端畫出與該端線段對齊的箭頭。`clip=False` 可讓線條以完整寬度越過繪圖區邊緣，座標軸預設組便採用此設定。

<!-- api: agora.mosaickit.guides_layers_3 -->

以 `fill` 填色、以 `stroke` 描邊的封閉多邊形。`RegionLabelLayer` 以它的 id 指稱它。

<!-- api: agora.mosaickit.guides_layers_4 -->

在每個點繪製一個標記。標記一律完整畫出：中心位於繪圖區邊緣的標記（例如座標軸上的點）不會被切半，中心落在繪圖區外的則會略過。

<!-- api: agora.mosaickit.guides_layers_5 -->

在 `position` 放置文字，並偏移 `offset` pt。`anchor` 指定文字框的哪一點要對準該位置：`center`、`left`、`right`、`top`、`bottom`、`top-left`、`top-right`、`bottom-left` 或 `bottom-right`。`math=True` 時，文字會以數學式排版（`"a_1"` 成為 $a_1$）。

<!-- api: agora.mosaickit.guides_layers_6 -->

從 `start` 指向 `end` 的直線箭頭。除非線條樣式指定其他 `ArrowStyle`，否則使用開放式箭頭；`label` 寫在中點。虛線、點線或點劃線只套用在箭身，箭頭維持實線。箭頭不受繪圖區裁切。

<!-- api: agora.mosaickit.guides_layers_7 -->

列出 `entries` 中各 id 所指定的圖層；`entries` 為空時，則列出所有帶有 `legend` 標籤的圖層。若 id 不存在或對應圖層沒有標籤，便會引發 `RenderError`。`LegendStyle(visible=False)` 可隱藏圖例。

<!-- api: agora.mosaickit.guides_layers_8 -->

由其他圖層組成的圖層。子圖層的繪製方式如同直接加入場景，但其 `z_index` 會再加上群組的值；隱藏群組也會隱藏其中所有子圖層。

## 座標軸

<!-- api: agora.mosaickit.guides_layers_9 -->

`build_axes` 將兩個座標軸規格轉成角色為 `axes` 的一般圖層。兩個規格都沒有 `arrow` 時，結果是圍住範圍的封閉框；否則，各軸會沿 $y = 0$ 或 $x = 0$ 畫成直線，並依指定的 `ArrowPlacement` 畫出實心三角箭頭。標題位於箭頭尖端之外 6 pt：x 軸標題在右側，y 軸標題在上方。

<!-- api: agora.mosaickit.guides_layers_10 -->

三種預設組依序為：從原點出發、遠端帶箭頭的兩軸；穿過原點、兩端帶箭頭的兩軸；以及不帶箭頭的外框。

每條座標軸都由 `PathLayer` 與 `TextLayer` 組成，因此可透過 `axes` 角色改變樣式、以 id（`axes.x`、`axes.y`、`axes.frame`、`axes.x.label`、`axes.y.label`）移除，或改用自行建立的圖層。
