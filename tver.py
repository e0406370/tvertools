"""
    Extracts links from one or more series currently streaming on TVer into a text file, using Selenium and Beautiful Soup.
"""

from helpers import *
from bs4 import BeautifulSoup


def render_tver(driver, link):

    driver.get(link)
    
    if is_element_visible(driver, Locators.ERROR_MODAL):
        print(f"Error: The provided series ID is invalid!")
        return False

    wait_element_invisible(driver, Locators.LOAD_ICON)

    if is_element_visible(driver, Locators.EPISODE_LIST_EMPTY):
        print(f"Error: This series is currently unavailable!")
        return False

    wait_element_visible(driver, Locators.EPISODE_LIST)
    
    return True


def scrape_tver(driver):

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    series_title = soup.select(css_selector_class_starts_with(ClassNames.SERIES_TITLE))[0].get_text()
    links = [
        TVER_BASE_URL + (link.get("href"))
        for link in soup.find_all("a", class_=compile_pattern(ClassNames.EPISODE_ROW))
    ]

    print(f"{series_title} [{len(links)}]")
    for i in range(len(links)):
        episode_link = links[i]
        episode_broadcast_date = soup.select(css_selector_class_starts_with(ClassNames.EPISODE_ROW_BROADCAST_DATE))[i].get_text()
        episode_title = soup.select(css_selector_class_starts_with(ClassNames.EPISODE_ROW_TITLE))[i].get_text()
        print(f"{episode_link} | {episode_broadcast_date} | {episode_title}")

    with open(TVER_BATCH_FILE, "a+") as output:
        for link in links:
            output.write(f"{link}\n")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python tver.py tver.jp/series/abc123 [tver.jp/series/cde456...]")  # supports single link or multiple links
        exit_script()

    links = validate_links(sys.argv[1:])
    if not links:
        exit_script()
    
    with open(TVER_BATCH_FILE, "w+") as output:
        pass

    with make_webdriver() as driver:
        for link in links:
            print(f"\nProcessing {link}")

            if render_tver(driver, link):
                scrape_tver(driver)                
        
        print(f"\nScript completed.")
