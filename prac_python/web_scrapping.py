import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody > tr')
print(len(movies))

for movie in movies:
    rank = movie.select_one('td.ac > img')
    title = movie.select_one('td.title > div > a')
    point = movie.select_one('td.point')
    if title:
        print(rank['alt'], title['title'], point.text)