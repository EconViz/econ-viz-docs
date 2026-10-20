---
seo_title: "绘制"
---

# 绘制

<span id="sec-rendering"></span>

## 渲染器

<!-- api: agora.mosaickit.guides_rendering_1 -->

所有后端都必须实现的协议。渲染器接收不可变的场景与私有的渲染上下文（规格、主题、覆盖、调色板、缓存与绑定），并返回由 `save` 写出的结果。网格与动画另需 `render_grid` 与 `save_animation`；渲染器如果没有实现它们，会引发 `RenderError`。内置后端仍在演进，因此渲染计划与上下文维持私有。

<!-- api: agora.mosaickit.guides_rendering_2 -->

`register(renderer)` 以 `name` 注册后端；如果对象缺少 `name`、`render` 或 `save`，或名称已被使用，会引发 `RenderError`。`get(name)` 返回已注册的渲染器，或加载内置渲染器。唯一的内置渲染器是 `"matplotlib"`，在第一次使用时才导入 [Hunter (2007)](../project/references.md#hunter2007)。

## Matplotlib 渲染器

绘制画布时先创建渲染计划：绑定场景（有自由参数时引发 `BindingError`）、展开群组、按 `z_index` 排序图层、解析每个图层的样式（参见[解析顺序](themes.md#thm-resolution)），并把调色板名称换成颜色。图形采用画布的尺寸与 DPI，背景为 `canvas` 角色的填色，坐标轴设为规格的范围并关闭 Matplotlib 自身的轴线；`mosaickit` 中的坐标轴是图层。

接下来由各图层类型的构建函数依次绘制图层。需要参考其他所有内容的图层类型（图例、点标签、区域标签、边栏文字、跨距大括号）会在后续的延后处理阶段绘制；各阶段按注册顺序运行，并一次接收该类型的所有图层。

<!-- api: agora.mosaickit.guides_rendering_3 -->

位于 `mosaickit.rendering.matplotlib`：不修改 `mosaickit` 就让渲染器识别新的图层类型。构建函数以 `builder(ax, resolved)` 调用并返回 Matplotlib artist；处理阶段以 `run(ax, layers, context)` 调用，`PassContext` 的 `handles` 把图层 id 对应到图例用的 artist。`resolved.layer` 是图层，`resolved.style` 是解析后的 `StyleBundle`。查询按方法解析顺序进行，子类因此继承父类的注册。图层以类变量 `style_slots` 声明每个槽的自带样式存于哪个字段，以 `fallback_category` 声明最后依据的角色。

区域标签的引线标注会避开坐标轴上的所有内容，包括第三方注册的构建函数所画的东西。

## 结果与保存

<!-- api: agora.mosaickit.guides_rendering_4 -->

结果的写出方式；`canvas.save(path, **options)` 把关键字参数传到这里。`transparent` 去除背景。`expand=True` 时，保存会把画布扩大到恰好容纳画到边缘外的内容（例如边栏文字），另加 4 pt 留白；它从不裁切，因此放得下的图维持 `CanvasSpec` 指定的尺寸。`expand=False` 保持指定尺寸。

```python
result = canvas.render()
try:
    # an interactive window
    result.show()
finally:
    result.close()
```

`render()` 返回 `MatplotlibResult`，提供 `figure`、`axes`、`show()`、`save(target, **options)` 与 `close()`。`canvas.save()` 会自行关闭暂时的结果。文件格式按扩展名决定：`.png`、`.pdf` 或 `.svg`（其他扩展名引发 `RenderError`）；动画接受 `.gif` 或 `.mp4`。网格中每格大小相同：宽为各画布宽度除以所跨列数的最大值，高为各画布高度除以所跨行数的最大值；DPI 取各画布中的最高者。

## 缓存

<!-- api: agora.mosaickit.guides_rendering_5 -->

有容量上限、线程安全的最近最少使用缓存，存放解析后的图层，以图层 id、绑定、模型、规格与样式为键。除非以 `cache=` 传入，每次绘制、网格或动画都创建自己的缓存，因此任务之间不会意外共用状态；要在多个任务间重用结果时，传入同一个缓存。无法哈希的模型不经缓存绘制，每种模型类型在每个缓存中只发出一次 `CacheBypassWarning`；模型请使用冻结的 dataclass。`clear()` 清空缓存。
