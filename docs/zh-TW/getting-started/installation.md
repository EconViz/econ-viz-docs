---
seo_title: "安裝"
description: "用 uv 安裝 econ-viz Python 套件，包含 GIF 動畫與 Jupyter 筆記本互動元件的選用功能。"
---

# 安裝

## 系統需求

建立專案前請先安裝以下工具：

- [Python](https://www.python.org/downloads/) 3.10 以上
- [uv](https://docs.astral.sh/uv/)

## 安裝 uv

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

亦可透過套件管理工具安裝：

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

## 安裝套件

建立專案並將 `econ-viz` 加入依賴：

```bash
uv init my-diagrams
cd my-diagrams
uv add econ-viz
```

透過 `uv run` 於專案環境中執行程式：

```bash
uv run python main.py
```

## 選用依賴

部分功能需要額外的套件，可依需求安裝對應的選用依賴：

```bash
uv add "econ-viz[animation]"    # GIF 匯出（Pillow）
uv add "econ-viz[interactive]"  # 筆記本互動元件
uv add "econ-viz[all]"          # 全部選用依賴
```

## 全域安裝命令列工具

若僅需命令列工具，可將其安裝為獨立工具，使 `econ-viz` 加入 `PATH`：

```bash
uv tool install econ-viz
```

## 開發環境設定

```bash
git clone https://github.com/EconViz/econ-viz.git
cd econ-viz
uv sync --all-extras
```

`uv sync` 預設會安裝 `dev` 依賴群組，`--all-extras` 則會一併安裝所有選用依賴。執行測試：

```bash
uv run pytest
```

## 驗證安裝

```bash
uv tree --package econ-viz --depth 0   # econ-viz v1.6.0
uv run econ-viz help
```
