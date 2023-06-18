from collections import defaultdict
from crawl import crawl_title
from crawlcsv import crawl_csv

# print('============eshop=============')

# eshop_pchome = crawl_title('e-shopping', 'pchome',5)
# crawl_csv(eshop_pchome,'eshop_pchome.csv')

# print('============women=============')

# women_pchome = crawl_title('WomenTalk', 'pchome',5)
# crawl_csv(women_pchome ,'women_pchome.csv')

# print('============E_app=============')

# E_app_pchome = crawl_title('E-appliance', 'pchome',5)
# crawl_csv(E_app_pchome,'E_app_pchome.csv')

# print('============Mobile=============')

# Mobile_pchome = crawl_title('MobileComm', 'pchome',5)
# crawl_csv(Mobile_pchome,'Mobile_pchome.csv')

# print('============PC_shop=============')

# PC_shop_pchome = crawl_title('PC_Shopping', 'pchome',5)
# crawl_csv(PC_shop_pchome,'PC_shop_pchome.csv')

# print('============nb=============')

# nb_pchome = crawl_title('nb-shopping', 'pchome',5)
# crawl_csv(nb_pchome,'nb_pchome.csv')
# print('============Audio=============')

# Audio_pchome = crawl_title('Audiophile', 'pchome',5)
# crawl_csv(Audio_pchome,'Audio_pchome.csv')

# print('============watch=============')

# watch_pchome = crawl_title('watch', 'pchome',5)
# crawl_csv(watch_pchome,'watch_pchome.csv')

# print('============Digital=============')

# Digital_pchome = crawl_title('Digitalhome', 'pchome',5)
# crawl_csv(Digital_pchome ,'Digital_pchome .csv')

# print('============MakeUp=============')

# MakeUp_pchome = crawl_title('MakeUp', 'pchome',5)
# crawl_csv(MakeUp_pchome,'MakeUp_pchome.csv')

print('============Beauty=============')

Beauty_pchome = crawl_title('BeautySalon', 'pchome',5)
crawl_csv(Beauty_pchome,'Beauty_pchome.csv')

print('============Lifeismoney=============')

Lifeismoney_pchome = crawl_title('Lifeismoney', 'pchome',5)
crawl_csv(Lifeismoney_pchome,'Lifeismoney_pchome.csv')

print('============Gossiping=============')

Gossiping_pchome = crawl_title('Gossiping', 'pchome',5)
crawl_csv(Gossiping_pchome ,'Gossiping_pchome.csv')

print('============END=============')