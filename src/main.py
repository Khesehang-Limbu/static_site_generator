import os
from utils import generate_page_recursive, copy_to_public
import sys

try:
    BASEPATH = sys.argv[1]
except Exception:
    BASEPATH = "/"


def main():
    if BASEPATH == "/":
        to_path = "public"
    else:
        to_path = "docs"

    copy_to_public("static", to_path)
    generate_page_recursive(BASEPATH, "content", "template.html", to_path)


if __name__ == "__main__":
    main()
