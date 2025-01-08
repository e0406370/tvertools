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

    render_tver(shared_driver, series_url)
    scrape_tver(shared_driver)

    return capsys.readouterr().out


def test_scrape_tver_series_title(setup_tver):

    series_name = Tver.TEST_SERIES["valid"]["name"]
    
    lines = setup_tver.strip().split("\n")
    
    assert lines[0] == f"{series_name} [{len(lines) - 1}]"
