# DB에 필요한 데이터를 미리 크롤링하는 코드
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('mongodb://yoonwoo:pw@3.36.71.134', 27017)
db = client.dbjungle

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('url', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
trs = soup.select('#old_content > table > tbody > tr')
