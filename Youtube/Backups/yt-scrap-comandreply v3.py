import os
from googleapiclient.discovery import build
import pandas as pd

# Set the YouTube Data API client
youtube = build('youtube', 'v3', developerKey='Use API Key')

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
            comment = item['snippet']['topLevelComment']['snippet']
            comment_text = comment['textDisplay']
            comment_time = comment['publishedAt']
            video_title = youtube.videos().list(part='snippet', id=video_id).execute()['items'][0]['snippet']['title'].split(' ', 1)[0]
            data.append((comment_text, 'comment', comment_time, video_title, video_id))
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
                    reply_time = reply['snippet']['publishedAt']
                    data.append((reply_text, 'reply', reply_time, video_title, video_id))
                    comment_count += 1

            if max_comments_per_video is not None and comment_count >= max_comments_per_video:
                break

        page_token = response.get('nextPageToken')
        if not page_token:
            break

    if max_videos is not None and len(data) >= max_videos * max_comments_per_video:
        break

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=['comment', 'type', 'time', 'video_title', 'video_id'])
df = df.reset_index()

# Reorder the columns
df = df[['index', 'time', 'video_title', 'type', 'comment', 'video_id']]

# Save DataFrame to CSV
csv_path = os.path.join(output_dir, 'yt_comments_data.csv')
df.to_csv(csv_path, index=False)

print("Data saved to:", csv_path)
