# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:54:36 2020

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

#자료의 개수를 센다.
count = len(grade_df['평균'])

#최대/최소값
max_value=grade_df['평균'].max()
min_value=grade_df['평균'].min()
print(max_value,min_value,count)

#나눌 구간 설정
step=5
#히스토그램 생성
#그래프 기본설정
pyplot.rcParams['font.family']='Malgun Gothic'
pyplot.rcParams['font.size']=20
pyplot.rcParams['figure.figsize']=(15,8)

#히스토그램 작성
n, bins, patches =pyplot.hist(grade_df['평균'], bins=step)
print(n,bins,patches)

#보정
for i, v in enumerate(bins):
    bins[i] = round(v,1)

print(bins)
pyplot.hist(grade_df['평균'],bins=step,color="blue")
pyplot.grid()
pyplot.xlabel('점수')
pyplot.ylabel('평균점수 구간별 학생수')
pyplot.title('평균점수 구간별 학생수')
pyplot.xticks(bins,bins)

#구간별 인원을 텍스트로 출력
for i,v in enumerate(n):
    txt ='%d명' %v
    print(txt)
    pyplot.text(bins[i],v,txt,fontsize=18,color="#ff0000", horizontalalignment="left",verticalalignment="bottom")
    
pyplot.show()




