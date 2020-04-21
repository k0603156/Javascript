# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:37:57 2020

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

#컬럼이름 변경
df1 = df.rename(columns={"국어":"화학"})
print(df1)
#인덱스 이름 변경
df2 = df.rename(index={"철수":"민수"})
print(df2)
#컬럼,인덱스 변경 :원본에 반영
df.rename(index={"철수":"민수"},columns={"국어":"화학"},inplace=True)
print(df)