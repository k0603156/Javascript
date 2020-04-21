# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:06:40 2020

@author: kimyongkuk
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
print(df)

#열 => 행 순으로 접근
print(df['국어'],['철수'])

#df['국어']['철수'] =100 #warning

#행 => 열 순으로 접근하기 (읽기,쓰기)
print(df.loc['철수','국어'])
df.loc['철수','국어']=100
print(df)

print(df.loc['철수','국어'])
print(df.loc['철수']['국어'])
