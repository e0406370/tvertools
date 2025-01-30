from helpers import Tver
from tver import download_tver


# [download_tver] Verify extracted message and no warnings/errors are displayed in output
def test_download_tver(capsys):
    
    episode_url = Tver.get_episode_url(Tver.TEST_EPISODE["valid"]["id"])
    
    with open(Tver.BATCH_FILE, "w+") as file:
        file.write(episode_url)
    
    download_tver(simulate=True)

    assert f"[TVer] Extracting URL: {episode_url}" in capsys.readouterr().out, "download_tver should produce extracted message"
    assert "WARNING" not in capsys.readouterr().out, "download_tver should not produce any warnings"
    assert "ERROR" not in capsys.readouterr().out, "download_tver should not produce any errors"
