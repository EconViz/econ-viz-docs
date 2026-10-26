---
seo_title: "OpenType 数学排版"
---

# OpenType 数学排版

<span id="sec-glyph-math-model"></span>

## 语义方框树

GlyphKit 先把一套小型的语义语言解析出来，再排成 `MathBox` 树。树把字形排版、子节点原点、范围、基线与横线彼此分开，所以绘图端不必实现 TeX，也能重现 [以 OpenType MATH 度量与精确字形轮廓排出的 Cobb–Douglas 效用函数](layout-math.md#fig-glyph-math)。

节点的 `kind` 说明它是什么：`text`（字形）、`sequence`（子节点并排）、`script`、`shifted`、`fraction`、`root`、`limits`、`operator`、`delimited`、`matrix`、`hat` 与 `overline`（重音符号与横线）以及 `space`。子节点的 `origin` 是它相对于父节点的位置，使用排版单位、y 轴向上；`baseline` 与 `bounds` 则在节点自己的坐标框里。

```python
def walk(node, depth=0):
    print("  " * depth, node.kind, node.origin)
    for child in node.children:
        walk(child, depth + 1)


walk(box)
```

## 上下标缩放

设显示大小为 $s$，`ScriptPercentScaleDown` 为 $r$ 百分比，上下标大小就是 $s_1 = s r / 100$。下一层以同样的方式套用 `ScriptScriptPercentScaleDown`，两者都以整个算式的大小为准。`MathStyle.script_scale` 与 `script_script_scale` 可以取代字体的值。

## 常数来自字体

位移、间距、横线粗细与操作符大小都来自字体的 MATH 表，例如 `SuperscriptShiftUp`、`SubscriptShiftDown`、`AxisHeight`、`FractionRuleThickness`、`RadicalVerticalGap` 与 `DisplayOperatorMinHeight`。每种结构如何使用它们，见[数学语法](math-grammar.md#how-a-formula-is-set)。字体没有提供的常数，会改用以点为单位的值，而且不会再缩放第二次。

## 样式与常数的覆写

<!-- api: glyphkit.guides_math_layout_model_1 -->

控制大小、字族、层级、字母的倾斜、上下标缩放比例的覆写值，以及依名称覆写其他 OpenType 常数。覆写值是 em 的比例，字体表里的值则由字体单位换算。
