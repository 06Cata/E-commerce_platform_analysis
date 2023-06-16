import os
import pymysql
import pandas as pd
import numpy as np

# Set the MariaDB connection details
host = 'localhost'
user = 'jack'
password = '123'
database = 'youtube'

# Set the path to the folder containing the CSV files
csv_folder = r'C:\Users\cheng\Desktop\VSCodeMain\Workshops\YouTube-Scrapper\src\jjTasks'

# Get a list of all files in the folder
files = os.listdir(csv_folder)

# Filter only the CSV files
csv_files = [file for file in files if file.endswith('.csv')]

if len(csv_files) == 0:
    print("No CSV files found in the specified folder.")
else:
    for csv_file in csv_files:
        # Set the path to the CSV file
        csv_path = os.path.join(csv_folder, csv_file)

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
            CREATE TABLE IF NOT EXISTS youtube_data (
                id INT PRIMARY KEY AUTO_INCREMENT,
                `time` DATE,
                video_title VARCHAR(255),
                `type` VARCHAR(10),
                comment TEXT,
                video_id VARCHAR(20),
                sentiment_score_translated FLOAT,
                translated_comment TEXT
            )
        '''
        cursor.execute(create_table_query)

        # Insert the data into the table
        for _, row in df.iterrows():
            insert_query = '''
                INSERT INTO youtube_data (`time`, video_title, `type`, comment, video_id, sentiment_score_translated, translated_comment)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            '''
            cursor.execute(insert_query, (
                row['time'],
                row['video_title'],
                row['type'],
                row['comment'],
                row['video_id'],
                row['Sentiment_Score_Trans'],
                row['Translated_Comment']
            ))

        # Commit the changes and close the cursor and connection
        connection.commit()
        cursor.close()
        connection.close()

        print(f"Data imported from {csv_file} into MariaDB.")
