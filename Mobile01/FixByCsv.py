import requests
import csv
from bs4 import BeautifulSoup

csv_file = "pchome_OneMobile_202306051401.csv"
results = []
with open(csv_file, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for index, row in enumerate(reader):
        published_time = row["published_time"]
        search_terms = row["search_terms"]
        title = row["title"]
        article = row["article"]
        link = row["link"]
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
            print(f"完成第 {index+1} 筆修正")

# 將結果儲存為 CSV 檔案
if results:
    with open("f_pchome.csv", "w", newline="", encoding="utf-8") as file:
        fieldnames = ["published_time", "search_terms", "article", "title", "link", "page_number", "Body"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print("資料已成功更正。")
else:
    print("未修改任何資料。")
