"""
    Extracts links from a series that is currently streaming on TVer into a text file, using Selenium and Beautiful Soup.
"""

import re, sys

from helpers import *
from bs4 import BeautifulSoup


def scrape_tver(link: str):

    driver = make_webdriver()
    driver.get(link)

    wait_element_invisible(driver, load_icon)
    # wait_element_visible(driver, episode_list)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    print(f"Title: {soup.select(f'[class^={ClassNames.SERIES_TITLE}]')[0].get_text()}")
    links = [
        TVER_BASE + (link.get("href"))
        for link in soup.find_all("a", class_=re.compile(ClassNames.EPISODE_ROW))
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
