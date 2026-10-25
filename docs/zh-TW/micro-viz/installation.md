---
seo_title: "安裝"
---

# 安裝

<span id="sec-install"></span>

## 系統需求

`micro-viz` 需要 Python 3.10 以上版本。唯一的執行期依賴是 `mosaickit`（1.0.0rc9 以上、2 以下），它透過 `matplotlib` 繪製圖形。

## 安裝套件

`micro-viz` 尚未上架 PyPI，請從 GitHub 安裝開發版：

```bash
uv add "micro-viz @ git+https://github.com/EconViz/micro-viz"
```

使用 `pip` 時，執行 `python -m pip install "micro-viz @ git+https://github.com/EconViz/micro-viz"`。`mosaickit` 1.0.0rc9 是預先發行版，在 1.0 正式版發布前，`uv` 要加 `--prerelease allow`（`pip` 加 `--pre`）。

<span id="sec-extras"></span>

## 選用依賴

`micro-viz[animation]` 會加裝 `kinetickit`，用來讓圖形隨參數動起來（見[動畫](guides/animation.md#sec-animation)）。靜態圖**不會**載入它。

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

`examples/scripts/` 的腳本會把 SVG 寫進 `examples/output/`。範例使用黑白的 `manual` 外觀，需要 TeX Gyre Pagella 字型；找不到時，用 `--fonts-dir` 指定字型資料夾。

```bash
uv run python examples/scripts/production.py
uv run python examples/scripts/production.py --config examples/econ-viz.zh-TW.toml \
    --fonts-dir path/to/NotoSerifTC
```
