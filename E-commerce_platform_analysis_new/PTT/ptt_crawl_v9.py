import re
import requests
from bs4 import BeautifulSoup
from urlextract import URLExtract
import datetime
from ptt_crawlcsv_v4 import crawl_csv
def crawl_title(query, i, min_comment_length):
    data1 = []  # 全部文章的資料
    ptts = ['e-shopping', 'WomenTalk', 'MobileComm', 'PC_Shopping', 'Lifeismoney', 'Gossiping']
    num = 0

    payload = {
        'from': '/bbs/Gossiping/index.html',
        'yes': 'yes'
    }
    extractor = URLExtract()

    chinese_pattern = re.compile(r'[\u4e00-\u9fff]')  # 中文字符範圍的正則表達式

    for ptt in ptts:
        base_url = f"https://www.ptt.cc/bbs/{ptt}/search"
        params = {"q": query}

        # 用session紀錄此次使用的cookie
        rs = requests.session()
        response = rs.post("https://www.ptt.cc/ask/over18", data=payload)

        for page in range(1, i):
            params["page"] = page
            response = rs.get(base_url, params=params)

            html_content = response.text

            res = BeautifulSoup(html_content, "html.parser")
            # 找出每篇文章的連結
            links = res.find_all("div", class_="title")

            for link in links:
                # 如果文章已被刪除，連結為None
                if link.a is not None:
                    article_data = {}  # 單篇文章的資料
                    href = link.a["href"]
                    href_url = f'https://www.ptt.cc/{href}'

                    href_response = rs.get(href_url)

                    soup = BeautifulSoup(href_response.text, "html.parser")

                    main_content = soup.find("div", id="main-content")
                    article_info = main_content.find_all("span", class_="article-meta-value")
                    if len(article_info) == 4:
                        author = article_info[0].string  # 作者
                        title = article_info[2].string  # 標題
                        input_string = article_info[3].string  # 時間
                        input_datetime = datetime.datetime.strptime(input_string, "%a %b %d %H:%M:%S %Y")
                        time = input_datetime.strftime("%Y/%m/%d %H:%M:%S %a")
                        
                        

 

                      

                    else:
                        author = "無"  # 作者
                        title = "無"  # 標題
                        time = "無"  # 時間

                    article_data["query"] = query
                    article_data["url"] = href_url
                    article_data["author"] = author
                    article_data["title"] = title
                    article_data["time"] = time

                    # 將整段文字內容抓出來
                    all_text = main_content.text
                    # 以--切割，抓最後一個--
                    pre_texts = all_text.split("--")[:-1]
                    # 將前面的所有內容合併成一個
                    one_text = "--".join(pre_texts)
                    # 以\n切割，第一行標題不要
                    texts = one_text.split("\n")[1:]
                    # 將每一行合併
                    content = "\n".join(texts)

                    # 過濾掉不包含中文的欄位
                    if chinese_pattern.search(content):
                        article_data["content"] = content.replace("\n", "")

                        # 一種留言一個列表
                        comment_dic = {}

                        push_dic = []
                        arrow_dic = []
                        shu_dic = []

                        # 抓出所有留言
                        comments = main_content.find_all("div", class_="push")

                        for comment in comments:
                            push_tag_elem = comment.find("span", class_="push-tag")

                            if push_tag_elem:
                                push_tag = push_tag_elem.string  # 分類標籤
                                push_userid = comment.find("span", class_="push-userid").string  # 使用者ID
                                push_content = comment.find("span", class_="push-content").text.strip()  # 留言內容
                                push_time_1 = comment.find("span", class_="push-ipdatetime").text.strip("\n")  # 留言時間
                                alltime = push_time_1.strip().split(" ")
                                if len(alltime) == 3:
                                    date = alltime[1]
                                    ptime = alltime[2]
                                    push_time = date + " " + ptime
                                    # 解析字符串 b 为日期时间对象，但年份设为与 datetime_a 相同
                                    push_time = datetime.datetime.strptime(push_time, "%m/%d %H:%M")
                                    push_time = push_time.replace(year=input_datetime.year)
                                    push_time = push_time.strftime("%Y/%m/%d %H:%M")
                                elif len(alltime) == 2:
                                    date = alltime[0]
                                    ptime = alltime[1]
                                    push_time = date + " " + ptime
                                    # 解析字符串 b 为日期时间对象，但年份设为与 datetime_a 相同
                                    push_time = datetime.datetime.strptime(push_time, "%m/%d %H:%M")
                                    push_time = push_time.replace(year=input_datetime.year)
                                    push_time = push_time.strftime("%Y/%m/%d %H:%M")
                            
                                else:
                                    push_time = alltime

                                # 使用 urlextract 套件擷取留言內容中的網址
                                urls = extractor.find_urls(push_content)
                                if len(push_content) >= min_comment_length and not urls and chinese_pattern.search(
                                        push_content):
                                    dict1 = {"push_userid": push_userid, "push_content": push_content}

                                    if push_tag == "推 ":
                                        push_dic.append(dict1)
                                    if push_tag == "→ ":
                                        arrow_dic.append(dict1)
                                    if push_tag == "噓 ":
                                        shu_dic.append(dict1)
                                    dict1["push_time"] = push_time

                        comment_dic["推"] = push_dic
                        comment_dic["→"] = arrow_dic
                        comment_dic["噓"] = shu_dic
                        article_data["comment"] = comment_dic

                        data1.append(article_data)

                        num += 1
                        article_data["index"] = num
                        print("第 " + str(num) + " 篇文章完成!")

    return data1
