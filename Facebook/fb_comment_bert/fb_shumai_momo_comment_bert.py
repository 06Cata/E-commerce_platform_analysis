# #按文本字符串分析
# # from cemotion import Cemotion

# # str_text1 = '好久不見'
# # str_text2 = '效率跟牛一樣'

# # c = Cemotion()
# # print('"', str_text1 , '"\n' , '預測值:{:6f}'.format(c.predict(str_text1) ) , '\n')
# # print('"', str_text2 , '"\n' , '預測值:{:6f}'.format(c.predict(str_text2) ) , '\n')


# # import json
# # from cemotion import Cemotion

# # # 读取JSON文件
# # with open('fb_shumai_momo_comment.json', 'r', encoding='utf-8') as file:
# #     data = json.load(file)

# # c = Cemotion()

# # result = []
# # # 迭代文章进行情绪分析
# # for item in data:
# #     str_text = item['文章']
# #     score = c.predict(str_text)
# #     print('文章:', str_text)
# #     print('情绪分数: {:6f}\n'.format(score))
    
# #     comments = item['留言']
# #     for comment in comments:
# #         str_text = comment
# #         score = c.predict(str_text)
# #         print('留言:', str_text)
# #         print('情绪分数: {:6f}\n'.format(score))

# # # 將結果寫入 JSON 檔案
# # with open('emotion_scores.json', 'w', encoding='utf-8') as file:
# #     json.dump(result, file, ensure_ascii=False, indent=4)

import json
from cemotion import Cemotion

# 读取JSON文件
with open('fb_shumai_momo_comment.json', 'r', encoding='utf-8') as file:
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
with open('fb_shumai_momo_comment_bert.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, ensure_ascii=False, indent=4)
