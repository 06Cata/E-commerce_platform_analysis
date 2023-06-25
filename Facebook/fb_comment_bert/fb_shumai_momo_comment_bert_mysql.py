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
CREATE TABLE IF NOT EXISTS facebook_shumai_bert (
    id INT PRIMARY KEY AUTO_INCREMENT,
    source VARCHAR(10),
    keyword VARCHAR(10),
    comment VARCHAR(500),
    time DATE,
    score FLOAT
)
"""
cursor.execute(create_table_query)

# Read the JSON file
with open('fb_shumai_momo_comment_momo_bert.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Insert data into the table
for entry in data:
    source = 'facebook'
    keyword = 'momo'
    time = entry['emo_time']
    comment = entry['emo_comment']
    score = entry['emo_score']

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

    insert_data_query = f"""
    INSERT INTO facebook_shumai_momo_bert (source, keyword, comment, time, score)
    VALUES ('{source}', '{keyword}', '{comment}', '{time}', {score})
    """
    cursor.execute(insert_data_query)

# Commit the changes and close the connection
db.commit()
db.close()
