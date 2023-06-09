import os
import pymysql
import pandas as pd

# Set the MariaDB connection details
host = 'localhost'
user = 'jack'
password = '123'
database = 'youtube'

# Set the path to the CSV file
csv_path = r'C:\Users\cheng\Desktop\VSCodeMain\Workshops\YouTube-Scrapper\src\yt_main_data.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_path)

# Connect to MariaDB
connection = pymysql.connect(host=host, user=user, password=password, database=database)

# Create a cursor object to execute SQL statements
cursor = connection.cursor()

# Create the table if it doesn't exist
create_table_query = '''
    CREATE TABLE IF NOT EXISTS youtube_data (
        id INT PRIMARY KEY AUTO_INCREMENT,
        time VARCHAR(10),
        video_title VARCHAR(25),
        type VARCHAR(10),
        comment TEXT,
        video_id VARCHAR(20)
    )
'''
cursor.execute(create_table_query)

# Insert the data into the table
for _, row in df.iterrows():
    insert_query = f'''
        INSERT INTO youtube_data (time, video_title, type, comment, video_id)
        VALUES ('{row['time']}', '{row['video_title']}', '{row['type']}', '{row['comment']}', '{row['video_id']}')
    '''
    cursor.execute(insert_query)

# Commit the changes and close the cursor and connection
connection.commit()
cursor.close()
connection.close()

print("Data imported into MariaDB.")
