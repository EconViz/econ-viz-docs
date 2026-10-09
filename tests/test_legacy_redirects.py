import re
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]
DOCS = ROOT / "docs"
LEGACY_PAGES = (
    "getting-started/cli.md",
    "getting-started/installation.md",
    "getting-started/quickstart.md",
    "guides/animation.md",
    "guides/canvas.md",
    "guides/config.md",
    "guides/consumer.md",
    "guides/export.md",
    "guides/interactive.md",
    "guides/themes.md",
    "models/advanced.md",
    "models/index.md",
    "project/changelog.md",
    "project/manual.md",
    "project/references.md",
    "tools/analysis.md",
    "tools/latex.md",
)


class LegacyRedirectTests(unittest.TestCase):
    def test_every_pre_package_page_resolves_in_every_language(self):
        config = (ROOT / "mkdocs.yml").read_text()
        redirects = dict(re.findall(r"^        (\S+\.md): (\S+\.md)$", config, re.MULTILINE))

        for locale in ("", "zh-TW/", "zh-CN/"):
            for relative in LEGACY_PAGES:
                old_path = locale + relative
                target = redirects.get(old_path)
                self.assertIsNotNone(target, old_path)
                self.assertTrue((DOCS / target).is_file(), (old_path, target))

    def test_legacy_pdf_urls_remain_available(self):
        for locale in ("en", "zh-TW", "zh-CN"):
            path = DOCS / "assets" / "manual" / f"econ-viz-manual-{locale}.pdf"
            self.assertTrue(path.is_file(), path)


if __name__ == "__main__":
    unittest.main()
