import requests
import csv
import json
import os
import datetime
from bs4 import BeautifulSoup
from dotenv import load_dotenv


json_file = "api_reuqest_pchome_202306051401.json"

results = []  
with open(json_file, "r",encoding='utf-8') as file:
    data = json.load(file)
# 修正取值    
    search_terms = data["queries"]["request"][0].get("searchTerms", "")
for item in data.get("items", []):
        link = item.get("link", "")
        article = item["pagemap"]["metatags"][0].get("article:section", "")
        published_time = item["pagemap"]["metatags"][0].get("article:published_time", "")
#分離後綴頁數檢查重複性       
        link_without_page = link.split("&p=")[0]
        if any(result["link"].startswith(link_without_page) for result in results):
            continue
# 取得連結完整標題及內文
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
        }
        response_article = requests.get(link,headers=headers)
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
            "search_terms": search_terms,
            "link": link,
            "title": h1_element.text.strip(),
            "article": article,
            "Body": article_body,
            "published_time": published_time,
            "page_number": max_page
        }
        
        results.append(result)


# 將結果儲存為 CSV 檔案
if results:
    with open("f_pchome_202306051401.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["published_time","search_terms", "article", "title", "link","page_number","Body" ])
        writer.writeheader()
        writer.writerows(results)
        
    print("資料已成功更正。")
else:
    print("未修改任何資料。")