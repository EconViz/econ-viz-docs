---
seo_title: "匯出"
---

# 匯出

<span id="sec-export"></span>

## 輸出格式

<!-- api: agora.utility_viz.guides_export_1 -->

依 `path` 的副檔名決定輸出格式。`Figure`、`DemandDiagram` 與 `EdgeworthBox` 使用相同介面。

- PNG：點陣圖，解析度由畫布的 `dpi` 設定，預設為 300。
- PDF、SVG：向量圖，可在列印或縮放時保留線條品質。
- TeX：TikZ 原始碼（`.tex`），可嵌入 LaTeX 文件。透過關鍵字參數 `tikz_scale` 與 `tikz_standalone` 調整輸出。

```python
# PNG 依畫布 DPI 預設 300
cvs.save("figure.png")
# PDF 向量
cvs.save("figure.pdf")
# SVG 向量
cvs.save("figure.svg")
# TikZ
cvs.save("figure.tex")
```

`dpi` 僅影響點陣圖。預覽時可降低解析度：

```python
# 降低 DPI 加快預覽
cvs = Canvas(x_max=20, y_max=15, dpi=150)
```

## GIF 動畫

使用 `Animator.save()` 匯出 GIF，完整範例詳見[動畫](animation.md#sec-animation)。

```python
from utility_viz.core.animation import Animator

Animator(draw_frame, frames=frames).save(
    "animation.gif", fps=12, dpi=120
)
```

## 互動視窗

`cvs.show()` 開啟 `matplotlib` 互動視窗，不會儲存檔案。命令列的 `plot` 省略 `--output` 時也會開啟視窗（詳見[繪圖](../getting-started/cli.md#sec-cli-plot)）：

```bash
utility-viz plot --model cobb-douglas --px 2 --py 3 --income 30
```
