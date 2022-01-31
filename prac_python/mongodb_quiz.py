from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle

matrix_point = db.movies.find_one({'title':'매트릭스'})['star']

for movie in db.movies.find({'star':matrix_point}):
    print(movie['title'])

db.movies.update_one({'title':'매트릭스'}, {'$set' : {'star':0}})