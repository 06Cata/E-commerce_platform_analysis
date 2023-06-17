#加了bert的main.py
from collections import defaultdict
from ptt_crawl_v9 import crawl_title
from ptt_crawlcsv_v4 import crawl_csv
from ptt_comment_mysql import ptt_db_com
from ptt_content_mysql import ptt_db_con
min_length = 15

#PTT_crawl
print('============CRAWL_START=============')
print('============ptt_momo=============')
eshop_momo = crawl_title('momo',2,min_length)
crawl_csv(eshop_momo,'eshop_momo_content.csv','eshop_momo_comments.csv')

print('============ptt_pchome=============')
eshop_pchome = crawl_title('pchome',2,min_length)
crawl_csv(eshop_pchome,'eshop_pchome_content.csv','eshop_pchome_comments.csv')

print('============ptt_蝦皮=============')
eshop_蝦皮 = crawl_title('蝦皮',2,min_length)
crawl_csv(eshop_蝦皮,'eshop_shopee_content.csv','eshop_shopee_comments.csv')

print('============CRAWL_END=============')

#DB_comments
print('============DB_momo_comments_START=============')
ptt_db('eshop_momo_comments.csv','momo')
print('============DB_momo_comments_END=============')


print('============DB_pchome_comments_START=============')
ptt_db('eshop_pchome_comments.csv','pchome')
print('============DB_pchome_comments_END=============')


print('============DB_shopee_comments_START=============')
ptt_db('eshop_shopee_comments.csv','shopee')
print('============DB_shopee_comments_END=============')

#DB_content

print('============DB_momo_content_START=============')
ptt_db('eshop_momo_content.csv','momo')
print('============DB_momo_content_END=============')


print('============DB_pchome_content_START=============')
ptt_db('eshop_pchome_content.csv','pchome')
print('============DB_pchome_content_END=============')


print('============DB_shopee_content_START=============')
ptt_db('eshop_shopee_content.csv','shopee')
print('============DB_shopee_content_END=============')