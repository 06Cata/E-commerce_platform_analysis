from collections import defaultdict
from crawl import crawl_title
from crawlcsv import crawl_csv

print('============eshop=============')

eshop_平台 = crawl_title('e-shopping', '平台',5)
crawl_csv(eshop_平台,'eshop_平台.csv')

print('============women=============')

women_平台 = crawl_title('WomenTalk', '平台',5)
crawl_csv(women_平台 ,'women_平台.csv')

print('============E_app=============')

E_app_平台 = crawl_title('E-appliance', '平台',5)
crawl_csv(E_app_平台,'E_app_平台.csv')

print('============Mobile=============')

Mobile_平台 = crawl_title('MobileComm', '平台',5)
crawl_csv(Mobile_平台,'Mobile_平台.csv')

print('============PC_shop=============')

PC_shop_平台 = crawl_title('PC_Shopping', '平台',5)
crawl_csv(PC_shop_平台,'PC_shop_平台.csv')

print('============nb=============')

nb_平台 = crawl_title('nb-shopping', '平台',5)
crawl_csv(nb_平台,'nb_平台.csv')

print('============Audio=============')

Audio_平台 = crawl_title('Audiophile', '平台',5)
crawl_csv(Audio_平台,'Audio_平台.csv')

print('============watch=============')

watch_平台 = crawl_title('watch', '平台',5)
crawl_csv(watch_平台,'watch_平台.csv')

print('============Digital=============')

Digital_平台 = crawl_title('Digitalhome', '平台',5)
crawl_csv(Digital_平台 ,'Digital_平台 .csv')

print('============MakeUp=============')

MakeUp_平台 = crawl_title('MakeUp', '平台',5)
crawl_csv(MakeUp_平台,'MakeUp_平台.csv')

print('============Beauty=============')

Beauty_平台 = crawl_title('BeautySalon', '平台',5)
crawl_csv(Beauty_平台,'Beauty_平台.csv')

print('============Lifeismoney=============')

Lifeismoney_平台 = crawl_title('Lifeismoney', '平台',5)
crawl_csv(Lifeismoney_平台,'Lifeismoney_平台.csv')

print('============Gossiping=============')

Gossiping_平台 = crawl_title('Gossiping', '平台',5)
crawl_csv(Gossiping_平台 ,'Gossiping_平台.csv')

print('============END=============')