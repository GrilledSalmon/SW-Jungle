import requests
from pymongo import MongoClient
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

client = MongoClient('mongodb://yoonwoo:pw@3.36.71.134', 27017) # 원격 MongoDB 연결. pw 입력 요
db = client.dbjungle

# home
@app.route('/')
def home():
    return render_template('index.html')

# GET API
@app.route('/api/list', methods=['GET'])
def show_stars():
    star_list = list(db.mystar.find({}, {'_id':False}))

    return jsonify({'result':'success', 'stars':star_list})

# POST API
@app.route('/api/like', methods=['POST'])
def like_star():
    name = request.form['name']
    
    return jsonify({'result':'success'})


if __name__=='__main__':
    app.run('0.0.0.0', port=5000, debug=True)