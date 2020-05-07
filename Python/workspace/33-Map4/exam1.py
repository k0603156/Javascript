# -*- coding: utf-8 -*-
"""
Created on Thu May  7 17:29:40 2020

@author: kimyongkuk
"""
import folium
import pandas as pd
from pandas import ExcelFile
from bs4 import BeautifulSoup as bs

xlsx = ExcelFile("data/school2019.xlsx")
df = xlsx.parse(xlsx.sheet_names[0])

df2= df.filter(['학교명','학교급구분','소재지도로명주소'])
df2.dropna(inplace=True)

df2['idx'] = df2['소재지도로명주소'].str.find(' ').astype(int)

for i in df2.index:
    addr = df2.loc[i, '소재지도로명주소']
    idx = df2.loc[i, 'idx']
    city = addr[:idx]
    df2.loc[i,'시도'] = city

df_result =df2.filter(['시도','학교급구분','학교명']).groupby(['시도','학교급구분']).count()
df_school_result = df_result.rename(columns={'학교명':'학교수'})

dict_elementry={}
for index in df_school_result.index :
    a = index[0]
    b = index[1]
    
    if b == '초등학교':
        dict_elementry[a] = df_school_result.loc[index, '학교수']
map_svg = None
with open('data/korea.svg','r',encoding='utf-8')as f:
    map_svg= f.read()

colors = ["#FFC2B8","#FF816B","#CC6756","#8A3B30","#804F36","#803E36","#B70F00"]

soup = bs(map_svg)

glist = soup.select('svg > g[id], svg > path[id]')

for item in glist:
    if item['id'] not in dict_elementry:
        continue

    count = dict_elementry[item['id']]
    
    if count > 1000:color_index=6
    elif  count > 600:color_index=5
    elif  count > 500:color_index=4
    elif  count > 400:color_index=3
    elif  count > 300:color_index=2
    elif  count > 200:color_index=1
    else: color_index=0
    
    for p in item.select("g, path"):
        p['fill'] = colors[color_index]
    print(item['id'],count)
    
new_svg = soup.prettify()
with open('new_svg.svg',"w",encoding='utf-8') as f:
    f.write(new_svg)