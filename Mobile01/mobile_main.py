import pymysql
import requests
import csv
import json
import os
from datetime import datetime
import time
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from app_mobils01_scrapy import google_api_link ,cat_com_by_csv_to_db, cat_link_by_csv_to_db

# queries = ["momo", "蝦皮", "pchome"]
# google_api_link( queries,num_results_per_page=5,total_results=10 )
    


# cat_link_by_csv_to_db()

cat_com_by_csv_to_db()



