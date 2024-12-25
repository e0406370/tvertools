import re


def validate_links(links):
    from helpers.constants import TVER_VALID_URL

    valid_links = []

    for link in links:
        if re.match(TVER_VALID_URL, link):
            valid_links.append(link)
        else:
            print(f"Warning: Invalid URL skipped - {link}")

    return valid_links


def css_selector_class_starts_with(class_name):

    return f"[class^='{class_name}']"
