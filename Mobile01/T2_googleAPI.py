import requests
import json
import csv

search_engine_id = "a282969c313d24cf6"
query = "momo"
num_results = 10

# 建立 API 請求的 URL
url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={query}&num={num_results}"

# 發送 GET 請求
response = requests.get(url)

# 檢查回應狀態碼
if response.status_code == 200:
    data = response.json()
    with open("search_results.json", "w",encoding='utf-8') as file:
        json.dump(data, file,ensure_ascii=False)
    print("資料已成功寫入檔案。")
else:
    print("發生錯誤:", response.status_code)
with open('search_results.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
search_information = data['searchInformation']
total_results = search_information['totalResults']
formatted_total_results = search_information['formattedTotalResults']
search_time = search_information['searchTime']
formatted_search_time = search_information['formattedSearchTime']
print("Total Results:", total_results)
print("Formatted Total Results:", formatted_total_results)
print("Search Time:", search_time)
print("Formatted Search Time:", formatted_search_time)
items = data['items']
for item in items:
    title = item['title']
    link = item['link']
    print("Title:", title)
    print("Link:", link)
    print()