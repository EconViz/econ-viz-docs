---
seo_title: "移植动画代码"
---

# 移植动画代码

<span id="sec-migration"></span>

KineticKit 是全新而且独立的引擎。它不会导入 MosaicKit 或任何 `*-viz` 软件包，也没有兼容层。移植的意思，是通过一个小适配器，把你的对象描述成 KineticKit 节点。已移除的 MosaicKit 与 utility-viz 动画 API 不会被重新导出。

## 从参数扫描移植

MosaicKit 的 `Animation.sweep(canvas, values)` 会产生不可变的场景帧。把每个图层描绘成以图层编号为键的 KineticKit 节点，再交给 KineticKit 在帧之间插补。

1. 替每个来源图层指定稳定的编号。
2. 写一个描绘函数，把一个图层转成节点。
3. 用 `kinetickit.adapters.transition` 把相邻的帧转成转场，并用 `then()` 接起它们的动作。
4. 用 `Animation.save()` 导出。

```python
from kinetickit import Animation
from kinetickit.adapters import transition


def depict(layer):  # 只使用 MosaicKit 的公开字段
    ...  # PathLayer -> PathNode2D(id=layer.id, ...)，依此类推


frames = list(sweep.frames())
steps = [transition(a.layers, b.layers, depict, duration=1.0) for a, b in zip(frames, frames[1:])]
motion = steps[0].motion
for step in steps[1:]:
    motion = motion.then(step.motion)
animation = Animation(steps[0].scene, motion)
```

<!-- api: kinetickit.examples_transition -->

依编号配对两个状态的节点，返回把前者带到后者的场景与动作。

图层的编号在各帧之间必须保持不变。没有配对到的编号会淡入或淡出，结构改变则会交叉淡化，并把诊断消息放在 `Transition.diagnostics`。适配器应该放在使用端的软件包里，因为只有那里懂得领域对象。

## 从工厂式动画器移植

用描绘函数取代工厂，直接创建动画。

1. 用 `adapt(objects, depict)` 把每个领域对象转成节点。
2. 用 `node.animate.<属性>.to(...)` 或 `SceneTransition.between()` 表达变化。
3. 用 `animation.save(path)` 导出。文件路径、帧率、DPI 与替代方案都由导出器负责。

## 字体

把特定绘图端的字体路径，换成由调用端持有的 `FontSource` 与 `FontLibrary`，并通过 `GlyphKitTypography` 转换排版结果（参见[文本排版](guides/typography.md#sec-typography)）。不要让场景模型或选用的绘图端去寻找字体。

现有使用 `Text2D`、`TextAsset`、`GlyphShape`、`FontResource` 与排版协定的程序，契约不变。
