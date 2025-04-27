# Youtube Channel Subtitles Downloader (subtitles_downloader-py)

import os
import re
import requests
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

# Insert your API key here
API_KEY = 'YOUR_API_KEY_HERE'  # <-- Replace with your own YouTube Data API v3 key

def sanitize_filename(name):
    # Removes forbidden characters from filenames
    return re.sub(r'[\\/*?\"<>|]', "", name)

def get_channel_id_from_url(url):
    # Extracts the channel ID from the page source of the provided URL
    try:
        response = requests.get(url)
        if response.status_code == 200:
            matches = re.findall(r'"channelId":"(UC[^"]+)"', response.text)
            if matches:
                # Important: the correct channel ID is usually the last one found on the page
                return matches[-1]
            else:
                print("❌ Could not find channelId on the page.")
                return None
        else:
            print(f"❌ Error loading channel page: {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ Error getting channelId: {e}")
        return None

def get_all_video_ids(channel_id):
    # Fetches all video IDs from a given channel ID using YouTube Data API
    video_ids = []
    base_url = 'https://www.googleapis.com/youtube/v3/search'
    next_page_token = ''

    while True:
        params = {
            'key': API_KEY,
            'channelId': channel_id,
            'part': 'id',
            'order': 'date',
            'maxResults': 50,
            'pageToken': next_page_token
        }
        response = requests.get(base_url, params=params).json()

        for item in response.get('items', []):
            if item['id']['kind'] == 'youtube#video':
                video_ids.append(item['id']['videoId'])

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    return video_ids

def download_all_subtitles(channel_url, language='ru'):
    try:
        if '?' in channel_url:
            channel_url = channel_url.split('?')[0]
        if '/featured' in channel_url or '/videos' in channel_url or '/about' in channel_url or '/community' in channel_url:
            channel_url = '/'.join(channel_url.split('/')[:4])

        if '/channel/' not in channel_url:
            channel_id = get_channel_id_from_url(channel_url)
            if not channel_id:
                print("❌ Failed to retrieve channelId. Exiting.")
                return
        else:
            channel_id = channel_url.split('/channel/')[1]

        video_ids = get_all_video_ids(channel_id)

        print(f"\n📹 Found videos: {len(video_ids)}")

        if not os.path.exists("subtitles"):
            os.makedirs("subtitles")

        for video_id in video_ids:
            try:
                video_info = requests.get(f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={API_KEY}").json()
                video_title = sanitize_filename(video_info['items'][0]['snippet']['title'])

                print(f"\n📄 Processing: {video_title}")

                transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])

                with open(f"subtitles/{video_title}.txt", "w", encoding="utf-8") as f:
                    for entry in transcript:
                        start_time = int(entry['start'])
                        minutes = start_time // 60
                        seconds = start_time % 60
                        f.write(f"[{minutes:02}:{seconds:02}] {entry['text']}\n")

                print("✅ Subtitles saved!")

            except TranscriptsDisabled:
                print("❌ No subtitles available in the selected language. Skipping.")
            except Exception as e:
                print(f"❌ Error with video {video_id}: {e}")

    except Exception as e:
        print(f"❌ Error loading channel: {e}")

if __name__ == "__main__":
    print("\n🚀 Welcome to the YouTube Channel Subtitles Downloader!")
    channel_link = input("\nPaste the channel URL (e.g., https://www.youtube.com/channel/CHANNELID_HERE): ").strip()
    # Set the subtitle language code (e.g., 'ru' for Russian, 'en' for English, 'de' for German)
    language_code = input("\nEnter subtitle language code (default 'ru' for Russian): ").strip()
    if not language_code:
        language_code = 'ru'
    download_all_subtitles(channel_link, language=language_code)
    input("\n👋 Press Enter to exit...")

"""
How to use:

1. Clone or download this repository.
2. Install required Python libraries:
   pip install youtube_transcript_api requests
3. Insert your YouTube API key into the 'API_KEY' variable at the top of the script.
4. Run the script. Paste the YouTube channel URL when prompted.

Important:
- To change the subtitle language, provide the ISO language code when asked (e.g., 'en' for English, 'de' for German, 'ru' for Russian).
- How to find the correct Channel ID: 
  Open the channel page (https://www.youtube.com/@channelname), view the source code (right-click > View Source), search for "channelId". 
  The **correct channelId** is typically the **last** one found at the bottom of the page.

Example:
- Input channel URL: https://www.youtube.com/channel/CHANNELID_HERE
- Subtitle language: ru

Result:
- All available Russian subtitles will be downloaded to the /subtitles folder, each in a separate .txt file named after the video title.
"""
