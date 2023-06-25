from collections import defaultdict
# from crawl import crawl_title
import csv
def crawl_csv(data,output_file):
# 创建字典来存储合并后的数据
    merged_data = defaultdict(list)

    # 合并数据
    for article in data:
        author = article['author']
        title = article['title']
        time = article['time']
        content = article['content']
        comments = article['comment']

        # 创建唯一的键，用于合并相同的行
        key = (author, title, time, content)

        # 将每一行的推文信息追加到对应的键下
        for push_tag, push_list in comments.items():
            for comment in push_list:
                push_userid = comment['push_userid']
                push_content = comment['push_content']
                push_time = comment['push_time']
                merged_data[key].append((push_tag, push_userid, push_content, push_time))

    # 将合并后的数据写入 CSV 文件
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)

        # 写入字段名
        writer.writerow(['Author', 'Title', 'Time', 'Content', 'Push Tag', 'Push User ID', 'Push Content', 'Push Time'])

        # 写入合并后的数据
        for key, comments in merged_data.items():
            author, title, time, content = key

            # 如果没有推文的评论，写入一行数据
            if not comments:
                writer.writerow([author, title, time, content, '', '', '', ''])
            else:
                # 写入原始文章信息的第一行
                writer.writerow([author, title, time, content, comments[0][0], comments[0][1], comments[0][2], comments[0][3]])

                # 写入推文的评论信息的后续行
                for comment in comments[1:]:
                    writer.writerow(['', '', '', '', comment[0], comment[1], comment[2], comment[3]])

    return


