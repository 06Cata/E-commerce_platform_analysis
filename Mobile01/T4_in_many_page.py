import requests
from bs4 import BeautifulSoup

base_url = "https://www.mobile01.com/topicdetail.php?f=37&t=6688033&p="
page_suffixes = []

# 发送请求获取第一页的内容
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
}
response = requests.get(base_url + "1", headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# 找到具有 data-page 属性的所有元素
page_elements = soup.find_all("a", attrs={"data-page": True})

# 提取出 data-page 属性的值并转换为整数
page_numbers = [int(element["data-page"]) for element in page_elements]

# 找到最大的页码值
max_page = max(page_numbers)
print(max_page)

for page in range(1, max_page + 1):
    page_suffixes.append(str(page))

# 根据不同后缀的 URL 进行处理
for suffix in page_suffixes:
    url = base_url + suffix
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
            print(text)



