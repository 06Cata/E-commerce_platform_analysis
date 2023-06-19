import json
from cemotion import Cemotion

# 读取JSON文件
with open('fb_shumai_pchome_comment.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

c = Cemotion()

# 建立存放結果的列表
result = []

# 迭代文章进行情绪分析
for index, item in enumerate(data):
    str_text = item['文章']
    article_score = c.predict(str_text)
    article_result = {'emo_comment': str_text, 'emo_score': float(article_score), 'emo_time': data[index]['時間']}
    result.append(article_result)

    comments = item['留言']
    for comment in comments:
        str_text = comment
        comment_score = c.predict(str_text)
        comment_result = {'emo_comment': str_text, 'emo_score': float(comment_score), 'emo_time': data[index]['時間']}
        result.append(comment_result)

# 將結果寫入 JSON 檔案
with open('fb_shumai_pchome_comment_bert.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, ensure_ascii=False, indent=4)
