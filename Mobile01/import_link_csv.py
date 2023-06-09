import requests
import csv
import json
import os
import datetime
from dotenv import load_dotenv

load_dotenv('C:\dotenv\key.env')
api_key = os.environ.get('GOOGLE_API_KEY')
search_engine_id = "a282969c313d24cf6"
#單一查詢
query = "pchome"
num_results_per_page = 10
total_results = 100

#API正常免費限制為100
num_pages = total_results // num_results_per_page

# 擷取並儲存資料的列表
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
        with open(fr"{folder_path}\{json_file}", "w",encoding='utf-8') as file:
            json.dump(data,file,ensure_ascii=False)
        
        # 擷取每筆資料並加入結果列表
        search_terms = data["queries"]["request"][0].get("searchTerms", "")
        for item in data.get("items", []):
            link = item.get("link", "")
            title = item.get("title", "")
            article = item["pagemap"]["metatags"][0].get("article:section", "")
            published_time = item["pagemap"]["metatags"][0].get("article:published_time", "")
            
            result = {
                "search_terms": search_terms,
                "link": link,
                "title": title,
                "article": article,
                "published_time": published_time
            }
            
            results.append(result)
        
    else:
        print("發生錯誤:", response.status_code)
        break

# 將結果儲存為 CSV 檔案
if results:
    with open(f"{query}_OneMobile_{timestamp}.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["published_time","search_terms", "title", "article", "link" ])
        writer.writeheader()
        writer.writerows(results)
        
    print("資料已成功寫入檔案。")
else:
    print("未取得任何資料。")

