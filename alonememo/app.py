from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/memo', methods=['GET'])
def listing():
    return jsonify({'result':'success', 'msg':'GET에 연결됨!'})

# /memo로 POST request가 오면 아래와 같이 응답.
@app.route('/memo', methods=['POST'])
def saving():
    # url과 comment request 받아오기
    reqst_dic = request.form # dict 형태로 POST data 받아옴
    url = reqst_dic['url']
    comment = reqst_dic['comment']

    # 데이터 url 가지고 data scrapping 하기
    

    return jsonify({'result':'success', 'msg':'POST에 연결됨!'})

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, debug=True)