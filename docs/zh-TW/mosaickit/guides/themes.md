---
seo_title: "主題與設定"
---

# 主題與設定

<span id="sec-themes"></span>

## 樣式組與主題

<!-- api: agora.mosaickit.guides_themes_1 -->

每個槽位包含一個稀疏樣式。槽位內的型別錯誤時，會引發 `ConfigurationError`。`merged_over(base)` 會逐槽位合併（參見[稀疏合併](styles.md#def-merge)）。

<!-- api: agora.mosaickit.guides_themes_2 -->

包含主題名稱，以及從角色名稱到樣式組的不可變對應。角色名稱必須是非空、以點分隔的字串（`"axes"`、`"axes.note"`、`"mypkg.boundary"`）。`with_roles(**patch)` 回傳新主題，並將每個修補角色合併在原有的樣式組之上。由於關鍵字名稱不能含點，帶點的角色要寫成 `with_roles(**{"mypkg.line": bundle})`。`resolve(role, fallback_category=...)` 僅根據主題解析角色。

<span id="tab-default-theme"></span>

| 角色 | 樣式組 |
| --- | --- |
| `primary` | 線條 `blue` |
| `secondary` | 線條 `red` |
| `accent` | 線條 `teal` |
| `guide` | 線條 `grey-400`、虛線 |
| `axes` | 線條 `grey-800`、寬 1 |
| `axes.note` | 文字 9 pt、`grey-600` |
| `canvas` | 填色 `white`、透明度 1（背景） |

其餘的值都來自[基本預設值](styles.md#tab-primitive)的基本預設值。此主題為 `mosaickit.themes.default`。

## 角色解析

解析圖層角色時，會依序查看該角色及其上層角色，最後才查看圖層型別的後備類別。這個過程逐欄進行；只有該角色與所有上層角色都未提供某欄的值時，才會使用後備類別的值。

<span id="def-chain"></span>

!!! abstract "定義 · 角色鏈"

    對後備類別為 $\phi$ 的角色 $\rho = \rho_1.\rho_2 \cdots \rho_m$，其*鏈*為序列

    $$
    \kappa(\rho) = (\rho_1 \cdots \rho_m, \, \rho_1 \cdots \rho_{m-1}, \, \ldots, \, \rho_1, \, \phi),
    $$

    由最具體到最一般，重複的鍵只保留第一次出現。

例如，文字圖層的 `"axes.note"` 角色鏈為（`axes.note`, `axes`, `text`）。後備類別包括 `primary`（路徑、群組）、`region`（填色）、`point`（標記）、`text`（文字、標籤、座標軸標記、註記、大括號）、`annotation`（箭頭）與 `legend`。

<span id="thm-resolution"></span>

!!! abstract "定理 · 解析順序"

    設某圖層的自帶樣式為 $E$、角色鏈為 $\kappa = (k_1, \ldots, k_n)$，畫在角色覆寫為 $C$ 的畫布上。再設生效設定的角色覆寫為 $G$、主題角色為 $T$，並令 $D$ 為基本預設值。則圖層解析後樣式的每個欄位，是序列

    $$
    E, \quad C[k_1], \ldots, C[k_n], \quad G[k_1], \ldots, G[k_n], \quad T[k_1], \ldots, T[k_n], \quad D
    $$

    中第一個不是 `None` 的值，其中不存在的角色視為空樣式組。

<span id="cor-override"></span>

!!! abstract "推論 · 覆寫優先於具體程度"

    畫布或設定對一般角色的覆寫，優先於主題對較具體角色的設定：若 $G[\text{text}]$ 設定了文字大小，且[解析順序](themes.md#thm-resolution)序列中在它之前沒有來源設定大小，則角色為 `axes.note` 的文字圖層採用該大小，而非主題的 9 pt。

本手冊的圖便運用了[覆寫優先於具體程度](themes.md#cor-override)：圖中同時覆寫 `text`、`axes` 與 `axes.note` 的文字大小，因為只覆寫 `text` 也會放大註記。

## 註冊領域角色

<!-- api: agora.mosaickit.guides_themes_3 -->

主題登錄表，建立時已含有 `default`。`register(theme)` 加入主題（名稱已被使用時引發 `ConfigurationError`），`get(name)` 查詢主題，`register_roles(name, roles)` 則把帶點的領域角色合併到已登錄的主題中，並回傳該主題。不帶點的角色會引發 `ConfigurationError`，因此領域套件無法遮蔽內建角色。

<!-- api: agora.mosaickit.guides_themes_4 -->

以型別定義領域套件角色的方式。`RolePack` 是帶有類別變數 `_namespace` 的 dataclass；每個不為 `None` 的欄位都會轉成 `namespace.field` 角色，欄位名稱中的底線則轉為點。

```python
from dataclasses import dataclass
from typing import ClassVar
from mosaickit import Stroke, StyleBundle, Theme, expand_roles
from mosaickit.themes import default


@dataclass(frozen=True)
class MyRoles:
    _namespace: ClassVar[str] = "mypkg"
    line: StyleBundle | None = StyleBundle(
        stroke=Stroke(color="blue", width=2)
    )
    line_dashed: StyleBundle | None = None


# {"mypkg.line": ...}
roles = expand_roles(MyRoles())
mytheme = Theme("mypkg", {**default.roles, **roles})
```

## 設定

<span id="sec-config"></span>

<!-- api: agora.mosaickit.guides_themes_5 -->

新畫布的執行期預設值：主題、規格、繪製器（名稱或 `Renderer`）、在主題之後套用的角色覆寫（[解析順序](themes.md#thm-resolution)中的 $G$），以及色盤。

<!-- api: agora.mosaickit.guides_themes_6 -->

讓 `config` 在區塊內成為生效的設定。此值存於 context variable，因此每個執行緒與非同步工作都有各自的設定；傳給 `Canvas` 的引數一律優先。

<!-- api: agora.mosaickit.guides_themes_7 -->

讀取嚴格的 TOML 設定。最上層的鍵為 `theme`（只能是 `"default"`；自訂主題須在 Python 中傳入）、`canvas`（`CanvasSpec` 的欄位）、`renderer`（只能是 `"matplotlib"`）、`palette` 與 `styles`。其他鍵、未知的樣式、錯誤的值或無法讀取的檔案，都引發指明檔案與鍵的 `ConfigurationError`。

```toml
[canvas]
x_range = [0, 20]
dpi = 150

[palette]
blue = "#0072B2"     # override a default color
accent = "#984EA3"   # add a new name

[styles."mypkg.boundary".stroke]
color = "accent"     # a palette name or a "#hex" value
width = 2
dash = "dashed"
```

`[palette]` 表疊加在 `DEFAULT_PALETTE` 之上，因此在此覆寫 `blue` 會改變 `primary` 以及所有指名 `blue` 的地方。樣式的 `color` 與 `edge_color` 可以是色盤名稱；未知名稱在載入檔案時（任何畫布繪製之前）就引發指明檔案與鍵的 `ConfigurationError`。
