from helpers.locators import Locator
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def make_webdriver() -> WebDriver:

    opt = Options()
    opt.add_argument("--headless")  # activates the browser in the background
    opt.add_argument("--log-level=2")  # suppresses TensorFlow-related messages

    driver = webdriver.Chrome(options=opt)
    return driver


def is_element_visible(driver: WebDriver, locator: Locator, timeout: float = 2) -> bool:

    try:
        wait_element_visible(driver, locator, timeout)
        return True

    except TimeoutException:
        return False


def wait_element_visible(driver: WebDriver, locator: Locator, timeout: float = 10) -> None:

    wait = WebDriverWait(driver, timeout)
    wait.until(EC.visibility_of_element_located(locator))


def wait_element_invisible(driver: WebDriver, locator: Locator, timeout: float = 10) -> None:

    wait = WebDriverWait(driver, timeout)
    wait.until(EC.invisibility_of_element_located(locator))


def get_element_text(driver: WebDriver, locator: Locator) -> str:

    return driver.find_element(*locator).text


def get_element_attribute(driver: WebDriver, locator: Locator, attribute: str) -> str:

    return driver.find_element(*locator).get_attribute(attribute)
