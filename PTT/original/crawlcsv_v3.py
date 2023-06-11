from collections import defaultdict
# from crawl import crawl_title
import csv
def crawl_csv(data,content_file,comment_file):

    with open(content_file, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Author', 'Title', 'Time', 'Content','Comment url'])
        for article_data in data:
            author = article_data['author']
            title = article_data['title']
            time = article_data['time']
            content = article_data['content']
            comment_url=article_data['url']
            # comments=article_data['comments']
            writer.writerow([author, title, time, content,comment_url])

    with open(comment_file, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Content url','Push Tag', 'Push User ID', 'Push Content', 'Push Time'])
            for article_data in data:
                comments = article_data['comment']
                content_url=article_data['url']
                for push_tag, push_list in comments.items():
                        for comment in push_list:
                            push_userid = comment['push_userid']
                            push_content = comment['push_content']
                            push_time = comment['push_time']

                            writer.writerow([content_url,push_tag,push_userid, push_content, push_time])               
    return
        
        