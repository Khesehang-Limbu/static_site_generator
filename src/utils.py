# Split Delimiter
# Now that we can convert TextNodes to HTMLNodes, we need to be able to create TextNodes from raw markdown strings. For example, the string:
#
# This is text with a **bolded phrase** in the middle
#
# Should become:
#
# [
#    TextNode("This is text with a ", TextType.TEXT),
#    TextNode("bolded phrase", TextType.BOLD),
#    TextNode(" in the middle", TextType.TEXT),
# ]
#
# We Don't Care About Nested Inline Elements
# Markdown parsers often support nested inline elements. For example, you can have a bold word inside of italics:
#
# This is an _italic and **bold** word_.
#
# For simplicity's sake, we won't allow it! If you want to extend the project to support multiple levels of nested inline text types, you're welcome to do so at the end of the project.
#
# Assignment
# Create a new function (I put this in a new code file, but you can organize your code as you please):
# def split_nodes_delimiter(old_nodes, delimiter, text_type):
#
# It takes a list of "old nodes", a delimiter, and a text type. It should return a new list of nodes, where any "text" type nodes in the input list are (potentially) split into multiple nodes based on the syntax. For example, given the following input:
#
# node = TextNode("This is text with a `code block` word", TextType.TEXT)
# new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
#
# new_nodes becomes:
#
# [
#    TextNode("This is text with a ", TextType.TEXT),
#    TextNode("code block", TextType.CODE),
#    TextNode(" word", TextType.TEXT),
# ]
#
# The beauty of this function is that it will take care of inline code, bold, and italic text, all in one! The logic is identical, the delimiter and matching text_type are the only thing that changes, e.g. ** for bold, _ for italic, and a backtick for code. Also, because it operates on an input list, we can call it multiple times to handle different types of delimiters. The order in which you check for different delimiters matters, which actually simplifies implementation.
#
# Write a bunch of tests. Be sure to test various types of delimiters.
# Run and submit the tests from the root of the project.
#
# Extract Links
# Time to extract the links and images from our Markdown using regex.
#
# Regex Examples (So You Have Them Handy)
# The findall function that will return a list of all the matches in a string.
#
# import re
# text = "I'm a little teapot, short and stout. Here is my handle, here is my spout."
# matches = re.findall(r"teapot", text)
# print(matches) # ['teapot']
#
# text = "My email is lane@example.com and my friend's email is hunter@example.com"
# matches = re.findall(r"(\w+)@(\w+\.\w+)", text)
# print(matches)  # [('lane', 'example.com'), ('hunter', 'example.com')]
#
# Use regexr.com for interactive regex testing, it breaks down each part of the pattern and explains what it does.
#
# Assignment
# Hint: There are spoilers in the tip section if you don't want to figure out the regex patterns yourself.
#
# Create a function extract_markdown_images(text) that takes raw markdown text and returns a list of tuples. Each tuple should contain the alt text and the URL of any markdown images. For example:
# text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
# print(extract_markdown_images(text))
# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
#
# Create a similar function extract_markdown_links(text) that extracts markdown links instead of images. It should return tuples of anchor text and URLs. For example:
# text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
# print(extract_markdown_links(text))
# [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
#
# Write a bunch of tests. Here's one for finding an image:
# def test_extract_markdown_images(self):
#    matches = extract_markdown_images(
#        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
#    )
#    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
#
# Run and submit the tests from the root of the project.

# Text to TextNodes
# Time to put all the "splitting" functions together into a function that can convert a raw string of markdown-flavored text into a list of TextNode objects.
#
# Assignment
# Create a text_to_textnodes(text) function. Here's some example input:
# This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)
#
# It should output this list of nodes:
#
# [
#    TextNode("This is ", TextType.TEXT),
#    TextNode("text", TextType.BOLD),
#    TextNode(" with an ", TextType.TEXT),
#    TextNode("italic", TextType.ITALIC),
#    TextNode(" word and a ", TextType.TEXT),
#    TextNode("code block", TextType.CODE),
#    TextNode(" and an ", TextType.TEXT),
#    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
#    TextNode(" and a ", TextType.TEXT),
#    TextNode("link", TextType.LINK, "https://boot.dev"),
# ]
#
# This function should be quite simple now that you've done all the hard work. Just use all your splitting functions one after the other.
#
# Write some tests.
# Run and submit the tests from the root of the project.

