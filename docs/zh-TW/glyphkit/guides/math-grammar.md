---
seo_title: "數學語法"
---

# 數學語法

<span id="sec-math-grammar"></span>

`parse_math()` 是有範圍限制、類 TeX 的轉接器，不是 TeX 的實作。它保留語意上的原文範圍，絕不執行 TeX、巨集、套件或外部程式。在 Python 原始碼裡，請把算式寫成原始字串 `r"\frac{a}{b}"`，每個命令才會只有一個反斜線。

| 形式 | 範例 |
| --- | --- |
| 識別字、數字 | `U(x_1, x_2) = 2` |
| 群組與上下標 | `x_{i+1}^2` |
| 分數 | `\frac{a}{b}` |
| 根號 | `\sqrt{x}`、`\sqrt[n]{x}` |
| 帶上下限的大型運算子 | `\sum_{i}^{n}`、`\prod`、`\bigcup`、`\lim`、`\max`、`\min`、`\sup`、`\inf` |
| 積分（上下標在側邊） | `\int_0^1`、`\iint`、`\iiint`、`\oint` |
| 函數名稱（用直立體） | `\sin`、`\cos`、`\tan`、`\ln`、`\log`、`\exp`、`\det`、`\Pr` 等 |
| 直立文字 | `\mathrm{TR}`、`\text{if }x`、`\operatorname{rank}` |
| 二元運算子 | `+`、`-`、`\times`、`\cdot`、`\pm`、`\cup`、`\cap`、`\setminus` |
| 關係符號 | `=`、`<`、`>`、`\le`、`\ge`、`\ne`、`\approx`、`\equiv`、`\in`、`\subset`、`\to`、`\Rightarrow` |
| 其他符號 | `\infty`、`\partial`、`\nabla`、`\forall`、`\exists`、`\ell`、`\ldots`、`\cdots` |
| 空白 | `\,`（3 mu）、`\:`（4）、`\;`（5）、`\!`（-3）、`\quad`、`\qquad` |
| 括號 | `\left( x \right)` |
| 重音符號 | `\hat{x}`、`\bar{x}`、`\vec{x}`、`\overline{x}`、`\underline{x}` |
| 希臘字母 | 整個字母表，`\alpha` 到 `\omega`、`\Gamma` 到 `\Omega`，另有 `\varepsilon`、`\vartheta`、`\varphi`、`\varrho`、`\varsigma` |
| 矩陣 | `\begin{matrix}a & b \\ c & d\end{matrix}` |

不認得的命令、格式錯誤的群組與不支援的環境，會拋出 `MathSyntaxError`。預設輸入上限是 100,000 個碼位，巢狀 256 層，矩陣內容 10,000 個儲存格，呼叫端可以設得更低。結構化排版需要明確指定一個有 OpenType `MATH` 表的字型。

```python
from glyphkit.math import parse_math

tree = parse_math(r"\frac{\partial U}{\partial x_1} = \lambda p_1")
```

<span id="how-a-formula-is-set"></span>

## 算式如何排版

排版依循 TeX 的規則（附錄 G），並使用字型 `MATH` 表裡的常數。

- **樣式。**算式從顯示樣式（display，`MathStyle.level`）開始。分數的分子與分母在顯示樣式用完整大小，在文字樣式用上下標大小。上下標依整個算式大小的 `ScriptPercentScaleDown` 與 `ScriptScriptPercentScaleDown` 縮小。
- **分數**沿用字型的上移與下移量，以及與分數線的最小間距。
- **上下標**維持下標與上標之間，以及與基線之間的最小間距。
- **上下限。**顯示樣式裡，大型運算子會放大（`DisplayOperatorMinHeight`）並對齊數學軸，上下限與它保持字型規定的最小間距；文字樣式裡，上下限是上下標。
- **間距。**原子分成一般、大型運算子、二元、關係、開括號、閉括號、標點與內部，依 TeX 的表加上薄、中、厚空白，非上下標樣式中分別是 3、4、5 mu（1/18 em）。沒有左運算元的二元運算子（例如 `(-x)` 的負號）視為一般符號。當作二元運算子的連字號，字型有 U+2212 時就用它來畫。
- **伸縮。**根號與括號是把原本的字形放大到內容的高度，不使用字型的尺寸變體或字形組合，所以很大的符號筆畫會比較粗。

`Symbol` 節點用 `role` 記錄類別：`ordinary`、`identifier`、`binary`、`relation`、`open`、`close`、`punct`、`large-operator`、`integral`、`function` 與 `upright`。較早的 `operator` 角色仍可讀取，並依字元當成關係符號或二元運算子。
