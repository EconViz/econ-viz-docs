# Agora reference synchronization

The utility-viz, principle-viz, mosaickit and bezierkit reference pages are sourced from the
three editions of the sibling `agora` repository. The source version is defined by each manual's
`manual.toml`.

Run `uv run --frozen python scripts/sync_agora.py ../agora` to update the mapped
pages and API data. This overwrites the destinations explicitly listed in
`MAPPING`; edit the corresponding agora chapter before re-running it. Package
landing pages and migration guides are maintained separately. Two utility-viz pages
are still written by hand because the manual has no equivalent: Themes (the six theme
images, kept in each theme's own colours) and Animation (the GIF gallery); `KEEP_SITE_PAGE`
in `sync_agora.py` lists them. The Settings File page is also hand-written. Navigation is configured in `mkdocs.yml`.

After syncing, run `python scripts/format_examples.py` with `black` installed
to restore the site's example formatting: 64-column Python, standalone comments,
and expanded long calls. The formatter checks AST equivalence and leaves
incomplete snippets unchanged. This authoring tool is not required for site builds.

The converter preserves examples, theorem statements, proofs, reference links,
release notes and localized descriptions. Release notes are collected exclusively
on each package's changelog page, not displayed inline in tutorials.
It converts Typst mathematics to LaTeX and PDF figures to SVG with `pdftocairo`
(Poppler). Image paths and local
links remain relative to each language. The CSS grayscale filter applies to
these figures like other examples.

`agora-manifest.json` records each source path and SHA-256, so the version of
each imported chapter is reviewable. `agora-navigation.json` records chapter
titles in all three editions. Neither file is fetched during a site build.

API blocks use `hooks/api_data/agora.json` and the existing API renderer. A
manual may document a selection of parameters or result members, so the renderer
does not invent types, required flags or default values when none were specified.
Class names remain gray; methods and functions use the site's blue accent.

Inline code references are linked during the HTML build using the same API
catalog and the directives present in documentation pages. Links stay within
the current package and language, prefer same-page definitions, and are only
added for unambiguous targets. Existing links and fenced examples are preserved.
Use a qualified name such as `Canvas.add()` when a short method name is ambiguous.

`hooks/api_sections.json` registers definitions presented as ordinary guide
sections. Its heading numbers are zero-based, excluding fenced examples; keep
them aligned across translations when reorganizing pages. API cards index every
signature in a group. Tests check all parseable Python examples in every language
for missing package-import targets, including examples nested in tabs.

The API hook detects reference tables by localized column headings, including
tables nested inside tabs or admonitions. `REFERENCE_TABLES` supplements this
with selected reference tables whose headings are less specific. Original
Markdown tables remain the content source, so future manual imports inherit the
same UI. Comparison tables are excluded.
Each row keeps every column's localized label and content and receives a stable
anchor based on its API name; links prefer these rows over broad guide sections.

Validate with `uv run --frozen python -m unittest discover -s tests` and
`uv run --frozen mkdocs build`. New Typst macros require explicit converter
support; unsupported macros fail instead of being silently omitted.

## utility-viz figures

Every figure of the utility-viz manual is drawn by the code printed beside it. The chapters
(`agora/packages/utility-viz/chapters/<edition>/*.typ`) hold `#example` blocks, each followed by its
`#fig`; `scripts/make_figures.py` in the agora repository runs the example before each figure and
saves the picture, so the PDF and the site show what the printed code produces. Regenerate with
`make figures PACKAGE=utility-viz`, rebuild the PDFs with `make publish PACKAGE=utility-viz`, and
sync again, which copies the SVGs.

* The house look (grey curves, black axes, white page) is `config/manual.toml`, which every example
  loads and which the themes chapter prints in full; the script checks the two agree.
* A figure whose code differs between editions (a translated title, a CJK font) gets its own file,
  `<name>.zh-TW.svg` or `<name>.zh-CN.svg`; otherwise the editions share one.
* The Themes page is converted from its chapter (six figures, one per built-in theme).
* The Animation page is converted from its chapter, and `scripts/supplements/animation.<locale>.md`
  is appended: a gallery of 14 GIFs drawn by `scripts/animation_figures.py` with the same settings.
