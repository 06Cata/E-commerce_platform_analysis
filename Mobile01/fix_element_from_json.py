import requests
import csv
import json
import os
import datetime
from dotenv import load_dotenv


json_file = ""

results = []  
with open(json_file, "r",encoding='utf-8') as file:
    data = json.load(file)
# 修正取值    
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


# 將結果儲存為 CSV 檔案
if results:
    with open("test", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["published_time","search_terms", "title", "article", "link" ])
        writer.writeheader()
        writer.writerows(results)
        
    print("資料已成功更正。")
else:
    print("未修改任何資料。")