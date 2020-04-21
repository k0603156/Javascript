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

# 1. 인덱스 이름 확인
print(df.index)
print(type(df.index))
i_list = list(df.index)
print(i_list)
print('-' * 30)

# 2. 컬럼이름 확인
print(df.columns)
c_list = list(df.columns)
print(c_list)
print('-' * 30)

# 3. 데이터 값 확인
print(df.values)

# 4. 전치 구하기
df_t = df.T
print(df_t)




