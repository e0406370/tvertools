import re, sys
from helpers.constants import Tver


def validate_links(links):

    valid_links = []

    for link in links:
        if re.match(Tver.VALID_SERIES_URL, link):
            valid_links.append(link)
            
        elif re.match(Tver.VALID_SERIES_ID, link):
            valid_links.append(Tver.get_series_url(link))

        else:
            print(f"Warning: Invalid URL/ID skipped - {link}")

    return valid_links


def compile_pattern(pattern):

    return re.compile(pattern)


def css_selector_class_starts_with(class_name):

    return f"[class^='{class_name}']"


def exit_script():

    print("\nExiting script...")
    sys.exit(1)