# Split Blocks
# Our grug-brain static site generator only cares about two things:
#
# Inline markdown
# Block markdown
# Inline markdown is what we just took care of. It's the stuff that's inside of a block. For example, the bolded text in this sentence is inline markdown.
#
# Block-level markdown is just the separation of different sections of an entire document. In well-written markdown (which we'll just assume is the only thing going into our generator) blocks are separated by a single blank line. Here are 3 distinct blocks:
#
# This is a heading
#
# This is a paragraph of text. It has some **bold** and _italic_ words inside of it.
#
# - This is the first list item in a list block
# - This is a list item
# - This is another list item
#
# The heading, the paragraph, and the unordered list are all separate blocks. The blank line between them is what separates them.
#
# Assignment
# Create a new function called markdown_to_blocks(markdown). It takes a raw Markdown string (representing a full document) as input and returns a list of "block" strings. The example above would be split into these three strings:
# This is a heading
#
# This is a paragraph of text. It has some **bold** and _italic_ words inside of it.
#
# - This is the first list item in a list block
# - This is a list item
# - This is another list item
#
# The .split() method can be used to split a string into blocks based on a delimiter (\n\n is a double newline).
# You should .strip() any leading or trailing whitespace from each block.
# Remove any "empty" blocks due to excessive newlines.
# Write tests for your function. Here's one to get you started:
# def test_markdown_to_blocks(self):
#    md = """
# This is **bolded** paragraph
#
# This is another paragraph with _italic_ text and `code` here
# This is the same paragraph on a new line
#
# - This is a list
# - with items
# """
#    blocks = markdown_to_blocks(md)
#    self.assertEqual(
#        blocks,
#        [
#            "This is **bolded** paragraph",
#            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
#            "- This is a list\n- with items",
#        ],
#    )
#
# Run and submit the tests from the root of the project.

# Block Types
# Our static site generator supports 6 types of markdown blocks:
#
# paragraph
# heading
# code
# quote
# unordered_list
# ordered_list
# We need a way to inspect a block of markdown text and determine what type of block it is.
#
# Assignment
# Create a BlockType enum with the block types from above.
#
# Create a block_to_block_type function that takes a single block of markdown text as input and returns the BlockType representing the type of block it is. You can assume all leading and trailing whitespace was already stripped (we did that in a previous lesson).
#
# Headings start with 1-6 # characters, followed by a space and then the heading text.
# Code blocks must start with 3 backticks and end with 3 backticks.
# Every line in a quote block must start with a > character.
# Every line in an unordered list block must start with a - character, followed by a space.
# Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.
# If none of the above conditions are met, the block is a normal paragraph.
# Write a bunch of unit tests for the function.
#
# Run and submit the CLI tests from the root of the project.

# Block to HTML
# I'm going to give you quite a few steps to do with a bit less guidance. I think you're a beautiful peacock and are ready for it.
#
# I'm a peacock from the other guys
#
# Assignment
# Create a new function called def markdown_to_html_node(markdown): that converts a full markdown document into a single parent HTMLNode. That one parent HTMLNode should (obviously) contain many child HTMLNode objects representing the nested elements.
#
# FYI: I created an additional 8 helper functions to keep my code neat and easy to understand, because there's a lot of logic necessary for markdown_to_html_node. I don't want to give you my exact functions because I want you to do this from scratch. However, I'll give you the basic order of operations:
#
# Split the markdown into blocks (you already have a function for this)
# Loop over each block:
# Determine the type of block (you already have a function for this)
# Based on the type of block, create a new HTMLNode with the proper data
# Assign the proper child HTMLNode objects to the block node. I created a shared text_to_children(text) function that works for all block types. It takes a string of text and returns a list of HTMLNodes that represent the inline markdown using previously created functions (think TextNode -> HTMLNode).
# The "code" block is a bit of a special case: it should not do any inline markdown parsing of its children. I didn't use my text_to_children function for this block type, I manually made a TextNode and used text_node_to_html_node.
# Make all the block nodes children under a single parent HTML node (which should just be a div) and return it.
# Create unit tests. Here are two to get you started:
# def test_paragraphs(self):
#    md = """
# This is **bolded** paragraph
# text in a p
# tag here
#
# This is another paragraph with _italic_ text and `code` here
#
# """
#
#    node = markdown_to_html_node(md)
#    html = node.to_html()
#    self.assertEqual(
#        html,
#        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
#    )
#
# def test_codeblock(self):
#    md = """
# ```
# This is text that _should_ remain
# the **same** even with inline stuff
# ```
# """
#
#    node = markdown_to_html_node(md)
#    html = node.to_html()
#    self.assertEqual(
#        html,
#        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
#    )
#
# Run and submit the tests from the root of the project.

