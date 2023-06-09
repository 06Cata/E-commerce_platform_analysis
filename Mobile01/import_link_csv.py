import requests
import csv
import json
import os
import datetime
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv('C:\dotenv\key.env')
api_key = os.environ.get('GOOGLE_API_KEY')
search_engine_id = "a282969c313d24cf6"

query = "蝦皮"  #Key-words
num_results_per_page = 10
total_results = 100 

#API正常免費限制為單日100篇單日10則
num_pages = total_results // num_results_per_page


results = []
current_time = datetime.datetime.now()
timestamp = current_time.strftime("%Y%m%d%H%M")
current_dir = os.getcwd()  # 獲取當前工作目錄的路徑
folder_name = f"{query}_{timestamp}api_json"  # 新資料夾的名稱
folder_path = os.path.join(current_dir, folder_name)
os.mkdir(folder_path) 
# 下迴圈進行搜尋結果的取得
for page in range(num_pages):
    start_index = page * num_results_per_page + 1
    
    # 建立 API 請求的 URL
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&filter=1&sort=date&q={query}&num={num_results_per_page}&start={start_index}&siteSearch=mobile01.com/topicdetail.php&siteSearchFilter=i"
    
    # 發送 GET 請求
    response = requests.get(url)
    
    # 檢查回應狀態碼
    if response.status_code == 200:
        # 解析 JSON 回應
        json_file = f"api_{query}_{timestamp}_{start_index}.json"
        data = response.json()
        #儲存每次的api原始檔，理論上一次會有10支檔案
        with open(fr"{folder_path}\{json_file}", "w",encoding='utf-8') as file:
            json.dump(data,file,ensure_ascii=False)
            print(f"{json_file} catched") 
        
        # 擷取每筆資料並加入結果列表
        search_terms = data["queries"]["request"][0].get("searchTerms", "")
        for item in data.get("items", []):
            link = item.get("link", "")
            title = item.get("title", "")
            article = item["pagemap"]["metatags"][0].get("article:section", "")
            published_time = item["pagemap"]["metatags"][0].get("article:published_time", "")
            if "&p=" in link:#確認抓取第一頁
                link = link[:link.index("&p=")]
            link_without_page = link.split("&p=")[0]# 分離後綴頁數檢查重複性
            if any(result["link"].startswith(link_without_page) for result in results):
                continue
        # 取得連結完整標題及內文
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
            }
            response_article = requests.get(link, headers=headers)
            soup = BeautifulSoup(response_article.content, "html.parser")
            h1_element = soup.find("h1", class_="t2")
            article_body_element = soup.find("div", itemprop="articleBody")

            # 確認是否找到標題和內文元素
            if h1_element is not None and article_body_element is not None:
                article_body = article_body_element.text.strip()[:300]

                # 新增連結頁數
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
                print(f"record{link}")     
            
        else:
            print("發生錯誤:", response.status_code)
            break

# 將結果儲存為 CSV 檔案
if results:
    with open(f"{query}_{timestamp}.csv", "w", newline="", encoding="utf-8") as file:
        fieldnames = ["published_time", "search_terms", "article", "title", "link", "page_number", "Body"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
        
    print("資料已成功寫入檔案。")
else:
    print("未取得任何資料。")

