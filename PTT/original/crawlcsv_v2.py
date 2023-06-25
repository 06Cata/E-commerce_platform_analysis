from collections import defaultdict
# from crawl import crawl_title
import csv
def crawl_csv(data,output_file):

    with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Author', 'Title', 'Time', 'Content', 'Push Tag', 'Push User ID', 'Push Content', 'Push Time'])
            for article in data:
                author = article['author']
                title = article['title']
                time = article['time']
                content = article['content']
                comments = article['comment']

                for push_tag, push_list in comments.items():
                        for comment in push_list:
                            push_userid = comment['push_userid']
                            push_content = comment['push_content']
                            push_time = comment['push_time']

                            writer.writerow([author, title, time, content, push_tag,push_userid, push_content, push_time])
                    
    return
        
        

        