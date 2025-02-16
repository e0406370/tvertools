from helpers import Driver, Tver, Locators
from helpers import reset_batch
from tver import render_tver_series, scrape_tver
import pytest


@pytest.fixture(scope="session", autouse=True)
def shared_driver():

    with Driver():
        pass


@pytest.fixture
def setup_tver(capsys):

    series_url = Tver.get_series_url(Tver.TEST_SERIES["valid"]["id"])

    reset_batch()
    render_tver_series(series_url)
    scrape_tver()

    return capsys.readouterr().out


# [scrape_tver] Verify series title is displayed in output
def test_scrape_tver_series_title(setup_tver):

    lines = setup_tver.strip().split("\n")

    series_name = Tver.TEST_SERIES["valid"]["name"]

    assert f"{series_name}" in lines[0], "scrape_tver should capture the series title"


# [scrape_tver] Verify no. of episode links is displayed in output
def test_scrape_tver_num_links(setup_tver):

    lines = setup_tver.strip().split("\n")

    Driver.wait_element_visible(Locators.SERIES_DESCRIPTION)
    series_description = Driver.get_element_text(Locators.SERIES_DESCRIPTION)

    num_links = series_description[series_description.find(Tver.TOTAL_CHAR_1) + 1 : series_description.find(Tver.TOTAL_CHAR_2)]

    assert f"[{num_links}]" in lines[0], "scrape_tver should capture the no. of episode links"


# [scrape_tver] Verify episode link is displayed in output
def test_scrape_tver_episode_link(setup_tver):

    lines = setup_tver.strip().split("\n")

    episode_link = Tver.get_episode_url(Tver.TEST_EPISODE["valid"]["id"])

    assert f"{episode_link}" in lines[1], "scrape_tver should capture the episode link"


# [scrape_tver] Verify broadcast date is displayed in output
def test_scrape_tver_broadcast_date(setup_tver):

    lines = setup_tver.strip().split("\n")

    broadcast_date = Tver.TEST_EPISODE["valid"]["broadcast"]

    assert f"{broadcast_date}" in lines[1], "scrape_tver should capture the broadcast date"


# [scrape_tver] Verify episode title is displayed in output
def test_scrape_tver_episode_title(setup_tver):

    lines = setup_tver.strip().split("\n")

    episode_title = Tver.TEST_EPISODE["valid"]["title"]

    assert f"{episode_title}" in lines[1], "scrape_tver should capture the episode title"


# [scrape_tver] Verify episode links are saved into the batch file
def test_scrape_tver_links_saved(setup_tver):

    lines = setup_tver.strip().split("\n")

    with open(Tver.BATCH_FILE, "r+") as input:
        links = [link.strip() for link in input]

    for i in range(len(links)):
        assert links[i] in lines[i + 1], "scrape_tver should save the episode links into the batch file"
