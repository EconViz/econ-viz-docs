---
seo_title: "遷移指南"
description: "principle-econ 已更名為 principle-viz：有哪些變動、如何切換套件，以及從 principle-econ 0.1.0 升級時會遇到的行為變化。"
---

# 遷移指南

`principle-econ` 已更名為 **principle-viz**，與 `utility-viz` 一同加入 EconViz 家族。

!!! warning "沒有相容層"

    `principle-econ` 在 v0.1.0 之後不再更新，`principle-viz` 也沒有提供 `principle_econ` 相容套件。
    切換時請一併更新匯入與指令。

## 變動一覽

| | principle-econ | principle-viz |
|---|---|---|
| 發行套件 | `uv add principle-econ` | `uv add principle-viz` |
| 匯入 | `import principle_econ` | `import principle_viz` |
| 命令列 | `principle-econ` | `principle-viz` |

## 切換套件

```bash
uv remove principle-econ
uv add principle-viz
```

接著在程式碼與腳本中替換名稱：

- 所有匯入中的 `principle_econ` 改為 `principle_viz`。
- Shell 腳本與 CI 中的 `principle-econ` 改為 `principle-viz`。

!!! tip "模組結構不變"

    `core`、`policy`、`welfare`、`plot`、`api`、`cli` 等子套件名稱都沒有變，
    所以 `principle_econ.core.line` 現在是 `principle_viz.core.line`。

## 0.1.0 之後的行為變化

從 principle-econ 0.1.0 升級，也會一併帶來直到 v0.10.0 為止的圖形變更。

| 項目 | 變更 |
|---|---|
| 圖例 | `MarketFigure.finalize()` 預設不再加入圖例；要保留舊行為請傳入 `finalize(legend=True)` |
| 福利標籤 | 區域改用名稱（「消費者剩餘」「DWL」等），不再用 `A/B/C/D` 字母 |
| `LabeledRegion` | 以 `key`、`label`、`short_label` 取代 `letter` |
| 曲線名稱 | 直接標在曲線末端旁，不再只出現在圖例 |
| 相依套件 | 需要 `mosaickit>=0.5.1,<0.6.0`，會自動安裝 |

!!! note "計算結果不變"

    福利與均衡的計算結果相同，改變的只有繪圖與標註。

## 給貢獻者

專案已由 Poetry 改為 uv：`pyproject.toml` 採用 PEP 621 與 `uv_build`，`uv.lock` 取代 `poetry.lock`。
請依[安裝](installation.md)中的方式用 `uv sync` 建立環境。
