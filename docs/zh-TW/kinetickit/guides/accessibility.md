---
seo_title: "無障礙與互動"
---

# 無障礙與互動

<span id="sec-accessibility"></span>

## 語意與減少動態

<!-- api: kinetickit.guides_accessibility_1 -->

每個節點的無障礙資料：角色、標籤、說明、閱讀順序，以及標示純裝飾物件的旗標。

<!-- api: kinetickit.guides_accessibility_2 -->

整段動畫的標題、說明、替代文字、語言與減少動態的處理方式。

<!-- api: kinetickit.guides_accessibility_3 -->

決定觀看者要求減少動態時，用哪個靜止畫面取代自動播放：最後一格、第一格，或指定的某個時間。

`ReducedMotion` 對應網頁平台的 `prefers-reduced-motion` 偏好設定 [{W3C} (2026)](../project/references.md#mediaqueries5)。它是作者設計的替代內容，不是自動降低影格率。觀看者主動要求時，仍然可以播放。

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

SVG 與 HTML 會保留標題、說明、穩定的物件編號與各節點的語意。HTML 另外提供可用鍵盤操作的控制項與依閱讀順序排列的物件清單。GIF 無法攜帶這些執行時的語意，所以要求 GIF 輸出無障礙內容時，必須提供文字說明，並可回傳代表性 PNG。

## 互動

<span id="sec-interaction"></span>

互動是資料。它指定某個節點上的事件，並指定要執行的動作。KineticKit 在寫出任何檔案之前，會拿場景的節點編號與標記逐一驗證每個綁定。

<!-- api: kinetickit.guides_accessibility_4 -->

可攜式的觸發事件：`HOVER_ENTER`、`HOVER_LEAVE`、`CLICK`、`DBLCLICK`、`FOCUS`、`SELECT`、`DESELECT`、`CAMERA_CHANGE` 或 `PLAYBACK_END`。

<!-- api: kinetickit.guides_accessibility_5 -->

把一個事件接到只含資料的動作，並標明這個互動是否為必要。

<!-- api: kinetickit.guides_accessibility_6 -->

經過驗證的綁定集合，加上 `PlayRange` 能播放的具名時間區間。

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

播放具名時間區間的動作。

<!-- api: kinetickit.examples_select -->

選取、取消選取或切換節點的動作。

<!-- api: kinetickit.examples_setproperty -->

設定節點屬性（例如不透明度）的動作。

動作有 `Play`、`Pause`、`Seek`、`PlayRange`、`Select`、`SetProperty`、`Toggle`、`SetSpeed`、`Reverse` 與 `ResetCamera`。標了 `required=True` 的綁定，在所選格式無法執行時，會在輸出之前就失敗；選用的綁定則會被捨棄，並在輸出清單的 `degraded` 列出。SVG 與 GIF 依政策捨棄互動，HTML 才會執行。

[互動範例](examples.md#sec-example-interactive)在一個兩點場景上同時用到兩半功能。
