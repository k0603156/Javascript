import numpy
import pandas as pd
from pandas import DataFrame
from pandas import ExcelFile
from matplotlib import pyplot

'''
xlsx = ExcelFile('data/dataset2017.xlsx')
df = xlsx.parse(xlsx.sheet_names[0])
print(df)
print('-' * 30)
'''

gen_sal = df.filter(['h12_g3','p1202_8aq1'])
print(gen_sal)
print('-' * 30)

df_gen_sal = gen_sal.rename(columns={'h12_g3':'성별','p1202_8aq1':'월급'})
print(df_gen_sal)
print('-' * 30)

df_gen_sal['성별'] = numpy.where(df_gen_sal['성별']==1, '남자', '여자')
print(df_gen_sal)
print('-' * 30)

print(df_gen_sal.isna().sum())
print('-' * 30)

df_gen_sal.dropna(inplace=True)
print(df_gen_sal.isna().sum())
print('-' * 30)

df_gen_sal['월급'] = numpy.where(((df_gen_sal['월급']<1) | (df_gen_sal['월급']>9998)), 
                               numpy.nan, df_gen_sal['월급'])
print(df_gen_sal.isna().sum())
print('-' * 30)

df_gen_sal.dropna(inplace=True)
print(df_gen_sal.isna().sum())
print('-' * 30)

df_gen_sal_mean = df_gen_sal.groupby('성별').mean()
print(df_gen_sal_mean)
print('-' * 30)

pyplot.rcParams['font.family'] = 'Malgun Gothic'
pyplot.rcParams['font.size'] = 16
pyplot.rcParams['figure.figsize'] = (12, 8) 

df_gen_sal_mean.plot.bar(rot=0)
pyplot.title('성별에 따른 평균 월급 차이 분석')
pyplot.grid()
pyplot.xlabel('성별')
pyplot.ylabel('월급')

for i, v in enumerate(list(df_gen_sal_mean['월급'])) :
    txt = '%d만원' %v
    pyplot.text(i, v, txt, fontsize=14, color='#000099',
                horizontalalignment='center',
                verticalalignment='bottom')
    
pyplot.show()














