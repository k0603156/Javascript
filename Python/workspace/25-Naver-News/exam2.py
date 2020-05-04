# -*- coding: utf-8 -*-
"""
Created on Mon May  4 14:40:55 2020

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

datetime = dt.datetime.now().strftime("%y%m%d_%H%M%S")
dirname = "뉴스기사_%s" %datetime
if not os.path.exists(dirname):
    os.mkdir(dirname)
for i, url in enumerate(url_list):
    print(">> [%d] 기사 수집 \n>> %s" %(i+1,url))
    
    r= session.get(url)
    if r.status_code != 200:
        print(['ERRO'])
        continue
    
    soup = bs(r.text,'html.parser')
    
    main_content = soup.select("#main_content")
    
    title = main_content[0].select("#articleTitle")
    title_str = title[0].text.strip()
    title_str = title_str.replace("'","")
    title_str = title_str.replace("/","")
    title_str = title_str.replace("\"","")
    title_str = title_str.replace(">","")
    title_str = title_str.replace("<","")
    title_str = title_str.replace("?","")

    article = main_content[0].select("#articleBodyContents")
    article_item = article[0]
    
    for target in article_item.find_all("script"):target.extract()
    for target in article_item.find_all("a"):target.extract()
    for target in article_item.find_all("span"):target.extract()
    for target in article_item.find_all("div"):target.extract()
    for target in article_item.find_all("br"):target.replace_with("\n")
    
    article_str = article_item.text.strip()
    
    if title_str and article_str :
        fname = dirname + "/" + str(i+1) + "_" + title_str + ".txt"
        with open(fname,"w", encoding="utf-8") as f:
            f.write(article_str)
            print(">> [SUCCESS]" + fname)
        
    