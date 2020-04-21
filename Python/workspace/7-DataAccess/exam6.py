# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:08:40 2020

@author: kimyongkuk
@title: preprocessing
"""
from pandas import DataFrame

grade_data = [
                {'국어':98, '영어':None, '수학':88, '과학':64},
                {'국어':88, '영어':90, '수학':62, '과학':72},
                {'국어':92, '영어':70, '수학':None, '과학':None},
                {'국어':63, '영어':60, '수학':31, '과학':70},
                {'국어':120, '영어':50, '수학':None, '과학':88}
            ]


df = DataFrame(grade_data, index=['철수','영희','민철','수현','호영'])

#컬럼(열)의 순서 변경
df1= df.reindex(columns=['국어','수학','과학','영어'])
print(df1)

#인덱스(행)의 순서 변경
df2= df.reindex(index=['영희','수현','철수','민철','호영'])
print(df2)
#인덱스(행)의 순서 변경 - 잘못된 인덱스를 입력하면 추가됨
df3= df.reindex(index=['영희','수현','철수','민수','호영'])
print(df3)

