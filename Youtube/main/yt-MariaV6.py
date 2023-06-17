import os
import shutil
import pymysql
import pandas as pd
import numpy as np
from datetime import date

# Set the MariaDB connection details
host = 'localhost'
user = 'jack'
password = '123'
database = 'youtube'

# Get the path to the current script file
current_script_path = os.path.dirname(os.path.abspath(__file__))

# Set the path to the folder containing the CSV files
csv_folder = 'jjTasks'

# Construct the full path to the CSV folder
csv_folder_path = os.path.join(current_script_path, csv_folder)

# Get a list of all files in the folder
files = os.listdir(csv_folder_path)

# Filter only the CSV files
csv_files = [file for file in files if file.endswith('.csv')]

if len(csv_files) == 0:
    print("No CSV files found in the specified folder.")
else:
    # Create the backup folder
    backup_folder_path = os.path.join(current_script_path, 'yt-bak')
    os.makedirs(backup_folder_path, exist_ok=True)

    # Backup each CSV file
    for csv_file in csv_files:
        # Set the path to the CSV file
        csv_path = os.path.join(csv_folder_path, csv_file)

        # Create the backup file name
        today = date.today().strftime("%Y-%m-%d")
        backup_file_name = f"{today}-{csv_file[:-4]}-bk.csv"
        backup_file_path = os.path.join(backup_folder_path, backup_file_name)

        # Backup the CSV file
        shutil.copy(csv_path, backup_file_path)
        print(f"Backup created: {backup_file_name}")

        # Delete the original CSV file
        os.remove(csv_path)
        print(f"Original file deleted: {csv_file}")

        # Connect to MariaDB
        connection = pymysql.connect(host=host, user=user, password=password, database=database)

        # Create a cursor object to execute SQL statements
        cursor = connection.cursor()

        # Create the table if it doesn't exist
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS youtube_data (
                id INT PRIMARY KEY AUTO_INCREMENT,
                source VARCHAR(255),
                `time` DATE,
                keyword VARCHAR(255),
                comment TEXT,
                video_id VARCHAR(20),
                score INT
            )
        '''
        cursor.execute(create_table_query)

        # Read the CSV file into a DataFrame
        df = pd.read_csv(backup_file_path)

        # Replace nan values with None
        df = df.replace({np.nan: None})

        # Check if 'video_id' column exists
        if 'video_id' in df.columns:
            # Check for duplicate records
            duplicate_rows = df[df.duplicated(subset=['source', 'time', 'keyword', 'comment', 'video_id', 'score'])]
            if not duplicate_rows.empty:
                print(f"Skipping {len(duplicate_rows)} duplicate comments.")

            # Remove duplicate records
            df = df.drop_duplicates(subset=['source', 'time', 'keyword', 'comment', 'video_id', 'score'])

            # Rename 'id' column to 'video_id'
            df = df.rename(columns={'id': 'video_id'})

        # Count the number of skipped comments
        skipped_comments = 0

        # Insert the data into the table
        for _, row in df.iterrows():
            # Check if comment already exists in the database
            check_query = '''
                SELECT COUNT(*) FROM youtube_data
                WHERE comment = %s
            '''
            cursor.execute(check_query, (row['comment'],))
            duplicate_count = cursor.fetchone()[0]

            if duplicate_count > 0:
                skipped_comments += 1
            else:
                insert_query = '''
                    INSERT INTO youtube_data (source, `time`, keyword, comment, video_id, score)
                    VALUES (%s, %s, %s, %s, %s, %s)
                '''
                cursor.execute(insert_query, (
                    row['source'],
                    row['time'],
                    row['keyword'],
                    row['comment'],
                    row['video_id'],
                    row['score']
                ))

        # Commit the changes
        connection.commit()

        print(f"Data imported from {csv_file} into MariaDB.")
        print(f"Number of comments skipped: {skipped_comments}")

        # Close the cursor and connection
        cursor.close()
        connection.close()
