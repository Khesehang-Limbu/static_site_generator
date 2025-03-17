import os
import shutil
from utils import BASE_DIR, generate_page_recursive, copy_to_public


def main():
    static_path = os.path.join(BASE_DIR, "static")
    public_path = os.path.join(BASE_DIR, "public")
    template_path = os.path.join(BASE_DIR, "template.html")
    copy_to_public(static_path, public_path)

    generate_page_recursive(os.path.join(BASE_DIR, "content"),
                            template_path, public_path)


if __name__ == "__main__":
    main()
