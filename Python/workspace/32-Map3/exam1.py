# -*- coding: utf-8 -*-
"""
Created on Thu May  7 16:35:07 2020

@author: kimyongkuk
"""


from bs4 import BeautifulSoup as bs
from pandas import DataFrame
from pandas import ExcelFile

xlsx = ExcelFile('data/senior_lsf.xlsx')
df = xlsx.parse(xlsx.sheet_names[0])

data_dict ={}
for i in df.index :
    key = df.loc[i, 'COUNTY']
    value = df.loc[i,'NUMBER']
    data_dict[key] = value
    
map_svg = None
with open('data/seoul.svg','r') as f:
    map_svg = f.read()

soup = bs(map_svg)

paths = soup.select('path[id]')

colors = ["#FFEA8C","#BFFFD7","#FFEFA6","#8C8DFF","#FF9E99","#BFF8FF"]

for p in paths:
    if p['id'] == "Yeongdeungpo-gu_1_":
        p['id'] = "Yeongdeungpo-gu"
        
    count = data_dict[p["id"]]
    
    if count > 250:color_index=5
    elif  count > 200:color_index=4
    elif  count > 150:color_index=3
    elif  count > 100:color_index=2
    elif  count > 50:color_index=1
    else: color_index=0
    
    p['fill'] = colors[color_index]

new_svg = soup.prettify()

with open('new_svg.svg',"w") as f:
    f.write(new_svg)