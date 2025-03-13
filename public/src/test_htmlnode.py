import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "Google")
        node1 = HTMLNode("a", "Google")
        self.assertEqual(node, node1)

    def test_not_eq(self):
        node = HTMLNode("a", "Google", [HTMLNode("img", "somethin")])
        node1 = HTMLNode("a", "Google", [HTMLNode("p", "Click Me")])
        self.assertNotEqual(node, node1)

    def test_prop_to_html(self):
        node = HTMLNode("a", "Google", props={
                        "href": "https://www.google.com",
                        "target": "_blank"
                        })

        self.assertEqual(node.props_to_html(),
                         ' href="https://www.google.com" target="_blank"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("p", "Hello, world!", {"class": "bg-red"})
        self.assertEqual(node.to_html(), '<p class="bg-red">Hello, world!</p>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),
                         "<div><span>child</span></div>")

    def test_to_html_with_children_and_props(self):
        child_node = LeafNode("span", "child", props={
                              "style": "font-size: 2rem;"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),
                         '<div><span style="font-size: 2rem;">child</span></div>')

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_grandchildren_and_child_with_props(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node], props={
                                "class": "text-center;", "style": "color: blue;"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span class="text-center;" style="color: blue;"><b>grandchild</b></span></div>',
        )


if __name__ == "__main__":
    unittest.main()
