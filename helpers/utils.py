from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def make_webdriver():

    opt = Options()
    opt.add_argument("--headless")  # activates the browser in the background

    driver = webdriver.Chrome(options=opt)
    return driver


def wait_element_visible(driver, locator, timeout=10):

    wait = WebDriverWait(driver, timeout)
    wait.until(EC.visibility_of_element_located(locator))


def wait_element_invisible(driver, locator, timeout=10):

    wait = WebDriverWait(driver, timeout)
    wait.until(EC.invisibility_of_element_located(locator))
