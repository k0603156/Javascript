from pandas import DataFrame
import numpy

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

# 2. 하나의 컬럼에 대해 여러개의 집계함수 동시 사용
# agg() 함수에 집계함수의 이름을 문자열 원소로 갖는 리스트로 설정
# -> 'min', 'max', 'sum', 'mean', 'std', 'var'
city_people = census.filter(['도시', '인구'])
print(city_people)
print('-' * 30)

result2 = city_people.groupby(city_people['도시']).agg(['min', 'max','std', 'sum'])
print(result2)
print('-' * 30)

# 행과 열의 구조 확인
print(result2.columns)
print(result2.index)
print('-' * 30)

# 3. 사용자 정의 함수를 적용하기
# x : 특정 컬럼에 대한 Series 객체
def my_range(x) :
    return numpy.max(x) - numpy.min(x)

result3 = city_people.groupby(city_people['도시'])\
          .agg(['min', 'max','std', 'sum', my_range])
print(result3)
print('-' * 30)

# 4. 여러 컬럼에 대해 서로 다른 집계함수 적용하기
# -> 딕셔너리 형식으로 {컬럼명: [함수리스트], 컬럼명: [함수리스트]}
local_city_people = census.filter(['지역', '도시','인구'])
print(local_city_people)
print('-' * 30)

result4 = local_city_people.groupby(local_city_people['지역'])\
        .agg({'도시':['count'], '인구':['sum']})
print(result4)
print('-' * 30)

# 행과 열의 구조 확인
print(result4.columns)
print(result4.index)















