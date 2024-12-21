from selenium.webdriver.common.by import By
from helpers.constants import ClassNames


class Locators:
    LOAD_ICON = (By.CSS_SELECTOR, f"[class^='{ClassNames.LOAD_ICON}']")

    EPISODE_LIST_EMPTY = (By.CSS_SELECTOR, f"[class^={ClassNames.EPISODE_LIST_EMPTY}]")
    EPISODE_LIST = (By.CSS_SELECTOR, f"[class^='{ClassNames.EPISODE_LIST}']")