import shutil
import os
from textnode import TextType, TextNode
from htmlnode import HTMLNode, ParentNode, LeafNode
from blocknode import BlockType
import re

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("TextNode Type Error")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        #        delimited_text = ""
        #        regular_text = ""
        #
        #        if delimiter is None or delimiter == "text":
        #            new_nodes.append(TextNode(node.text, TextType.TEXT))
        #            return new_nodes
        #
        #        text_list = node.text.split()
        #        for text in text_list:
        #            if delimiter in text:
        #                if delimiter in text[:2:] and delimiter in text[len(text)-3::]:
        #                    delimited_text = text
        #                elif delimiter in text[:2:]:
        #                    delimited_text += text + " "
        #                elif delimiter in text[len(text)-3::]:
        #                    delimited_text += text
        #
        #                if regular_text != "":
        #                    new_nodes.append(
        #                        TextNode(regular_text, text_type=TextType.TEXT))
        #                    regular_text = ""
        #
        #                if delimited_text != "" and delimiter in delimited_text[:2:] and delimiter in delimited_text[len(delimited_text)-3::]:
        #                    new_nodes.append(
        #                        TextNode(delimited_text.replace(delimiter, ""), text_type=get_delimited_type(delimiter)))
        #                    delimited_text = ""
        #            else:
        #                if text_list[-1] == text:
        #                    regular_text += " " + text
        #                else:
        #                    regular_text += text + " "
        #
        #        new_nodes.append(TextNode(regular_text, TextType.TEXT))

        original_text = node.text

        text_list = original_text.split(delimiter, maxsplit=2)

        if len(text_list) == 1:
            new_nodes.append(TextNode(node.text, node.text_type))

        while (len(text_list) == 3):
            new_nodes.append(TextNode(text_list[0], TextType.TEXT))
            new_nodes.append(
                TextNode(text_list[1], get_delimited_type(delimiter)))
            original_text = text_list[-1]
            text_list = original_text.split(delimiter, 2)

        if len(text_list) == 1 and text_list[0] != node.text:
            new_nodes.append(TextNode(text_list[-1], TextType.TEXT))
    return new_nodes


def get_delimited_type(delimiter):
    match delimiter:
        case TextType.TEXT.value:
            return TextType.TEXT
        case TextType.BOLD.value:
            return TextType.BOLD
        case TextType.LINK.value:
            return TextType.LINK
        case TextType.IMAGE.value:
            return TextType.IMAGE
        case TextType.ITALIC.value:
            return TextType.ITALIC
        case TextType.CODE.value:
            return TextType.CODE
        case _:
            raise Exception("Delimiter Invalid")


def extract_markdown_images(text):
    regex_image_md_pattern = r"!\[.+?\)"
    regex_alt_pattern = r"!\[(.+?)\]"
    regex_url_pattern = r"\((.+?)\)"
    image_mds = re.findall(regex_image_md_pattern, text)
    alt_link_list = []
    for md in image_mds:
        alt_text = re.findall(regex_alt_pattern, md)
        url_text = re.findall(regex_url_pattern, md)
        alt_link_list.append((alt_text[0], url_text[0]))
    return alt_link_list


