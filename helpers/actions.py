from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def make_webdriver():

    opt = Options()
    opt.add_argument("--headless")  # activates the browser in the background
    opt.add_argument("--log-level=2")  # suppresses tensorflow-related messages

    driver = webdriver.Chrome(options=opt)
    return driver


def is_element_visible(driver, locator, timeout=2):

    try:
        wait_element_visible(driver, locator, timeout)
        return True

    except TimeoutException:
        return False


def wait_element_visible(driver, locator, timeout=10):

    wait = WebDriverWait(driver, timeout)
    wait.until(EC.visibility_of_element_located(locator))


def wait_element_invisible(driver, locator, timeout=10):

    wait = WebDriverWait(driver, timeout)
    wait.until(EC.invisibility_of_element_located(locator))
