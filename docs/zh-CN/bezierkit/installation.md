---
seo_title: "安装"
---

# 安装

<span id="sec-install"></span>

## 系统需求

`bezierkit` 需要 Python 3.10 以上版本与 `NumPy`。另有两组可选依赖：

<!-- api: agora.bezierkit.installation_1 -->

## 安装软件包

```bash
uv add bezierkit                 # the library
uv add "bezierkit[cli]"          # with the command-line interface
uv add "bezierkit[matplotlib]"   # with the Matplotlib adapter
uv add "bezierkit==1.0.0"        # the version this manual describes
```

使用 `pip` 时，运行 `python -m pip install bezierkit`，可选依赖的写法相同。1.0.0 是第一个正式版：`bezierkit` 及其文档所列子包导出的名称按语义化版本管理，JSON 路径格式维持第 1 版。

## 开发环境设置

```bash
git clone https://github.com/EconViz/bezierkit.git
cd bezierkit
uv sync --all-extras --dev
uv run pytest
uv run ruff check src tests benchmarks
uv run lint-imports
```

持续整合流程在 Python 3.10、3.11、3.12 与 3.13 上运行相同命令。`lint-imports` 检查软件包分层：数学核心不导入任何绘图端，只有适配器导入 Matplotlib。
