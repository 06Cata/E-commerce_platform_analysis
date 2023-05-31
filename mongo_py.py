import pymongo
from bson.objectid import ObjectId    # 對應到 【四、】搜尋所有符合_id條件的資料

# 【一、必要, 連線到mongodb】
client = pymongo.MongoClient("mongodb://localhost:27017/")  # 27017是預設



# 【二、必要, 選擇db和collection】
db = client.test                      # client下的db
collection = db.users                 # db下的 collection



# 【三、insert資料】
# data = collection.insert_one({ "name": "Emma", "gender": "F" })
# data = collection.insert_many([{"name": "Ivy", "gender": "F", "email":"ivy0529@gmail.com"},
                            #    {"name": "Jock", "gender": "M", "email":"Jock1010@gmail.com"}])



# 【四、find資料】
# data = collection.find_one({"gender": "F" })
# data = collection.find()                          # 需要搭配下方迴圈, 印出所有結果
# data = collection.find({"gender": "F" })          # 需要搭配下方迴圈, 印出所有結果



# 【五、update(覆蓋/不存在就新增)資料】 # "$set" 在python中, 要用雙引號包起來 
# data = collection.update_one({"name":"Ivy"},{"$set":{"email":"ivy_0529@gmail.com"}})
# data = collection.update_many({"name":"Jock"},{"$set":{"level":2}})



# 【六、加減數字欄位資料】 # "$inc" 在python中, 要用雙引號包起來 
# data = collection.update_many({"name":"Jock"},{"$inc":{"level":-1}})   # 原本是 2, 減一後變成1



# 【七、乘除數字欄位資料】 # "$mul" 在python中, 要用雙引號包起來 
# data = collection.update_many({"name":"Jock"},{"$mul":{"level":0.5}})   # 0.5 等於除二



# 【八、清除欄位】 # "$unset" 在python中, 要用雙引號包起來  # 等同 mysql drop
# data = collection.update_many({"name":"Jock"},{"$unset":{"level":1.5}})  # 整個 level欄位刪掉, 數值不重要   



# 【九、刪除資料】 
# data = collection.delete_many({"name":"Jock","gender":"M"})  
# data = collection.delete_many({"$and":[{"name":"Ivy"},{"gender":"F"}]})  



# 【十、排序資料】 # sort=排序方式   # <> DESCENDING
data = collection.find({},sort=[("name",pymongo.ASCENDING)])




# 【十一、必要, 印出插入資料庫的資料做確認】
print("成功!")
print(data)

# print(data.matched_count)       # 符合篩選條件的文件數量
# print(data.modified_count)      # 實際完成更新的文件數量

# print(data.inserted_id)       # 搭配 【三、】insert_one()
# print(data.inserted_ids)      # 搭配 【三、】insert_many()

# print(data["_id"])            # 搭配 【四、】find_one(), 找出有興趣欄位
# print(data["name"])           # 搭配 【四、】find_one(), 找出有興趣欄位

for x in data:                
    print(x)                    # 迴圈, 搭配 【四、】find()、搭配 【十、】sort()

# 也可以去mongodb檢查
# show dbs
# use test
# db.users.find()