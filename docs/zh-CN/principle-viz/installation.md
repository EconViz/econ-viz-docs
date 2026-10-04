---
seo_title: "安装 principle-viz"
description: "用 pip 或 uv 安装 principle-viz，确认安装成功，并设置开发环境。"
---

# 安装

## 环境要求

- [Python](https://www.python.org/downloads/) 3.10 以上

`principle-viz` 依赖 [mosaickit](../mosaickit/index.md)（`>=0.5.1,<0.6.0`），pip 与 uv 会自动一并安装。

## 安装软件包

=== ":simple-pypi: pip"

    ```bash
    pip install principle-viz
    ```

=== ":simple-uv: uv"

    ```bash
    uv add principle-viz
    ```

本页对应 principle-viz 0.10.0。

## 验证安装

```bash
python -c "import principle_viz; print('principle_viz imported')"
principle-viz --help
```

第二个命令会列出子命令，例如 `equilibrium`、`tax`、`subsidy`、`trade` 与 `controls`。

## 开发环境设置

```bash
git clone https://github.com/EconViz/principle-viz.git
cd principle-viz
uv sync
```

运行检查与测试：

```bash
uv run ruff check src tests examples/scripts
uv run pytest -q
```
