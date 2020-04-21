# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:04:44 2020

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

#특정 열로 오름차순 정렬
asc = df.sort_values('국어')
print(asc)
#특정 열로 내차순 정렬
desc = df.sort_values('국어',ascending=False)
print(desc)