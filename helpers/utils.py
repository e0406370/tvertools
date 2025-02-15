import re, sys
from helpers.classes import Links
from helpers.constants import Tver, Messages

 
def validate_links(links: list[str]) -> Links:

    valid_episodes = []
    valid_series = []

    valid_episode_url = compile_pattern(Tver.VALID_EPISODE_URL)
    valid_episode_id = compile_pattern(Tver.VALID_EPISODE_ID)
    valid_series_url = compile_pattern(Tver.VALID_SERIES_URL)
    valid_series_id = compile_pattern(Tver.VALID_SERIES_ID)

    for link in links:
        if valid_episode_url.match(link):
            valid_episodes.append(link)

        elif valid_episode_id.match(link):
            valid_episodes.append(Tver.get_episode_url(link))

        elif valid_series_url.match(link):
            valid_series.append(link)

        elif valid_series_id.match(link):
            valid_series.append(Tver.get_series_url(link))

        else:
            print(Messages.WARNING_INVALID_URL_ID % link)

    return Links(valid_episodes, valid_series)


def compile_pattern(pattern: str) -> re.Pattern[str]:

    return re.compile(pattern)


def css_selector_class_starts_with(class_name: str) -> str:

    return f"[class^='{class_name}']"


def reset_batch() -> None:

    with open(Tver.BATCH_FILE, "w+"):
        pass


def exit_script() -> None:

    print(Messages.SCRIPT_EXIT)
    sys.exit(1)
