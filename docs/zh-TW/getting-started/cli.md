---
seo_title: "命令列工具"
description: "用 econ-viz 命令列工具直接在終端機產生無異曲線與預算限制圖，不需要寫任何 Python。"
---

# 命令列工具

`econ-viz` 內建命令列工具，不寫 Python 也能產生圖形。

用 `uv tool install econ-viz` 把它裝成全域指令，或在 uv 專案中於每個指令前加上 `uv run`。詳見[安裝](installation.md)。

## 指令

| 指令 | 說明 |
|---------|-------------|
| `econ-viz help [<command>]` | 顯示命令列工具或特定指令的說明 |
| `econ-viz models` | 列出所有支援的效用模型 |
| `econ-viz plot ...` | 產生並匯出圖形 |
| `econ-viz solve-tex ...` | 以純 TeX 文字印出 Marshall 需求的封閉解 |

## 說明 {#econ-viz-help data-toc-label="說明"}

```bash
econ-viz help          # 所有指令
econ-viz help plot     # plot 選項
econ-viz help models   # models 選項
```

## 模型 {#econ-viz-models data-toc-label="模型"}

```bash
econ-viz models
```

印出所有模型名稱與對應參數。

## 繪圖 {#econ-viz-plot data-toc-label="繪圖"}

### 選擇模型

`--model` 和 `--latex` **擇一**提供，不能同時使用。

```bash
# 指定模型名稱
econ-viz plot --model cobb-douglas --alpha 0.5 --beta 0.5 ...

# LaTeX 算式
econ-viz plot --latex "x^{0.4} y^{0.6}" ...
```

### 範例

```bash
# Cobb-Douglas．可行集合陰影
econ-viz plot --model cobb-douglas --alpha 0.5 --beta 0.5 \
              --px 2 --py 3 --income 30 \
              --fill --output cobb_douglas.png

# LaTeX 輸入．Nord 主題．擴張路徑
econ-viz plot --latex "x^{0.4} y^{0.6}" \
              --px 2 --py 3 --income 30 \
              --theme nord --show-ray \
              --output cd_latex.png

# 完全互補．加大畫布
econ-viz plot --model leontief --a 1 --b 2 \
              --px 2 --py 3 --income 30 \
              --x-max 20 --y-max 15 \
              --output leontief.png

# CES．只畫無異曲線
econ-viz plot --model ces --rho -0.5 \
              --x-max 20 --y-max 15 --n-curves 6 \
              --no-budget --no-equilibrium \
              --output ces.png

# 飽和（極樂點）
econ-viz plot --model satiation --bliss-x 6 --bliss-y 4 \
              --x-max 12 --y-max 10 \
              --no-budget --no-equilibrium \
              --output satiation.png

# 不加 --output：開啟視窗
econ-viz plot --model cobb-douglas --px 2 --py 3 --income 30
```

### 所有選項

| 旗標 | 預設值 | 說明 |
|------|---------|-------------|
| `--model`, `-m` | — | 模型名稱：`cobb-douglas`、`leontief`、`perfect-substitutes`、`ces`、`satiation` |
| `--latex`, `-l` | — | LaTeX 算式（Cobb-Douglas / 完全互補 / 完全替代） |
| `--px` | — | 商品 x 的價格 |
| `--py` | — | 商品 y 的價格 |
| `--income` | — | 消費者所得 |
| `--alpha` | 0.5 | Alpha 參數（Cobb-Douglas / CES） |
| `--beta` | 0.5 | Beta 參數（Cobb-Douglas / CES） |
| `--a` | 1.0 | a 參數（完全互補 / 完全替代 / 飽和） |
| `--b` | 1.0 | b 參數（完全互補 / 完全替代 / 飽和） |
| `--rho` | 0.5 | 替代參數（CES） |
| `--bliss-x` | 5.0 | 飽和點的 x 座標（飽和） |
| `--bliss-y` | 5.0 | 飽和點的 y 座標（飽和） |
| `--x-max` | 10 | 橫軸上限 |
| `--y-max` | 10 | 縱軸上限 |
| `--x-label` | `x` | 橫軸標籤 |
| `--y-label` | `y` | 縱軸標籤 |
| `--title` | — | 圖形標題 |
| `--theme` | `default` | 配色主題：`default`、`nord` |
| `--n-curves` | 5 | 無異曲線數量 |
| `--dpi` | 300 | 點陣輸出解析度 |
| `--fill` | 關閉 | 為預算線下方的可行集合加上陰影 |
| `--show-ray` | 關閉 | 畫出通過最適點的擴張路徑射線 |
| `--no-budget` | 關閉 | 不畫預算線 |
| `--no-equilibrium` | 關閉 | 不畫均衡點 |
| `--no-curves` | 關閉 | 不畫無異曲線 |
| `--output`, `-o` | — | 輸出檔案（`.png`、`.pdf`、`.svg`）；省略時會開啟互動視窗 |

## 需求公式 {#econ-viz-solve-tex data-toc-label="需求公式"}

只想取得 Marshall 需求的封閉解公式、不需要畫圖時，使用 `solve-tex`。

```bash
# 數值參數
econ-viz solve-tex --model cobb-douglas --alpha 0.4 --beta 0.6

# 符號參數
econ-viz solve-tex --model cobb-douglas --symbolic-params

# 自訂價格與所得符號
econ-viz solve-tex --model leontief --a 2 --b 3 \
                   --px-symbol p_1 --py-symbol p_2 --income-symbol M
```

目前支援封閉解的模型：

- `cobb-douglas`
- `leontief`
- `perfect-substitutes`
- Cobb-Douglas、完全互補與完全替代的 LaTeX 簡寫

輸出是純 TeX 文字，可以直接貼進 Markdown 數學式、LaTeX 文件或簡報工具。
