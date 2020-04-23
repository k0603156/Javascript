from pandas import DataFrame

# 서울, 부산, 인천의 5년 단위 인구 분포
city_people = {
    '도시':['서울','서울','서울','부산','부산','부산','인천','인천'],
    '연도':['2015','2010','2005','2015','2010','2005','2015','2010'],
    '인구':[9904312,9631482,9762546,3448737,3393191,3512547,2890451,2632035],
    '지역':['수도권','수도권','수도권','경상군','경상군','경상군','수도권','수도권',]
}

# 1. 데이터프레임 생성
census = DataFrame(city_people)
print(census)
print('-' * 30)

# 2. 15년간의 도시별 최대 인구수
# 하나의 컬럼을 집단별로 나구고 그룹분석 수행하기
# 분석을 할 컬럼만 추출
city_people = census.filter(['도시','인구'])
print(city_people)
print('-' * 30)

# 특정 컬럼을 그룹으로 묶고 다른 컬럼으로 집계 수행
# -> 그룹으로 묶인 컬럼은 인덱스로 구성된다.
# -> 도시별 최대 인구수
city_people_max = city_people.groupby(city_people['도시']).max()
print(city_people_max)
print('-' * 30)

# 열과 행의 구성확인
print(city_people_max.columns)
print(city_people_max.index)









