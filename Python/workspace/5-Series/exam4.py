from pandas import Series

week1 = Series([290000, 310000], index=['토', '일'])
print(week1)
print('-' * 30)

week2 = Series([120000, 220000], index=['일', '토'])
print(week2)
print('-' * 30)

# 시리즈 객체의 사칙연산
# -> index가 동일한 항목끼리 연산이 수행된다.
result = week1 + week2
print(result)
print(type(result))
