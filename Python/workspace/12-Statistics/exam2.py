# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:07:32 2020

@author: kimyongkuk
"""

from pandas import DataFrame
from pandas import read_csv
from matplotlib import pyplot

grade_csv = read_csv("data/grade.csv",encoding='euc-kr')

#전처리
#열 이름을 인덱스로 사용
name={}
for i, v in enumerate(list(grade_csv['이름'])):
    name[i] = v

#인덱스에 이름 설정 
grade_df = grade_csv.rename(index=name)

#컬럼 이름 삭제
grade_df.drop('이름',axis=1, inplace=True)

#컬럼에 대한 요약 통계량 일괄 확인
des= grade_df.describe()
print(des)
print(type(des))

#특정 컬럼에 대한 요약 통계량 확인
desc_kor = grade_df['국어'].describe()
print(desc_kor)
print(type(desc_kor))

#요약통계량 시각화 :boxplot
pyplot.rcParams['font.family'] ='Malgun Gothic'
pyplot.rcParams['font.size']=14
pyplot.rcParams['figure.figsize']=(8,6)

#전체 데이터프레임의 상자그림 생성
grade_df.boxplot()
pyplot.show()

#특정 컬럼만 상자그림 표시
grade_df.boxplot(['국어'])

#이미지 저장
pyplot.savefig("국어_점수분포.png",dpi=200)
