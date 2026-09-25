---
seo_title: "安裝 Econ-Viz"
description: "用 uv 安裝 econ-viz Python 套件，包含 GIF 動畫與 Jupyter 筆記本互動元件的選用功能。"
---

# 安裝

## 系統需求

- Python 3.12 以上
- [uv](https://docs.astral.sh/uv/)

## 安裝 uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows 或其他套件管理工具的安裝方式，請見 [uv 安裝說明](https://docs.astral.sh/uv/getting-started/installation/)。

## 把 econ-viz 加進專案

```bash
uv init my-diagrams
cd my-diagrams
uv add econ-viz
```

用 `uv run` 在專案環境中執行你的程式：

```bash
uv run python main.py
```

## 選用功能

只安裝你需要的部分：

```bash
uv add "econ-viz[animation]"    # Pillow for GIF export
uv add "econ-viz[interactive]"  # ipywidgets + IPython for notebooks
uv add "econ-viz[all]"          # both extras
```

## 把命令列工具裝成全域指令

如果只需要命令列工具，可以把它裝成全域指令，在任何終端機都能直接使用 `econ-viz`：

```bash
uv tool install econ-viz
```

## 開發環境安裝

```bash
git clone https://github.com/EconViz/econ-viz.git
cd econ-viz
uv sync --all-extras
```

`uv sync` 預設會一起安裝開發用的依賴套件，`--all-extras` 則會加上筆記本與動畫的選用工具。執行測試：

```bash
uv run pytest
```

## 確認安裝

```bash
uv tree --package econ-viz --depth 0   # econ-viz v1.6.0
uv run econ-viz help
```
