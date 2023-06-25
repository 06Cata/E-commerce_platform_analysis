#用正則表達式把有網址的欄位洗掉 並把預測加在後面
import pandas as pd
from cemotion import Cemotion
import re

def remove_urls(text):
    # 使用正則表達式尋找並移除網址
    url_pattern = re.compile(r'http[s]?://\S+')
    return url_pattern.sub('', text)

df = pd.read_csv('eshop_momo_commentt.csv')
c = Cemotion()

# 移除包含網址的那一行
#PTT有留言是網址 把他用正則表達式篩選掉 但是目前問題是會變空白
#我最後直接從爬蟲程式把非文字留言洗掉 並洗掉小於15個字的留言
df['Push Content'] = df['Push Content'].apply(remove_urls)
df = df[~df['Push Content'].str.contains(r'http[s]?://\S+')]

# 進行預測並生成結果欄位
df['prediction'] = df['Push Content'].apply(lambda x: '预测值:{:6f}'.format(c.predict(x)))

# 寫入結果到檔案
df.to_csv('result.csv', index=False, encoding='utf-8-sig')
