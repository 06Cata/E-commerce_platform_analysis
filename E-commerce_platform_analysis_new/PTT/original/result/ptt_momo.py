from collections import defaultdict
from crawl import crawl_title
from crawlcsv_v2 import crawl_csv
print('============eshop=============')

eshop_momo = crawl_title('e-shopping', 'momo',2)
crawl_csv(eshop_momo,'eshop_momo.csv')

print('============women=============')

women_momo = crawl_title('WomenTalk', 'momo',5)
crawl_csv(women_momo ,'women_momo.csv')

print('============E_app=============')

E_app_momo = crawl_title('E-appliance', 'momo',5)
crawl_csv(E_app_momo,'E_app_momo.csv')

print('============Mobile=============')

Mobile_momo = crawl_title('MobileComm', 'momo',5)
crawl_csv(Mobile_momo,'Mobile_momo.csv')

print('============PC_shop=============')

PC_shop_momo = crawl_title('PC_Shopping', 'momo',5)
crawl_csv(PC_shop_momo,'PC_shop_momo.csv')

print('============nb=============')

nb_momo = crawl_title('nb-shopping', 'momo',5)
crawl_csv(nb_momo,'nb_momo.csv')

print('============Audio=============')

Audio_momo = crawl_title('Audiophile', 'momo',5)
crawl_csv(Audio_momo,'Audio_momo.csv')

print('============watch=============')

watch_momo = crawl_title('watch', 'momo',5)
crawl_csv(watch_momo,'watch_momo.csv')

print('============Digital=============')

Digital_momo = crawl_title('Digitalhome', 'momo',5)
crawl_csv(Digital_momo ,'Digital_momo .csv')

print('============MakeUp=============')

MakeUp_momo = crawl_title('MakeUp', 'momo',5)
crawl_csv(MakeUp_momo,'MakeUp_momo.csv')

print('============Beauty=============')

Beauty_momo = crawl_title('BeautySalon', 'momo',5)
crawl_csv(Beauty_momo,'Beauty_momo.csv')

print('============Lifeismoney=============')

Lifeismoney_momo = crawl_title('Lifeismoney', 'momo',5)
crawl_csv(Lifeismoney_momo,'Lifeismoney_momo.csv')

print('============Gossiping=============')

Gossiping_momo = crawl_title('Gossiping', 'momo',5)
crawl_csv(Gossiping_momo ,'Gossiping_momo.csv')

print('============END=============')