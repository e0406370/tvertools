"""
    Extracts links from a series that is currently streaming on TVer into a text file, using Selenium and Beautiful Soup.
"""

import re, sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup


TVER_BASE = "https://tver.jp"
TVER_FILE = "tver.txt"


def make_webdriver():

    opt = Options()
    # opt.add_argument("--headless")  # activates the browser in the background

    driver = webdriver.Chrome(options=opt)
    return driver


def wait_element_visible(driver, by, locator, timeout=10):

    wait = WebDriverWait(driver, timeout)
    wait.until(EC.visibility_of_element_located((by, locator)))


def scrape_tver(link: str):

    driver = make_webdriver()
    driver.get(link)

    wait_element_visible(driver, By.CSS_SELECTOR, "[class^='episode-live-list-column_episodeList']")

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    print(f"Title: {soup.select('[class^=series-main_title]')[0].get_text()}")
    links = [
        TVER_BASE + (link.get("href"))
        for link in soup.find_all("a", class_=re.compile("episode-row_container"))
    ]
    print(f"Links ({len(links)}): {links}")

    with open(TVER_FILE, "w+") as output:
        for link in links:
            output.write(f"{link}\n")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python tver.py tver.jp/series/abc123")  # must be a series that is currently streaming
        sys.exit(1)

    link = sys.argv[1]

    scrape_tver(link)
