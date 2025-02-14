from helpers import make_webdriver
from helpers import Tver, Messages
from tver import render_tver_episode, render_tver_series
import pytest


@pytest.fixture(scope="session")
def shared_driver():

    with make_webdriver() as driver:
        yield driver


# [render_tver_episode] Verify rendering succeeds for valid episode
def test_render_tver_valid_episode(shared_driver):

    episode_url = Tver.get_episode_url(Tver.TEST_EPISODE["valid"]["id"])
    render_status = render_tver_episode(shared_driver, episode_url)

    assert render_status is True, "render_tver_episode should return True for valid episode"


# [render_tver_episode] Verify rendering fails for invalid episode
def test_render_tver_invalid_episode(shared_driver, capsys):

    episode_url = Tver.get_episode_url(Tver.TEST_EPISODE["invalid"]["id"])
    render_status = render_tver_episode(shared_driver, episode_url)

    assert Messages.ERROR_INVALID_EPISODE_ID in capsys.readouterr().out, "Expected error message for invalid episode"
    assert render_status is False, "render_tver_episode should return False for invalid episode"
    

# [render_tver_series] Verify rendering succeeds for valid series
def test_render_tver_valid_series(shared_driver):

    series_url = Tver.get_series_url(Tver.TEST_SERIES["valid"]["id"])
    render_status = render_tver_series(shared_driver, series_url)

    assert render_status is True, "render_tver_series should return True for valid series"


# [render_tver_series] Verify rendering fails for invalid series
def test_render_tver_invalid_series(shared_driver, capsys):

    series_url = Tver.get_series_url(Tver.TEST_SERIES["invalid"]["id"])
    render_status = render_tver_series(shared_driver, series_url)

    assert Messages.ERROR_INVALID_SERIES_ID in capsys.readouterr().out, "Expected error message for invalid series"
    assert render_status is False, "render_tver_series should return False for invalid series"


# [render_tver_series] Verify rendering fails for not airing series
def test_render_tver_not_airing_series(shared_driver, capsys):

    series_url = Tver.get_series_url(Tver.TEST_SERIES["not_airing"]["id"])
    render_status = render_tver_series(shared_driver, series_url)

    assert Messages.ERROR_NOT_AIRING_SERIES in capsys.readouterr().out, "Expected error message for not airing series"
    assert render_status is False, "render_tver_series should return False for not airing series"
