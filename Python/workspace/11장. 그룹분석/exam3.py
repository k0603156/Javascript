from pandas import DataFrame

# 서울, 부산, 인천의 5년 단위 인구 분포
city_people = {
    '도시':['서울','서울','서울','부산','부산','부산','인천','인천'],
    '연도':['2015','2010','2005','2015','2010','2005','2015','2010'],
    '인구':[9904312,9631482,9762546,3448737,3393191,3512547,2890451,2632035],
    '지역':['수도권','수도권','수도권','경상권','경상권','경상권','수도권','수도권',]
}

# 1. 데이터프레임 생성
census = DataFrame(city_people)
print(census)
print('-' * 30)

# 2. 각지역별 5년단위 최대 인구수
# 두개 이상의 컬럼을 집단별로 나누고 그룹분석 수행하기
# 기준이 될 컬럼2개와 집계를 수행할 컬럼 추출
local_year_people = census.filter(['지역','연도','인구'])
print(local_year_people)
print('-' * 30)

# 두개 이상의 컬럼을 그룹으로 묶은 후, 집계 수행
# -> 그룹으로 묶인 결과가 인덱스로 구성된다.
local_year_people_max = local_year_people.groupby([local_year_people['지역'],
                                        local_year_people['연도']]).max()
print(local_year_people_max)
print('-' * 30)

# 열과 행의 구성 확인
print(local_year_people_max.columns)
print(local_year_people_max.index)
print('-' * 30)

# 인덱스를 구성하지 않고 그룹으로 묶기
result1 = local_year_people.groupby([local_year_people['지역'],
                        local_year_people['연도']], as_index=False).max()
print(result1)
print('-' * 30)



















