# -*- coding: utf-8 -*-
"""
Created on Thu May  7 15:23:01 2020

@author: kimyongkuk
"""
import folium
from pandas import DataFrame
from pandas import ExcelFile

xlsx = ExcelFile("data/school2019.xlsx")
df = xlsx.parse(xlsx.sheet_name[0])

df2 = df.filter(["학교명","학교급구분","소재지도로명주소","위도","경도"])
df3 = df2[df2['학교급구분']=='초등학교']
df4 = df3[df3['소재지도로명주소'].str.contains('서울') == True] 

map_osm = folium.Map(location=[35.572833,126.])
