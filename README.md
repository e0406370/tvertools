## Requirements:

- **`selenium`**
  - Install using `pip install selenium`.

- **`beautifulsoup4`**
  - Install using `pip install beautifulsoup4`.

- **`yt-dlp`**
  - Retrieve from [this repository](https://github.com/yt-dlp/yt-dlp).
  
## Usage:

Assuming the CLI is in the directory containing the **`yt-dlp`** executable and **`tverbatch`** folder, execute the following command:

```sh
python tverbatch/tver.py tver.jp/series/abc123 [tver.jp/series/cde456...] && yt-dlp --write-subs -a tver.txt
```