from selenium.webdriver.common.by import By
from helpers.utils import css_selector_class_starts_with


TVER_BASE = "https://tver.jp"
TVER_FILE = "tver.txt"


class ClassNames:
    LOAD_ICON = "loading_box"
    SERIES_TITLE = "series-main_title"

    EPISODE_LIST_EMPTY = "episode-live-list-column_empty"
    EPISODE_LIST = "episode-live-list-column_episodeList"
    EPISODE_ROW = "episode-row_container"


class Locators:
    LOAD_ICON = (By.CSS_SELECTOR, css_selector_class_starts_with(ClassNames.LOAD_ICON))

    EPISODE_LIST_EMPTY = (By.CSS_SELECTOR, css_selector_class_starts_with(ClassNames.EPISODE_LIST_EMPTY))
    EPISODE_LIST = (By.CSS_SELECTOR, css_selector_class_starts_with(ClassNames.EPISODE_LIST))
