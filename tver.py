"""
    Extracts links from one or more series currently streaming on TVer into a text file, using Selenium and Beautiful Soup.
    Afterwards, it uses yt-dlp internally to download the episodes based on the extracted links. 
"""

from helpers import *
from bs4 import BeautifulSoup
import yt_dlp


def render_tver(driver, link):

    driver.get(link)

    if is_element_visible(driver, Locators.ERROR_MODAL):
        print(Messages.ERROR_INVALID_SERIES_ID)
        return False

    wait_element_invisible(driver, Locators.LOAD_ICON)

    if is_element_visible(driver, Locators.EPISODE_LIST_EMPTY):
        print(Messages.ERROR_NOT_AIRING_SERIES)
        return False

    wait_element_visible(driver, Locators.EPISODE_LIST)

    return True


def scrape_tver(driver):

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    series_title = soup.select_one(css_selector_class_starts_with(ClassNames.SERIES_TITLE)).get_text()
    episodes = [
        Episode(
            (
                Tver.BASE_URL + href
            ),
            (
                date.get_text()
                if (date := episode_container.select_one(css_selector_class_starts_with(ClassNames.EPISODE_ROW_BROADCAST_DATE)))
                else ""
            ),
            (
                title.get_text()
                if (title := episode_container.select_one(css_selector_class_starts_with(ClassNames.EPISODE_ROW_TITLE)))
                else ""
            )
        )
        for episode_container in soup.select(css_selector_class_starts_with(ClassNames.EPISODE_ROW))
        if (href := episode_container.get("href")) and "episodes" in href
    ]

    print(f"{series_title} [{len(episodes)}]")
    print("\n".join(str(epi) for epi in episodes))

    with open(Tver.BATCH_FILE, "a+") as output:
        for epi in episodes:
            output.write(f"{epi.episode_link}\n")


def download_tver():

    with open(Tver.BATCH_FILE, "r+") as input:
        links = input.readlines()

    ydl_opts = {
        "writesubtitles": True,
        "outtmpl": "downloads/%(title)s.%(ext)s",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(Messages.PROCESS_DOWNLOAD)
        ydl.download(links)


if __name__ == "__main__":

    reset_batch()

    if len(sys.argv) < 2:
        print(Messages.USAGE)
        exit_script()

    links = validate_links(sys.argv[1:])

    if not links.episodes and not links.series:
        print(Messages.WARNING_NO_VALID_LINKS)
        exit_script()

    if links.episodes:
        with open(Tver.BATCH_FILE, "a+") as output:
            for episode in links.episodes:
                print(Messages.PROCESS_EPISODE % episode)
                
                output.write(f"{episode}\n")

    if links.series:
        with make_webdriver() as driver:
            for series in links.series:
                print(Messages.PROCESS_SERIES % series)

                if render_tver(driver, series):
                    scrape_tver(driver)

    download_tver()

    print(Messages.SCRIPT_COMPLETE)
