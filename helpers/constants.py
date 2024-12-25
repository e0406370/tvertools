TVER_VALID_URL = r"https?://(?:www\.)?tver\.jp/series/([a-zA-Z0-9]+)"
TVER_BASE_URL = "https://tver.jp"
TVER_BATCH_FILE = "tver.txt"


class ClassNames:
    LOAD_ICON = "loading_box"
    SERIES_TITLE = "series-main_title"

    EPISODE_LIST_EMPTY = "episode-live-list-column_empty"
    EPISODE_LIST = "episode-live-list-column_episodeList"

    EPISODE_ROW = "episode-row_container"
    EPISODE_ROW_TITLE = "episode-row_title"
    EPISODE_ROW_BROADCAST_DATE = "episode-row_broadcastDateLabel"
