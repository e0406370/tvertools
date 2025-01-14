from helpers import *


def test_validate_links_episodes_valid_url():

    links = [
        Tver.get_episode_url(Tver.TEST_EPISODE["valid"]["id"])
    ]
    expected = links

    assert validate_links(links).get_all() == expected, "[episodes] validate_links should capture all valid links (URL format)"


def test_validate_links_episodes_valid_id():

    links = [
        Tver.TEST_EPISODE["valid"]["id"]
    ]
    expected = [Tver.get_episode_url(link) for link in links]

    assert validate_links(links).get_all() == expected, "[episodes] validate_links should capture all valid links (ID format)"


def test_validate_links_episodes_valid_invalid(capsys):

    links = [
        Tver.get_episode_url(Tver.TEST_EPISODE["valid"]["id"]),
        "abc123",
    ]
    expected = [Tver.get_episode_url(Tver.TEST_EPISODE["valid"]["id"])]

    assert validate_links(links).get_all() == expected, "[episodes] validate_links should capture valid links but not invalid links"

    output = capsys.readouterr().out

    for link in set(links).difference(expected):
        assert Messages.WARNING_INVALID_URL_ID % link in output, "[episodes] Expected warning message for invalid link"


def test_validate_links_series_valid_url():

    links = [
        Tver.get_series_url(Tver.TEST_SERIES["valid"]["id"]),
        Tver.get_series_url(Tver.TEST_SERIES["valid_2"]["id"]),
    ]
    expected = links

    assert validate_links(links).get_all() == expected, "[series] validate_links should capture all valid links (URL format)"


def test_validate_links_series_valid_id():

    links = [
        Tver.TEST_SERIES["valid"]["id"], 
        Tver.TEST_SERIES["valid_2"]["id"]
    ]
    expected = [Tver.get_series_url(link) for link in links]

    assert validate_links(links).get_all() == expected, "[series] validate_links should capture all valid links (ID format)"


def test_validate_links_series_valid_invalid(capsys):

    links = [
        Tver.get_series_url(Tver.TEST_SERIES["valid"]["id"]),
        "abc123",
    ]
    expected = [Tver.get_series_url(Tver.TEST_SERIES["valid"]["id"])]

    assert validate_links(links).get_all() == expected, "[series] validate_links should capture valid links but not invalid links"

    output = capsys.readouterr().out

    for link in set(links).difference(expected):
        assert Messages.WARNING_INVALID_URL_ID % link in output, "[series] Expected warning message for invalid link"

    
def test_validate_links_mixed_valid_url():

    links = [
        Tver.get_episode_url(Tver.TEST_EPISODE["valid"]["id"]),
        Tver.get_series_url(Tver.TEST_SERIES["valid"]["id"]),
    ]
    expected = links

    assert validate_links(links).get_all() == expected, "[mixed] validate_links should capture all valid links (URL format)"
    
    
def test_validate_links_mixed_valid_id():

    links = [
        Tver.TEST_EPISODE["valid"]["id"],
        Tver.TEST_SERIES["valid"]["id"],
    ]
    expected = [Tver.get_episode_url(links[0]), Tver.get_series_url(links[1])]

    assert validate_links(links).get_all() == expected, "[mixed] validate_links should capture all valid links (ID format)"   
    

def test_validate_links_mixed_valid_invalid(capsys):

    episodes = [
        Tver.get_episode_url(Tver.TEST_EPISODE["valid"]["id"]),
        Tver.TEST_EPISODE["valid"]["id"],
    ]
    series = [
        Tver.get_series_url(Tver.TEST_SERIES["valid"]["id"]),
        Tver.TEST_SERIES["valid"]["id"],
    ]
    invalid = [
        "https://www.google.com/",
        "abc123",
    ]

    links = [
        *episodes,
        *series,
        *invalid
    ]
    expected = [
        *[Tver.get_episode_url(Tver.TEST_EPISODE["valid"]["id"]), Tver.get_episode_url(Tver.TEST_EPISODE["valid"]["id"])],
        *[Tver.get_series_url(Tver.TEST_SERIES["valid"]["id"]), Tver.get_series_url(Tver.TEST_SERIES["valid"]["id"])]
    ]

    assert validate_links(links).get_all() == expected, "[mixed] validate_links should capture valid links but not invalid links"

    output = capsys.readouterr().out

    for link in invalid:
        assert Messages.WARNING_INVALID_URL_ID % link in output, "[mixed] Expected warning message for invalid link"


def test_validate_links_invalid_only(capsys):

    links = [
        "https://www.google.com/",
        "abc123",
    ]
    expected = []

    assert validate_links(links).get_all() == expected, "validate_links should not capture any invalid links (both URL and ID formats)"

    output = capsys.readouterr().out

    for link in links:
        assert Messages.WARNING_INVALID_URL_ID % link in output, "Expected warning message for invalid link"