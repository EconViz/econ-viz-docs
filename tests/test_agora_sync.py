import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('sync_agora', ROOT / 'scripts/sync_agora.py')
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


class AgoraMathTests(unittest.TestCase):
    def test_greek_scripts_and_literal_text(self):
        self.assertEqual(sync.math_latex('beta_1'), r'\beta_1')
        self.assertEqual(sync.math_latex('"int" P'), r'\text{int} P')

    def test_visible_sets_and_grouped_scripts(self):
        self.assertEqual(sync.math_latex('{p}'), r'\lbrace p\rbrace')
        self.assertEqual(sync.math_latex('b_(i,n)'), 'b_{i,n}')

    def test_interval_does_not_break_content_parser(self):
        content,end=sync.balanced('[Domain $[0, 1)$, `f(x)`.]',0)
        self.assertEqual(content,'Domain $[0, 1)$, `f(x)`.')

    def test_arrays_and_multiline_equations(self):
        self.assertIn(r'\begin{pmatrix}',sync.math_latex('mat(1, 2; 3, 4)'))
        self.assertIn(r'\begin{aligned}',sync.math_latex('a &= b \\\n &= c'))


if __name__=='__main__':
    unittest.main()
