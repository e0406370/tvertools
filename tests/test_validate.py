from helpers import *


def test_validate_links_valid_url():

    links = [
        Tver.get_series_url(Tver.TEST_SERIES["valid"]["id"]),
        Tver.get_series_url(Tver.TEST_SERIES["valid_2"]["id"]),
    ]
    expected = links

    assert validate_links(links) == expected, "validate_links should capture all valid links (URL format)"


def test_validate_links_valid_id():

    links = [
        Tver.TEST_SERIES["valid"]["id"], 
        Tver.TEST_SERIES["valid_2"]["id"]
    ]
    expected = [Tver.get_series_url(link) for link in links]
    
    assert validate_links(links) == expected, "validate_links should capture all valid links (ID format)"


def test_validate_links_invalid_url_id(capsys):
  
    links = [
        "https://www.google.com/",
        "ep12345678",
    ]
    expected = []
    
    assert validate_links(links) == expected, "validate_links should not capture any invalid links (both URL and ID formats)"

    output = capsys.readouterr().out
    
    for link in links:
        assert Messages.WARNING_INVALID_URL_ID % link in output, "Expected warning message for invalid link"


def test_validate_links_mixed(capsys):
  
    links = [
        Tver.get_series_url(Tver.TEST_SERIES["valid"]["id"]),
        "ep12345678",
    ]
    expected = [Tver.get_series_url(Tver.TEST_SERIES["valid"]["id"])]
    
    assert validate_links(links) == expected, "validate_links should capture valid links but not invalid links"

    output = capsys.readouterr().out
    
    for link in set(links).difference(expected):
        assert Messages.WARNING_INVALID_URL_ID % link in output, "Expected warning message for invalid link"
