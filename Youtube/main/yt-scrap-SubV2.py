import os
from googleapiclient.discovery import build
import pandas as pd

# Set the YouTube Data API client
youtube = build('youtube', 'v3', developerKey='AIzaSyBgLALDG3o7gZhxGKlhZicjgtLb8tZ801g')

# Video IDs
video_ids = ["ZYiw9BrO8J8", "4qpWzUeV4Rc", "00sgA1rqouI", "HcGkDrDAm08", "GeOJXmhGPcc", 
             "Tdef7RLS6G8", "t1yPg8nfFMg", "4CFFqrujxxQ", "RsQOqyp_cRI", "PvtIULOsevg", 
             "ZYiw9BrO8J8", "4qpWzUeV4Rc", "00sgA1rqouI", "HcGkDrDAm08", "GeOJXmhGPcc", 
             "Tdef7RLS6G8", "t1yPg8nfFMg", "4CFFqrujxxQ", "RsQOqyp_cRI", "PvtIULOsevg"]

# Set the maximum number of videos to scrape (set to None for no limit)
max_videos = None

# Set the maximum number of comments per video (set to None for no limit)
max_comments_per_video = 0

# Set the output directory
output_dir = r'C:\Users\cheng\Desktop\VSCodeMain\Workshops\YouTube-Scrapper\src'

# Set whether to include replies or not
include_replies = True

# List to store the scraped data
data = []

# Scrape video information
for video_id in video_ids[:max_videos]:
    video_info = youtube.videos().list(part='snippet,statistics,contentDetails', id=video_id).execute()['items'][0]
    video_duration = video_info['contentDetails']['duration'][2:]  # Remove 'PT' from the duration
    video_likes = video_info['statistics']['likeCount']
    video_dislikes = video_info['statistics'].get('dislikeCount', 0)
    video_views = video_info['statistics']['viewCount']
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    # Retrieve the channel information
    channel_id = video_info['snippet']['channelId']
    channel_info = youtube.channels().list(part='statistics', id=channel_id).execute()['items'][0]
    video_subscribers = channel_info['statistics'].get('subscriberCount', 0)

    data.append((video_info['snippet']['publishedAt'][:10], video_duration, video_likes, video_dislikes, video_subscribers, video_views, video_url, video_id))

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=['time', 'video_duration', 'like', 'dislike', 'subscriber', 'views', 'url', 'video_id'])

# Show preview of the first 5 lines
preview = df.head(5)
print("Preview of the first 5 lines:")
print(preview)
print()

# Save DataFrame to CSV (append mode)
csv_path = os.path.join(output_dir, 'yt_Sub_data.csv')
df.to_csv(csv_path, index=False, mode='a', header=(not os.path.exists(csv_path)))

print("Data appended to:", csv_path)

# Set the path to the JSON file
json_path = os.path.join(output_dir, 'yt_Sub_data.json')

# Save DataFrame to JSON with indentation and line breaks
df.to_json(json_path, orient='records', indent=4)

print("Data saved to JSON:", json_path)
