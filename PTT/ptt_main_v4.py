from collections import defaultdict
from crawl_v5 import crawl_title
from crawlcsv_v4 import crawl_csv
# data,content_file,comments_data,comment_file,href_url)
min_length = 15
print('============START=============')
print('============ptt_momo=============')
eshop_momo = crawl_title('momo',2,min_length)
crawl_csv(eshop_momo,'eshop_momo_content.csv','eshop_momo_comments.csv')

print('============ptt_pchome=============')
eshop_pchome = crawl_title('pchome',2,min_length)
crawl_csv(eshop_pchome,'eshop_pchome_content.csv','eshop_pchome_comments.csv')

print('============ptt_蝦皮=============')
eshop_蝦皮 = crawl_title('蝦皮',2,min_length)
crawl_csv(eshop_蝦皮,'eshop_shopee2_content.csv','eshop_shopee2_comments.csv')


print('============ptt_END=============')

