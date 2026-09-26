"""natbib-style citations from docs/references.bib, formatted in APA 7.

In Markdown pages:

    \\citet{key}          Haagsma (2012)
    \\citep{key}          (Haagsma, 2012)
    \\citep[p. 2]{key}    (Haagsma, 2012, p. 2)
    \\citep{a,b}          (Kugler & Andrews, 1996; thriveth, 2014)
    \\citeauthor{key}     Haagsma
    \\citeyear{key}       2012

Chinese pages use full-width parentheses. Each citation links to its entry on
the references page, and a line containing only ``\\bibliography`` there
expands to every entry in the .bib file, each followed by links back to the
pages that cite it. An unknown key fails the build.
"""

from __future__ import annotations

import html
import posixpath
import re
from pathlib import Path

import bibtexparser
from bibtexparser.bparser import BibTexParser
from mkdocs.exceptions import PluginError

BIB_FILE = "references.bib"
REFERENCES_PAGE = "project/references.md"

_CITE = re.compile(r"\\cite(?P<kind>t|p|author|year)(?:\[(?P<note>[^\]]*)\])?\{(?P<keys>[^}]+)\}")
# Fenced code blocks and inline code are left untouched.
_CODE = re.compile(r"(^(?P<fence>`{3,}|~{3,}).*?^(?P=fence)[ \t]*$|`[^`\n]+`)", re.M | re.S)
_MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], start=1)}
_MONTH_NAMES = ["January", "February", "March", "April", "May", "June", "July",
                "August", "September", "October", "November", "December"]

_entries: dict[str, dict] = {}


def on_config(config, **kwargs):
    path = Path(config.docs_dir) / BIB_FILE
    parser = BibTexParser(common_strings=True)
    parser.ignore_nonstandard_types = False
    with path.open(encoding="utf-8") as handle:
        database = bibtexparser.load(handle, parser=parser)
    _entries.clear()
    _entries.update({entry["ID"]: entry for entry in database.entries})
    return config


def on_page_markdown(markdown, page, config, **kwargs):
    chinese = str(config.theme["language"]).lower().startswith("zh")
    src = page.file.src_uri
    prefix = src.split("/", 1)[0] + "/" if src.startswith(("zh-TW/", "zh-CN/")) else ""
    target = posixpath.relpath(prefix + REFERENCES_PAGE, posixpath.dirname(src) or ".")

    counts: dict[str, int] = {}

    def cite(match: re.Match) -> str:
        keys = _keys(match)
        for key in keys:
            if key not in _entries:
                raise PluginError(f"{src}: unknown citation key {key!r} (not in {BIB_FILE})")
        anchors = [_anchor(key, counts) for key in keys]
        return _render(match["kind"], keys, match["note"], target, chinese, anchors)

    markdown = _outside_code(markdown, lambda text: _CITE.sub(cite, text))

    if src.endswith(REFERENCES_PAGE):
        backrefs = _backrefs(Path(config.docs_dir), prefix, src)
        markdown = re.sub(
            r"^\\bibliography[ \t]*$", lambda _: _bibliography(backrefs), markdown, flags=re.M
        )
    return markdown


def _outside_code(markdown: str, transform) -> str:
    """Apply *transform* to the text between code blocks and inline code."""
    parts = []
    last = 0
    for code in _CODE.finditer(markdown):
        parts.append(transform(markdown[last:code.start()]))
        parts.append(code.group(0))
        last = code.end()
    parts.append(transform(markdown[last:]))
    return "".join(parts)


def _keys(match: re.Match) -> list[str]:
    return [key.strip() for key in match["keys"].split(",")]


def _anchor(key: str, counts: dict[str, int]) -> str:
    """Id of the n-th citation of *key* on a page: cite-<key>-<n>."""
    counts[key] = counts.get(key, 0) + 1
    return f"cite-{key}-{counts[key]}"


