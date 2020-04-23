# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:34:20 2020

@author: kimyongkuk
"""


from pandas import DataFrame
from pandas import read_csv

grade_csv = read_csv("data/grade.csv",encoding='euc-kr')
print(grade_csv.head)
print(grade_csv.tail)

#전처리
#열 이름을 인덱스로 사용

name={}
for i, v in enumerate(list(grade_csv['이름'])):
    name[i] = v

print(name)

#인덱스에 이름 설정 
grade_df = grade_csv.rename(index=name)
print(grade_df)

# 컬럼 이름 삭제
grade_df.drop('이름',axis=1, inplace=True)
print(grade_df)

#데이터프레임 전체크기를 튜플로 조회
print(grade_df.shape)