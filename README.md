
# subtitles_downloader-py

A Python script to automatically download subtitles from all videos of a YouTube channel using the YouTube Data API v3.

## Features

- Downloads all available subtitles in the chosen language (default is Russian `ru`).
- Supports any language that YouTube provides subtitles for.
- Automatically saves each video's subtitles as a `.txt` file with timestamps.

## Requirements

- Python 3.8 or higher
- Libraries: youtube_transcript_api, requests

```bash
pip install youtube_transcript_api requests
```

## How to Use

1. Insert your YouTube API key into the `API_KEY` variable.
2. Run the script:

```bash
python subtitles_downloader.py
```

3. Paste the YouTube Channel URL:

```
https://www.youtube.com/channel/CHANNELID_HERE
```

> ❗ Important: Only use links like `https://www.youtube.com/channel/CHANNELID_HERE`.

To find the correct Channel ID:
- Open the channel page.
- Right-click > View Page Source.
- Search for `"channelId"`.
- Use the **last channelId** found at the bottom of the page.

4. Choose the subtitle language (e.g., `ru`, `en`, `de`).

5. Subtitles will be downloaded into the `/subtitles` folder.

## License

MIT License
