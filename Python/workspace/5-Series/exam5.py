from pandas import date_range

# 데이터 생성
s1 = date_range(start='2020-01-01', end='2020-01-04')  # 1일씩 증가
print(s1)
print(type(s1))
print('-' * 30)

s1 = date_range(start='2020-1-1', end='2020-1-4')  # 1일씩 증가
print(s1)
print(type(s1))
print('-' * 30)

s1 = date_range(start='2020/1/1', end='2020/1/4')  # 1일씩 증가
print(s1)
print(type(s1))
print('-' * 30)

s1 = date_range(start='2020/1/1', periods=4)  # 1일씩 증가
print(s1)
print(type(s1))
print('-' * 30)

# 2일씩 증가
s1 = date_range(start='2020/1/1', periods=4, freq='2D')  
print(s1)
print(type(s1))
print('-' * 30)

# 1주일씩 증가
# freq='W' : 일요일을 시작 기준으로 일주일 주기, freq='W-SUN'과 같은 의미
s1 = date_range(start='2020/1/1', periods=4, freq='W-MON')  
print(s1)
print(type(s1))
print('-' * 30)

# BM : 업무 월말 날짜 기준 주기
# 2BM : 업무일 기준 2개월 월말 주기
s1 = date_range(start='2020/1/1', periods=4, freq='BM')  
print(s1)
print(type(s1))
print('-' * 30)

s1 = date_range(start='2020/1/1', periods=4, freq='2BM')  
print(s1)
print(type(s1))
print('-' * 30)



