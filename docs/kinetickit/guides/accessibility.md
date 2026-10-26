---
seo_title: "Accessibility and interaction"
---

# Accessibility and interaction

<span id="sec-accessibility"></span>

## Semantics and reduced motion

<!-- api: kinetickit.guides_accessibility_1 -->

Per-node accessibility metadata: role, label, description, reading order and a flag for decorative objects.

<!-- api: kinetickit.guides_accessibility_2 -->

Animation-level title, description, alternative texts, language and the reduced-motion policy.

<!-- api: kinetickit.guides_accessibility_3 -->

Chooses the representative still state that replaces autoplay when the viewer asks for reduced motion: the final state, the first state, or one explicit time.

`ReducedMotion` follows the web platform's `prefers-reduced-motion` preference [{W3C} (2026)](../project/references.md#mediaqueries5). It is an authored alternative, not an automatic reduction in frame rate. Playback is still available when the viewer asks for it.

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

SVG and HTML keep titles, descriptions, stable object ids and per-node semantics. HTML adds keyboard-operable controls and an ordered object list. A GIF cannot carry these runtime semantics, so asking for accessibility output on a GIF needs a text description and can return a representative PNG.

## Interaction

<span id="sec-interaction"></span>

An interaction is data. It names an event on a node, and it names actions to run. KineticKit validates every binding against the node ids and the markers of the scene before it writes anything.

<!-- api: kinetickit.guides_accessibility_4 -->

A portable trigger: `HOVER_ENTER`, `HOVER_LEAVE`, `CLICK`, `DBLCLICK`, `FOCUS`, `SELECT`, `DESELECT`, `CAMERA_CHANGE` or `PLAYBACK_END`.

<!-- api: kinetickit.guides_accessibility_5 -->

Connects one event to data-only actions, and says whether the interaction is required.

<!-- api: kinetickit.guides_accessibility_6 -->

The validated collection of bindings, plus the named time ranges that `PlayRange` can play.

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

Action that plays a named time range.

<!-- api: kinetickit.examples_select -->

Action that selects, deselects or toggles a node.

<!-- api: kinetickit.examples_setproperty -->

Action that sets a property of a node, such as its opacity.

The actions are `Play`, `Pause`, `Seek`, `PlayRange`, `Select`, `SetProperty`, `Toggle`, `SetSpeed`, `Reverse` and `ResetCamera`. A binding with `required=True` fails before output when the chosen format cannot run it. An optional binding is dropped, and the manifest lists it under `degraded`. SVG and GIF drop interactions by policy; HTML runs them.

[The interactive example](examples.md#sec-example-interactive) combines both halves on a two-point scene.
