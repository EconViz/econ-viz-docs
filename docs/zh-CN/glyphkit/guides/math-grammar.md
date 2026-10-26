---
seo_title: "数学语法"
---

# 数学语法

<span id="sec-math-grammar"></span>

`parse_math()` 是有范围限制、类 TeX 的适配器，不是 TeX 的实作。它保留语意上的原文范围，绝不运行 TeX、宏、软件包或外部程序。在 Python 原代码里，请把算式写成原始字符串 `r"\frac{a}{b}"`，每个命令才会只有一个反斜线。

| 形式 | 示例 |
| --- | --- |
| 识别字、数字 | `U(x_1, x_2) = 2` |
| 群组与上下标 | `x_{i+1}^2` |
| 分数 | `\frac{a}{b}` |
| 根号 | `\sqrt{x}`、`\sqrt[n]{x}` |
| 带上下限的大型操作符 | `\sum_{i}^{n}`、`\prod`、`\bigcup`、`\lim`、`\max`、`\min`、`\sup`、`\inf` |
| 积分（上下标在侧边） | `\int_0^1`、`\iint`、`\iiint`、`\oint` |
| 函数名称（用直立体） | `\sin`、`\cos`、`\tan`、`\ln`、`\log`、`\exp`、`\det`、`\Pr` 等 |
| 直立文本 | `\mathrm{TR}`、`\text{if }x`、`\operatorname{rank}` |
| 二元操作符 | `+`、`-`、`\times`、`\cdot`、`\pm`、`\cup`、`\cap`、`\setminus` |
| 关系符号 | `=`、`<`、`>`、`\le`、`\ge`、`\ne`、`\approx`、`\equiv`、`\in`、`\subset`、`\to`、`\Rightarrow` |
| 其他符号 | `\infty`、`\partial`、`\nabla`、`\forall`、`\exists`、`\ell`、`\ldots`、`\cdots` |
| 空白 | `\,`（3 mu）、`\:`（4）、`\;`（5）、`\!`（-3）、`\quad`、`\qquad` |
| 括号 | `\left( x \right)` |
| 重音符号 | `\hat{x}`、`\bar{x}`、`\vec{x}`、`\overline{x}`、`\underline{x}` |
| 希腊字母 | 整个字母表，`\alpha` 到 `\omega`、`\Gamma` 到 `\Omega`，另有 `\varepsilon`、`\vartheta`、`\varphi`、`\varrho`、`\varsigma` |
| 矩阵 | `\begin{matrix}a & b \\ c & d\end{matrix}` |

不认得的命令、格式错误的群组与不支持的环境，会抛出 `MathSyntaxError`。缺省输入上限是 100,000 个码位，嵌套 256 层，矩阵内容 10,000 个保存格，调用端可以设得更低。结构化排版需要明确指定一个有 OpenType `MATH` 表的字体。

```python
from glyphkit.math import parse_math

tree = parse_math(r"\frac{\partial U}{\partial x_1} = \lambda p_1")
```

## 算式如何排版

排版依循 TeX 的规则（附录 G），并使用字体 `MATH` 表里的常数。

- **样式。**算式从显示样式（display，`MathStyle.level`）开始。分数的分子与分母在显示样式用完整大小，在文本样式用上下标大小。上下标依整个算式大小的 `ScriptPercentScaleDown` 与 `ScriptScriptPercentScaleDown` 缩小。
- **分数**沿用字体的上移与下移量，以及与分数线的最小间距。
- **上下标**维持下标与上标之间，以及与基线之间的最小间距。
- **上下限。**显示样式里，大型操作符会放大（`DisplayOperatorMinHeight`）并对齐数学轴，上下限与它保持字体规定的最小间距；文本样式里，上下限是上下标。
- **间距。**原子分成一般、大型操作符、二元、关系、开括号、闭括号、标点与内部，依 TeX 的表加上薄、中、厚空白，非上下标样式中分别是 3、4、5 mu（1/18 em）。没有左操作数的二元操作符（例如 `(-x)` 的负号）视为一般符号。当作二元操作符的连字号，字体有 U+2212 时就用它来画。
- **伸缩。**根号与括号是把原本的字形放大到内容的高度，不使用字体的尺寸变体或字形组合，所以很大的符号笔画会比较粗。

`Symbol` 节点用 `role` 记录类别：`ordinary`、`identifier`、`binary`、`relation`、`open`、`close`、`punct`、`large-operator`、`integral`、`function` 与 `upright`。较早的 `operator` 角色仍可读取，并依字符当成关系符号或二元操作符。
