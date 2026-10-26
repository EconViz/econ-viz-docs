---
seo_title: "變更紀錄"
---

# 變更紀錄

<span id="sec-changelog"></span>

本文件涵蓋的 `glyphkit` 版本。

## 1.0.0b4（2026-10-22）

- 字型只解析一次並保留下來（最近用過的八個），不再每個字形輪廓、每次數學排版各解析一次。輪廓與排版結果完全相同。解析後的字型在鎖保護下共用，所以並行讀取仍然是確定的（參見[輪廓](../guides/outlines-embedding.md#sec-outlines-embedding)）。

## 1.0.0b3（2026-10-21）

- 數學排版依循 TeX 的規則與字型的 MATH 常數：分數、上下標、大型運算子與上下限、伸縮的根號與括號、重音符號，以及 `\overline` 與 `\underline` 的線（參見[數學語法](../guides/math-grammar.md#sec-math-grammar)）。
- 原子依 TeX 的表加上間距。沒有左運算元的二元運算子視為一般符號，字型有 U+2212 時，`-` 就用它來畫。
- `MathStyle.level` 除了 `"display"` 與 `"script"`，也接受 `"text"` 與 `"scriptscript"`。
- 新增更多命令：完整的希臘字母、符號與關係符號、函數名稱、`\mathrm`、`\text`、`\operatorname`、空白與積分。`Symbol.role` 為原子分類，並新增 `Space` 節點。

## 1.0.0b2（2026-10-13）

- `MathStyle` 接受 `script_scale` 與 `script_script_scale`，以及 `constants` 與 `letter_slant`（參見[文字排版與數學式](../guides/layout-math.md#sec-layout-math)）。

## 1.0.0b1（2026-10-12）

- 公開排版契約的第一個整合測試版：明確的字型來源、配對、後備與字型清單，Unicode 分段、支援雙向文字的字形處理、段落排版與輪廓、OpenType MATH 排版、會檢查權限的子集、有版本的序列化（參見[簡介](../guides/introduction.md#sec-intro)）。
