import json
import pymysql
import datetime

# Connect to the database
db = pymysql.connect(host="localhost",
                     user="root",
                     password="000000",
                     database="facebook")

cursor = db.cursor()

# Create the table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS facebook_shumai_momo (
    comment_id INT AUTO_INCREMENT,
    source VARCHAR(10),
    keyword VARCHAR(10),
    time DATE,
    post VARCHAR(500),
    comment VARCHAR(500),
    PRIMARY KEY (comment_id)
)
"""
cursor.execute(create_table_query)

# Read the JSON file
with open('fb_shumai_momo_comment.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Insert data into the table
for entry in data:
    source = 'facebook'
    keyword = 'momo'
    time = entry['時間']
    post = entry['文章']
    comments = entry['留言']

    try:
        parsed_date = datetime.datetime.strptime(time, '%m月%d日上午%H:%M')
        parsed_date = parsed_date.replace(year=2023)   
        time = parsed_date.strftime('%Y-%m-%d')   
    except ValueError:
        try:
            parsed_date = datetime.datetime.strptime(time, '%m月%d日')
            parsed_date = parsed_date.replace(year=2023)  # 替換年份
            time = parsed_date.strftime('%Y-%m-%d')   
        except ValueError:
            pass

    for comment in comments:
        insert_data_query = """
        INSERT INTO facebook_shumai_momo (source, keyword, time, post, comment)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_data_query, (source, keyword, time, post, comment))

# Commit the changes and close the connection
db.commit()
db.close()
