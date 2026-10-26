---
seo_title: "更新紀錄"
---

# 更新紀錄

`macro-viz` 版本為 `0.2.0.dev0`。儲存庫的 [CHANGELOG](https://github.com/EconViz/macro-viz/blob/main/CHANGELOG.md) 列出每一項變更。

## 尚未發布

### 新增

- 模型家族 `keynesian`、`money`、`adas`、`islm`、`growth`、`labor`、`open_economy` 與 `panels`，各有型別化模型、比較與繪圖函式。
- 已註冊的 `[macro.*]` 設定結構，以及英文、繁體中文與簡體中文的語系表。
- `macro_viz.animation` 與 `macro-viz[animation]` 選項：任何繪圖函式都能輸出 GIF 與動畫 SVG。
- 帶型別化曲線移動的連動四面板與五面板圖。

### 變更

- 圖形遵循 manual 風格：黑白、只有價格 `p` 用小寫、細的 45 度線。
- 變動後的曲線是細實線；平行移動是從舊均衡指向新曲線的直線箭頭；彎曲箭頭只代表轉動；曲線名稱放在線的末端。

### 移除

- 資料序列、國民所得帳與景氣循環系列：統計圖不在範圍內。
