import numpy
import pandas as pd
from pandas import DataFrame
from pandas import ExcelFile
from matplotlib import pyplot
import datetime as dt


xlsx = ExcelFile('data/dataset2017.xlsx')
df = xlsx.parse(xlsx.sheet_names[0]);
print(df)
print('-' * 30)


year_sal = df.filter(['h12_g4', 'p1202_8aq1'])
print(year_sal)
print('-' * 30)

df_year_sal = year_sal.rename(columns={'h12_g4':'출생년도', 'p1202_8aq1':'월급'})
print(df_year_sal)
print('-' * 30)

yy = dt.datetime.now().year
print(yy)
print('-' * 30)

df_year_sal['나이'] = yy - df_year_sal['출생년도'] + 1
print(df_year_sal)
print('-' * 30)

print(df_year_sal.isna().sum())
print('-' * 30)

df_year_sal.dropna(inplace=True)
print(df_year_sal.isna().sum())
print('-' * 30)

df_year_sal['월급'] = numpy.where(((df_year_sal['월급'] < 1) | (df_year_sal['월급'] > 9998)), 
                                numpy.nan, df_year_sal['월급'])
print(df_year_sal.isna().sum())
print('-' * 30)

df_year_sal.dropna(inplace=True)
print(df_year_sal.isna().sum())
print('-' * 30)

print(df_year_sal)
print('-' * 30)

df_year_sal_mean = df_year_sal.filter(['나이', '월급']).groupby('나이').mean()
print(df_year_sal_mean)
print('-' * 30)















