import unittest

from textnode import TextType, TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node3)

    def test_not_eq_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.BOLD, "http://www.google.com/")
        self.assertNotEqual(node, node3)


if __name__ == "__main__":
    unittest.main()
