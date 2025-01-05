import re, sys
from helpers.constants import Tver, Messages


def validate_links(links):

    valid_links = []

    for link in links:
        if re.match(Tver.VALID_SERIES_URL, link):
            valid_links.append(link)
            
        elif re.match(Tver.VALID_SERIES_ID, link):
            valid_links.append(Tver.get_series_url(link))

        else:
            print(Messages.WARNING_INVALID_URL_ID % link)

    return valid_links


def compile_pattern(pattern):

    return re.compile(pattern)


def css_selector_class_starts_with(class_name):

    return f"[class^='{class_name}']"


def exit_script():

    print(Messages.SCRIPT_EXIT)
    sys.exit(1)
