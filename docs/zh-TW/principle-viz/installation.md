---
seo_title: "安裝 principle-viz"
description: "用 pip 或 uv 安裝 principle-viz，確認安裝成功，並設定開發環境。"
---

# 安裝

## 系統需求

- [Python](https://www.python.org/downloads/) 3.10 以上

`principle-viz` 依賴 [mosaickit](../mosaickit/index.md)（`>=0.5.1,<0.6.0`），pip 與 uv 會自動一併安裝。

## 安裝套件

=== ":simple-pypi: pip"

    ```bash
    pip install principle-viz
    ```

=== ":simple-uv: uv"

    ```bash
    uv add principle-viz
    ```

本頁對應 principle-viz 0.10.0。

## 驗證安裝

```bash
python -c "import principle_viz; print('principle_viz imported')"
principle-viz --help
```

第二個指令會列出子指令，例如 `equilibrium`、`tax`、`subsidy`、`trade` 與 `controls`。

## 開發環境設定

```bash
git clone https://github.com/EconViz/principle-viz.git
cd principle-viz
uv sync
```

執行檢查與測試：

```bash
uv run ruff check src tests examples/scripts
uv run pytest -q
```
