## Requirements:

- **`selenium`**
  - `install via pip`
  <pre>
- **`beautifulsoup4`**
  - `install via pip`
  <pre>
- **`yt-dlp`**
  - `retrieve from github.com/yt-dlp/yt-dlp`

## Usage:

Assuming the CLI is in the directory containing the **`yt-dlp`** executable and **`tverbatch`** folder, execute the following command:

```sh
python tverbatch/tver.py tver.jp/series/abc123 [tver.jp/series/cde456...] && yt-dlp --write-subs -a tver.txt
```