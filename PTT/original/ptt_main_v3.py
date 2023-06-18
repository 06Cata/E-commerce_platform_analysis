from collections import defaultdict
from crawl_v5 import crawl_title
from crawlcsv_v4 import crawl_csv
# data,content_file,comments_data,comment_file,href_url)
min_length = 15
print('============START=============')
print('============ptt_momo=============')
eshop_momo = crawl_title('momo',2,min_length)
crawl_csv(eshop_momo,'eshop_momo_content.csv','eshop_momo_comments.csv')

# ptt_posts = get_ptt_posts(url, min_length)

# print('============ptt_pchome=============')
# eshop_pchome = crawl_title('pchome',2,min_length)
# crawl_csv(eshop_pchome,'eshop_pchome_content.csv','eshop_pchome_comments.csv')

# print('============ptt_shopee=============')
# eshop_shopee = crawl_title('shopee',2,min_length)
# crawl_csv(eshop_shopee,'eshop_shopee_content.csv','eshop_shopee_comments.csv')

# print('============ptt_蝦皮=============')
# eshop_蝦皮 = crawl_title('蝦皮',2,min_length)
# crawl_csv(eshop_蝦皮,'eshop_shopee2_content.csv','eshop_shopee2_comments.csv')

# print('============ptt_電商=============')
# eshop_電商 = crawl_title('電商',2,min_length)
# crawl_csv(eshop_電商,'eshop_ec_content.csv','eshop_ec_comments.csv')

# print('============ptt_平台=============')
# eshop_平台 = crawl_title('平台',2,min_length)
# crawl_csv(eshop_平台,'eshop_平台_content.csv','eshop_平台_comments.csv')

print('============ptt_END=============')

# women_momo = crawl_title('WomenTalk', 'momo',5)
# crawl_csv(women_momo ,'women_momo.csv')

# print('============E_app=============')

# E_app_momo = crawl_title('E-appliance', 'momo',5)
# crawl_csv(E_app_momo,'E_app_momo.csv')

# print('============Mobile=============')

# Mobile_momo = crawl_title('MobileComm', 'momo',5)
# crawl_csv(Mobile_momo,'Mobile_momo.csv')

# print('============PC_shop=============')

# PC_shop_momo = crawl_title('PC_Shopping', 'momo',5)
# crawl_csv(PC_shop_momo,'PC_shop_momo.csv')

# print('============nb=============')

# nb_momo = crawl_title('nb-shopping', 'momo',5)
# crawl_csv(nb_momo,'nb_momo.csv')

# print('============Audio=============')

# Audio_momo = crawl_title('Audiophile', 'momo',5)
# crawl_csv(Audio_momo,'Audio_momo.csv')

# print('============watch=============')

# watch_momo = crawl_title('watch', 'momo',5)
# crawl_csv(watch_momo,'watch_momo.csv')

# print('============Digital=============')

# Digital_momo = crawl_title('Digitalhome', 'momo',5)
# crawl_csv(Digital_momo ,'Digital_momo .csv')

# print('============MakeUp=============')

# MakeUp_momo = crawl_title('MakeUp', 'momo',5)
# crawl_csv(MakeUp_momo,'MakeUp_momo.csv')

# print('============Beauty=============')

# Beauty_momo = crawl_title('BeautySalon', 'momo',5)
# crawl_csv(Beauty_momo,'Beauty_momo.csv')

# print('============Lifeismoney=============')

# Lifeismoney_momo = crawl_title('Lifeismoney', 'momo',5)
# crawl_csv(Lifeismoney_momo,'Lifeismoney_momo.csv')

# print('============Gossiping=============')

# Gossiping_momo = crawl_title('Gossiping', 'momo',5)
# crawl_csv(Gossiping_momo ,'Gossiping_momo.csv')

# print('============END=============')