from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.action_chains import ActionChains
import csv

# # selenium # #
# 【零、設置好登入條件】
FACEBOOK_ID = " @gmail.com"
FACEBOOK_PW = " "
TARGET_URL = "https://www.facebook.com/momofans/"


# 【一、創建瀏覽器、指定無痕模式】
options = webdriver.ChromeOptions()
# options.add_argument("incognito")


# 【二、創建 Chrome 瀏覽器的 webdriver 實例，打開 url】
# print 出頁面的標題
driver = webdriver.Chrome(options = options)
driver.get("https://www.facebook.com")

print("go " + driver.title )
time.sleep(3)


# 【三、使用 find_element() 找到要輸入的表格】
email =  driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "pass")
login = driver.find_element(By.NAME, "login")

# 【三-二、輸入零、的資料, 送出】
email.send_keys(FACEBOOK_ID)
password.send_keys(FACEBOOK_PW)
login.submit()
time.sleep(3)


# # 到 beautifulsoup # #
#【一、取得網頁內容】
# 要求get url
driver.get(TARGET_URL)
time.sleep(10)


# # 【二、找到搜尋欄】
# element = driver.find_element(By.CSS_SELECTOR, 'div.x1i10hfl[aria-label="搜尋"]')
# element.click()
# time.sleep(3)

# # 【二-二、輸入】
# input_element = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="搜尋此社團"]')
# input_element.send_keys("momo")
# time.sleep(3)

# # 【二-三、提交】
# option_element = driver.find_element(By.XPATH, '//span[contains(text(), "momo")]')
# option_element.click()
# time.sleep(3)


# 【三、設置js滾動滑鼠的次數】
for x in range(1, 450):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(6)


#【四、HTML 內容轉換為 BeautifulSoup 物件】
soup = BeautifulSoup(driver.page_source, 'html.parser')


# 【五、找出所有文章+時間, 寫進迴圈】
titles = soup.findAll("div", {"class":"x78zum5 x1n2onr6 xh8yej3"})
# times = soup.select('.x4k7w5x a')


# # 【八、印出來】
print("一共:" + str(len(titles)) + " 則文章...")

data = []
for t in range(len(titles)):
    # time_text = times[i].text
    title_text = titles[t].text

    data.append(title_text)
    
    # print("時間:", time_text)
    print("po文:", title_text)
    print("----------------------------------------")
    

with open("momo_post.csv", "w", encoding='utf-8', newline='') as file:
    writer = csv.writer(file)

    for d in data:
        writer.writerow([d])
    

# 【九、關閉瀏覽器】
driver.quit()
