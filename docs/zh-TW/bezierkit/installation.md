---
seo_title: "安裝"
---

# 安裝

<span id="sec-install"></span>

## 系統需求

`bezierkit` 需要 Python 3.10 以上版本與 `NumPy`。另有兩組選用依賴：

<!-- api: agora.bezierkit.installation_1 -->

## 安裝套件

```bash
uv add bezierkit                 # the library
uv add "bezierkit[cli]"          # with the command-line interface
uv add "bezierkit[matplotlib]"   # with the Matplotlib adapter
uv add "bezierkit==1.0.0"        # the version this manual describes
```

使用 `pip` 時，執行 `python -m pip install bezierkit`，選用依賴的寫法相同。1.0.0 是第一個正式版：`bezierkit` 及其文件所列子套件匯出的名稱依語意化版本管理，JSON 路徑格式維持第 1 版。

## 開發環境設定

```bash
git clone https://github.com/EconViz/bezierkit.git
cd bezierkit
uv sync --all-extras --dev
uv run pytest
uv run ruff check src tests benchmarks
uv run lint-imports
```

持續整合流程在 Python 3.10、3.11、3.12 與 3.13 上執行相同指令。`lint-imports` 檢查套件分層：數學核心不匯入任何繪圖端，只有轉接器匯入 Matplotlib。
