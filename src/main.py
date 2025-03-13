from textnode import TextNode, TextType


def main():
    print(TextNode("This is some anchor text", TextType.LINK_TEXT, "https://www.boot.dev"))


main()
