import os
import pyfiglet
import scrapetube
from datetime import datetime
import pandas as pd

from utils import extract_number

ascii_art = pyfiglet.figlet_format("YT Scraper Analyzer")
print(ascii_art)

channel_url = input("Insert channel URL: ")
if channel_url == "":
    channel_url = "https://www.youtube.com/c/EntropyforLife"
    print("Set: " + channel_url)

while True:
    limit = input("How many videos do you want? ")
    if limit == "":
        print("No input received. Exiting...")
        exit()
    elif limit.isdigit():
        limit = int(limit)
        break
    else:
        print("Invalid input. Please insert a number.")
print("")

print("Searching {} videos for {}".format(limit, channel_url))

videos = scrapetube.get_channel(channel_url=channel_url, limit=limit)

now = datetime.now()
videos_data = []
x = -1
for video in videos:
    video_id = video['videoId']
    title = video['title']['runs'][x+1]['text']
    view_count = extract_number(video['viewCountText']['simpleText'])
    view_count = view_count
    videos_data.append((now, video_id, view_count, title))

videos_data.reverse()
df = pd.DataFrame(videos_data, columns=['date_time', 'video_id', 'view_count', 'title'])
print(df)

# Set the output directory
output_dir = '/home/admin1/main/the-youtube-scraper-master/'

# Save DataFrame to CSV
csv_path = os.path.join(output_dir, 'videos_data.csv')
df.to_csv(csv_path, index=False)

print("Data saved to:", csv_path)
