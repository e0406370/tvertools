import re, sys
from helpers.constants import TVER_VALID_URL


def validate_links(links):

    valid_links = []

    for link in links:
        if re.match(TVER_VALID_URL, link):
            valid_links.append(link)

        else:
            print(f"Warning: Invalid URL skipped - {link}")

    return valid_links


def compile_pattern(pattern):

    return re.compile(pattern)


def css_selector_class_starts_with(class_name):

    return f"[class^='{class_name}']"


def exit_script():

    print("\nExiting script...")
    sys.exit(1)
