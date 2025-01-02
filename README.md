## Overview

This command-line tool retrieves episode links from one or more series currently streaming on [TVer](https://tver.jp/) and saves them to a text file, using **Selenium** and **Beautiful Soup**. Afterwards, it executes **yt-dlp** internally to download the episodes.

## Requirements

Assuming the CLI is in the **`tverbatch`** directory, install all required dependencies by running:

```sh
pip install -r requirements.txt
```

## Usage

Assuming the CLI is in the **`tverbatch`** directory, execute the following command:

```sh
python tver.py https://tver.jp/series/abc123 [https://tver.jp/series/cde456...]
```

This command will retrieve episode links from the provided series links and save them to **`tver.txt`**.
\
The episodes will then be downloaded to the **`downloads`** folder, with subtitles included where available.
