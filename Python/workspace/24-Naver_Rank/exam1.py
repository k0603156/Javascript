# -*- coding: utf-8 -*-
"""
Created on Fri May  1 15:37:40 2020

@author: kimyongkuk
"""


import requests
from bs4 import BeautifulSoup as bs
from pandas import DataFrame


url = 'https://datalab.naver.com/keyword/realtimeList.naver?where=main'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
session = requests.Session()
session.headers.update({'User-agent':user_agent, 'referer':None})

df = DataFrame()
r = session.get(url)

if r.status_code != 200 :
    print('[ERROR]')
    quit()

soup = bs(r.text, 'html.parser')

with open('네이버실시간검색어.txt','w',encoding='utf-8')as f:
    f.write(r.text)

selector = soup.select('.item_title_wrap > .item_title')

if not selector :
    print('크롤링 실패')
    quit()

rank_list = []
keyword_list = []

for i, item in enumerate(selector):
    rank_list.append('%02d위' %(i+1))
    keyword_list.append(item.text.strip())


print(DataFrame(keyword_list,rank_list, columns=['검색어']))