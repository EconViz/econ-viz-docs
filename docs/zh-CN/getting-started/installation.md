---
seo_title: "安装"
description: "用 uv 安装 econ-viz Python 包，包含 GIF 动画与 Jupyter 笔记本交互组件的可选功能。"
---

# 安装

## 系统需求

创建项目前请先安装以下工具：

- [Python](https://www.python.org/downloads/) 3.10 以上
- [uv](https://docs.astral.sh/uv/)

## 安装 uv

=== ":fontawesome-brands-apple: macOS"

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

=== ":fontawesome-brands-linux: Linux"

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

=== ":fontawesome-brands-windows: Windows"

    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

也可通过包管理工具安装：

=== ":simple-homebrew: Homebrew"

    ```bash
    brew install uv
    ```

=== ":simple-macports: MacPorts"

    ```bash
    sudo port install uv
    ```

=== ":fontawesome-brands-windows: WinGet"

    ```powershell
    winget install --id=astral-sh.uv -e
    ```

=== ":material-bucket-outline: Scoop"

    ```powershell
    scoop install main/uv
    ```

=== ":simple-pipx: pipx"

    ```bash
    pipx install uv
    ```

=== ":simple-rust: Cargo"

    ```bash
    cargo install --locked uv
    ```

## 安装软件包

创建项目并将 `econ-viz` 添加为依赖：

```bash
uv init my-diagrams
cd my-diagrams
uv add econ-viz
```

通过 `uv run` 在项目环境中运行代码：

```bash
uv run python main.py
```

## 可选依赖

部分功能需要额外的包，可按需安装对应的可选依赖：

```bash
uv add "econ-viz[animation]"    # GIF 导出（Pillow）
uv add "econ-viz[interactive]"  # 笔记本交互组件
uv add "econ-viz[all]"          # 全部可选依赖
```

## 全局安装命令行工具

若仅需命令行工具，可将其安装为独立工具，使 `econ-viz` 加入 `PATH`：

```bash
uv tool install econ-viz
```

## 开发环境配置

```bash
git clone https://github.com/EconViz/econ-viz.git
cd econ-viz
uv sync --all-extras
```

`uv sync` 默认会安装 `dev` 依赖组，`--all-extras` 则会一并安装所有可选依赖。运行测试：

```bash
uv run pytest
```

## 验证安装

```bash
uv tree --package econ-viz --depth 0   # econ-viz v1.6.0
uv run econ-viz help
```
