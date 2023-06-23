import pandas as pd
import re, time, requests
import random
import csv, json
import pymysql
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
# # 登入fb, 找到特定粉絲團, 在裡面搜尋並下滾n次
    # 【零、先設變數】

search_keyword = input(str("what is your keyword? momo or pchome? "))


FACEBOOK_ID = "catalinakuowork@gmail.com"
FACEBOOK_PW = "Aa_0954033969"
url = 'https://www.facebook.com/groups/shumai'
n = 6

def FindLinks(url, n):
    
    # 【一、設置 def 進入facebook, 使用 find_element() 找到要輸入的表格, 並登入】
    driver.get("https://www.facebook.com")
    time.sleep(random.randint(3, 7))
    
    email =  driver.find_element(By.ID, "email")
    password = driver.find_element(By.ID, "pass")
    login = driver.find_element(By.NAME, "login")

    email.send_keys(FACEBOOK_ID)
    password.send_keys(FACEBOOK_PW)
    login.submit()
    time.sleep(random.randint(3, 7))
    
    
    # 【二-一、找到粉絲團】 # '電商燒賣研究所' 要先登入才能搜尋
    driver.get(url)
    time.sleep(random.randint(3, 7))
    
    # 【二-二、找到搜尋欄】
    element = driver.find_element(By.CSS_SELECTOR,'div.x1i10hfl[aria-label="搜尋"]')
    element.click()
    time.sleep(random.randint(3, 7))
    
    # 【二-三、輸入】
    input_element = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="搜尋此社團"]')
    input_element.send_keys(f"{search_keyword}")
    
    time.sleep(random.randint(3, 7))

    # 【二-四、提交】
    action = ActionChains(driver)
    option_element = driver.find_element(By.XPATH, f'//span[contains(text(), "{search_keyword}")]')
    action.move_to_element(option_element).click().perform()

    # option_element.click()
    time.sleep(random.randint(3, 7))
    return 
options = webdriver.ChromeOptions()
options.add_argument("incognito")    
driver = webdriver.Chrome(options = options)
for x in range(1, n):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(random.randint(3, 7))
Links = FindLinks(url, n)

