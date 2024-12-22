Requirements:
- `selenium`
  - `install via pip`
  
- `beautifulsoup4`
  - `install via pip`
  
- `yt-dlp`
  - `retrieve from github.com/yt-dlp/yt-dlp`

Assuming the CLI is in the directory containing the `yt-dlp` executable and `tverbatch` folder, execute the following command:

```sh
python tverbatch/tver.py tver.jp/series/abc123 && yt-dlp --write-subs -a tver.txt
```