---
seo_title: "安装"
---

# 安装

<span id="sec-install"></span>

## 系统需求

`micro-viz` 需要 Python 3.10 以上版本。唯一的运行期依赖是 `mosaickit`（1.0.0rc9 以上、2 以下），它通过 `matplotlib` 绘制图形。

## 安装套件

`micro-viz` 尚未上架 PyPI，请从 GitHub 安装开发版：

```bash
uv add "micro-viz @ git+https://github.com/EconViz/micro-viz"
```

使用 `pip` 时，运行 `python -m pip install "micro-viz @ git+https://github.com/EconViz/micro-viz"`。`mosaickit` 1.0.0rc9 是预先发行版，在 1.0 正式版发布前，`uv` 要加 `--prerelease allow`（`pip` 加 `--pre`）。

<span id="sec-extras"></span>

## 选用依赖

`micro-viz[animation]` 会加装 `kinetickit`，用来让图形随参数动起来（见[动画](guides/animation.md#sec-animation)）。静态图**不会**加载它。

```bash
uv add "micro-viz[animation] @ git+https://github.com/EconViz/micro-viz"
```

## 开发环境

```bash
git clone https://github.com/EconViz/micro-viz.git
cd micro-viz
uv sync --locked
uv run pytest
```

## 运行范例

`examples/scripts/` 的脚本会把 SVG 写进 `examples/output/`。范例使用黑白的 `manual` 外观，需要 TeX Gyre Pagella 字体；找不到时，用 `--fonts-dir` 指定字体文件夹。

```bash
uv run python examples/scripts/production.py
uv run python examples/scripts/production.py --config examples/econ-viz.zh-TW.toml \
    --fonts-dir path/to/NotoSerifTC
```