def extract_markdown_links(text):
    regex_link_md_pattern = r"\[.+?\)"
    regex_anchor_pattern = r"\[(.+?)\]"
    regex_url_pattern = r"\((.+?)\)"
    link_mds = re.findall(regex_link_md_pattern, text)
    anchor_url_list = []

    for link in link_mds:
        anchor_text = re.findall(regex_anchor_pattern, link)
        url_text = re.findall(regex_url_pattern, link)
        anchor_url_list.append((anchor_text[0], url_text[0]))
    return anchor_url_list


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:

        # word_list = re.split(r"\s+(?=[^\[\]]*(?:\[|$))", node.text)

        images = extract_markdown_images(node.text)

        if len(images) == 0:
            new_nodes.append(TextNode(node.text, node.text_type, node.url))

        original_text = node.text
        word_list = []
        for image in images:
            word_list = original_text.split(f"![{image[0]}]({image[1]})", 1)
            new_nodes.append(TextNode(word_list[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            original_text = "".join(word_list[1])

        if original_text != node.text and original_text != "":
            new_nodes.append(TextNode(original_text, node.text_type))


#        for word in word_list:
#            image = extract_markdown_images(word)
#            if len(image) > 0:
#                new_nodes.append(TextNode(regular_text, TextType.TEXT))
#                new_nodes.append(
#                    TextNode(image[0][0], TextType.IMAGE, image[0][1]))
#                regular_text = " "
#            else:
#                if word == word_list[-1]:
#                    regular_text += " " + word
#                else:
#                    regular_text += word + " "
#        if regular_text != "" and regular_text != " ":
#            new_nodes.append(TextNode(regular_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)

        if len(links) == 0:
            new_nodes.append(TextNode(node.text, node.text_type, node.url))

        # Tried To Split with re.split()
#        word_list = re.split(r"\s+(?=[^\[\]]*(?:\[|$))", node.text)
        original_text = node.text
        for link in links:
            word_list = original_text.split(f"[{link[0]}]({link[1]})", 1)
            new_nodes.append(TextNode(word_list[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = "".join(word_list[1])

        if original_text != node.text and original_text != "":
            new_nodes.append(TextNode(original_text, node.text_type))

#            new_nodes.append(TextNode(word_list[0], TextType.TEXT))
#            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))

#        for word in word_list:
#            link = extract_markdown_links(word)
#            if len(link) > 0:
#                new_nodes.append(TextNode(regular_text, TextType.TEXT))
#                new_nodes.append(
#                    TextNode(link[0][0], TextType.LINK, link[0][1]))
#                regular_text = " "
#            else:
#                if word == word_list[-1]:
#                    regular_text += " " + word
#                else:
#                    regular_text += word + " "
#        if regular_text != "" and regular_text != " ":
#            new_nodes.append(TextNode(regular_text, TextType.TEXT))
    return new_nodes


def text_to_textnodes(text):
    node = [TextNode(text, TextType.TEXT)]
    new_nodes = split_nodes_delimiter(node, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes


def markdown_to_blocks(markdown):
    markdown_blocks = markdown.split("\n\n")
    markdown_blocks = [block.strip() for block in markdown_blocks]
    return list(filter(lambda block: block != "", markdown_blocks))


def block_to_block_type(markdown_block):
    if "# " in markdown_block[:7:]:
        return BlockType.HEADING
    elif "```" == markdown_block[:3:] and "```" == markdown_block[len(markdown_block)-3::]:
        return BlockType.CODE
    elif ">" == markdown_block[0]:
        return BlockType.QUOTE
    elif "- " == markdown_block[:2:]:
        ul = markdown_block.split("\n")
        is_ul = True
        for item in ul:
            if item[:2:] != "- ":
                is_ul = False
                break
        if is_ul:
            return BlockType.UNORDERED_LIST
    elif re.match("^\d. ", markdown_block):
        ol = markdown_block.split("\n")
        is_ol = True
        num = -1
        num_seq = []

        for item in ol:
            try:
                num = int(item[0])
                num_seq.append(num)
                if item[1:3:] != ". ":
                    is_ol = False
                    break
            except Exception:
                is_ol = False
        if num_seq != [i + 1 for i in range(len(ol))]:
            is_ol = False
        if is_ol:
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children_list = []

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type is not BlockType.CODE and block_type is not BlockType.UNORDERED_LIST and block_type is not BlockType.ORDERED_LIST and block_type is not BlockType.QUOTE:
            block = " ".join(block.split())
        html_node = block_to_html_node(block, block_type)
        children = text_to_children(block)
        if block_type is BlockType.CODE:
            texts = block.replace("```", "").split("\n")
            new_text = ""
            for text in texts:
                text = text.strip()
                if len(text) > 0:
                    new_text += text + "\n"
            children = text_node_to_html_node(
                TextNode(new_text, TextType.CODE))
            html_node.value = None
            html_node.children = [children]
            children_list.append(html_node)
            continue
        if len(children) != 0:
            html_node.value = None
            html_node.children = children
            children_list.append(html_node)
    return ParentNode("div", children_list)


def text_to_children(text):
    html_nodes = []
    children = text_to_textnodes(text)

    if text[0] == "-":
        text_list = text.split("\n")
        text_list = list(map(lambda t: t[2::], text_list))
        li_list = []
        for line in text_list:
            children = text_to_textnodes(line)
            li = ParentNode("li", [])
            li_children = []
            for child in children:
                li_children.append(text_node_to_html_node(child))
            li.children = li_children
            li_list.append(li)
        return li_list
    elif re.match("\d+. ", text):
        text_list = text.split("\n")
        text_list = list(map(lambda t: t[3::], text_list))
        li_list = []
        for line in text_list:
            children = text_to_textnodes(line)
            li = ParentNode("li", [])
            li_children = []
            for child in children:
                li_children.append(text_node_to_html_node(child))
            li.children = li_children
            li_list.append(li)
        return li_list
    elif text[0] == ">":
        text_list = text.split("\n")
        p_list = []
        for text in text_list:
            text = text.replace("> ", "")
            children = text_to_textnodes(text)
            p_children = []
            p = ParentNode("p", [])
            for child in children:
                p_children.append(text_node_to_html_node(child))

            p.children = p_children
            p_list.append(p)
        return p_list

    for child in children:
        try:
            if child.text[0] == "#":
                child.text = child.text.replace("#", "")[1::]
        except Exception:
            pass
        html_nodes.append(text_node_to_html_node(child))
    return html_nodes


def block_to_html_node(block, block_type):
    if block_type is BlockType.PARAGRAPH:
        return ParentNode("p", [])
    elif block_type is BlockType.HEADING:
        heading_symbols = block.split()[0]
        heading_number = len(
            "".join(list(filter(lambda char: char == "#", heading_symbols))))
        return block_to_heading_with_number(heading_number)
    elif block_type is BlockType.CODE:
        return ParentNode("pre", [])
    elif block_type is BlockType.QUOTE:
        return ParentNode("blockquote", [])
    elif block_type is BlockType.UNORDERED_LIST:
        return ParentNode("ul", [])
    elif block_type is BlockType.ORDERED_LIST:
        return ParentNode("ol", [])
    return ParentNode("p", [])


def block_to_heading_with_number(number):
    heading_chars = number * "#"
    return ParentNode(f"h{number}", [])


def extract_title(markdown):
    blocks = markdown.split("\n\n")
    for block in blocks:
        if "# " == block[:2:]:
            return block.replace("# ", "").strip()


def generate_page(basepath, from_path, template_path, to_path):
    print(f"Generating page from {from_path} to {
          to_path}, using {template_path}")
    template = ""
    markdown = ""
    with open(template_path) as file:
        template = file.read()
    with open(from_path) as file:
        markdown = file.read()
    html = markdown_to_html_node(markdown)
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title).replace(
        "{{ Content }}", html.to_html()).replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
    try:
        if os.path.exists(to_path):
            with open(os.path.join(to_path, "index.html"), "w") as file:
                file.write(template)
    except Exception as e:
        print("Error :", e)


def copy_to_public(source, destination):
    if os.path.exists(destination):
        # TODO 1: Delete the contents within public/
        try:
            shutil.rmtree(destination)
            # TODO 2: Create public/ dir and copy the new contents to it
            os.mkdir(destination)
            source_directories = os.listdir(source)
            for file in source_directories:
                src = os.path.join(source, file)
                dst = os.path.join(destination, file)
                if os.path.isfile(src):
                    try:
                        copied_path = shutil.copy(src, dst)
                        print(f"File: {file}, copied sucessfully, Destination: {
                              copied_path}")
                    except Exception as e:
                        print(e)
                else:
                    copy_to_public(src, dst)
        except Exception as e:
            print("Error: ", e)

    else:
        os.mkdir(destination)
        copy_to_public(source, destination)


def generate_page_recursive(basepath, dir_path_content, template_path, dest_dir_path):
    print(f"Generating Pages from: {dir_path_content}, using {
          template_path}, in {dest_dir_path}")
    content_list = os.listdir(dir_path_content)
    for item in content_list:
        source = os.path.join(dir_path_content, item)
        if os.path.isfile(source):
            generate_page(basepath, source, template_path, dest_dir_path)
        else:
            destination = os.path.join(dest_dir_path, item)
            os.mkdir(destination)
            generate_page_recursive(basepath, source, template_path, destination)
