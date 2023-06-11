from collections import defaultdict
# from crawl import crawl_title
import csv
def crawl_csv(data,content_file,comment_file):

    with open(content_file, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Index','Qurery','Author', 'Title', 'Time', 'Content','Url'])
        for article_data in data:
            index=article_data['index']
            query=article_data['query']
            author = article_data['author']
            title = article_data['title']
            time = article_data['time']
            content = article_data['content']
            comment_url=article_data['url']

            # comments=article_data['comments']
            writer.writerow([index,query,author, title, time, content,comment_url])

    with open(comment_file, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Index','Qurery','Url','Push Tag', 'Push User ID', 'Push Content', 'Push Time'])
            for article_data in data:
                index=article_data['index']
                query=article_data['query']
                comments = article_data['comment']
                content_url=article_data['url']

                for push_tag, push_list in comments.items():
                        for comment in push_list:
                            push_userid = comment['push_userid']
                            push_content = comment['push_content']
                            push_time = comment['push_time']

                            writer.writerow([index,query,content_url,push_tag,push_userid, push_content, push_time])               
    return
        
        