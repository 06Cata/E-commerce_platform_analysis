import requests
from bs4 import BeautifulSoup
import csv

input_csv = ""

with open(input_csv, "r", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader) 

    with open(f"{input_csv}_comment.csv", "w", newline="", encoding="utf-8") as comment_csvfile:
        writer = csv.writer(comment_csvfile)
        writer.writerow(["url", "text", "timestamp"])

        for row in reader:
            link = row[4]  # link所在的列
            page_number = row[5]  # page_number所在的列
            base_url = link 

            for suffix in range(1, int(page_number) + 1):
                url = base_url+ "&p=" + str(suffix)
                print(url) #檢查活動
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

                        # 寫入URL、內文和時間到CSV
                        writer.writerow([url, text, timestamp])

