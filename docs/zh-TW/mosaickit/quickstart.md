---
seo_title: "mosaickit 快速開始"
description: "用 mosaickit 圖層組出圖形並存成 SVG，再把參數掃描排成網格。"
---

# 快速開始

以下輸出都是以 mosaickit 0.5.1 實際執行程式碼的結果。

## 用圖層組出圖形

`Canvas` 負責存放圖層。`quadrant_axes(10, 10)` 提供兩條座標軸，每呼叫一次 `add()` 就加入一個圖層。

```python
from mosaickit import (
    Canvas,
    Fill,
    FillLayer,
    MarkerLayer,
    PathLayer,
    Stroke,
    TextLayer,
    quadrant_axes,
)

canvas = Canvas().extend(quadrant_axes(10, 10))
canvas.add(
    FillLayer(
        [(1, 1), (1, 7), (8, 1)],
        fill=Fill(color="#377EB8", opacity=0.12),
        z_index=-1,
    )
)
canvas.add(
    PathLayer(
        [(1, 8), (2, 5), (4, 3), (7, 1.5), (9, 1)],
        stroke=Stroke(color="#984EA3", width=2),
        id="curve",
    )
)
canvas.add(MarkerLayer([(4, 3)], id="point"))
canvas.add(TextLayer((4, 3), "A", offset=(8, 8)))
canvas.save("diagram.svg")

scene = canvas.snapshot()
print(type(scene).__name__, len(scene.layers), "layers")
```

輸出：

```text
Scene 6 layers
```

六個圖層是兩條座標軸，加上你加入的四個。`canvas.snapshot()` 會回傳不可變的 `Scene`，
不必渲染就能檢視即將繪出的內容。

![存下來的圖形](../../assets/mosaickit/diagram.svg){ width="360" }

`save()` 依副檔名決定格式：PNG、SVG 與 PDF 都由內建的 Matplotlib 渲染器處理。

## 把參數掃描排成網格

`Parameter` 可以代替座標值。`CanvasGrid.sweep` 會對每個值各渲染一次同一份範本。

```python
from mosaickit import Canvas, CanvasGrid, Parameter, TextLayer, quadrant_axes

position = Parameter("position", value_type=float)
template = Canvas().extend(quadrant_axes(10, 10))
template.add(TextLayer((position, 5), "moving"))

values = position.values([1.0, 3.0, 5.0])
CanvasGrid.sweep(template, values, cols=3).save("sweep.svg")
print("wrote sweep.svg")
```

輸出：

```text
wrote sweep.svg
```

`Animation.sweep(template, values, fps=2).save("sweep.gif")` 可以把同一份範本變成 GIF
（GIF 與 MP4 的需求請見[安裝](installation.md)）。
