---
seo_title: "Themes and configuration"
---

# Themes and configuration

<span id="sec-themes"></span>

## Style bundles and themes

<!-- api: agora.mosaickit.guides_themes_1 -->

One sparse style per slot. A slot holding the wrong type raises
`ConfigurationError`. `merged_over(base)` merges slot by slot
([Sparse merge](styles.md#def-merge)).

<!-- api: agora.mosaickit.guides_themes_2 -->

A theme name and an immutable mapping from role names to bundles. Role
names are non-empty dotted strings (`"axes"`, `"axes.note"`,
`"mypkg.boundary"`).
`with_roles(**patch)` returns a theme with each patched role merged over
its old bundle; since keyword names cannot contain dots, pass dotted
roles as `with_roles(**{"mypkg.line": bundle})`.
`resolve(role, fallback_category=...)` resolves a role against the theme
alone.

<span id="tab-default-theme"></span>

| Role | Bundle |
| --- | --- |
| `primary` | stroke `blue` |
| `secondary` | stroke `red` |
| `accent` | stroke `teal` |
| `guide` | stroke `grey-400`, dashed |
| `axes` | stroke `grey-800`, width 1 |
| `axes.note` | text 9 pt, `grey-600` |
| `canvas` | fill `white`, opacity 1 (the background) |

Every other value comes from the primitive defaults of [Primitive defaults](styles.md#tab-primitive). The
theme is `mosaickit.themes.default`.

## Role resolution

A layer's role is resolved through its ancestor roles and then through the
fallback category for its layer type. For each field, the fallback applies
only when neither the role nor any ancestor supplies a value.

<span id="def-chain"></span>

!!! abstract "Definition · Role chain"

    The _chain_ of a role $\rho = \rho_1.\rho_2 \cdots \rho_m$ with fallback
    category $\phi$ is the sequence

    $$
    \kappa(\rho) = (\rho_1 \cdots \rho_m, \, \rho_1 \cdots \rho_{m-1}, \, \ldots, \, \rho_1, \, \phi),
    $$

    most specific first, with a repeated key kept only at its first place.

For example `"axes.note"` on a text layer has the chain
(`axes.note`, `axes`, `text`). The fallback categories are `primary`
(paths, groups), `region` (fills), `point` (markers), `text` (text, labels,
marks, notes, braces), `annotation` (arrows) and `legend`.

<span id="thm-resolution"></span>

!!! abstract "Theorem · Resolution order"

    Let a layer with explicit styles $E$ and role chain
    $\kappa = (k_1, \ldots, k_n)$ be drawn on a canvas with role overrides $C$,
    under a configuration with role overrides $G$ and theme roles $T$, and let
    $D$ be the primitive defaults. Then each field of the layer's resolved
    style is the first value that is not `None` in the sequence

    $$
    E, \quad C[k_1], \ldots, C[k_n], \quad G[k_1], \ldots, G[k_n], \quad T[k_1], \ldots, T[k_n], \quad D,
    $$

    where a missing role counts as the empty bundle.

<span id="cor-override"></span>

!!! abstract "Corollary · Overrides beat specificity"

    A canvas or configuration override of a general role takes precedence over
    the theme's value for a more specific role: if $G[\text{text}]$ sets a text size
    and no source before it in [Resolution order](themes.md#thm-resolution) does, a text layer with role
    `axes.note` gets that size, not the theme's 9 pt.

The figures in this manual use [Overrides beat specificity](themes.md#cor-override). They override the text size of
`text`, `axes` and `axes.note` together because overriding `text` alone would
also enlarge the notes.

## Registering domain roles

<!-- api: agora.mosaickit.guides_themes_3 -->

A registry of themes, holding `default` from the start. `register(theme)`
adds one (a taken name raises `ConfigurationError`), `get(name)` looks one
up, and `register_roles(name, roles)` merges dotted domain roles into a
registered theme and returns it; an undotted role raises
`ConfigurationError`, so domain packages cannot shadow the built-in roles.

<!-- api: agora.mosaickit.guides_themes_4 -->

A typed representation of a domain package's roles. A `RolePack` is a
dataclass with a class variable `_namespace`; each field that is not `None`
becomes the role `namespace.field`, with underscores in the field name
turned into dots.

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

## Configuration

<span id="sec-config"></span>

<!-- api: agora.mosaickit.guides_themes_5 -->

Runtime defaults for new canvases: the theme, the specification, the
renderer (a name or a `Renderer`), role overrides applied after the theme
($G$ in [Resolution order](themes.md#thm-resolution)) and the palette.

<!-- api: agora.mosaickit.guides_themes_6 -->

Makes `config` the active configuration inside the block. A context
variable stores the value, so each thread and asynchronous task sees its
own configuration. Arguments passed to `Canvas` always take precedence.

<!-- api: agora.mosaickit.guides_themes_7 -->

Reads a strict TOML configuration. Top-level keys are `theme` (only
`"default"`; custom themes are passed in Python), `canvas` (fields of
`CanvasSpec`), `renderer` (only `"matplotlib"`), `palette` and `styles`.
Any other key, unknown style, bad value or unreadable file raises
`ConfigurationError` naming the file and the key.

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

The `[palette]` table is merged over `DEFAULT_PALETTE`, so overriding `blue`
there recolors `primary` and everything else that names `blue`. Style
`color` and `edge_color` values may be palette names; an unknown name
raises `ConfigurationError` naming the file and key when the file is
loaded, before any canvas renders.
