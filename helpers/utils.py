import re, sys
from helpers.classes import Links
from helpers.constants import Tver, Messages


def validate_links(links):

    valid_episodes = []
    valid_series = []

    for link in links:
        if re.match(Tver.VALID_EPISODE_URL, link):
            valid_episodes.append(link)

        elif re.match(Tver.VALID_EPISODE_ID, link):
            valid_episodes.append(Tver.get_episode_url(link))

        elif re.match(Tver.VALID_SERIES_URL, link):
            valid_series.append(link)

        elif re.match(Tver.VALID_SERIES_ID, link):
            valid_series.append(Tver.get_series_url(link))

        else:
            print(Messages.WARNING_INVALID_URL_ID % link)

    return Links(valid_episodes, valid_series)


def compile_pattern(pattern):

    return re.compile(pattern)


def css_selector_class_starts_with(class_name):

    return f"[class^='{class_name}']"


def reset_batch():

    with open(Tver.BATCH_FILE, "w+"):
        pass


def exit_script():

    print(Messages.SCRIPT_EXIT)
    sys.exit(1)
