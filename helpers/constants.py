class Tver:
    BATCH_FILE = "tver.txt"
    BASE_URL = "https://tver.jp"

    VALID_EPISODE_URL = r"https?://(?:www\.)?tver\.jp/episodes/([a-zA-Z0-9]+)"
    VALID_EPISODE_ID = r"ep[a-z0-9]{8}"

    VALID_SERIES_URL = r"https?://(?:www\.)?tver\.jp/series/([a-zA-Z0-9]+)"
    VALID_SERIES_ID = r"sr[a-z0-9]{8}"

    TEST_SERIES = {
        "valid": {
            "id": "srtxft431v",
            "name": "名探偵コナン"
        },
        "valid_2": {
            "id": "srtsxzl3si", 
            "name": "ドラえもん"
        },
        "invalid": {
            "id": "sr12345678",
            "name": "invalid"
        },
        "not_airing": {
            "id": "sre9gy29cj",
            "name": "家族ゲーム"
        },
    }

    @classmethod
    def get_episode_url(cls, episode_id):
        return f"{cls.BASE_URL}/episodes/{episode_id}"

    @classmethod
    def get_series_url(cls, series_id):
        return f"{cls.BASE_URL}/series/{series_id}"


class ClassNames:
    ERROR_MODAL = "error-modal_message"
    LOAD_ICON = "loading_box"
    SERIES_TITLE = "series-main_title"

    EPISODE_LIST_EMPTY = "episode-live-list-column_empty"
    EPISODE_LIST = "episode-live-list-column_episodeList"

    EPISODE_ROW = "episode-row_container"
    EPISODE_ROW_TITLE = "episode-row_title"
    EPISODE_ROW_BROADCAST_DATE = "episode-row_broadcastDateLabel"


class Messages:
    USAGE = """
        Description:
            This script extracts episode links from series currently available on TVer and then downloads the corresponding episodes.
            
        Usage: 
            python tver.py URL [URL...]
            
            URL can be one of the following formats:
            - episode_url => https://tver.jp/episodes/ep12345678
            - episode_id => ep12345678 
            - series_url => https://tver.jp/series/sr12345678
            - series_id => sr12345678
            
        Repository:
            https://github.com/e0406370/tverbatch
    """

    WARNING_INVALID_URL_ID = "Warning: Invalid URL/ID skipped - %s"
    WARNING_NO_VALID_LINKS = "Warning: No valid links were found. Please provide at least one valid episode or series link."
    ERROR_INVALID_SERIES_ID = "Error: The provided series ID is invalid!"
    ERROR_NOT_AIRING_SERIES = "Error: This series is currently not airing!"

    PROCESS_EPISODE = "\nAdded %s to batch file."
    PROCESS_SERIES = "\nProcessing %s"
    PROCESS_DOWNLOAD = "\nStarting download..."

    SCRIPT_EXIT = "\nExiting script..."
    SCRIPT_COMPLETE = "\nScript completed."
