import pymysql
import requests
import csv
import json
import os
from datetime import datetime
import time
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv('key.env')
api_key = os.environ.get('GOOGLE_API_KEY')
search_engine_id = "a282969c313d24cf6"
password = os.environ.get('jock_pwd')
current_time = datetime.now()

def google_api_link(queries,num_results_per_page=10,total_results=100):
    num_results_per_page = 10
    total_results = 100
    num_pages = total_results // num_results_per_page
    current_time = datetime.now()
    timestamp = current_time.strftime("%Y%m%d%H%M")
    current_dir = os.getcwd()
    folder_name = f"{timestamp}_json"
    folder_path = os.path.join(current_dir, folder_name)
    os.mkdir(folder_path)

    for query in queries:
        results = []
        for page in range(num_pages):
            start_index = page * num_results_per_page + 1
            url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&filter=1&sort=date&q={query}&num={num_results_per_page}&start={start_index}&siteSearch=mobile01.com/topicdetail.php&siteSearchFilter=i"
            response = requests.get(url)
            
            if response.status_code == 200:
                json_file = f"{timestamp}_{query}_{start_index}.json"
                data = response.json()
                with open(fr"{folder_path}/{json_file}", "w", encoding='utf-8') as file:
                    json.dump(data, file, ensure_ascii=False)
                    print(f"{json_file} catched")

                search_terms = data["queries"]["request"][0].get("searchTerms", "")
                for item in data.get("items", []):
                    link = item.get("link", "")
                    title = item.get("title", "")
                    article = item["pagemap"]["metatags"][0].get("article:section", "")
                    published_time = item["pagemap"]["metatags"][0].get("article:published_time", "")
                    
                    if "&p=" in link:
                        link = link[:link.index("&p=")]
                    link_without_page = link.split("&p=")[0]
                    
                    if any(result["link"].startswith(link_without_page) for result in results):
                        continue
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
                    }
                    response_article = requests.get(link, headers=headers)
                    time.sleep(1)
                    soup = BeautifulSoup(response_article.content, "html.parser")
                    h1_element = soup.find("h1", class_="t2")
                    article_body_element = soup.find("div", itemprop="articleBody")

                    if h1_element is not None and article_body_element is not None:
                        article_body = article_body_element.text.strip()[:300]
                        page_elements = soup.find_all("a", attrs={"data-page": True})
                        page_numbers = [int(element["data-page"]) for element in page_elements]
                        if page_numbers:
                            max_page = max(page_numbers)
                        else:
                            max_page = 1

                        result = {
                            "published_time": published_time,
                            "search_terms": search_terms,
                            "article": article,
                            "title": title,
                            "link": link,
                            "page_number": max_page,
                            "Body": article_body
                        }

                        results.append(result)
                        print(f"record {link}")
            else:
                print("發生錯誤:", response.status_code)
                break
        
        if results:
            with open(f"{timestamp}_{query}_link.csv", "w", newline="", encoding="utf-8") as file:
                fieldnames = ["published_time", "search_terms", "article", "title", "link", "page_number", "Body"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(results)

            print(f"{query} 資料已成功寫入檔案。")
        else:
            print(f"{query} 未取得任何資料。")

def cat_link_by_csv_to_db():
    db = pymysql.connect(
        host='localhost',
        user='jock',
        password=password,
        database='mobile01',
        charset="utf8mb4"
    )
    # 建立資料庫游標
    cursor = db.cursor()
    current_time = datetime.now()
    # 讀取 mobile01_links 資料表中的前 50 筆資料
    query = "SELECT link FROM mobile01_links limit 55"
    cursor.execute(query)

    # 建立字典來保存現有資料庫內的資料
    existing_links = []
    for (link,) in cursor:
        existing_links.append(link)
    existing_links = set(existing_links)
    #搜尋符合條件的 CSV 檔案
    csv_files = []
    for file in os.listdir('.'):
        if file.endswith("_link.csv") and "finish" not in file:
            csv_files.append(file)


    # 處理每個符合條件的 CSV 檔案
    for csv_file in csv_files:
        with open(csv_file, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            new_records = []
            header_skipped = False 
            for row in csv_reader:
                if not header_skipped:
                    header_skipped = True
                    continue  # 跳過標頭行

                record = {
                    "published_time": datetime.strptime(row[0], "%Y-%m-%dT%H:%M:%S%z").strftime("%Y-%m-%d %H:%M:%S"),
                    "search_terms": row[1],
                    "article": row[2],
                    "title": row[3],
                    "link": row[4],
                    "page_number": int(row[5]),
                    "Body": row[6]
                }
                link = record["link"]
                if link not in existing_links:
                    new_records.append(record)
                    print(f"檔案{csv_file} 新增 {len(new_records)} 項\n")

            # 新增新的紀錄到資料庫
            if new_records!=[]:
                query = "INSERT INTO mobile01_links (published_time, search_terms, article, title, link, page_number, Body) VALUES (%(published_time)s, %(search_terms)s, %(article)s, %(title)s, %(link)s, %(page_number)s, %(Body)s)"
                values = new_records
                cursor.executemany(query, values)
                db.commit()
                new_count = len(new_records)

                # 更新紀錄到 update.log
                log_message = f"{csv_file} 新增 {new_count} 項 {current_time}\n"
                with open("update.log", "a") as log_file:
                    log_file.write(log_message)
                
                file.close()
                # 更名使用過的 CSV 檔案
                os.rename(csv_file, f"{csv_file.split('.csv')[0]}_finish.csv")
            else:
                file.close()
                os.rename(csv_file, f"{csv_file.split('.csv')[0]}_finish.csv")
                log_message = f"{csv_file} 新增 0 項 {current_time}\n"
                with open("update.log", "a") as log_file:
                    log_file.write(log_message) 

    # 關閉資料庫連線
    cursor.close()
    db.close()


def cat_com_by_csv_to_db():
    db = pymysql.connect(
    host='localhost',
    user='jock',
    password=password,
    database='mobile01',
    charset="utf8mb4"
    )

    # 建立資料庫游標
    cursor = db.cursor()

    # 搜尋符合條件的 CSV 檔案
    csv_files = []
    for file in os.listdir('.'):
        if file.endswith("_link_finish.csv") and "com" not in file:
            csv_files.append(file)

    # 處理每個符合條件的 CSV 檔案
    for csv_file in csv_files:
        with open(csv_file, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # 跳過標頭行

            # 建立新的紀錄列表
            new_records = []

            for row in csv_reader:
                link = row[4]  # link所在的列
                page_number = int(row[5])  # page_number所在的列
                base_url = link.split("&p=")[0]  # 取得 URL 基礎部分

                # 刪除相同 link 前綴的資料
                query = "DELETE FROM mobile01_comments WHERE url LIKE %s"
                cursor.execute(query, (base_url + "%",))
                db.commit()

                for suffix in range(1, page_number + 1):
                    url = base_url + "&p=" + str(suffix)
                    print(f"爬取{url}")  # 檢查活動
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
                    }
                    response = requests.get(url, headers=headers)
                    soup = BeautifulSoup(response.content, "html.parser")
                    target_class = "u-gapBottom--max c-articleLimit"
                    elements = soup.find_all(class_=target_class)

                    for element in elements:
                        if element.find("article"):
                            text = element.get_text()

                            # 找時間所在的父元素
                            timestamp_parent = element.find_next(class_="l-navigation__item")
                            if timestamp_parent:
                                timestamp_element = timestamp_parent.find(class_="o-fNotes o-fSubMini")
                                if timestamp_element:
                                    timestamp = timestamp_element.text.strip()
                                else:
                                    timestamp = "N/A"
                            else:
                                timestamp = "N/A"

                            # 寫入URL、內文和時間到新的紀錄列表
                            new_records.append([url, text, timestamp])

            # 新增新的紀錄到資料庫
            if new_records:
                query = "INSERT INTO mobile01_comments (url, text, timestamp) VALUES (%s, %s, %s)"
                cursor.executemany(query, new_records)
                db.commit()
                log_message = f"{csv_file} 新增 {len(new_records)} 項 {current_time}\n"
                with open("update.log", "a") as log_file:
                    log_file.write(log_message)

            file.close()

            # 更名使用過的 CSV 檔案
            os.rename(csv_file, f"{csv_file.split('.csv')[0]}_com.csv")
                    # 更新紀錄到 update.log
        log_message = f"{csv_file} 新增 {len(new_records)} 項 {current_time}\n"
        with open("update.log", "a") as log_file:
                log_file.write(log_message)

    # 關閉資料庫連線
    cursor.close()
    db.close()