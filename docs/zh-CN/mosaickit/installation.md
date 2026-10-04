---
seo_title: "安装 mosaickit"
description: "用 pip 或 uv 安装 mosaickit，了解 GIF 与 MP4 输出的需求，并设置开发环境。"
---

# 安装

## 环境要求

- [Python](https://www.python.org/downloads/) 3.10 以上（项目支持 3.10 至 3.13）

安装 mosaickit 时会一并安装 `numpy` 与 `matplotlib`，Python 3.10 还会安装 `tomli`。

## 安装软件包

=== ":simple-pypi: pip"

    ```bash
    pip install mosaickit
    ```

=== ":simple-uv: uv"

    ```bash
    uv add mosaickit
    ```

本页对应 mosaickit 0.5.1。

## 动画输出

`Animation` 以 Pillow 输出 GIF，而 Pillow 会随 Matplotlib 一起安装，所以正常安装后就能输出 GIF。
输出 MP4 则需要 `PATH` 中有 `ffmpeg`。

## 验证安装

```bash
python -c "import mosaickit; print(mosaickit.__version__)"
```

本文档对应的版本会打印出 `0.5.1`。

## 开发环境设置

```bash
git clone https://github.com/EconViz/mosaickit.git
cd mosaickit
uv sync --locked
uv run pytest
```
