import os
import sys
import pymysql
import pandas as pd
import numpy as np

# Set the MariaDB connection details
host = 'localhost'
user = 'jack'
password = '123'
database = 'youtube'

# Get the path to the current script file
current_script_path = os.path.dirname(os.path.abspath(__file__))

# Set the path to the folder containing the CSV file
csv_folder = current_script_path

# Construct the full path to the CSV file
csv_file = 'yt_Sub_data.csv'
csv_path = os.path.join(csv_folder, csv_file)

# Check if the CSV file exists
if not os.path.isfile(csv_path):
    print(f"CSV file '{csv_file}' not found in the specified folder.")
else:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_path)

    # Replace nan values with None
    df = df.replace({np.nan: None})

    # Connect to MariaDB
    connection = pymysql.connect(host=host, user=user, password=password, database=database)

    # Create a cursor object to execute SQL statements
    cursor = connection.cursor()

    # Create the table if it doesn't exist
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS youtube_subdata (
            id INT PRIMARY KEY AUTO_INCREMENT,
            source VARCHAR(255),
            `time` DATE,
            video_duration VARCHAR(10),
            `like` INT,
            dislike INT,
            subscriber INT,
            views INT,
            url VARCHAR(255),
            video_id VARCHAR(20)
        )
    '''
    cursor.execute(create_table_query)

    # Insert the data into the table
    for _, row in df.iterrows():
        insert_query = '''
            INSERT INTO youtube_subdata (source, `time`, video_duration, `like`, dislike, subscriber, views, url, video_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(insert_query, (
            row['source'],
            row['time'],
            row['video_duration'],
            row['like'],
            row['dislike'],
            row['subscriber'],
            row['views'],
            row['url'],
            row['id']
        ))

    # Commit the changes and close the cursor and connection
    connection.commit()
    cursor.close()
    connection.close()

    print(f"Data imported from {csv_file} into MariaDB.")
