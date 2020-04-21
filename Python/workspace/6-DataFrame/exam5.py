from pandas import ExcelFile  # Excel 파일을 읽어들이기 위한 클래스

xls = ExcelFile('data/children_house.xlsx')
print(xls)
print(type(xls))
print('-' * 30)

# 엑셀 파일의 sheet이름에 대한 리스트
print(xls.sheet_names)
print('-' * 30)

# 가져오고자 하는 sheet이름을 지정하여 데이터프레임으로 변환
df = xls.parse(xls.sheet_names[0])
print(df)
print(type(df))

