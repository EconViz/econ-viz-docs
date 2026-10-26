---
seo_title: "无障碍与交互"
---

# 无障碍与交互

<span id="sec-accessibility"></span>

## 语意与减少动态

<!-- api: kinetickit.guides_accessibility_1 -->

每个节点的无障碍数据：角色、标签、说明、阅读顺序，以及标示纯装饰对象的旗标。

<!-- api: kinetickit.guides_accessibility_2 -->

整段动画的标题、说明、替代文本、语言与减少动态的处理方式。

<!-- api: kinetickit.guides_accessibility_3 -->

决定观看者要求减少动态时，用哪个静止画面取代自动播放：最后一格、第一格，或指定的某个时间。

`ReducedMotion` 对应网页平台的 `prefers-reduced-motion` 偏好设置 [{W3C} (2026)](../project/references.md#mediaqueries5)。它是作者设计的替代内容，不是自动降低帧率。观看者主动要求时，仍然可以播放。

```python
from kinetickit import AccessibilityInfo, ReducedMotion, Semantics

semantics = Semantics(role="graphics-symbol", label="Start", reading_order=1)
info = AccessibilityInfo(
    title="Reaching the goal",
    description="A dot travels to a target",
    long_description="A dot starts at the lower left and moves to the upper right.",
    reduced_motion=ReducedMotion("time", 1.0),
)
```

SVG 与 HTML 会保留标题、说明、稳定的对象编号与各节点的语意。HTML 另外提供可用键盘操作的控制项与依阅读顺序排列的对象清单。GIF 无法携带这些运行时的语意，所以要求 GIF 输出无障碍内容时，必须提供文本说明，并可返回代表性 PNG。

## 交互

<span id="sec-interaction"></span>

交互是数据。它指定某个节点上的事件，并指定要运行的动作。KineticKit 在写出任何文件之前，会拿场景的节点编号与标记逐一验证每个绑定。

<!-- api: kinetickit.guides_accessibility_4 -->

可携式的触发事件：`HOVER_ENTER`、`HOVER_LEAVE`、`CLICK`、`DBLCLICK`、`FOCUS`、`SELECT`、`DESELECT`、`CAMERA_CHANGE` 或 `PLAYBACK_END`。

<!-- api: kinetickit.guides_accessibility_5 -->

把一个事件接到只含数据的动作，并标明这个交互是否为必要。

<!-- api: kinetickit.guides_accessibility_6 -->

经过验证的绑定集合，加上 `PlayRange` 能播放的具名时间区间。

```python
from kinetickit.interaction import Binding, Event, InteractionSpec, PlayRange, Select, SetProperty

interactions = InteractionSpec(
    (
        Binding(Event.CLICK, (PlayRange("run"),), "a"),
        Binding(Event.CLICK, (Select(mode="toggle"), SetProperty(None, "opacity", 0.6)), "b"),
    ),
    {"run": (0.0, 2.0)},
)
```

<!-- api: kinetickit.examples_playrange -->

播放具名时间区间的动作。

<!-- api: kinetickit.examples_select -->

选取、取消选取或切换节点的动作。

<!-- api: kinetickit.examples_setproperty -->

设置节点属性（例如不透明度）的动作。

动作有 `Play`、`Pause`、`Seek`、`PlayRange`、`Select`、`SetProperty`、`Toggle`、`SetSpeed`、`Reverse` 与 `ResetCamera`。标了 `required=True` 的绑定，在所选格式无法运行时，会在输出之前就失败；选用的绑定则会被舍弃，并在输出清单的 `degraded` 列出。SVG 与 GIF 依政策舍弃交互，HTML 才会运行。

[交互示例](examples.md#sec-example-interactive)在一个两点场景上同时用到两半功能。
