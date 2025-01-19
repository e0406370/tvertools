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
    
    SERIES_TITLE = (
        By.CSS_SELECTOR,
        css_selector_class_starts_with(ClassNames.SERIES_TITLE)
    )
    
    SERIES_DESCRIPTION = (
        By.CSS_SELECTOR,
        css_selector_class_starts_with(ClassNames.SERIES_DESCRIPTION)
    )

    EPISODE_LIST_EMPTY = (
        By.CSS_SELECTOR,
        css_selector_class_starts_with(ClassNames.EPISODE_LIST_EMPTY)
    )
    
    EPISODE_LIST = (
        By.CSS_SELECTOR,
        css_selector_class_starts_with(ClassNames.EPISODE_LIST)
    )
    
    EPISODE_ROW = (
        By.CSS_SELECTOR,
        css_selector_class_starts_with(ClassNames.EPISODE_ROW)
    )
    
    EPISODE_ROW_TITLE = (
        By.CSS_SELECTOR,
        css_selector_class_starts_with(ClassNames.EPISODE_ROW_TITLE)
    )
    
    EPISODE_ROW_BROADCAST_DATE = (
        By.CSS_SELECTOR,
        css_selector_class_starts_with(ClassNames.EPISODE_ROW_BROADCAST_DATE)
    )
    
    EPISODE_ROW_END_DATE = (
        By.CSS_SELECTOR,
        css_selector_class_starts_with(ClassNames.EPISODE_ROW_END_DATE)
    )
