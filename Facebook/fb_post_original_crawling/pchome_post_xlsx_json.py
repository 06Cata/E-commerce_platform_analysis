import openpyxl
import json

# 開啟 Excel 檔案
workbook = openpyxl.load_workbook('C:/Users/catal/Desktop/py/pchome_try.xlsx')

# 選取第一個工作表
worksheet = workbook.active

# 初始化結果字典
result_dict = {}

# 逐行處理行銷貼文
for row in worksheet.iter_rows(values_only=True):
    line = row[0]
    if line:
        line = line.strip()  # 移除多餘的空白字元

        # 判斷是否為有效的行銷貼文
        if line.startswith("PChome") or line.startswith("總是有那麼幾個時刻覺得自己老了"):
            # 將行銷貼文拆分為產品類別和內容
            parts = line.split(" ", 1)  # 以第一個空格作為分隔符號拆分

            if len(parts) == 2:
                category = parts[0]
                content = parts[1]

                # 將分類結果存入字典
                if category not in result_dict:
                    result_dict[category] = []
                result_dict[category].append(content)

# 將整理後的結果轉換成 JSON 格式
json_data = json.dumps(result_dict, ensure_ascii=False)

# 將 JSON 寫入檔案
with open('C:/Users/catal/Desktop/py/pchome_try.json', 'w', encoding='utf-8') as file:
    file.write(json_data)

# 印出結果
print("JSON 檔案已寫入成功。")