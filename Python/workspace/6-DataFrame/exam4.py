from pandas import read_csv  # csv파일을 읽어들이기 위한 함수

# 외부에서 csv나 xlsx 파일을 가져오는 경우,
# index가 인식되지 않기 때문에
# 특정 컬럼의 값들을 인덱스로 지정하고, 그 컬럼을 삭제하는 전처리가 필요함
# => 뒤에서 할 예정
df = read_csv('data/grade.csv', encoding='euc-kr')
print(df)
print(type(df))
print('-' * 30)

df = read_csv('data/grade1.csv')
print(df)
print(type(df))
print('-' * 30)
