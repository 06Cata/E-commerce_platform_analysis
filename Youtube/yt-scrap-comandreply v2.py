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
max_comments_per_video = 5

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
            data.append((video_id, comment_text, 'comment'))
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
                    data.append((video_id, reply_text, 'reply'))
                    comment_count += 1

            if max_comments_per_video is not None and comment_count >= max_comments_per_video:
                break

        page_token = response.get('nextPageToken')
        if not page_token:
            break

    if max_videos is not None and len(data) >= max_videos * max_comments_per_video:
        break

# Process and print the data
for i, (video_id, comment_text, comment_type) in enumerate(data, start=1):
    print(f"{i}. Video ID: {video_id} - Type: {comment_type} - Comment: {comment_text}")

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=['video_id', 'comment', 'type'])

# Add a sequential index starting from 0
df['index'] = range(len(df))

# Reorder the columns
df = df[['index', 'video_id', 'type', 'comment']]

# Save DataFrame to CSV
csv_path = os.path.join(output_dir, 'yt_comments_data.csv')
df.to_csv(csv_path, index=False)

print("Data saved to:", csv_path)
