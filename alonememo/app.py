from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

from pymongo import MongoClient
# client = MongoClient('mongodb://yoonwoo:4565@3.36.71.134', 27017) # 서버 컴퓨터의 DB를 사용할 때
client = MongoClient('localhost', 27017) # 로컬 컴퓨터의 DB를 사용할 때
db = client.dbjungle

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/memo', methods=['GET'])
def read_articles():
    article_list = list(db.articles.find({}, {'_id':False}))
    # print(article_list)
    return jsonify({'result':'success', 'articles':article_list})

# /memo로 POST request가 오면 아래와 같이 응답.
@app.route('/memo', methods=['POST'])
def post_articles():
    # url과 comment request 받아오기
    reqst_dic = request.form # dict 형태로 POST data 받아옴
    url = reqst_dic['url']
    comment = reqst_dic['comment']
    
    # 데이터 url 가지고 data scrapping 하기
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    # print('해치웠나?')

    image = soup.select_one('meta[property="og:image"]')['content']
    title = soup.select_one('meta[property="og:title"]')['content']
    desc = soup.select_one('meta[property="og:description"]')['content']

    article_json = {'url':url, 'title':title, 'desc':desc, 'image':image, 'comment':comment}

    # articles라는 db에 document 넣기
    db.articles.insert_one(article_json)

    return jsonify({'result':'success', 'msg':'POST에 연결됨!'})

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, debug=True)