---
seo_title: "变更纪录"
---

# 变更纪录

<span id="sec-changelog"></span>

本文档涵盖的 `glyphkit` 版本。

## 1.0.0b4（2026-10-22）

- 字体只解析一次并保留下来（最近用过的八个），不再每个字形轮廓、每次数学排版各解析一次。轮廓与排版结果完全相同。解析后的字体在锁保护下共用，所以并行读取仍然是确定的（参见[轮廓](../guides/outlines-embedding.md#sec-outlines-embedding)）。

## 1.0.0b3（2026-10-21）

- 数学排版依循 TeX 的规则与字体的 MATH 常数：分数、上下标、大型操作符与上下限、伸缩的根号与括号、重音符号，以及 `\overline` 与 `\underline` 的线（参见[数学语法](../guides/math-grammar.md#sec-math-grammar)）。
- 原子依 TeX 的表加上间距。没有左操作数的二元操作符视为一般符号，字体有 U+2212 时，`-` 就用它来画。
- `MathStyle.level` 除了 `"display"` 与 `"script"`，也接受 `"text"` 与 `"scriptscript"`。
- 添加更多命令：完整的希腊字母、符号与关系符号、函数名称、`\mathrm`、`\text`、`\operatorname`、空白与积分。`Symbol.role` 为原子分类，并添加 `Space` 节点。

## 1.0.0b2（2026-10-13）

- `MathStyle` 接受 `script_scale` 与 `script_script_scale`，以及 `constants` 与 `letter_slant`（参见[文本排版与数学式](../guides/layout-math.md#sec-layout-math)）。

## 1.0.0b1（2026-10-12）

- 公开排版契约的第一个集成测试版：明确的字体来源、配对、后备与字体清单，Unicode 分段、支持双向文本的字形处理、段落排版与轮廓、OpenType MATH 排版、会检查权限的子集、有版本的串行化（参见[简介](../guides/introduction.md#sec-intro)）。
