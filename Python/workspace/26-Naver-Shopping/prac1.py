# -*- coding: utf-8 -*-
"""
Created on Mon May  4 18:52:51 2020

@author: kimyongkuk
"""


import requests
import urllib
from bs4 import BeautifulSoup as bs
from pandas import DataFrame as df

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
session = requests.Session()
session.headers.update({'User-agent':user_agent, 'referer':None})

keyword = "에어프라이어"
MAX_PAGE = 5
base_url = "https://www.coupang.com/np/search"

base_param = {
    "q":keyword,
    "page":1,
    "listSize":36,
    "filter":"",  
    }

data_list = []
for page in range(1, MAX_PAGE+1):
    base_param["pagingIndex"] = page
    query = urllib.parse.urlencode(base_param)
    content_url =  f"{base_url}?{query}"
    r =  session.get(content_url)
    if r.status_code != 200 :
        print('[ERROR]')
        continue
    
    soup = bs(r.text, "html.parser")
    info_list = soup.select(".descriptions")
    
    for info in info_list:
        item_dict = {}
        title_list = info.select(".name")
        '''base_price_list = info.select(".price .base-price")
        disc_price_list = info.select(".price .price-value")
        item_dict['상품명'] = title_list[0].text.strip()
        item_dict['기존가'] = base_price_list[0].text.strip()
        item_dict['할인가'] = disc_price_list[0].text.strip()'''
        

    