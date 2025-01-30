from helpers import Tver
from tver import download_tver

TEST_EPISODE_URL = Tver.get_episode_url(Tver.TEST_EPISODE["valid"]["id"])
EXTRACTED_URL_MESSAGE = "[TVer] Extracting URL: %s"
ERROR_TAG = "ERROR"


def setup_download():

    with open("tver.txt", "w+") as file:
        file.write(TEST_EPISODE_URL)


# [download_tver] Verify extracted message and no errors are displayed in output
def test_download_tver(capsys):

    setup_download()
    download_tver(simulate=True)

    assert EXTRACTED_URL_MESSAGE % TEST_EPISODE_URL in capsys.readouterr().out
    assert ERROR_TAG not in capsys.readouterr().out
