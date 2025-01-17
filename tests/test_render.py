import pytest
from helpers import *
from tver import render_tver


@pytest.fixture(scope="session")
def shared_driver():

    with make_webdriver() as driver:
        yield driver


# render_tver -> Valid series
def test_render_tver_valid_series(shared_driver):

    series_url = Tver.get_series_url(Tver.TEST_SERIES["valid"]["id"])
    render_status = render_tver(shared_driver, series_url)

    assert render_status is True, "render_tver should return True for valid series"


# render_tver -> Invalid series
def test_render_tver_invalid_series(shared_driver, capsys):

    series_url = Tver.get_series_url(Tver.TEST_SERIES["invalid"]["id"])
    render_status = render_tver(shared_driver, series_url)

    assert Messages.ERROR_INVALID_SERIES_ID in capsys.readouterr().out, "Expected error message for invalid series"
    assert render_status is False, "render_tver should return False for invalid series"


# render_tver -> Not airing series
def test_render_tver_not_airing_series(shared_driver, capsys):

    series_url = Tver.get_series_url(Tver.TEST_SERIES["not_airing"]["id"])
    render_status = render_tver(shared_driver, series_url)

    assert Messages.ERROR_NOT_AIRING_SERIES in capsys.readouterr().out, "Expected error message for not airing series"
    assert render_status is False, "render_tver should return False for not airing series"
