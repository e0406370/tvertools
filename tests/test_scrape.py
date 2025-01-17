import pytest
from helpers import *
from tver import render_tver, scrape_tver


@pytest.fixture(scope="session")
def shared_driver():

    with make_webdriver() as driver:
        yield driver


@pytest.fixture
def setup_tver(shared_driver, capsys):

    series_url = Tver.get_series_url(Tver.TEST_SERIES["valid"]["id"])

    reset_batch()
    render_tver(shared_driver, series_url)
    scrape_tver(shared_driver)

    return capsys.readouterr().out


# scrape_tver -> Check series title in output
def test_scrape_tver_series_title(setup_tver):

    lines = setup_tver.strip().split("\n")

    series_name = Tver.TEST_SERIES["valid"]["name"]

    assert f"{series_name}" in lines[0], "scrape_tver should capture the series title"


# scrape_tver -> Check no. of episode links in output
def test_scrape_tver_num_links(shared_driver, setup_tver):

    lines = setup_tver.strip().split("\n")

    wait_element_visible(shared_driver, Locators.SERIES_DESCRIPTION)
    series_description = shared_driver.find_element(*Locators.SERIES_DESCRIPTION).text

    num_links = series_description[series_description.find(Tver.TOTAL_CHAR_1) + 1 : series_description.find(Tver.TOTAL_CHAR_2)]

    assert f"[{num_links}]" in lines[0], "scrape_tver should capture the no. of episode links"


# scrape_tver -> Check episode title in output
def test_scrape_tver_episode_title(setup_tver):

    lines = setup_tver.strip().split("\n")

    episode_title = Tver.TEST_EPISODE["valid"]["title"]

    assert f"{episode_title}" in lines[1], "scrape_tver should capture the episode title"


# scrape_tver -> Check broadcast date in output
def test_scrape_tver_broadcast_date(setup_tver):

    lines = setup_tver.strip().split("\n")

    broadcast_date = Tver.TEST_EPISODE["valid"]["start"]

    assert f"{broadcast_date}" in lines[1], "scrape_tver should capture the broadcast date"


# scrape_tver -> Check links are saved into batch file
def test_scrape_tver_links_saved(setup_tver):

    lines = setup_tver.strip().split("\n")

    with open(Tver.BATCH_FILE, "r+") as input:
        links = [link.strip() for link in input]

    for i in range(len(links)):
        assert links[i] in lines[i + 1], "scrape_tver should save the episode links into the batch file"