def _backrefs(docs_dir: Path, prefix: str, references_src: str) -> dict[str, list[tuple[str, str]]]:
    """For each key, (link to its first citation, page title) on every page of this language."""
    found: dict[str, list[tuple[str, str]]] = {}
    for path in sorted(docs_dir.rglob("*.md")):
        src = path.relative_to(docs_dir).as_posix()
        in_language = src.startswith(prefix) if prefix else not src.startswith(("zh-TW/", "zh-CN/"))
        if not in_language or src == references_src:
            continue
        text = path.read_text(encoding="utf-8")
        cited: list[str] = []

        def record(match: re.Match) -> str:
            cited.extend(key for key in _keys(match) if key not in cited)
            return match.group(0)

        _outside_code(text, lambda chunk: _CITE.sub(record, chunk))
        if not cited:
            continue
        heading = re.search(r"^# (.+)$", text, re.M)
        title = heading.group(1).strip() if heading else src
        link = posixpath.relpath(src, posixpath.dirname(references_src))
        for key in cited:
            found.setdefault(key, []).append((f"{link}#cite-{key}-1", title))
    return found


# ------------------------------------------------------------------
# In-text citations
# ------------------------------------------------------------------

def _render(kind: str, keys: list[str], note: str | None, target: str, chinese: bool, anchors: list[str]) -> str:
    left, right = ("（", "）") if chinese else ("(", ")")
    ids = dict(zip(keys, anchors))

    def link(key: str, text: str) -> str:
        title = _reference(_entries[key], markup=False).replace('"', "&quot;")
        return f'[{text}]({target}#{key} "{title}"){{#{ids[key]} .ev-cite}}'

    if kind == "author":
        return "; ".join(link(key, _in_text_authors(_entries[key], narrative=True)) for key in keys)
    if kind == "year":
        return ", ".join(link(key, _year(_entries[key])) for key in keys)
    if kind == "t":
        cited = [
            link(key, f"{_in_text_authors(_entries[key], narrative=True)}{left}{_year(_entries[key])}"
                      f"{', ' + note if note and i == len(keys) - 1 else ''}{right}")
            for i, key in enumerate(keys)
        ]
        return ", ".join(cited)
    cited = "; ".join(link(key, f"{_in_text_authors(_entries[key], narrative=False)}, {_year(_entries[key])}")
                      for key in keys)
    return f"{left}{cited}{', ' + note if note else ''}{right}"


def _in_text_authors(entry: dict, *, narrative: bool) -> str:
    surnames = [author[0] for author in _authors(entry)]
    if len(surnames) == 1:
        return surnames[0]
    if len(surnames) == 2:
        return f"{surnames[0]} {'and' if narrative else '&'} {surnames[1]}"
    return f"{surnames[0]} et al."


# ------------------------------------------------------------------
# Reference list (APA 7)
# ------------------------------------------------------------------

def _bibliography(backrefs: dict[str, list[tuple[str, str]]]) -> str:
    def sort_key(entry: dict):
        return (_authors(entry)[0][0].lower(), _year(entry))

    items = []
    for entry in sorted(_entries.values(), key=sort_key):
        pages = backrefs.get(entry["ID"], [])
        # Markdown links (not raw <a>) so MkDocs resolves and validates them.
        back = (
            ' <span class="ev-bib-backrefs">↩ '
            + " · ".join(f"[{title}]({link})" for link, title in pages)
            + "</span>"
            if pages else ""
        )
        items.append(
            f'<div class="ev-bib-entry" id="{entry["ID"]}" markdown>\n'
            f'{_reference(entry, markup=True)}{back}\n'
            f'</div>'
        )
    return "\n\n".join(items)


