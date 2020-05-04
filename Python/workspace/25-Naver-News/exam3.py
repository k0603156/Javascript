# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:45:15 2020

@author: kimyongkuk
"""


import os
import requests
import datetime as dt
from bs4 import BeautifulSoup as bs
from pandas import DataFrame
from collections import Counter
from wordcloud import WordCloud
from konlpy.tag import Okt

url = 'https://news.naver.com/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
session = requests.Session()
session.headers.update({'User-agent':user_agent, 'referer':None})

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


datetime = dt.datetime.now().strftime("%y%m%d_%H%M%S")
dirname = "뉴스기사_%s" %datetime

content_merge =""

for i, url in enumerate(url_list):
    
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
    content_merge += article_str

nlp =Okt()
nouns = nlp.nouns(content_merge)

for i, v in enumerate(nouns):
    if(len(v) < 2): del(nouns[i])
count = Counter(nouns)

most = count.most_common(100)

tags={}
for n, c in most:
    tags[n] = c

print(tags)

wc = WordCloud(font_path="data/NanumBarunGothic.ttf", width=1200,height=600,background_color="#fff")
wc.generate_from_frequencies(tags)
wc.to_file("news.png")

from matplotlib import pyplot
pyplot.figure(figsize=(15,10))
pyplot.imshow(wc)
pyplot.axis('off')
pyplot.show()
    