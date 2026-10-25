---
seo_title: "安裝"
---

# 安裝

<span id="sec-install"></span>

## 系統需求

`micro-viz` 需要 Python 3.10 以上版本 (Python 官方網站提供各作業系統的安裝程式：[https://www.python.org/downloads/](https://www.python.org/downloads/)。)。唯一的執行期依賴是 `mosaickit`（1.0.0rc9 以上、2 以下），它透過 `matplotlib` 繪製圖形。

## 安裝 `uv`

本手冊的指令以 `uv` (`uv` 是 Astral 開發的 Python 套件與專案管理工具，速度快且可一併管理 Python 版本；安裝方式與完整說明見官方文件：[https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)。) 為準。既有專案仍可使用 `pip`；套件 API 不受管理工具影響。

### macOS、Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## 安裝 `micro-viz`

`micro-viz` 尚未發布到 PyPI。從 GitHub 安裝開發版：

```bash
uv init my-diagrams
cd my-diagrams
uv add "micro-viz @ git+https://github.com/EconViz/micro-viz"
```

使用 `pip` 時，執行 `python -m pip install "micro-viz @ git+https://github.com/EconViz/micro-viz"`。`mosaickit` 1.0.0rc9 是預發行版，在 1.0 正式版發布之前，`uv` 需加上 `--prerelease allow`（`pip` 則加 `--pre`）。

## 選用依賴

<span id="sec-extras"></span>

`micro-viz[animation]` 會加裝 `kinetickit`，讓圖形隨參數變化成為動畫（參見 [動畫](guides/animation.md#sec-animation)）。靜態圖不會引入它。

```bash
uv add "micro-viz[animation] @ git+https://github.com/EconViz/micro-viz"
```

## 開發環境

```bash
git clone https://github.com/EconViz/micro-viz.git
cd micro-viz
uv sync --locked
uv run pytest
```

## 執行範例

<span id="sec-run-examples"></span>

`examples/scripts/` 中的腳本把 SVG 檔寫入 `examples/output/`。它們使用黑白的 `manual` 外觀，需要 TeX Gyre Pagella 字型；找不到時，以 `--fonts-dir` 指定字型檔所在的目錄。

```bash
uv run python examples/scripts/production.py
uv run python examples/scripts/production.py \
    --config examples/econ-viz.zh-TW.toml \
    --fonts-dir path/to/NotoSerifTC
```

本手冊的圖形就是由這些腳本繪製；[簡介](guides/introduction.md#sec-intro) 連結的壓縮檔包含這些腳本與三份設定檔。
