---
seo_title: "安裝"
---

# 安裝

<span id="sec-install"></span>

`glyphkit` 支援 Python 3.10 到 3.13。它目前以預發行版本放在 PyPI，所以 uv 要加上 `--prerelease allow`。

```bash
uv add --prerelease allow glyphkit
uv add --prerelease allow "glyphkit[portable]"  # 加入 WOFF2 子集資料
uv add "glyphkit==1.0.0b4"                       # 固定在某個版本
```

基本安裝包含 FontTools、HarfBuzz 綁定（`uharfbuzz`）、Unicode 分段（`uniseg`）與雙向文字支援（`python-bidi`）。`portable` 額外安裝 Brotli，WOFF2 輸出需要它；沒有它也能輸出 SFNT 子集。兩種安裝都不包含繪圖端。

字型也不會一起安裝。GlyphKit 只讀取你傳進去的字型，所以範例假設腳本旁邊有一個 `fonts/` 資料夾。範例使用開源字型 Source Sans 3 與 Noto Sans TC，數學式則使用 STIX Two Math。

開發環境的設定方式如下：

```bash
git clone https://github.com/EconViz/glyphkit.git
cd glyphkit
uv sync --all-extras
uv run pytest
uv run ruff check .
uv run mypy
uv run lint-imports
```
