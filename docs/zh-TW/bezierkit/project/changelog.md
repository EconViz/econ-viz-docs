---
seo_title: "更新紀錄"
---

<span id="sec-changelog"></span>

# 更新紀錄

本章列出影響套件使用的版本變更，不含僅修改文件的版本；各條目依 l3doc 慣例標註於它所描述的功能旁，頁碼即該功能的實際頁碼。

## 1.0.0

- 第一個正式版；公開 API 依語意化版本管理 [簡介](../guides/introduction.md)
- `bezierkit` — 持續整合測試 Python 3.10、3.11、3.12 與 3.13 [安裝](../installation.md)
- `PiecewiseBezier.segment` — `t0` 落在線段內部時回傳正確的區間；先前會先在 `t0` 分割再對後半段重新參數化，導致終點錯誤 [三次線段與路徑](../guides/paths.md)

## 0.5.0rc1

- 首次發布到 PyPI：任意次數的 Bézier 曲線、三次線段與路徑、建構、Hermite 插值、擬合、等值線描繪、取樣、匯出器與命令列介面 [簡介](../guides/introduction.md)

