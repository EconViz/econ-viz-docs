---
seo_title: "安裝 bezierkit"
description: "用 pip 或 uv 安裝 bezierkit 0.5.0rc1 預先發行版，加裝選用的 CLI 與 Matplotlib 功能，並設定開發環境。"
---

# 安裝

## 系統需求

- [Python](https://www.python.org/downloads/) 3.10 以上

bezierkit 唯一必要的依賴是 `numpy`。

## 安裝套件

bezierkit 0.5.0rc1 是預先發行版，pip 與 uv 預設都會略過預先發行版。請加上 `--pre` 表示接受，或直接指定完整版本。

=== ":simple-pypi: pip"

    ```bash
    pip install --pre bezierkit
    # 或指定完整版本：
    pip install bezierkit==0.5.0rc1
    ```

=== ":simple-uv: uv"

    ```bash
    uv add --prerelease allow bezierkit
    # 或指定完整版本：
    uv add bezierkit==0.5.0rc1
    ```

## 選用額外功能

| 額外功能 | 加入內容 | 安裝指令 |
|---|---|---|
| `cli` | `bezierkit` 指令（typer 與 rich） | `pip install --pre "bezierkit[cli]"` |
| `matplotlib` | Matplotlib 路徑轉接器 | `pip install --pre "bezierkit[matplotlib]"` |

使用 uv 時，同樣寫成 `uv add --prerelease allow "bezierkit[cli]"`。

## 驗證安裝

```bash
python -c "import bezierkit; print(bezierkit.__version__)"
```

會印出 `0.5.0rc1`。安裝 `cli` 額外功能後，執行 `bezierkit --help` 可列出所有指令。

## 開發環境設定

```bash
git clone https://github.com/EconViz/bezierkit.git
cd bezierkit
uv sync --all-extras --dev
uv run pytest
```
