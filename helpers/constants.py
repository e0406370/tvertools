class Tver:
    BATCH_FILE = "tver.txt"

    BASE_URL = "https://tver.jp"
    VALID_SERIES_URL = r"https?://(?:www\.)?tver\.jp/series/([a-zA-Z0-9]+)"

    SERIES_ID = {
        "valid": "srtxft431v",  # 名探偵コナン
        "invalid": "s123456789",
        "not_airing": "sre9gy29cj",  # 家族ゲーム
    }

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
    ERROR_INVALID_SERIES_ID = "Error: The provided series ID is invalid!"
    ERROR_NOT_AIRING_SERIES = "Error: This series is currently not airing!"
