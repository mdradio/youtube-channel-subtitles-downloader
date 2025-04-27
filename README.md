```markdown
# subtitles_downloader-py

A Python script to automatically download subtitles from all videos of a YouTube channel using the YouTube Data API v3.

## Features

- Downloads all available subtitles in the chosen language (`ru` by default).
- Automatically finds all videos on a channel by Channel ID.
- Saves subtitles into `.txt` files with timestamps.
- Supports Russian, English, German, and any language YouTube provides subtitles for.

## Requirements

- Python 3.8 or higher
- Installed libraries:
  ```bash
  pip install youtube_transcript_api requests
  ```

## Setup

1. Clone or download this repository.
2. Insert your YouTube API key into the `API_KEY` variable at the top of the `subtitles_downloader-py` script.

## How to use

1. Run the script:

   ```bash
   python subtitles_downloader-py
   ```

2. When prompted, paste the YouTube channel URL in this format:

   ```
   https://www.youtube.com/channel/CHANNELID_HERE
   ```

   > ❗ Important: **Do not use links like `@username` or `/videos`! Only `https://www.youtube.com/channel/CHANNELID_HERE` is accepted.**

   To find the correct **Channel ID**:
   - Open the channel page (`https://www.youtube.com/@channelname`)
   - Right-click > **View Page Source**
   - Search for `channelId`
   - **Use the last `channelId`** found in the page source (it's usually near the bottom).

3. Choose the subtitle language (e.g., `ru`, `en`, `de`).

4. Subtitles will be downloaded into the `/subtitles` folder.

## Example

Input:
```
Channel URL: https://www.youtube.com/channel/CHANNELID_HERE
Language: ru
```

Result:
- All available Russian subtitles are saved in `/subtitles/`, each file named after the video title.

---

## License

This project is licensed under the MIT License.
```

git push
```
