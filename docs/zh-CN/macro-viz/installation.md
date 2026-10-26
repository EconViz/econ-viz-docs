---
seo_title: "安装"
---

# 安装

<span id="sec-install"></span>

## 需求

`macro-viz` 需要 Python 3.10 或更新版本。运行时依赖 `mosaickit`（1.0.0rc10 以上、2 以下），它通过 `matplotlib` 绘图；以及 `bezierkit`（1.1.1 以上、2 以下），它提供转动记号的曲线几何。

## 安装套件

`macro-viz` 尚未发布到 PyPI。从 GitHub 安装开发版：

```bash
uv add "macro-viz @ git+https://github.com/EconViz/macro-viz"
```

使用 `pip` 时，运行 `python -m pip install "macro-viz @ git+https://github.com/EconViz/macro-viz"`。`mosaickit` 1.0.0rc10 是预先发行版，在 1.0 正式版发布前，`uv` 需加 `--prerelease allow`（`pip` 加 `--pre`）。

<span id="sec-extras"></span>

## 选用依赖

`macro-viz[animation]` 会加入 `kinetickit` 及其 raster 选项，用来让图形随参数变动（参见 [动画](guides/animation.md#sec-animation)）。静态图形从不导入它。

```bash
uv add "macro-viz[animation] @ git+https://github.com/EconViz/macro-viz"
```

## 字体

这些页面的图形以 TeX Gyre Pagella 排版文本与数学，中文则用思源宋体（Noto Serif TC 或 SC）。字库写在 `econ-viz.toml` 的 `[font]` 与 `[fonts]` 表（参见 [设置](guides/settings.md#sec-settings)）；没有字库时，图形会退回缺省的衬线字体。范例会在 TeX 发行版或环境变量 `MACRO_VIZ_FONT_DIR` 列出的文件夹中寻找 TeX Gyre 字库。

## 开发环境

```bash
git clone https://github.com/EconViz/macro-viz.git
cd macro-viz
uv sync --locked
uv run pytest
```
