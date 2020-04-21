from pandas import DataFrame

# 딕셔너리를 원소로 갖는 리스트
grade_data = [
                {'국어':98, '영어':None, '수학':88, '과학':64},
                {'국어':88, '영어':90, '수학':62, '과학':72},
                {'국어':92, '영어':70, '수학':None, '과학':None},
                {'국어':63, '영어':60, '수학':31, '과학':70},
                {'국어':120, '영어':50, '수학':None, '과학':88}
            ]

# 딕셔너리의 키가 컬럼이름으로 사용되므로, 인덱스만 지정
df = DataFrame(grade_data, index=['철수','영희','민철','수현','호영'])
print(df)
print('-' * 30)

# 1. 데이터의 크기
# 튜플타입의 속성 : (행, 열)
print(df.shape)
print('rows :', df.shape[0])
print('cols :', df.shape[1])
print('-' * 30)

# 2. 상위 데이터 3건만 확인
top3 = df.head(3)
print(top3)
print(type(top3))
print('-' * 30)

# 2. 하위 데이터 3건만 확인
last3 = df.tail(3)
print(last3)
print(type(last3))
print('-' * 30)










