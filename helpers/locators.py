from selenium.webdriver.common.by import By
from helpers.constants import ClassNames
from helpers.utils import css_selector_class_starts_with


class Locators:
    ERROR_MODAL = (
        By.CSS_SELECTOR,
        css_selector_class_starts_with(ClassNames.ERROR_MODAL)
    )
    
    LOAD_ICON = (
        By.CSS_SELECTOR,
        css_selector_class_starts_with(ClassNames.LOAD_ICON)
    )

    EPISODE_LIST_EMPTY = (
        By.CSS_SELECTOR,
        css_selector_class_starts_with(ClassNames.EPISODE_LIST_EMPTY)
    )
    
    EPISODE_LIST = (
        By.CSS_SELECTOR,
        css_selector_class_starts_with(ClassNames.EPISODE_LIST)
    )
