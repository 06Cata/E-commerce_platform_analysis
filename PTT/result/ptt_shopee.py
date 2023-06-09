from collections import defaultdict
from crawl import crawl_title
from crawlcsv import crawl_csv

print('============eshop=============')

eshop_shopee = crawl_title('e-shopping', 'shopee',5)
crawl_csv(eshop_shopee,'eshop_shopee.csv')

print('============women=============')

women_shopee = crawl_title('WomenTalk', 'shopee',5)
crawl_csv(women_shopee ,'women_shopee.csv')

print('============E_app=============')

E_app_shopee = crawl_title('E-appliance', 'shopee',5)
crawl_csv(E_app_shopee,'E_app_shopee.csv')

print('============Mobile=============')

Mobile_shopee = crawl_title('MobileComm', 'shopee',5)
crawl_csv(Mobile_shopee,'Mobile_shopee.csv')

print('============PC_shop=============')

PC_shop_shopee = crawl_title('PC_Shopping', 'shopee',5)
crawl_csv(PC_shop_shopee,'PC_shop_shopee.csv')

print('============nb=============')

nb_shopee = crawl_title('nb-shopping', 'shopee',5)
crawl_csv(nb_shopee,'nb_shopee.csv')

print('============Audio=============')

Audio_shopee = crawl_title('Audiophile', 'shopee',5)
crawl_csv(Audio_shopee,'Audio_shopee.csv')

print('============watch=============')

watch_shopee = crawl_title('watch', 'shopee',5)
crawl_csv(watch_shopee,'watch_shopee.csv')

print('============Digital=============')

Digital_shopee = crawl_title('Digitalhome', 'shopee',5)
crawl_csv(Digital_shopee ,'Digital_shopee .csv')

print('============MakeUp=============')

MakeUp_shopee = crawl_title('MakeUp', 'shopee',5)
crawl_csv(MakeUp_shopee,'MakeUp_shopee.csv')

print('============Beauty=============')

Beauty_shopee = crawl_title('BeautySalon', 'shopee',5)
crawl_csv(Beauty_shopee,'Beauty_shopee.csv')

print('============Lifeismoney=============')

Lifeismoney_shopee = crawl_title('Lifeismoney', 'shopee',5)
crawl_csv(Lifeismoney_shopee,'Lifeismoney_shopee.csv')

print('============Gossiping=============')

Gossiping_shopee = crawl_title('Gossiping', 'shopee',5)
crawl_csv(Gossiping_shopee ,'Gossiping_shopee.csv')

print('============END=============')