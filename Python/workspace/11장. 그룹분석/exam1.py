from pandas import DataFrame

grade_dic = {
    '국어':[98, 88, 92, 63, 120],
    '영어':[None, 90, 70, 60, 50],
    '수학':[88, 62, None, 31, None],
    '과학':[64, 72, None, 70, 88]
}

# 1. 데이터프레임 생성
df = DataFrame(grade_dic, index=['철수','영희','민철','수현','호영'])
print(df)
print('-' * 30)

# 2. 전체 열에 대한 집계
# 과목별 총점
print(df.sum())
print('-' * 30)

# 과목별 평균
print(df.mean())
print(type(df.mean()))
print('-' * 30)

# 3. 특정열에 대한 집계
# 국어 과목에서 총점, 평균, 최고점수
print(df['국어'].sum())
print(df['국어'].mean())
print(df['국어'].max())
print(df['국어'].min())
print('-' * 30)

# 4. 행 단위 집계
# 집계함수에 axis=1 파라미터를 지정한다.

# 학생별 총점
print(df.sum(axis=1))
print('-' * 30)

# 학생별 평균
print(df.mean(axis=1))
print('-' * 30)

# 5. 특정 행에 대한 집계
# '영희'의 총점, 평균점수
print(df.loc['영희'].sum())
print(df.loc['영희'].mean())
print('-' * 30)

# 6. 행단위 집계 결과를 새로운 열로 추가하기

# 학생별 총점과 평균 산출
tot = df.sum(axis=1)
print(tot)
print('-' * 30)

avg = df.mean(axis=1)
print(avg)
print('-' * 30)

# 산출한 집계결과를 새로운 열로 추가
df['총점'] = tot
df['평균'] = avg
print(df)
print('-' * 30)















