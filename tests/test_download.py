from helpers import Tver, Messages
from tver import download_tver, reset_batch
import pytest


# [download_tver] Verify extracted message and no warnings/errors are displayed, when at least one valid link is present in the batch file
def test_download_tver_with_link(capsys):
    
    episode_url = Tver.get_episode_url(Tver.TEST_EPISODE["valid"]["id"])
    
    with open(Tver.BATCH_FILE, "w+") as file:
        file.write(episode_url)
    
    download_tver(simulate=True)

    assert f"[TVer] Extracting URL: {episode_url}" in capsys.readouterr().out, "Expected extracted message when at least one valid link is present in the batch file"
    assert "WARNING" not in capsys.readouterr().out, "download_tver should not produce any warnings"
    assert "ERROR" not in capsys.readouterr().out, "download_tver should not produce any errors"


# [download_tver] Verify warning message is displayed and the script exits, when no valid links are present in the batch file
def test_download_tver_without_link(capsys):
    
    reset_batch()
    
    with pytest.raises(SystemExit) as exc_info:
        download_tver(simulate=True)

    assert Messages.WARNING_NO_VALID_LINKS in capsys.readouterr().out, "Expected warning message when no valid links are present in the batch file"
    assert exc_info.value.code == 1, "download_tver should exit with code 1 when no links are found"
