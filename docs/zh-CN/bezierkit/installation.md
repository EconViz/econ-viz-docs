---
seo_title: "安装 bezierkit"
description: "用 pip 或 uv 安装 bezierkit 0.5.0rc1 预发布版本，加装可选的 CLI 与 Matplotlib 功能，并设置开发环境。"
---

# 安装

## 环境要求

- [Python](https://www.python.org/downloads/) 3.10 以上

bezierkit 唯一必要的依赖是 `numpy`。

## 安装软件包

bezierkit 0.5.0rc1 是预发布版本，pip 与 uv 默认都会略过预发布版本。请加上 `--pre` 表示接受，或直接指定完整版本。

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

## 可选的额外依赖

| 额外依赖 | 加入内容 | 安装命令 |
|---|---|---|
| `cli` | `bezierkit` 命令（typer 与 rich） | `pip install --pre "bezierkit[cli]"` |
| `matplotlib` | Matplotlib 路径适配器 | `pip install --pre "bezierkit[matplotlib]"` |

使用 uv 时，同样写成 `uv add --prerelease allow "bezierkit[cli]"`。

## 验证安装

```bash
python -c "import bezierkit; print(bezierkit.__version__)"
```

会打印出 `0.5.0rc1`。安装 `cli` 额外依赖后，运行 `bezierkit --help` 可列出所有命令。

## 开发环境设置

```bash
git clone https://github.com/EconViz/bezierkit.git
cd bezierkit
uv sync --all-extras --dev
uv run pytest
```
