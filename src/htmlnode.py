"""

HTMLNode
Next, we need a way to represent HTML nodes.

Our "TextNode" class represents the various types of inline text that can exist in HTML and Markdown.
Our "HTMLNode" class will represent a "node" in an HTML document tree (like a <p> tag and its contents, or an <a> tag and its contents). It can be block level or inline, and is designed to only output HTML.
Assignment
Create a new file called htmlnode.py in the src directory and define a class called HTMLNode in it.

The HTMLNode class should have 4 data members set in the constructor:

tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
children - A list of HTMLNode objects representing the children of this node
props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
Perhaps counterintuitively, every data member should be optional and default to None:

An HTMLNode without a tag will just render as raw text
An HTMLNode without a value will be assumed to have children
An HTMLNode without children will be assumed to have a value
An HTMLNode without props simply won't have any attributes
Add a to_html(self) method. For now, it should just raise a NotImplementedError. Child classes will override this method to render themselves as HTML.

Add a props_to_html(self) method. It should return a string that represents the HTML attributes of the node. For example, if self.props is:

{
    "href": "https://www.google.com",
    "target": "_blank",
}

Then self.props_to_html() should return:

 href="https://www.google.com" target="_blank"

Notice the leading space character before href and before target. This is important. HTML attributes are always separated by spaces.

Add a __repr__(self) method. Give yourself a way to print an HTMLNode object and see its tag, value, children, and props. This will be useful for your debugging.
Create some tests for the HTMLNode class (at least 3). I used a new file called src/test_htmlnode.py. Create a few nodes and make sure the props_to_html method works as expected.
When you're satisfied that your class is behaving as expected and your unit tests are running successfully, run and submit the tests.


LeafNode
Time to render some HTML strings!

A LeafNode is a type of HTMLNode that represents a single HTML tag with no children. For example, a simple <p> tag with some text inside of it:

<p>This is a paragraph of text.</p>

We call it a "leaf" node because it's a "leaf" in the tree of HTML nodes. It's a node with no children. In this next example, <p> is not a leaf node, but <b> is.

<p>
  This is a paragraph. It can have a lot of text inside tbh.
  <b>This is bold text.</b>
  This is the last sentence.
</p>

Assignment
Create a child class of HTMLNode called LeafNode. Its constructor should differ slightly from the HTMLNode class because:

It should not allow for any children
The value data member should be required (and tag even though the tag's value may be None)
Use the super() function to call the constructor of the HTMLNode class.

Add a .to_html() method that renders a leaf node as an HTML string (by returning a string).

If the leaf node has no value, it should raise a ValueError. All leaf nodes must have a value.
If there is no tag (e.g. it's None), the value should be returned as raw text.
Otherwise, it should render an HTML tag. For example, these leaf nodes:
LeafNode("p", "This is a paragraph of text.").to_html()
"<p>This is a paragraph of text.</p>"

LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
"<a href="https://www.google.com">Click me!</a>"

Add some tests. Here's one to get you started:
def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

Add more tests for different tag types.

Once everything is working as intended, run and submit the tests from the root of the project.

ParentNode
I heard you like recursion.

types of headaches recursion meme

Our new ParentNode class will handle the nesting of HTML nodes inside of one another. Any HTML node that's not "leaf" node (i.e. it has children) is a "parent" node.

Assignment
Create another child class of HTMLNode called ParentNode. Its constructor should differ from HTMLNode in that:
The tag and children arguments are not optional
It doesn't take a value argument
props is optional
(It's the exact opposite of the LeafNode class)
Add a .to_html method.
If the object doesn't have a tag, raise a ValueError.
If children is a missing value, raise a ValueError with a different message.
Otherwise, return a string representing the HTML tag of the node and its children. This should be a recursive method (each recursion being called on a nested child node). I iterated over all the children and called to_html on each, concatenating the results and injecting them between the opening and closing tags of the parent.
For example, this node and its children:

node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

node.to_html()

Should convert to:

<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>

Don't worry about indentation or pretty-printing. If pretty-printed it would look like this:

<p>
  <b>Bold text</b>
  Normal text
  <i>italic text</i>
  Normal text
</p>

Most editors are easily configured to auto-format HTML on save, so we won't worry about implementing that in our code.

I wrote many tests for this class. I recommend you do the same, there is a lot of room for error. Test all the edge cases you can think of, including nesting ParentNode objects inside of one another, multiple children, and no children. Here's a couple to get you started:
def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )

Once you're happy that everything is working as intended, run and submit the tests from the root of the project.

"""


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        html = " "
        for key, value in self.props.items():
            html += f'{key}="{value}" '
        return html[:len(html)-1:]

    def __eq__(self, other_node):
        if self.tag == other_node.tag and self.value == other_node.value and self.children == other_node.children and self.props == other_node.props:
            return True
        return False

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        properties = ""
        if self.value is None:
            raise ValueError("Leaf Node is required to have a value.")
        if self.tag is None:
            return self.value
        if self. props is not None:
            properties = self.props_to_html()
        return f"<{self.tag}{properties}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode should have a tag")

        if self.children is None:
            raise ValueError("ParentNode must have children")

        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        properties = ""
        if self.props:
            properties = self.props_to_html()

        return f'<{self.tag}{properties}>{children_html}</{self.tag}>'
