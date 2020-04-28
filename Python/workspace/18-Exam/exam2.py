import numpy
import pandas as pd
from pandas import DataFrame
from pandas import ExcelFile
from matplotlib import pyplot
'''
xlsx = ExcelFile('data/dataset2017.xlsx')
df = xlsx.parse(xlsx.sheet_names[0]);
#print(df)
print('-' * 30)
'''
gender = df.filter(['h12_g3'])
print(gender)
print('-' * 30)

df_gender = gender.rename(columns={'h12_g3':'성별'})
df_gender['성별'] = numpy.where(df_gender['성별'] == 1, '남자', '여자')
print(df_gender.head())
print('-' * 30)

print(df_gender.isna().sum())
print('-' * 30)

gen_cnt = df_gender['성별'].value_counts()
print(gen_cnt)
print('-' * 30)

df_gen_cnt = DataFrame(gen_cnt)
print(df_gen_cnt)
print('-' * 30)

df_gen_cnt_result = df_gen_cnt.rename(columns={'성별':'총인원'})
print(df_gen_cnt_result)
print('-' * 30)

df_gen_cnt_result.sort_values('총인원', inplace=True)
print(df_gen_cnt_result)
print('-' * 30)

pyplot.rcParams['font.family'] = 'Malgun Gothic'
pyplot.rcParams['font.size'] = 16 
pyplot.rcParams['figure.figsize'] = (10, 8) 

df_gen_cnt_result.plot.bar(rot=0)
pyplot.title('조사대상들에 대한 성별 분포')
pyplot.grid()
pyplot.xlabel('성별')
pyplot.ylabel('명')

for i, v in enumerate(list(df_gen_cnt_result['총인원'])) :
    txt = "%d명" %v
    pyplot.text(i, v, txt, fontsize=14, color='blue',
                horizontalalignment='center',
                verticalalignment='bottom')

pyplot.show()









