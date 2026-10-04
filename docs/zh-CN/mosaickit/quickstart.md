---
seo_title: "mosaickit 快速开始"
description: "用 mosaickit 图层组出图形并保存为 SVG，再把参数扫描排成网格。"
---

# 快速开始

以下输出都是以 mosaickit 0.5.1 实际运行代码的结果。

## 用图层组出图形

`Canvas` 负责存放图层。`quadrant_axes(10, 10)` 提供两条坐标轴，每调用一次 `add()` 就加入一个图层。

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

输出：

```text
Scene 6 layers
```

六个图层是两条坐标轴，加上你加入的四个。`canvas.snapshot()` 会返回不可变的 `Scene`，
不必渲染就能查看即将绘制的内容。

![保存的图形](../../assets/mosaickit/diagram.svg){ width="360" }

`save()` 根据扩展名决定格式：PNG、SVG 与 PDF 都由内置的 Matplotlib 渲染器处理。

## 把参数扫描排成网格

`Parameter` 可以代替坐标值。`CanvasGrid.sweep` 会对每个值各渲染一次同一份模板。

```python
from mosaickit import Canvas, CanvasGrid, Parameter, TextLayer, quadrant_axes

position = Parameter("position", value_type=float)
template = Canvas().extend(quadrant_axes(10, 10))
template.add(TextLayer((position, 5), "moving"))

values = position.values([1.0, 3.0, 5.0])
CanvasGrid.sweep(template, values, cols=3).save("sweep.svg")
print("wrote sweep.svg")
```

输出：

```text
wrote sweep.svg
```

`Animation.sweep(template, values, fps=2).save("sweep.gif")` 可以把同一份模板变成 GIF
（GIF 与 MP4 的需求请见[安装](installation.md)）。
