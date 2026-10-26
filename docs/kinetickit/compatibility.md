---
seo_title: "Compatibility"
---

# Compatibility

<span id="sec-compatibility"></span>

## Supported platforms

- Python 3.10, 3.11, 3.12 and 3.13.
- Base installations include NumPy and GlyphKit. `raster` and `interactive` are optional extras. Their third-party engines are private implementation details.

## Stable surfaces (1.0)

| Surface | Import path |
| --- | --- |
| Timeline, tween, keyframes, scheduler | `kinetickit.timeline`, `.tween`, `.keyframes`, `.scheduler`, `.easing`, `.interpolation` |
| 2D and 3D scene contracts | `kinetickit.scene`, `.geometry`, `.styles` |
| Morphing and transitions | `kinetickit.morph`, `.transitions` |
| Renderer and exporter protocols | `kinetickit.renderers` (`Renderer`, `RendererCapabilities`, `register_renderer`), `kinetickit.exporters` (`Destination`, `ExportManifest`, `register_exporter`) |
| Interaction and accessibility | `kinetickit.interaction`, `.accessibility` |
| Typography port and text assets | `kinetickit.typography` |
| Conformance fixtures | `kinetickit.conformance` |

Everything exported in a public package's `__all__` is public. Names that start with an underscore, and everything in modules whose name starts with an underscore (`_matplotlib`, `_plotly`, `_gif_stream`), are private and can change at any time. Visualization semantics are out of scope.

## Versioning

KineticKit follows Semantic Versioning from 1.0. Pre-releases (`1.0.0bN`, `1.0.0rcN`) may change public contracts between pre-release versions, and each change is recorded in the change history.

## Deprecation

1. A deprecated public name keeps working for at least one minor release.
2. It emits `DeprecationWarning` that names the replacement and the removal version.
3. The removal is recorded in the change history.
4. Deprecated names are removed only in a major release.

An output format follows the same rule. A change that alters existing artifacts, such as the structure of the SVG, is visible in the change history and updates the golden files in the same commit.
