## Overview

This command-line tool retrieves episode links from one or more series currently streaming on [TVer](https://tver.jp/) and saves them to a text file, using **Selenium** and **Beautiful Soup**. Afterwards, it executes **yt-dlp** internally to download the episodes.

## Requirements

Assuming the CLI is in the **`tverbatch`** directory, install all required dependencies by running:

```sh
pip install -r requirements.txt
```

## Usage

Assuming the CLI is in the **`tverbatch`** directory, execute either of the following commands:

##### Using URL

```sh
python tver.py https://tver.jp/series/sr12345678 [https://tver.jp/series/sr23456789 ...]
```

##### Using Series ID

```sh
python tver.py sr12345678 [sr23456789 ...]
```

These commands will retrieve episode links from the provided series links and save them into **`tver.txt`**.
\
The episodes will then be downloaded to the **`downloads`** folder, with subtitles included where available.
