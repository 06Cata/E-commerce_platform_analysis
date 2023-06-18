import os
from googleapiclient.discovery import build
import pandas as pd
import re
from datetime import date

# Set the YouTube Data API client
youtube = build('youtube', 'v3', developerKey='KeyHere')

# Video IDs, maximum number of videos, and maximum comments per video
video_ids = ["ZYiw9BrO8J8", "4qpWzUeV4Rc", "00sgA1rqouI", "HcGkDrDAm08", "GeOJXmhGPcc",
             "Tdef7RLS6G8", "t1yPg8nfFMg", "4CFFqrujxxQ", "RsQOqyp_cRI", "PvtIULOsevg"]

max_videos = None
max_comments_per_video = 3

# Set the output directory
current_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(current_dir)

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
            if not comment:
                continue  # Skip if comment data is missing

            comment_text = comment.get('textDisplay', '')
            if not comment_text:
                continue  # Skip if comment text is missing

            comment_time = comment.get('publishedAt', '')[:10]
            if not comment_time:
                continue  # Skip if comment time is missing

            video_title_full = youtube.videos().list(part='snippet', id=video_id).execute()['items'][0]['snippet']['title']
            video_title = video_title_full[:25] if len(video_title_full) > 25 else video_title_full
            data.append((comment_time, video_title, comment_text, video_id))
            comment_count += 1

            if include_replies:
                # Get replies to comments
                reply_response = youtube.comments().list(
                    part='snippet',
                    parentId=item['snippet']['topLevelComment']['id'],
                    maxResults=100
                ).execute()
                for reply in reply_response['items']:
                    reply_text = reply['snippet'].get('textDisplay', '')
                    if not reply_text:
                        continue  # Skip if reply text is missing

                    reply_time = reply['snippet'].get('publishedAt', '')[:10]
                    if not reply_time:
                        continue  # Skip if reply time is missing

                    data.append((reply_time, video_title, reply_text, video_id))
                    comment_count += 1

            if max_comments_per_video is not None and comment_count >= max_comments_per_video:
                break

        page_token = response.get('nextPageToken')
        if not page_token:
            break

    if max_videos is not None and len(data) >= max_videos * max_comments_per_video:
        break

# Create a DataFrame from the scraped data
df = pd.DataFrame(data, columns=['time', 'keyword', 'comment', 'video_id'])

# Sort the DataFrame by time (newest to oldest)
df['time'] = pd.to_datetime(df['time'])
df = df.sort_values(by='time', ascending=False)

# Filter the DataFrame to include only comments from June 2023 onwards
df = df[df['time'].dt.year >= 2023]
df = df[df['time'].dt.month >= 6]

# Get the date from the first row of the DataFrame
scraping_date = df['time'].iloc[0].strftime("%Y-%m-%d")

# Clean the comment column
df['comment'] = df['comment'].apply(lambda x: re.sub(r'\s+', ' ', x).strip())

# Add the 'source' column
df['source'] = 'YouTube'

# Reorder the columns
df = df[['source', 'time', 'keyword', 'comment', 'video_id']]

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Save the DataFrame as a CSV file
output_path = os.path.join(output_dir, 'yt_Main_data.csv')
df.to_csv(output_path, index=False)

# Scraping complete
comments_scraped = df.shape[0]
print("Scraping complete.")
print("Date:", scraping_date)
print("Number of comments scraped:", comments_scraped)
print("CSV file saved at:", output_path)
