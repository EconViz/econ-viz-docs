---
seo_title: "命令列工具"
---

# 命令列工具

<span id="sec-cli"></span>

命令列工具可繪圖、批次處理及輸出需求公式。以 `uv tool install utility-viz` 安裝為獨立工具，或在 `uv` 專案中於指令前加上 `uv run`（詳見[安裝命令列工具](installation.md#sec-install-cli)）。由 `econ-viz` 相容套件安裝的 1.x 指令 `econ-viz` 在 2.x 仍可使用：它會發出棄用警告，再以相同參數執行 `utility-viz`（詳見[從 `econ-viz` 遷移](installation.md#sec-migrate)）。

| 指令 | 說明 |
| --- | --- |
| `utility-viz help [``command``]` | 顯示命令列工具或特定指令的說明 |
| `utility-viz models` | 列出所有支援的效用模型 |
| `utility-viz plot ...` | 產生並匯出圖形 |
| `utility-viz solve-tex ...` | 以 TeX 格式輸出 Marshall 需求的閉式解 |
| `utility-viz init [path]` | 建立 `econ-viz.toml` 設定範本 |

## 說明與模型

<!-- api: agora.utility_viz.getting_started_cli_1 -->

未指定參數時列出所有指令；指定指令名稱時顯示該指令的選項。

```bash
utility-viz help          # 所有指令
utility-viz help plot     # plot 選項
utility-viz help models   # models 選項
```

<!-- api: agora.utility_viz.getting_started_cli_2 -->

列出命令列介面支援的模型名稱與參數。`--model` 使用 kebab-case 名稱，與 Python 類別名稱不同（參見[命令列模型](cli.md#tab-models)）。參數選項詳見[繪圖](cli.md#sec-cli-plot)。

<span id="tab-models"></span>

| 模型 | `--model` 值 | 必要參數 | 選用參數 |
| --- | --- | --- | --- |
| Cobb-Douglas | `cobb-douglas` | `alpha`、`beta` | -- |
| CES | `ces` | `rho` | `alpha`、`beta` |
| 完全互補 | `leontief` | `a`、`b` | -- |
| 完全替代 | `perfect-substitutes` | `a`、`b` | -- |
| 飽和偏好 | `satiation` | `bliss-x`、`bliss-y` | `a`、`b` |
| 準線性 | `quasi-linear` | -- | `v-func`、`linear-in` |
| Stone-Geary | `stone-geary` | -- | `alpha`、`beta`、`bar-x`、`bar-y` |
| Translog | `translog` | -- | `alpha-0`、`alpha-x`、`alpha-y`、`beta-xx`、`beta-yy`、`beta-xy` |

## 繪圖

<span id="sec-cli-plot"></span>

<!-- api: agora.utility_viz.getting_started_cli_3 -->

使用 `--model` 指定模型，或使用 `--latex` 輸入效用函數，兩者擇一。指定 `--output` 時匯出檔案，省略時開啟互動視窗。

預算線與均衡點需要完整的價格與所得。`--no-budget`、`--no-equilibrium`、`--no-curves` 可分別省略對應圖層，且可併用（參見[圖層控制選項](cli.md#tab-plot-flags)）。

<span id="tab-plot-flags"></span>

| 情況 | 結果 |
| --- | --- |
| 提供完整 `--px`、`--py`、`--income` | 繪製預算線並求解均衡 |
| 省略任一價格或所得 | 僅繪製無異曲線，不畫預算線與均衡點 |
| 加上 `--no-equilibrium` | 略過求解與均衡標示，即使提供了價格與所得 |
| 加上 `--no-budget` | 隱藏預算線，即使提供了價格與所得 |
| `--no-curves` 搭配完整價格與所得 | 只呈現預算線與均衡點，不畫無異曲線 |

```bash
# 指定模型名稱
utility-viz plot --model cobb-douglas --alpha 0.5 --beta 0.5 ...

# LaTeX 算式
utility-viz plot --latex "x^{0.4} y^{0.6}" ...
```

```bash
# Cobb-Douglas 並為可行集合加陰影
utility-viz plot --model cobb-douglas --alpha 0.5 --beta 0.5 \
              --px 2 --py 3 --income 30 \
              --fill --output cobb_douglas.png

# 用 LaTeX 與 Nord 主題畫擴張路徑
utility-viz plot --latex "x^{0.4} y^{0.6}" \
              --px 2 --py 3 --income 30 \
              --theme nord --show-ray \
              --output cd_latex.png

# 完全互補並放大畫布
utility-viz plot --model leontief --a 1 --b 2 \
              --px 2 --py 3 --income 30 \
              --x-max 20 --y-max 15 \
              --output leontief.png

# CES 只畫無異曲線
utility-viz plot --model ces --rho -0.5 \
              --x-max 20 --y-max 15 --n-curves 6 \
              --no-budget --no-equilibrium \
              --output ces.png

# 飽和效用與極樂點
utility-viz plot --model satiation --bliss-x 6 --bliss-y 4 \
              --x-max 12 --y-max 10 \
              --no-budget --no-equilibrium \
              --output satiation.png

# 不加 --output 就開啟視窗
utility-viz plot --model cobb-douglas --px 2 --py 3 --income 30
```

### 選擇模型

### 價格與所得

### 模型參數

準線性、Stone-Geary 與 Translog 另有下列選項，可依模型使用：

```bash
utility-viz plot --model stone-geary --bar-x 2 --bar-y 2 \
              --px 2 --py 3 --income 30 \
              --x-max 20 --y-max 15 --output stone_geary.png
```

此例的最低消費支出為 $2 \times 2 + 3 \times 2 = 10$，所得 $30$ 高於此限制。若將所得改為 $10$ 或更低，求解會因不符合模型定義域而失敗。

### 畫布與圖層

批次產圖時，為每組參數指定不同檔名，並先建立輸出目錄。`--x-max` 與 `--y-max` 不會隨價格自動調整；軸截距或最適點超出範圍時，應同步增大畫布上限。

## 建立設定檔

<span id="sec-cli-init"></span>

<!-- api: agora.utility_viz.getting_started_cli_4 -->

建立含註解的 `econ-viz.toml` 範本：頂層為共用設定，utility-viz 自身的設定位於 `[utility]` 下。省略路徑時寫入目前目錄；檔案已存在時，必須使用 `--force` 才會覆寫。`--migrate` 則改為把 utility-viz 位於頂層的表格移到 `[utility]` 下，並保留註解：同一目錄有 `utility-viz.toml` 時，將其改寫為 `econ-viz.toml` 並保留舊檔；沒有時，則直接改寫舊格式的 `econ-viz.toml`。

```bash
utility-viz init
utility-viz init config/figures.toml
utility-viz init --migrate
utility-viz plot --config econ-viz.toml --model cobb-douglas \
              --px 2 --py 3 --income 30 --output figure.png
```

## 需求公式

<!-- api: agora.utility_viz.getting_started_cli_5 -->

以 TeX 格式輸出 Marshall 需求的閉式解，可用於支援 TeX 數學式的文件。

```bash
# 數值參數
utility-viz solve-tex --model cobb-douglas --alpha 0.4 --beta 0.6

# 符號參數
utility-viz solve-tex --model cobb-douglas --symbolic-params

# 自訂價格與所得符號
utility-viz solve-tex --model leontief --a 2 --b 3 \
                   --px-symbol p_1 --py-symbol p_2 --income-symbol M
```

支援 `cobb-douglas`、`leontief`、`perfect-substitutes` 及其 LaTeX 表示式。此指令只輸出公式文字，不產生圖檔。
