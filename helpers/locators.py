from selenium.webdriver.common.by import By

from helpers.constants import ClassNames

load_icon = (By.CSS_SELECTOR, f"[class^='{ClassNames.LOAD_ICON}']")
episode_list = (By.CSS_SELECTOR, f"[class^='{ClassNames.EPISODE_LIST}']")
