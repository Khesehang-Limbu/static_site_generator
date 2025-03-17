import unittest
from utils import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_title_extraction_at_first_position(self):
        md = "# Tolkien Fan Club\n\n![JRR Tolkien sitting](/images/tolkien.png)\n\nHere's the deal, **I like Tolkien**."
        self.assertEqual(extract_title(md), "Tolkien Fan Club")

    def test_title_extraction_at_any_position(self):
        md = "![JRR Tolkien sitting](/images/tolkien.png)\n\n# Tolkien Fan Club\n\nHere's the deal, **I like Tolkien**."
        self.assertEqual(extract_title(md), "Tolkien Fan Club")


if __name__ == "__main__":
    unittest.main()