#========================================================================================================
# 點進留言後再打開'查看更多' & '所有留言'
def Expand_Post_Comment():
        print("開始")
        data=[]
        time.sleep(random.randint(10, 15))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        #文章陣列
        all_articles = soup.find_all("div", {"class":"xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a"})                                  
        print(all_articles)
        # results={}
        #i=0   i=1
        for i in range(1,len(all_articles)):
            time.sleep(3)

            # 【一、展開留言】 # 點開文章留言, 進去後最相關留言 => 所有留言
            try:
                comment_button = driver.find_elements(By.CSS_SELECTOR,'div.xq8finb.x16n37ib [aria-label="留言"]')
                # comment_button= comment_buttons.find_element(By.CSS_SELECTOR,'[aria-label="留言"]')
                time.sleep(3)
                action = ActionChains(driver)
                action.move_to_element(comment_button[i-1]).click().perform()  
            except NoSuchElementException:
                print("留言點擊失败")

            try:
                time.sleep(random.randint(5, 10))
                related_button= driver.find_element(By.CSS_SELECTOR,'div.x6s0dn4.x78zum5.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xe0p6wg div')
                time.sleep(3)
                action = ActionChains(driver)
                action.move_to_element(related_button).click().perform()
                time.sleep(3)
            except NoSuchElementException:
                print("-> 點擊失敗")

            try:
                # related_button = driver.find_element(By.XPATH, '//span[contains(text(), "所有留言")]')
                related_button = driver.find_element(By.CSS_SELECTOR,'div.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj div[role="menuitem"]:nth-child(3)')
                # related_button2= related_buttons.find_element(By.CSS_SELECTOR,'div[role="menuitem"]')
                # related_button = related_buttons[2]
                
                time.sleep(3)

                action = ActionChains(driver)
                action.move_to_element(related_button).click().perform()
                time.sleep(random.randint(5, 10))
            except NoSuchElementException:
                print("-> 所有留言點擊失敗")

        # 【二、展開'顯示更多'】 # 點開留言裡面的顯示更多. 抓取完整文章內容
            show_more_buttons = driver.find_elements(By.XPATH, "//div[contains(text(), '顯示更多')]")
            if show_more_buttons:
                for button in show_more_buttons:
                    try:
                        button.click()
                        time.sleep(random.randint(3, 7))
                        print('Clicked "顯示更多" button')
                    except:
                        pass
                
        # 【三、模擬鍵盤按鍵，向下滾動彈出視窗的內容】  # selenium python how to scroll down in a pop up window
                element_inside_popup = driver.find_element(By.XPATH, '//*[@id="facebook"]')
                element_inside_popup.send_keys(Keys.END)
                time.sleep(random.randint(5, 10))
                    
                # 【四、轉換html物件】    
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                #【五、找到時間/Po文/留言】
                print("一共:" + str(len(all_articles)) + " 則文章...")
                article={}
                allin_article = soup.find_all("div",{"class":"x78zum5 xdt5ytf x1iyjqo2 x1n2onr6 xaci4zi x129vozr"})
                for allin in allin_article:
                    time.sleep(3)
                    artical_text= allin.find("div",{"class":"xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a"})
                    time.sleep(5)
                    article_times= allin.find("a", {"class":"x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv xo1l8bm"})
                    time.sleep(5)
                    comments = allin.findAll("div", {"class": "xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs"})
                    print("一共:" + str(len(comments)) + " 則留言...")
                    article["文章"] =artical_text.text
                    article["時間"]=article_times.text
                    print("文章:",artical_text.text)
                    print("時間:",article_times.text)
                    article_comments=[]
                    for comment in comments :
                        article_comments.append(comment.text)
                        article["留言"]=article_comments
                        print("留言:", comment.text)     
                    data.append(article)               
                    # print(data)
                    print("#################################")



                # 【四、關閉留言】
                    # close_button = driver.find_element(By.CSS_SELECTOR, 'div.x1i10hfl div [aria-label]')
                    # close_button.click()
                try:
                        close_button = driver.find_element(By.CSS_SELECTOR, 'div.x1i10hfl div')
                        actions = ActionChains(driver)
                        actions.move_to_element(close_button).click().perform()

                        element_popup = driver.find_element(By.XPATH, '//*[@id="facebook"]')
                        element_popup.send_keys(Keys.PAGE_DOWN)
                        time.sleep(random.randint(5, 10))
                        if element_popup.location['y'] >= int(element_popup.get_attribute('scrollHeight')):
                            element_popup.send_keys(Keys.HOME)
                            time.sleep(random.randint(5, 10))
                            break
                except:
                    pass
                    print("失敗")
        return data


data = Expand_Post_Comment()
with open(f'fb_shumai_{search_keyword}_comment.json', mode='w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False)

print('已寫入JSON文件')

"=============================================================================="

# Connect to the database
db = pymysql.connect(host="localhost",
                     user="root",
                     password="000000",
                     database="facebook")

cursor = db.cursor()


# Read the JSON file
with open(f'fb_shumai_{search_keyword}_comment.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Insert data into the table
for entry in data:
    source = 'facebook'
    keyword = search_keyword
    time = entry['時間']
    post = entry['文章']
    comments = entry['留言']

    try:
        parsed_date = datetime.datetime.strptime(time, '%m月%d日上午%H:%M')
        parsed_date = parsed_date.replace(year=2023)   
        time = parsed_date.strftime('%Y-%m-%d')   
    except ValueError:
        try:
            parsed_date = datetime.datetime.strptime(time, '%m月%d日')
            parsed_date = parsed_date.replace(year=2023)  # 替換年份
            time = parsed_date.strftime('%Y-%m-%d')   
        except ValueError:
            pass

    for comment in comments:
        insert_data_query = """
        INSERT INTO facebook_shumai_{} (source, keyword, time, post, comment)
        VALUES (%s, %s, %s, %s, %s)
        """.format(search_keyword)
        cursor.execute(insert_data_query, (source, keyword, time, post, comment))
        print('已寫入Mysql')



# Commit the changes and close the connection
db.commit()
db.close()
