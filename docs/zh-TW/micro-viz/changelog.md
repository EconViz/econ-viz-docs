---
seo_title: "更新紀錄"
---

<span id="sec-changelog"></span>

# 更新紀錄

`micro-viz` 的發行紀錄。套件目前為 0.2.0.dev0 版，尚未發布到 PyPI；儲存庫的 [CHANGELOG](https://github.com/EconViz/micro-viz/blob/main/CHANGELOG.md) 列出每一項變更。純文件的變更不列入；每一條紀錄標記在它所描述功能的說明處，依 l3doc 慣例，頁碼即實際頁碼。

## 0.2.0.dev0

- 開發版的第一版手冊：生產者理論、市場結構、要素市場、不確定性與資訊 [簡介](guides/introduction.md)
- 圖形以 `mosaickit` 繪製（`mosaickit>=1.0.0rc9,<2.0.0`） [簡介](guides/introduction.md)
- `Config` — 設定讀自共用的 `econ-viz.toml`；`micro-viz` 在 `[micro]` 下宣告自己的表 [設定](guides/settings.md)
- `Config` — `[micro.region]` 決定是否為邊際報酬區間上色，以及底色填到圖頂或只填到曲線 [設定](guides/settings.md)
- `save_svg` — 以畫出靜態圖的同一個繪圖函式製作動畫 SVG 與 GIF；需要 `animation` 選用依賴 [動畫](guides/animation.md)

