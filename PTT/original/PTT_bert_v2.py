#把有網址的欄位洗掉 並把預測加在後面
import pandas as pd
from cemotion import Cemotion
import re

def bert_prediction(input):
    df = pd.read_csv(input)
    c = Cemotion()
    # 進行預測並生成結果欄位
    df['prediction'] = df['Push Content'].apply(lambda x: '预测值:{:6f}'.format(c.predict(x)))
    input_file= input.split(".csv")[0]
    output=f'{input_file}_bert.csv'

    # 寫入結果到檔案
    df.to_csv(output, index=False, encoding='utf-8-sig')
    return 

