import requests
from bs4 import BeautifulSoup


def crawl_title(query,i,min_comment_length):
    data1 = [] # 全部文章的資料
    ptts=['e-shopping','WomenTalk','MobileComm','PC_Shopping','Lifeismoney','Gossiping']
    num = 0
  
    payload = {
        'from': '/bbs/Gossiping/index.html',
        'yes': 'yes'
    }
    for ptt in ptts:
        base_url = f"https://www.ptt.cc/bbs/{ptt}/search"
        params = {"q": query}

        # 用session紀錄此次使用的cookie
        rs = requests.session()
        response = rs.post("https://www.ptt.cc/ask/over18", data=payload)
    

        for page in range(1,i):
            params["page"] = page
            response = rs.get(base_url, params=params)
            
            html_content = response.text

            res = BeautifulSoup(html_content, "html.parser")
            # 找出每篇文章的連結
            links = res.find_all("div", class_="title")
            # for index, link in enumerate(links):
                 # 在这里使用索引值和 link 进行操作
                #  print(f"Index: {index}, Link: {link}")
            for link in links:
            # 如果文章已被刪除，連結為None
                if link.a != None:

                    article_data = {}   # 單篇文章的資料
                    href=link.a["href"]
                    href_url = f'https://www.ptt.cc/{href}'
        
                    href_response = rs.get(href_url)
                    
                    soup = BeautifulSoup(href_response.text, "html.parser")
                    
                    main_content = soup.find("div", id="main-content")
                    article_info = main_content.find_all(
                        "span", class_="article-meta-value")
                    if len(article_info) == 4 :
                        author = article_info[0].string  # 作者
                        title = article_info[2].string  # 標題
                        time = article_info[3].string   # 時間
                    else:
                        author = "無"  # 作者
                        title = "無"  # 標題
                        time = "無"   # 時間
                    
            
                    # print(author)
                    # print(title)
                    # print(time)
                   
                    article_data["query"]=query
                    article_data["url"]=href_url
                    article_data["author"] = author
                    article_data["title"] = title
                    article_data["time"] = time

                    # 將整段文字內容抓出來
                    all_text = main_content.text
                    # 以--切割，抓最後一個--前的所有內容
                    pre_texts = all_text.split("--")[:-1]
                    # 將前面的所有內容合併成一個
                    one_text = "--".join(pre_texts)
                    # 以\n切割，第一行標題不要
                    texts = one_text.split("\n")[1:]
                    # 將每一行合併
                    content = "\n".join(texts)

                    # print(content)
                    article_data["content"] = content.replace("\n", "")
                    # data1.append(article_data)

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
                            push_tag = push_tag_elem.string   # 分類標籤
                            push_userid = comment.find(
                                "span", class_="push-userid").string  # 使用者ID
                            push_content = comment.find(
                                "span", class_="push-content").text.strip()  # 留言內容
                            push_time_1 = comment.find(
                                "span", class_="push-ipdatetime").text.strip("\n")   # 留言時間
                            alltime=push_time_1.strip().split(" ")
                        if len(alltime) == 3:
                            date = alltime[1]
                            time = alltime[2]
                            push_time= date + " " + time
                        else:
                            push_time=alltime
                        # print(alltime)
                        # print(push_tag, push_userid, push_content, push_time)
                        if len(push_content) >= min_comment_length:
                            dict1 = {"push_userid": push_userid,
                                    "push_content": push_content, "push_time": push_time}
                            
                            if push_tag == "推 ":
                                push_dic.append(dict1)
                            if push_tag == "→ " :
                                arrow_dic.append(dict1)
                            if push_tag == "噓 ":
                                shu_dic.append(dict1)

                    # print(push_dic)
                    # print(arrow_dic)
                    # print(shu_dic)
                    # print("--------")

                    comment_dic["推"] = push_dic
                    comment_dic["→"] = arrow_dic
                    comment_dic["噓"] = shu_dic
                    article_data["comment"] = comment_dic

                    # print(article_data)
                    data1.append(article_data)
                    
                    num += 1
                    article_data["index"]=num
                    print("第 "+str(num)+" 篇文章完成!")
                    

    return data1