def _reference(entry: dict, *, markup: bool) -> str:
    def em(text: str) -> str:
        return f"<em>{text}</em>" if markup else text

    def link(url: str) -> str:
        return f'<a href="{url}">{html.escape(url)}</a>' if markup else url

    authors = _reference_authors(entry)
    title = _clean(entry.get("title", ""))
    kind = entry.get("ENTRYTYPE", "misc")
    locator = _locator(entry)

    if kind == "article":
        source = em(f"{_clean(entry['journal'])}, {entry['volume']}") if "volume" in entry else em(_clean(entry["journal"]))
        if "number" in entry:
            source += f"({entry['number']})"
        if "pages" in entry:
            source += f", {_clean(entry['pages'])}"
        elif "eid" in entry:
            source += f", Article {entry['eid']}"
        text = f"{authors} ({_year(entry)}). {_end(title)} {source}."
    elif kind == "book":
        publisher = f" {_end(_clean(entry['publisher']))}" if "publisher" in entry else ""
        text = f"{authors} ({_year(entry)}). {em(_end(title))}{publisher}"
    elif kind == "incollection":
        editors = _names(entry.get("editor", ""))
        eds = f"In {editors} (Ed{'s' if ' and ' in entry.get('editor', '') else ''}.), " if editors else "In "
        pages = f" (pp. {_clean(entry['pages'])})" if "pages" in entry else ""
        publisher = f" {_end(_clean(entry['publisher']))}" if "publisher" in entry else ""
        text = f"{authors} ({_year(entry)}). {_end(title)} {eds}{em(_clean(entry['booktitle']))}{pages}.{publisher}"
    else:
        kind_note = f" [{_clean(entry['type'])}]" if "type" in entry else ""
        where = f" {_end(_clean(entry['howpublished']))}" if "howpublished" in entry else ""
        text = f"{authors} ({_date(entry)}). {em(title)}{kind_note}.{where}"
    return f"{text} {link(locator)}" if locator else text


def _reference_authors(entry: dict) -> str:
    names = [f"{last}, {initials}" if initials else last for last, initials in _authors(entry)]
    if len(names) == 1:
        return _end(names[0])
    if len(names) <= 20:
        return _end(", ".join(names[:-1]) + ", & " + names[-1])
    return _end(", ".join(names[:19]) + ", . . . " + names[-1])


def _names(field: str) -> str:
    people = [f"{initials} {last}".strip() for last, initials in _split_names(field)]
    if len(people) <= 2:
        return " & ".join(people)
    return ", ".join(people[:-1]) + ", & " + people[-1]


def _authors(entry: dict) -> list[tuple[str, str]]:
    return _split_names(entry.get("author", "Anonymous"))


def _split_names(field: str) -> list[tuple[str, str]]:
    people = []
    for raw in re.split(r"\s+and\s+", field.strip()):
        raw = raw.strip()
        if raw.startswith("{") and raw.endswith("}"):
            people.append((_clean(raw), ""))  # Organisation or handle, kept verbatim.
            continue
        if "," in raw:
            last, first = (part.strip() for part in raw.split(",", 1))
        else:
            *first_parts, last = raw.split()
            first = " ".join(first_parts)
        people.append((_clean(last), _initials(_clean(first))))
    return people


def _initials(first: str) -> str:
    parts = [part for part in re.split(r"[\s.]+", first) if part]
    return " ".join(
        "-".join(f"{piece[0]}." for piece in part.split("-") if piece) for part in parts
    )


def _year(entry: dict) -> str:
    return entry.get("year", "n.d.")


def _date(entry: dict) -> str:
    month = _MONTHS.get(entry.get("month", "")[:3].lower())
    if month is None:
        return _year(entry)
    day = f" {entry['day']}" if "day" in entry else ""
    return f"{_year(entry)}, {_MONTH_NAMES[month - 1]}{day}"


def _locator(entry: dict) -> str:
    if "doi" in entry:
        return f"https://doi.org/{entry['doi']}"
    return entry.get("url", "")


def _clean(text: str) -> str:
    text = text.replace("--", "–").replace(r"\&", "&")
    return re.sub(r"\s+", " ", text.replace("{", "").replace("}", "")).strip()


def _end(text: str) -> str:
    return text if text.endswith((".", "?", "!")) else text + "."
