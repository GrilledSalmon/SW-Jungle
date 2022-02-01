from pymongo import MongoClient

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbjungle

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/list', methods=['GET'])
def show_stars():
    star_list = list(db.mystar.find({}, {'_id':False}))
    star_list.sort(key=lambda dic:-dic['like']) # 좋아요 순으로 내림차순

    return jsonify({'result':'success', 'stars':star_list})

@app.route('/api/like', methods=['POST'])
def like_star():
    name = request.form['name']
    now_like = db.mystar.find_one({'name':name})['like']
    db.mystar.update_one({'name':name}, {'$set':{'like':now_like+1}})

    return jsonify({'result':'success'})

@app.route('/api/delete', methods=['POST'])
def delete_star():
    name = request.form['name']
    db.mystar.delete_one({'name':name})

    return jsonify({'result':'success'})

if __name__=='__main__':
    app.run('0.0.0.0', port=5000, debug=True)