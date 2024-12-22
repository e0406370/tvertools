"""
    Extracts links from one or more series currently streaming on TVer into a text file, using Selenium and Beautiful Soup.
"""

import re, sys

from helpers import *
from bs4 import BeautifulSoup


def render_tver(driver, link):

    driver.get(link)

    wait_element_invisible(driver, Locators.LOAD_ICON)

    if is_element_visible(driver, Locators.EPISODE_LIST_EMPTY):
        print(f"Error: The selected series is not currently available")
        sys.exit(1)

    wait_element_visible(driver, Locators.EPISODE_LIST)


def scrape_tver(driver):

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    print(f"Title: {soup.select(css_selector_class_starts_with(ClassNames.SERIES_TITLE))[0].get_text()}")
    links = [
        TVER_BASE + (link.get("href"))
        for link in soup.find_all("a", class_=re.compile(ClassNames.EPISODE_ROW))
    ]
    print(f"Links ({len(links)}): {links}")

    with open(TVER_FILE, "a+") as output:
        for link in links:
            output.write(f"{link}\n")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python tver.py tver.jp/series/abc123 [tver.jp/series/cde456...]")  # supports single link or multiple links
        sys.exit(1)

    links = sys.argv[1:]
    
    with open(TVER_FILE, "w+") as output:
        pass

    with make_webdriver() as driver:
        for link in links:
            print(f"\nProcessing link: {link}")

            render_tver(driver, link)
            scrape_tver(driver)
            
            print("\n")
