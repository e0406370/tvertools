from helpers.locators import Locator
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Driver:

    _instance = None

    def __init__(self):

        self._instance = None


    def __enter__(self):

        return self.get_instance()


    def __exit__(self, exc_type, exc_val, exc_tb):

        if self._instance:
            self._instance.quit()
            Driver._instance = None


    @classmethod
    def get_instance(cls) -> WebDriver:

        if cls._instance is None:
            cls._instance = cls.make_webdriver()

        return cls._instance


    @classmethod
    def make_webdriver(cls) -> WebDriver:

        opt = Options()
        # opt.add_argument("--headless")  # activates the browser in the background
        opt.add_argument("--log-level=2")  # suppresses TensorFlow-related messages

        driver = webdriver.Chrome(options=opt)
        return driver


    @classmethod
    def is_element_visible(cls, locator: Locator, timeout: float = 2) -> bool:

        try:
            cls.wait_element_visible(locator, timeout)
            return True

        except TimeoutException:
            return False


    @classmethod
    def wait_element_visible(cls, locator: Locator, timeout: float = 10) -> None:

        wait = WebDriverWait(cls._instance, timeout)
        wait.until(EC.visibility_of_element_located(locator))


    @classmethod
    def wait_element_invisible(cls, locator: Locator, timeout: float = 10) -> None:

        wait = WebDriverWait(cls._instance, timeout)
        wait.until(EC.invisibility_of_element_located(locator))


    @classmethod
    def get_element_text(cls, locator: Locator) -> str:

        return cls._instance.find_element(*locator).text


    @classmethod
    def get_element_attribute(cls, locator: Locator, attribute: str) -> str:

        return cls._instance.find_element(*locator).get_attribute(attribute)
