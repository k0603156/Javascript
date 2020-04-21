from pandas import Series
from pandas import date_range

data1 = [10, 20, 30, 40, 50]
index_date = date_range(start='2020-1-1', periods=5)

s1 = Series(data1, index=index_date)
print(s1)


