# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 16:46:35 2020

@author: kimyongkuk
"""
from pandas import DataFrame
from pandas import read_csv
from matplotlib import pyplot


grade_csv = read_csv("data/grade.csv",encoding='euc-kr')

#전처리 컬럼 이름을 인덱스로 설정
grade_df = grade_csv.rename(index=grade_csv['이름']).drop('이름',axis=1)

#평균점수 컬럼 추가: axis=1 행
grade_df['평균']=grade_df.mean(axis=1)
print(grade_df)

#구간 설정
step=5
n,bins,patches=pyplot.hist(grade_df['평균'],bins=step)

idx=[]
for i in range(0,len(bins)-1):
    k = '%.1f~%.1f' %(bins[i], bins[i+1])
    idx.append(k)
print(idx)

#데이터프레임만들기
df= DataFrame(n, index=idx, columns=['빈도'])
print(df)