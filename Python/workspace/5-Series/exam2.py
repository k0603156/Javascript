from pandas import Series

items = [10, 30, 50, 70, 90]
column = Series(items)
print(column)
print('-' * 30)

# 시리즈의 색인(index)만 추출
i = column.index
print(i)
print(type(i))
print('-' * 30)

# 시리즈의 색인을 리스트로 변환
index_list = list(i)
print(index_list)
print(type(index_list))
print('-' * 30)

# 시리즈의 값들만 추출
v = column.values
print(v)
print(type(v))
print('-' * 30)

# 시리즈의 값들을 리스트로 변환
value_list = list(v)
print(value_list)
print(type(value_list))








