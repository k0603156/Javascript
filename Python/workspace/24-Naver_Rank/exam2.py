# -*- coding: utf-8 -*-
"""
Created on Fri May  1 16:45:18 2020

@author: kimyongkuk
"""

import requests
from bs4 import BeautifulSoup as bs
from pandas import DataFrame


url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=025&aid=0002997509'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
session = requests.Session()
session.headers.update({'User-agent':user_agent, 'referer':None})

df = DataFrame()
r = session.get(url)

if r.status_code != 200 :
    print('[ERROR]')
    quit()

soup = bs(r.text, 'html.parser')

title = soup.select('.article_info #articleTitle')[0]
body = soup.select('.article_body #articleBodyContents')[0]

for target in body.find_all('script'):target.extract()
for target in body.find_all('a'):target.extract()
for target in body.find_all('span'):target.extract()
for target in body.find_all('div'):target.extract()
for target in body.find_all('br'):target.replace_with('\n')

print(title.text.strip())
print(body.text.strip())




