import pymysql

# 假設爬下所有標題和內文了
class Crawling:
    def __init__(self):
        pass

    # 【一、創建資料庫, 如果有就刪掉, 創一個, 沒有就直接創一個】
    def create_database(self, database):
        db = pymysql.connect(host="localhost",
                             port=3306,
                             user="root",
                             password="000000"
                             )
        cursor = db.cursor()
        cursor.execute(f"SHOW DATABASES LIKE '{database}'")
        result = cursor.fetchone()

        if result is not None:
            print("Database exists!")
            cursor.execute(f"DROP DATABASE {database}")
            cursor.execute(f"CREATE DATABASE {database}")
        else:
            print("Database does not exist.")
            cursor.execute(f"CREATE DATABASE {database}")
        db.commit()


    # 【二、創建資料表】
    def create_table(self, database, table, field1, field2):
        db = pymysql.connect(host="localhost",
                             port=3306,
                             user="root",
                             password="000000"
                             )
        cursor = db.cursor()
        cursor.execute(f"USE {database}")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table} ({field1} VARCHAR(300), {field2} VARCHAR(1000))")
        db.commit()


    # 【三、資料存入資料表】field1 field2 是自己取的欄位名稱, 如果要加 field3 欄位, title, content, 後面也要加上main.py 設好的名稱
    def insert_data(self, database, table, field1, field2, title, content):
        db = pymysql.connect(host="localhost",
                             port=3306,
                             user="root",
                             password="000000"
                             )
        cursor = db.cursor()
        cursor.execute(f"USE {database}")
        sql = (f"INSERT INTO {table} ({field1}, {field2}) VALUES (%s, %s)")
        val = (title, content)
        cursor.execute(sql, val)
        db.commit()


    # 【四、SHOW 出資料表】
    def show_data(self, database, table):
        db = pymysql.connect(host="localhost",
                             port=3306,
                             user="root",
                             password="000000"
                             )
        cursor = db.cursor()
        cursor.execute(f"USE {database}")
        cursor.execute(f"SELECT * FROM {table}")
        result = cursor.fetchall()

        for x in result:
            print(x)

        db.commit()

        cursor.close()
        db.close()
