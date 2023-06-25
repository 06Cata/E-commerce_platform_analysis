import openpyxl
import json
# momo_try
# 開啟 Excel 檔案
workbook = openpyxl.load_workbook('C:/Users/catal/Desktop/py/momo_post.xlsx')

# 選取第一個工作表
worksheet = workbook.active

# 初始化結果字典
result_dict = {"momo": []}

# 逐行處理行銷貼文
for row in worksheet.iter_rows(values_only=True):
    line = row[0]
    if line:
        line = line.strip()  # 移除多餘的空白字元

        # 判斷是否為有效的行銷貼文
        if line.startswith("momo") or line.startswith("總是有那麼幾個時刻覺得自己老了"):
            # 將行銷貼文拆分為產品類別和內容
            parts = line.split(" ", 1)  # 以第一個空格作為分隔符號拆分

            if len(parts) == 2:
                content = parts[1]

                # 將內容存入字典
                result_dict["momo"].append(content)

# 將整理後的結果轉換成 JSON 格式
json_data = json.dumps(result_dict, ensure_ascii=False)

# 將 JSON 寫入檔案
with open('C:/Users/catal/Desktop/py/momo_post.json', 'w', encoding='utf-8') as file:
    file.write(json_data)

# 印出結果
print("JSON 檔案已寫入成功。")
