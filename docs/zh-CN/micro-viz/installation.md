---
seo_title: "安装"
---

# 安装

<span id="sec-install"></span>

## 系统需求

`micro-viz` 需要 Python 3.10 以上版本 (Python 官方网站提供各操作系统的安装程序：[https://www.python.org/downloads/](https://www.python.org/downloads/))。唯一的运行时依赖是 `mosaickit`（1.0.0rc9 以上、2 以下），它通过 `matplotlib` 绘制图形。

## 安装 `uv`

本页的指令以 `uv` (`uv` 是 Astral 开发的 Python 软件包与项目管理工具，速度快且可一并管理 Python 版本；安装方式与完整说明见官方文档：[https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)) 为准。既有项目仍可使用 `pip`；软件包 API 不受管理工具影响。

### macOS、Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## 安装 `micro-viz`

`micro-viz` 尚未发布到 PyPI。从 GitHub 安装开发版：

```bash
uv init my-diagrams
cd my-diagrams
uv add "micro-viz @ git+https://github.com/EconViz/micro-viz"
```

使用 `pip` 时，运行 `python -m pip install "micro-viz @ git+https://github.com/EconViz/micro-viz"`。`mosaickit` 1.0.0rc9 是预发行版，在 1.0 正式版发布之前，`uv` 需加上 `--prerelease allow`（`pip` 则加 `--pre`）。

## 选用依赖

<span id="sec-extras"></span>

`micro-viz[animation]` 会加装 `kinetickit`，让图形随参数变化成为动画（参见 [动画](guides/animation.md#sec-animation)）。静态图不会引入它。

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

## 运行示例

<span id="sec-run-examples"></span>

`examples/scripts/` 中的脚本把 SVG 档写入 `examples/output/`。它们使用黑白的 `manual` 外观，需要 TeX Gyre Pagella 字体；找不到时，以 `--fonts-dir` 指定字体所在的目录。

```bash
uv run python examples/scripts/production.py
uv run python examples/scripts/production.py \
    --config examples/econ-viz.zh-TW.toml \
    --fonts-dir path/to/NotoSerifTC
```

本页的图形就是由这些脚本绘制；[简介](guides/introduction.md#sec-intro) 链接的压缩包包含这些脚本与三份配置文件。
