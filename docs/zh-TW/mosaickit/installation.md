---
seo_title: "安裝 mosaickit"
description: "用 pip 或 uv 安裝 mosaickit，了解 GIF 與 MP4 輸出的需求，並設定開發環境。"
---

# 安裝

## 系統需求

- [Python](https://www.python.org/downloads/) 3.10 以上（專案支援 3.10 至 3.13）

安裝 mosaickit 時會一併安裝 `numpy` 與 `matplotlib`，Python 3.10 另外會安裝 `tomli`。

## 安裝套件

=== ":simple-pypi: pip"

    ```bash
    pip install mosaickit
    ```

=== ":simple-uv: uv"

    ```bash
    uv add mosaickit
    ```

本頁對應 mosaickit 0.5.1。

## 動畫輸出

`Animation` 以 Pillow 輸出 GIF，而 Pillow 會隨 Matplotlib 一起安裝，所以正常安裝後就能輸出 GIF。
輸出 MP4 則需要 `PATH` 中有 `ffmpeg`。

## 驗證安裝

```bash
python -c "import mosaickit; print(mosaickit.__version__)"
```

本文件對應的版本會印出 `0.5.1`。

## 開發環境設定

```bash
git clone https://github.com/EconViz/mosaickit.git
cd mosaickit
uv sync --locked
uv run pytest
```
