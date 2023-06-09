import os
from googleapiclient.discovery import build
import pandas as pd

# Set the YouTube Data API client
youtube = build('youtube', 'v3', developerKey='AIzaSyBgLALDG3o7gZhxGKlhZicjgtLb8tZ801g')

# Video IDs
video_ids = ["4CFFqrujxxQ", "RsQOqyp_cRI", "PvtIULOsevg"]

# Set the maximum number of videos to scrape (set to None for no limit)
max_videos = None

# Set the maximum number of comments per video (set to None for no limit)
max_comments_per_video = 3

# Set the output directory
output_dir = r'C:\Users\cheng\Desktop\VSCodeMain\Workshops\YouTube-Scrapper\src'

# Set whether to include replies or not
include_replies = True

# List to store the scraped data
data = []

# Scrape comments for each video
for video_id in video_ids[:max_videos]:
    # Get video comments and replies using YouTube Data API
    page_token = None
    comment_count = 0
    while True:
        response = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=100,
            pageToken=page_token
        ).execute()
        for item in response['items']:
            comment = item.get('snippet', {}).get('topLevelComment', {}).get('snippet', {})
            if 'publishedAt' not in comment:
                continue  # Skip if 'publishedAt' key is not present
            comment_text = comment.get('textDisplay', '')
            comment_time = comment['publishedAt'][:10]  # Extract only the date part
            video_title_full = youtube.videos().list(part='snippet', id=video_id).execute()['items'][0]['snippet']['title']
            video_title = video_title_full[:25] if len(video_title_full) > 25 else video_title_full
            data.append((comment_time, video_title, 'comment', comment_text, video_id))
            comment_count += 1

            if include_replies:
                # Get replies to comments
                reply_response = youtube.comments().list(
                    part='snippet',
                    parentId=item['snippet']['topLevelComment']['id'],
                    maxResults=100
                ).execute()
                for reply in reply_response['items']:
                    reply_text = reply['snippet']['textDisplay']
                    reply_time = reply['snippet']['publishedAt'][:10]  # Extract only the date part
                    data.append((reply_time, video_title, 'reply', reply_text, video_id))
                    comment_count += 1

            if max_comments_per_video is not None and comment_count >= max_comments_per_video:
                break

        page_token = response.get('nextPageToken')
        if not page_token:
            break

    if max_videos is not None and len(data) >= max_videos * max_comments_per_video:
        break

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=['time', 'video_title', 'type', 'comment', 'video_id'])

# Show preview of the first 5 lines
preview = df.head(5)
print("Preview of the first 5 lines:")
print(preview)
print()

# Save DataFrame to CSV (append mode)
csv_path = os.path.join(output_dir, 'yt_main_data.csv')
df.to_csv(csv_path, index=False, mode='a', header=(not os.path.exists(csv_path)))

print("Data appended to:", csv_path)

# Set the path to the JSON file
json_path = os.path.join(output_dir, 'yt_main_data.json')

# Save DataFrame to JSON with indentation and line breaks
df.to_json(json_path, orient='records', indent=4)

print("Data saved to JSON:", json_path)
