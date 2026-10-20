---
seo_title: "画布与场景"
---

# 画布与场景

<span id="sec-canvas"></span>

## 画布规格

<!-- api: agora.mosaickit.guides_canvas_1 -->

图形的物理尺寸与坐标范围。`x_range` 与 `y_range` 是显示的数据范围；`width` 与 `height` 是以英寸计算的图形尺寸；`dpi` 是 $[1, 1200]$ 内的整数。属性 `x_min`、`x_max`、`y_min`、`y_max` 可读取范围，`replace(**changes)` 则返回只修改指定字段的副本。范围必须有限且 `lo < hi`，尺寸必须是有限正数，否则会引发 `ConfigurationError`。

<!-- api: agora.mosaickit.guides_canvas_2 -->

有限的递增区间，`lo < hi`，供规格与坐标轴共用。

## 画布

<!-- api: agora.mosaickit.guides_canvas_3 -->

封装不可变场景的流式构建器。如果参数为 `None`，便采用创建画布当下生效的配置（详见[配置](themes.md#sec-config)），分别是其中的 `canvas_spec`、`theme` 与 `renderer`。`role_overrides` 将角色名称映射到 `StyleBundle`，并应用在主题与配置之上（参见[解析顺序](themes.md#thm-resolution)）。

构造方法会修改画布，但不会就地改动场景：每次调用都以新场景取代画布中的场景，因此先前获取的快照、副本或绑定后的画布都会维持原有内容。

```python
from mosaickit import Canvas, PathLayer

canvas = Canvas()
before = canvas.snapshot()
canvas.add(PathLayer([(0, 0), (1, 1)], id="line"))
# the old snapshot is unchanged
assert before.layers == ()
assert canvas.snapshot().layers[0].id == "line"
```

## 场景

<!-- api: agora.mosaickit.guides_canvas_4 -->

具有持久性且有序的图层集合，也就是每次操作都会保留旧版本。`add()`、`extend()`、`remove()` 与 `clear()` 都会返回新场景；`Scene.empty()` 是空场景。图层 id 在整个场景（包括群组）中必须唯一，如有重复便引发 `ConfigurationError`。`ordered_layers` 按 `z_index` 排序顶层图层；值相同时维持加入顺序，而这个顺序就是绘制顺序。

## 错误与警告

| 类 | 引发或发出的时机 |
| --- | --- |
| `MosaicKitError` | 以下三个错误的基础类 |
| `ConfigurationError` | 模型、样式、主题、规格或配置值无效 |
| `BindingError` | 参数缺少值、类型错误，或表达式无法求值 |
| `RenderError` | 渲染器无法完成要求：未知的格式或渲染器、缺少的图例项目 |
| `LayoutWarning` | 自动布局无法避开所有障碍物（详见[区域标签与点标签](labels.md#sec-labels)） |
| `CacheBypassWarning` | 图层的模型无法哈希，因此不经缓存绘制 |
