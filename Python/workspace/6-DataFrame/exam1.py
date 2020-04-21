from pandas import DataFrame

# 어느 학급의 성적표를 표현한 2차원 리스트
#             국   영   수   과
grade_list = [[98, None, 88, 64],    # 철수
              [88, 90, 62, 72],      # 영희
              [92, 70, None, None],  # 민철
              [63, 60, 31, 70],      # 수현
              [120, 50, None, 88]]   # 호영

# 행과 열을 갖는 표 형태의 DataFrame 생성
df = DataFrame(grade_list)
print(df)
print(type(df))
print('-' * 30)

# 컬럼이름 지정
# -> 컴럼이름은 리스트로 지정
c_names = ['국어', '영어', '수학', '과학']
df = DataFrame(grade_list, columns=c_names)
print(df)
print(type(df))
print('-' * 30)

# 인덱스 이름 지정
# -> 인덱스 이름은 리스트로 지정
i_names = ['철수', '영희', '민철', '수현', '호영']
df = DataFrame(grade_list, index=i_names)
print(df)
print(type(df))
print('-' * 30)

# 인덱스와 컬럼 이름을 모두 지정
df = DataFrame(grade_list, index=i_names, columns=c_names)
print(df)
print(type(df))
print('-' * 30)








