import csv
import pymysql

# 数据库连接配置
def ptt_db_com(filename,query):
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "123456",
        "database": "PTT"
    }

    # 建立数据库连接
    db = pymysql.connect(**db_config)
    cursor = db.cursor()

    # 创建数据表
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {query} (
        id INT PRIMARY KEY AUTO_INCREMENT,
        source VARCHAR(255),
        keyword VARCHAR(255),
        comment TEXT,
        time VARCHAR(255)
    )
    """
    cursor.execute(create_table_query)

    # 插入数据
    insert_query = f"""
    INSERT INTO {query} (source, keyword, comment, time)
    VALUES ( %s, %s, %s, %s)
    """

    with open(filename, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            keyword = row['Qurery']
            comment = row['Push Content']
            time = row['Push Time']
            # score = row['prediction']
            source = ['PTT']
            
            # 执行插入语句
            cursor.execute(insert_query, (source, keyword, comment, time))

    # 提交更改并关闭数据库连接
    db.commit()
    db.close()
    return
