---
seo_title: "安裝"
---

# 安裝

<span id="sec-install"></span>

`kinetickit` 支援 Python 3.10 到 3.13。每種安裝都會包含 NumPy 與 GlyphKit。它目前以預發行版本放在 PyPI，所以 uv 要加上 `--prerelease allow`。

```bash
uv add --prerelease allow kinetickit               # 動態 SVG
uv add --prerelease allow "kinetickit[raster]"     # SVG 與 GIF
uv add --prerelease allow "kinetickit[interactive]"# SVG 與 HTML
uv add --prerelease allow "kinetickit[studio]"     # 全部內建格式
uv add "kinetickit[studio]==1.0.0b2"               # 固定在某個版本
```

| 額外安裝項 | 加入的套件 | 輸出 |
| --- | --- | --- |
| 無 | NumPy、GlyphKit | 動態 SVG（`vector`） |
| `raster` | Matplotlib、Pillow | GIF（`raster`） |
| `interactive` | Plotly | 互動 HTML（`interactive`） |
| `studio` | 以上全部 | 三種都有 |

這些第三方套件只出現在私有轉接器後面，不會進入公開的場景或繪圖端介面，之後也可能在不造成破壞性變更的情況下換掉。

要存成的格式缺少對應的額外安裝項時，會拋出 `CapabilityError` 並指出該裝哪一項，同時不會寫出任何檔案。`available_formats()` 列出的是已登錄的格式，所以即使缺少額外安裝項，也會列出三種。

開發環境的設定方式如下：

```bash
git clone https://github.com/EconViz/kinetickit.git
cd kinetickit
uv sync --all-extras
uv run pytest
uv run ruff check .
uv run mypy
uv run lint-imports
uv run python -m kinetickit.conformance
```
