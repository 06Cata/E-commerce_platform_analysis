import requests
from bs4 import BeautifulSoup



# 发送HTTP GET请求并获取页面内容
url = "https://www.mobile01.com/topicdetail.php?f=731&t=6593121"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
}
response = requests.get(url, headers=headers)
html_content = response.content

# 使用Beautiful Soup解析HTML页面
soup = BeautifulSoup(html_content, "html.parser")
# 找到所有指定class的元素并提取文本内容


target_class = "u-gapBottom--max c-articleLimit"
elements = soup.find_all(class_=target_class)

for element in elements:
    if element.find("article"):
        text = element.get_text()
        print(text)

