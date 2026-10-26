---
seo_title: "Output formats"
---

# Output formats

<span id="sec-outputs"></span>

One scene and one motion drive every output. The suffix of the destination picks the format.

| Format | Capability | 2D | 3D | Interactive | Vector-preserving |
| --- | --- | :-: | :-: | :-: | :-: |
| Animated SVG | `vector` | yes | projected (sampled) | no | yes (2D) |
| GIF | `raster` | yes | projected | no | no |
| HTML | `interactive` | yes (native SVG and player) | yes (native 3D, orbit and zoom) | yes | 2D yes |

<!-- api: kinetickit.guides_outputs_1 -->

The immutable export report: format, renderer, destination, dimensions, duration, what was preserved or degraded, warnings and network dependencies.

<!-- api: kinetickit.guides_outputs_2 -->

Returns the registered output formats, `('gif', 'html', 'svg')`. It does not check the optional dependencies: saving a GIF without `kinetickit[raster]` raises `CapabilityError` with an install hint.

<!-- api: kinetickit.guides_outputs_3 -->

The lower-level entry point of the exporter registry. Most callers use `Animation.save()`.

<!-- api: kinetickit.guides_outputs_4 -->

Declares which scene dimensions, geometry, features, outputs and interactions a renderer supports.

<!-- api: kinetickit.guides_outputs_5 -->

The capabilities an animation needs, worked out from its scene, motion, interactions and accessibility data.

<!-- api: kinetickit.guides_outputs_6 -->

Computes the `Requirements` of an animation before any file is written. Every export compares them with the renderer's capabilities first: an unsupported combination raises `CapabilityError` that names the missing capabilities and gives a hint, and a failed export leaves no file.

Animated SVG uses SVG's vector scene model [{W3C} (2018)](../project/references.md#svg2) and declarative SMIL timing [{W3C} (2008)](../project/references.md#smil3). KineticKit writes explicit values and durations, so the document does not depend on Python at playback time.

## Options
<span id="sec-options"></span>

`save()` passes its keyword options to the chosen output.

| Output | Options |
| --- | --- |
| SVG | `width`, `height`, `loop` (default `False`), `title`, `description`, `samples`, `embed_fonts`, `reduced_motion`, `degradation` |
| GIF | `width`, `height`, `fps`, `dpi`, `loop`, `colors`, `dither`, `palette`, `disposal`, `accessibility`, `description` |
| HTML | `width`, `height`, `packaging`, `autoplay`, `loop`, `speed`, `controls`, `fps`, `max_frames`, `title`, `description`, `lang` |

`loop=True` makes an SVG repeat forever, which is what an animation on a page usually needs. A GIF repeats forever unless `loop=None`. Unknown option names raise an error.

## GIF settings

<!-- api: kinetickit.guides_outputs_7 -->

The GIF part of the options: frame rate, palette, dithering, looping, disposal and the accessibility text.

<!-- api: kinetickit.guides_outputs_8 -->

Streams encoded PNG frames into a GIF without keeping every decoded frame in memory.

Raster output renders one frame at a time, so memory does not grow with the duration. DPI goes up to 1200. GIF frame intervals below 10 ms are rejected. Time is spread over integer centiseconds with the error carried forward, so the total duration stays right. An expensive raster job issues `RenderCostWarning`; it does not lower the size or DPI behind your back.

## HTML packaging

`packaging="offline"` embeds the runtime and needs no network. `packaging="compact"` references a pinned CDN copy and records the address in `ExportManifest.network_dependencies`. 2D scenes are the embedded animated SVG driven by a small dependency-free player: play, pause, seek, step, speed, loop and markers, with keyboard operation and pan and zoom. 3D scenes are pre-sampled at `fps` (default 30, at most `max_frames`) and shown by a private plotting runtime with native orbit and zoom.

## Capability notes

- **Vector 3D** is a time-varying 2D projection, with flat baked shading and the painter's order fixed at $t = 0$. It fails if primitives enter or leave the view, rather than guess.
- **Not supported in 1.0.0b2:** video encoders, audio, physics, multi-panel layout, implicit surfaces, 3D text, drag interaction and animated overlays on 3D scenes.

## Fallbacks without JavaScript or motion

| Case | Behaviour |
| --- | --- |
| 2D HTML without JavaScript | the embedded SVG plays once natively (SMIL); controls are inert |
| 3D HTML without JavaScript | a `<noscript>` block shows a static SVG of the final state |
| SVG used as an `<img>` | the animation plays; scripts, including reduced-motion handling, are ignored |
| GIF | no runtime semantics; use the manifest description and the representative PNG |
| `prefers-reduced-motion` | no autoplay; the representative state (default: the final one) is shown; Play still works |

## What each format keeps

`ExportManifest.preserved` and `.degraded` list this for every export.

| Semantics | SVG | HTML | GIF |
| --- | --- | --- | --- |
| Title, description | yes | yes | manifest only |
| Roles, labels, descriptions | yes (`role`, `aria-label`, `<title>`, `<desc>`) | yes | no |
| Reading order | `data-kk-order` (DOM order is z-order) | yes (ordered text list) | no |
| Keyboard-operable controls | n/a | yes (native buttons, range, select) | n/a |
| Interactions | dropped by policy, or an error if `required` | yes | dropped by policy, or an error |
| Fonts | embedded subsets as `@font-face` | through the embedded SVG | drawn into pixels |
| Stable object ids | `data-kk-id` | `data-kk-id` and an `objects` map | n/a |

Projected 3D output keeps the ids of drawable nodes. Groups and lights have no element of their own.
