# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:58:34 2020

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

#행의 값들을 list로 변환 
ls =list(df.loc['철수'])
print(ls)

#행 슬라이싱 
df1= df[0:2]
print(df1)

#행 슬라이싱 2 시작인덱스명<= 행 <= 종료인덱스명
df2 = df.loc['철수':'영희']
print(df2)
