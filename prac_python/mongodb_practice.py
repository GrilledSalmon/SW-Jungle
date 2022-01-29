from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

# 데이터 삽입
db.users.insert_one({'name':'bobby', 'age':21})
db.users.insert_one({'name':'kay', 'age':27})
db.users.insert_one({'name':'john', 'age':30})

# MongoDB에서 데이터 모두 보기
all_users = list(db.users.find({}))
print(all_users)