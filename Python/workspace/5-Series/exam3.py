from pandas import Series

items = [10, 30, 50, 70, 90]
column = Series(items)
print(column)
print('-' * 30)

# 특정 조건에 맞는 항목들만 추출
# 시리즈이름[이름에 대한 조건식]
# -> 30초과인 항목들만 추출
in1 = column[column > 30]
print(in1)
print(type(in1))
print('-' * 30)

# AND 조건
# -> 70이하 and 10초과인 항목들만 추출
in2 = column[(column>10) & (column<=70)]
print(in2)
print(type(in2))
print('-' * 30)

# OR 조건
# -> 10이하 or 70이상인 항목들만 추출 -> () 필수
in3 = column[(column<=10) | (column>=70)]
print(in3)
print(type(in3))
print('-' * 30)












