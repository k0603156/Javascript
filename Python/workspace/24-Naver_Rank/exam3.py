# -*- coding: utf-8 -*-
"""
Created on Fri May  1 17:44:45 2020

@author: kimyongkuk
"""


# -*- coding: utf-8 -*-
"""
Created on Fri May  1 16:45:18 2020

@author: kimyongkuk
"""

import os
import requests
import datetime as dt
from bs4 import BeautifulSoup as bs
from pandas import DataFrame


url = 'https://news.naver.com/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
session = requests.Session()
session.headers.update({'User-agent':user_agent, 'referer':None})

df = DataFrame()
r = session.get(url)

if r.status_code != 200 :
    print('[ERROR]')
    quit()

soup = bs(r.text, 'html.parser')

selector = soup.select('.lnk_hdline_main_ariticle, .lnk_hdline_article, .mtype_img > dt > a, .mlist2 > li > a')

url_list = []
for item in selector:
    if 'href' in item.attrs:
        url_list.append(item['href'])

for i, v in enumerate(url_list):
    if 'https://news.naver.com' not in v:
        url_list[i] = 'https://news.naver.com' + v
print(url_list)

