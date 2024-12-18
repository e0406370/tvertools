"""
  1. Execute the following commands in a terminal:
    pip install selenium
    pip install beautifulsoup4
    
  2. tver.txt must be in the same directory as tver.py
"""

import re, sys, time

TVER_BASE = "https://tver.jp"
TVER_FILE = "tver.txt"


def make_webdriver():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    opt = Options()
    opt.add_argument("--headless")  # activates the browser in the background

    driver = webdriver.Chrome(options=opt)
    return driver


def scrape_tver(link: str):
    from bs4 import BeautifulSoup

    driver = make_webdriver()
    driver.get(link)
    time.sleep(5)

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
