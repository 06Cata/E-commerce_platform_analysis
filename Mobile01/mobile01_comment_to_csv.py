import requests
from bs4 import BeautifulSoup
import csv

input_link = "f_pchome"

with open(f"{input_link}.csv", "r", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # 跳过标题行

    with open(f"{input_link}_comment.csv", "w", newline="", encoding="utf-8") as comment_csvfile:
        writer = csv.writer(comment_csvfile)
        writer.writerow(["url", "text", "timestamp"])

        for row in reader:
            link = row[4]  # 提取链接（link）所在的列
            page_number = row[5]  # 提取页面编号（page_number）所在的列
            base_url = link 

            for suffix in range(1, int(page_number) + 1):
                url = base_url+ "&p=" + str(suffix)
                print(url) #檢查
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

                        # 查找时间戳所在的父元素
                        timestamp_parent = element.find_next(class_="l-navigation__item")
                        if timestamp_parent:
                            timestamp_element = timestamp_parent.find(class_="o-fNotes o-fSubMini")
                            if timestamp_element:
                                timestamp = timestamp_element.text.strip()
                            else:
                                timestamp = "N/A"  # 如果没有找到时间戳元素，则使用默认值 "N/A"
                        else:
                            timestamp = "N/A"  # 如果没有找到时间戳父元素，则使用默认值 "N/A"

                        # 写入URL、文本和时间戳到CSV文件中
                        writer.writerow([url, text, timestamp])

