from collections import defaultdict
from crawl import crawl_title
from crawlcsv import crawl_csv

print('============eshop=============')

eshop_蝦皮 = crawl_title('e-shopping', '蝦皮',5)
crawl_csv(eshop_蝦皮,'eshop_蝦皮.csv')

print('============women=============')

women_蝦皮 = crawl_title('WomenTalk', '蝦皮',5)
crawl_csv(women_蝦皮 ,'women_蝦皮.csv')

print('============E_app=============')

E_app_蝦皮 = crawl_title('E-appliance', '蝦皮',5)
crawl_csv(E_app_蝦皮,'E_app_蝦皮.csv')

print('============Mobile=============')

Mobile_蝦皮 = crawl_title('MobileComm', '蝦皮',5)
crawl_csv(Mobile_蝦皮,'Mobile_蝦皮.csv')

print('============PC_shop=============')

PC_shop_蝦皮 = crawl_title('PC_Shopping', '蝦皮',5)
crawl_csv(PC_shop_蝦皮,'PC_shop_蝦皮.csv')

print('============nb=============')

nb_蝦皮 = crawl_title('nb-shopping', '蝦皮',5)
crawl_csv(nb_蝦皮,'nb_蝦皮.csv')

print('============Audio=============')

Audio_蝦皮 = crawl_title('Audiophile', '蝦皮',5)
crawl_csv(Audio_蝦皮,'Audio_蝦皮.csv')

print('============watch=============')

watch_蝦皮 = crawl_title('watch', '蝦皮',5)
crawl_csv(watch_蝦皮,'watch_蝦皮.csv')

print('============Digital=============')

Digital_蝦皮 = crawl_title('Digitalhome', '蝦皮',5)
crawl_csv(Digital_蝦皮 ,'Digital_蝦皮 .csv')

print('============MakeUp=============')

MakeUp_蝦皮 = crawl_title('MakeUp', '蝦皮',5)
crawl_csv(MakeUp_蝦皮,'MakeUp_蝦皮.csv')

print('============Beauty=============')

Beauty_蝦皮 = crawl_title('BeautySalon', '蝦皮',5)
crawl_csv(Beauty_蝦皮,'Beauty_蝦皮.csv')

print('============Lifeismoney=============')

Lifeismoney_蝦皮 = crawl_title('Lifeismoney', '蝦皮',5)
crawl_csv(Lifeismoney_蝦皮,'Lifeismoney_蝦皮.csv')

print('============Gossiping=============')

Gossiping_蝦皮 = crawl_title('Gossiping', '蝦皮',5)
crawl_csv(Gossiping_蝦皮 ,'Gossiping_蝦皮.csv')

print('============END=============')