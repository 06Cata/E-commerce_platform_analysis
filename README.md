# E-commerce_platform_analysis
First of all, thank you for watching, I'm learning data analysis in bootcamp, this is my first commercial project with my team members. 
@ivyyyyy5299 @chengtaj @JockYellow

Theme: E-commerce platform analysis

Our analysis market is in Taiwan, so we will analyze momo and pchome. At the same time, we will compare the impact of Shopee merchants and individual sellers, as well as Taobao and tariff policies, on the general customers' choice of purchasing platforms.


首先, 感謝你點進來~ 這是我在轉職班和組員們的第一個商業分析專案

主題: 電商平台分析

我們的分析市場在台灣, 因此將會分析momo和pchome.同時會比較蝦皮商家和個人賣家, 以及淘寶和關稅政策, 對一般客戶選擇購買平台帶來的影響

產業分析: https://docs.google.com/document/d/17--tLdvq2oRIwdv31Uz1qeLoKBamjZhLoPBBGPV5RZw/edit

時程: https://docs.google.com/spreadsheets/d/1unktMQzdtxoamAShBXyji-MwwTjrQDhI/edit#gid=2137173062


--------------------

db:  Facebook / Mobile01 / PTT / Youtube

table： （👇🏻）

--------------------

Cata：

☘️原行銷po文（爬蟲）

fb_momo_post.py
fb_momo_post.json
fb_momo_post_mysql.py
fb_pchome_post.py
fb_pchome_post.json
fb_pchome_post_mysql.py

☘️openai清洗過的行銷po文佔比

fb_momo_post_from1ofMay.json
openai_post_count_only.py (table：momo_types)
fb_momo_post_amount.json
fb_momo_post_amount_mysql.py
fb_pchome_post_from1ofMay.json
openai_post_count_only.py (table：pc_types)
fb_pchome_post_amount.json
fb_pchome_post_amount_mysql.py

☘️ openai text-davinci-003 模型

openai_post_count_only.py
openai_post_all.py


🌺原電商燒賣po文+留言（爬蟲）

fb_shumai_momo_comment.py
fb_shumai_momo_comment.json
fb_shumai_momo_comment_mysql.py（table：fb_shumai_momo）
fb_shumai_pchome_comment.py
fb_shumai_pchome_comment.json
fb_shumai_pchome_comment_mysql.py（table：fb_shumai_pchome）

🌺openai清洗過的電商燒賣po文+留言佔比

fb_shumai_momo_comment_bert.py
fb_shumai_momo_comment_bert.json
fb_shumai_momo_comment_bert_mysql.py（table：fb_shumai_momo_bert）
fb_shumai_pchome_comment_bert.py
fb_shumai_pchome_comment_bert.json
fb_shumai_pchome_comment_bert_mysql.py（table：fb_shumai_pchome_bert）


Ivy:

爬蟲程式+導出csv+導出Bert——csv

🌸 爬蟲+進資料庫

ptt_main_BERT_v5.py
ptt_crawlcsv_v4
PTT_bert_v2
ptt_crawl_v5.py

eshop_momo_comments_bert.csv
eshop_pchome_comments_bert.csv
eshop_shopee_comments_bert.csv
eshop_momo_contents_bert.csv
eshop_pchome_contents_bert.csv
eshop_shopee_contents_bert.csv

eshop_momo_comments.csv
eshop_momo_content.csv
eshop_pchome_comments.csv
eshop_pchome_content.csv
eshop_shopee_comments.csv
eshop_shopee_content.csv

ptt_momo_comment_mysql.py（table: ptt_momo)
ptt_pchome_comment_mysql.py （table: ptt_pchome)
ptt_shopee_comment_mysql.py （table: ptt_shopee)

ptt_momo_content_mysql.py （table: ptt_momo)
ptt_pchome_content_mysql.py（table: ptt_pchome)
ptt_shopee_content_mysql.py （table: ptt_shopee)

🌸 Bert進資料庫

ptt_momo_comment_bert_mysql.py （table: momo)
ptt_pchome_comment_bert_mysql.py（table: pchome)
ptt_shopee_comment_bert_mysql.py（table: shopee)

ptt_momo_content_bert_mysql.py（table: momo)
ptt_pchome_content_bert_mysql.py（table: pchome)
ptt_shopee_content_bert_mysql.py（table: shopee)


Jack:

🌼 爬蟲

yt-scrap-MainV8.py
yt-scrap-SubV2.py

yt_Main_data.csv
yt_Sub_data.csv

🌼 with bert 進資料庫

yt-FileBreak.py 
yt-scrap-BERT-V5.py 

Final_BERT.csv
yt-MariaV4.py （table：youtube_data）

yt-_Sub_data.csv
yt-scrap-SubV3.py（table：youtube_subdata）


Jock:

🌹爬蟲

import_link_func.py （抓api）
results_link_finish.csv

mariadb.session.sql （創建sql）

link_in_db.py （table：mobile01_links）
com_in_db.py （table：mobile01_comments）

🌹with bert 進資料庫

mobile01_bert.py
bert_output.csv （table：）
