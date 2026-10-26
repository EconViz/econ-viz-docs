---
seo_title: "OpenType 數學排版"
---

# OpenType 數學排版

<span id="sec-glyph-math-model"></span>

## 語意方框樹

GlyphKit 先把一套小型的語意語言解析出來，再排成 `MathBox` 樹。樹把字形排版、子節點原點、範圍、基線與橫線彼此分開，所以繪圖端不必實作 TeX，也能重現 [以 OpenType MATH 度量與精確字形輪廓排出的 Cobb–Douglas 效用函數](layout-math.md#fig-glyph-math)。

節點的 `kind` 說明它是什麼：`text`（字形）、`sequence`（子節點並排）、`script`、`shifted`、`fraction`、`root`、`limits`、`operator`、`delimited`、`matrix`、`hat` 與 `overline`（重音符號與橫線）以及 `space`。子節點的 `origin` 是它相對於父節點的位置，使用排版單位、y 軸向上；`baseline` 與 `bounds` 則在節點自己的座標框裡。

```python
def walk(node, depth=0):
    print("  " * depth, node.kind, node.origin)
    for child in node.children:
        walk(child, depth + 1)


walk(box)
```

## 上下標縮放

設顯示大小為 $s$，`ScriptPercentScaleDown` 為 $r$ 百分比，上下標大小就是 $s_1 = s r / 100$。下一層以同樣的方式套用 `ScriptScriptPercentScaleDown`，兩者都以整個算式的大小為準。`MathStyle.script_scale` 與 `script_script_scale` 可以取代字型的值。

## 常數來自字型

位移、間距、橫線粗細與運算子大小都來自字型的 MATH 表，例如 `SuperscriptShiftUp`、`SubscriptShiftDown`、`AxisHeight`、`FractionRuleThickness`、`RadicalVerticalGap` 與 `DisplayOperatorMinHeight`。每種結構如何使用它們，見[數學語法](math-grammar.md#how-a-formula-is-set)。字型沒有提供的常數，會改用以點為單位的值，而且不會再縮放第二次。

## 樣式與常數的覆寫

<!-- api: glyphkit.guides_math_layout_model_1 -->

控制大小、字族、層級、字母的傾斜、上下標縮放比例的覆寫值，以及依名稱覆寫其他 OpenType 常數。覆寫值是 em 的比例，字型表裡的值則由字型單位換算。
