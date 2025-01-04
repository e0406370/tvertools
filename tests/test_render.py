from helpers import *
from tver import render_tver


def test_render_tver_valid_series():
    
    with make_webdriver() as driver:
        render_status = render_tver(driver, Tver.get_series_url(Tver.SERIES_ID["valid"]))

    assert render_status == True
