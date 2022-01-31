from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

# users라는 collection에 데이터 삽입
# db.users.insert_one({'name':'bobby', 'age':21})
# db.users.insert_one({'name':'kay', 'age':27})
# db.users.insert_one({'name':'john', 'age':30})

# MongoDB에서 데이터 모두 보기
# db.users.delete_one({'name':'bobby'})
# db.users.delete_one({'name':'kay'})
# db.users.delete_one({'name':'john'})
# db.users.drop()
all_users = list(db.users.find())
print(all_users)

some_users = list(db.users.find({'name':'john'}, {'age':False}))
db.users.update_one({'name':'john'},{'$set':{'age':190}})
john = db.users.find_one({'name':'john'}, {'_id':False})
print(john)