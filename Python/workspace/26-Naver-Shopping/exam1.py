# -*- coding: utf-8 -*-
"""
Created on Mon May  4 17:53:08 2020

@author: kimyongkuk
"""
import requests
import urllib
from bs4 import BeautifulSoup as bs
from pandas import DataFrame as df


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
session = requests.Session()
session.headers.update({'User-agent':user_agent, 'referer':None})

keyword = "태블릿"
MAX_PAGE = 5
base_url="https://search.shopping.naver.com/search/all.nhn"
base_param={
    "origQuery":keyword,
    "pagingIndex":1,
    "pagingSize":40, 
    "viewType":"list",
    "sort":"rel",
    "frm":"NVSHATC",
    "query":keyword
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
    info_list = soup.select(".info")
    
    for info in info_list:
        item_dict = {}
        title_list = info.select(".tit")
        item_dict['상품명'] = title_list[0].text.strip()
        
        price_list = info.select(".num")
        price = price_list[0].text.strip()
        price = price.replace(",", "")
        
        item_dict['가격'] = int(price)
        
        spec_list = info.select(".detail > a")
        for v in spec_list:
            v = v.text.strip()
            tmp = v.split(":")
            
            if len(tmp)  == 2 :
                key = tmp[0].strip()
                value = tmp[1].strip()
                item_dict[key] = value
        
        data_list.append(item_dict)
        
        
#print(data_list)
df = df(data_list)
df.to_excel(f"{keyword}.xlsx")
    