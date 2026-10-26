---
seo_title: "安裝"
---

# 安裝

<span id="sec-install"></span>

## 需求

`macro-viz` 需要 Python 3.10 或更新版本。執行時依賴 `mosaickit`（1.0.0rc10 以上、2 以下），它透過 `matplotlib` 繪圖；以及 `bezierkit`（1.1.1 以上、2 以下），它提供轉動記號的曲線幾何。

## 安裝套件

`macro-viz` 尚未發布到 PyPI。從 GitHub 安裝開發版：

```bash
uv add "macro-viz @ git+https://github.com/EconViz/macro-viz"
```

使用 `pip` 時，執行 `python -m pip install "macro-viz @ git+https://github.com/EconViz/macro-viz"`。`mosaickit` 1.0.0rc10 是預先發行版，在 1.0 正式版發布前，`uv` 需加 `--prerelease allow`（`pip` 加 `--pre`）。

<span id="sec-extras"></span>

## 選用依賴

`macro-viz[animation]` 會加入 `kinetickit` 及其 raster 選項，用來讓圖形隨參數變動（參見 [動畫](guides/animation.md#sec-animation)）。靜態圖形從不匯入它。

```bash
uv add "macro-viz[animation] @ git+https://github.com/EconViz/macro-viz"
```

## 字型

這些頁面的圖形以 TeX Gyre Pagella 排版文字與數學，中文則用思源宋體（Noto Serif TC 或 SC）。字型檔寫在 `econ-viz.toml` 的 `[font]` 與 `[fonts]` 表（參見 [設定](guides/settings.md#sec-settings)）；沒有字型檔時，圖形會退回預設的襯線字型。範例會在 TeX 發行版或環境變數 `MACRO_VIZ_FONT_DIR` 列出的資料夾中尋找 TeX Gyre 字型檔。

## 開發環境

```bash
git clone https://github.com/EconViz/macro-viz.git
cd macro-viz
uv sync --locked
uv run pytest
```
