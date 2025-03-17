import unittest
from textnode import TextType, TextNode
from utils import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_text_node(self):
        node = TextNode("This is a simple Test.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "text", TextType.TEXT)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a simple Test.", TextType.TEXT)
            ]
        )

    def test_bold_node(self):
        node = TextNode("This is a **simple Test** now.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("simple Test", TextType.BOLD),
                TextNode(" now.", TextType.TEXT),
            ]
        )

    def test_italic_node(self):
        node = TextNode("This is an _Italic Test_ now.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is an ", TextType.TEXT),
                TextNode("Italic Test", TextType.ITALIC),
                TextNode(" now.", TextType.TEXT),
            ]
        )

    def test_code_node(self):
        node = TextNode(
            "This is text with a `code block` word.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word.", TextType.TEXT),
            ]
        )


if __name__ == "__main__":
    unittest.main()
