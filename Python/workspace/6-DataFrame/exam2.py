from pandas import DataFrame

# 리스트를 원소로 갖는 딕셔너리
grade_dic = {
                '국어': [98, 88, 92, 63, 120],
                '영어': [None, 90, 70, 60, 50],
                '수학': [88, 62, None, 31, None],
                '과학': [64, 72, None, 70, 88]                
            }
# 딕셔너리의 키값이 컬럼의 이름으로 지정됨
# 리스트를 원소로 갖는 딕셔너리를 사용하면, 인덱스만 따로 지정함
df = DataFrame(grade_dic, index=['철수','영희','민철','수현','호영'])
print(df)

