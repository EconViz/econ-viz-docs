---
seo_title: "安装 Econ-Viz"
description: "用 uv 安装 econ-viz Python 包，包含 GIF 动画与 Jupyter 笔记本交互组件的可选功能。"
---

# 安装

## 系统需求

- Python 3.12 以上
- [uv](https://docs.astral.sh/uv/)

## 安装 uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows 或其他包管理工具的安装方式，请参阅 [uv 安装说明](https://docs.astral.sh/uv/getting-started/installation/)。

## 把 econ-viz 添加到项目

```bash
uv init my-diagrams
cd my-diagrams
uv add econ-viz
```

用 `uv run` 在项目环境中运行你的代码：

```bash
uv run python main.py
```

## 可选功能

只安装你需要的部分：

```bash
uv add "econ-viz[animation]"    # Pillow for GIF export
uv add "econ-viz[interactive]"  # ipywidgets + IPython for notebooks
uv add "econ-viz[all]"          # both extras
```

## 把命令行工具安装为全局命令

如果只需要命令行工具，可以把它安装为全局命令，在任何终端都能直接使用 `econ-viz`：

```bash
uv tool install econ-viz
```

## 开发环境安装

```bash
git clone https://github.com/EconViz/econ-viz.git
cd econ-viz
uv sync --all-extras
```

`uv sync` 默认会一起安装开发用的依赖包，`--all-extras` 则会加上笔记本与动画的可选工具。运行测试：

```bash
uv run pytest
```

## 确认安装

```bash
uv tree --package econ-viz --depth 0   # econ-viz v1.6.0
uv run econ-viz help
```
