import unittest
from utils import block_to_block_type
from blocknode import BlockType


class TestBlockToBlockType(unittest.TestCase):
    def test_block_paragraph(self):
        markdown_text = "This is a block"
        self.assertEqual(block_to_block_type(
            markdown_text), BlockType.PARAGRAPH)

    def test_block_headings(self):
        markdown_text = "# This is a heading"
        self.assertEqual(block_to_block_type(
            markdown_text), BlockType.HEADING)
        markdown_text = "#! This is not a heading"
        self.assertNotEqual(block_to_block_type(
            markdown_text), BlockType.HEADING)
        markdown_text = "## This is a heading 2"
        self.assertEqual(block_to_block_type(
            markdown_text), BlockType.HEADING)
        markdown_text = "### This is a heading 3"
        self.assertEqual(block_to_block_type(
            markdown_text), BlockType.HEADING)
        markdown_text = "#### This is a heading 4"
        self.assertEqual(block_to_block_type(
            markdown_text), BlockType.HEADING)
        markdown_text = "##### This is a heading 5"
        self.assertEqual(block_to_block_type(
            markdown_text), BlockType.HEADING)
        markdown_text = "###### This is a heading 6"
        self.assertEqual(block_to_block_type(
            markdown_text), BlockType.HEADING)
        markdown_text = "####### This is not heading"
        self.assertNotEqual(block_to_block_type(
            markdown_text), BlockType.HEADING)
        markdown_text = "########## This is not heading"
        self.assertNotEqual(block_to_block_type(
            markdown_text), BlockType.HEADING)

    def test_block_code(self):
        markdown_text = "```This is code```"
        self.assertEqual(block_to_block_type(
            markdown_text), BlockType.CODE)
        markdown_text = "``This is not code``"
        self.assertNotEqual(block_to_block_type(
            markdown_text), BlockType.CODE)
        markdown_text = "`#This is not code#`"
        self.assertNotEqual(block_to_block_type(
            markdown_text), BlockType.CODE)

    def test_block_quote(self):
        markdown_text = ">This is quote"
        self.assertEqual(block_to_block_type(
            markdown_text), BlockType.QUOTE)
        markdown_text = "#>This is quote"
        self.assertNotEqual(block_to_block_type(
            markdown_text), BlockType.QUOTE)

    def test_block_unordered_list(self):
        markdown_text = "- This is ul1\n- This is ol2"
        self.assertEqual(block_to_block_type(
            markdown_text), BlockType.UNORDERED_LIST)
        markdown_text = "- This is ul1\n-1 This is ol2"
        self.assertNotEqual(block_to_block_type(
            markdown_text), BlockType.UNORDERED_LIST)
        markdown_text = "-1 This is ul1\n-1 This is ol2"
        self.assertNotEqual(block_to_block_type(
            markdown_text), BlockType.UNORDERED_LIST)

    def test_block_ordered_list(self):
        markdown_text = "1. This is ol1\n2. This is ol2"
        self.assertEqual(block_to_block_type(
            markdown_text), BlockType.ORDERED_LIST)

        markdown_text = "1. This is ol1\n2!. This is ol2"
        self.assertNotEqual(block_to_block_type(
            markdown_text), BlockType.ORDERED_LIST)

        markdown_text = "1. This is ol1\n3. This is ol2"
        self.assertNotEqual(block_to_block_type(
            markdown_text), BlockType.ORDERED_LIST)

        markdown_text = "*. This is ol1\n3. This is ol2"
        self.assertNotEqual(block_to_block_type(
            markdown_text), BlockType.ORDERED_LIST)


if __name__ == "__main__":
    unittest.main()
