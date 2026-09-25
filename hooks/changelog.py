"""Pull the release history from the main econ-viz repository at build time.

Every language's changelog page contains a `<!-- changelog -->` marker that is
replaced with the entries of econ-viz's CHANGELOG.md, so the docs never lag
behind a release.
"""

import logging
import urllib.request

CHANGELOG_URL = "https://raw.githubusercontent.com/EconViz/econ-viz/main/CHANGELOG.md"
CHANGELOG_PAGE = "https://github.com/EconViz/econ-viz/blob/main/CHANGELOG.md"
MARKER = "<!-- changelog -->"

log = logging.getLogger("mkdocs.hooks.changelog")
_cache: str | None = None


def _fetch() -> str:
    global _cache
    if _cache is None:
        with urllib.request.urlopen(CHANGELOG_URL, timeout=10) as response:
            text = response.read().decode("utf-8")
        # Drop the file's own title and the semantic-release marker; the page has its own heading.
        lines = [
            line
            for line in text.splitlines()
            if not line.startswith("# ") and line.strip() != "<!-- version list -->"
        ]
        _cache = "\n".join(lines).strip() + "\n"
    return _cache


def on_page_markdown(markdown, page, **kwargs):
    if MARKER not in markdown:
        return markdown
    try:
        entries = _fetch()
    except OSError as exc:
        log.warning(f"Could not fetch {CHANGELOG_URL}: {exc}")
        entries = f"See [CHANGELOG.md]({CHANGELOG_PAGE})."
    return markdown.replace(MARKER, entries)
