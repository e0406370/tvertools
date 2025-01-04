import pytest
from helpers import *
from tver import render_tver


@pytest.fixture(scope="session")
def shared_driver():

    with make_webdriver() as driver:
        yield driver


def test_render_tver_with_valid_series(shared_driver):

    render_status = render_tver(shared_driver, Tver.get_series_url(Tver.SERIES_ID["valid"]))

    assert render_status is True


def test_render_tver_with_invalid_series(shared_driver):

    render_status = render_tver(shared_driver, Tver.get_series_url(Tver.SERIES_ID["invalid"]))

    assert render_status is False


def test_render_tver_with_not_airing_series(shared_driver):

    render_status = render_tver(shared_driver, Tver.get_series_url(Tver.SERIES_ID["not_airing"]))

    assert render_status is False
