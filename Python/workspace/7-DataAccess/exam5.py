# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 17:50:31 2020

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

#컬럼 이름을 통한 열 삭제
k1 = df.drop('국어',axis=1)
print(df)
print(k1)

#여러 열 삭제 
k2 = df.drop(['영어','수학','과학'],axis=1)
print(k2)

#인덱스 번호로 열 삭제
k3 = df.drop(df.columns[3],axis=1)
print(k3)

#슬라이싱으로 지정된 범위 삭제
k4 = df.drop(df.columns[1:4],axis=1)
print(k4)

#삭제 결과를 원본에 반영
df.drop(df.columns[1:4], axis=1,inplace=True)
print(df)
