# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:44:33 2020

@author: kimyongkuk
"""


import numpy
import pandas as pd
from pandas import DataFrame
from pandas import ExcelFile
from matplotlib import pyplot
import datetime as dt

xlsx = ExcelFile('data/dataset2017.xlsx')
df = xlsx.parse(xlsx.sheet_names[0]);
year_sal = df.filter(['h12_g4'])
df_year_sal = year_sal.rename(columns={'h12_g4':'출생년도'})
yy = dt.datetime.now().year
df_year_sal['나이'] = yy - df_year_sal['출생년도'] + 1
df_year_sal['연령대'] = (df_year_sal['나이']//10)*10

print(df_year_sal)

vcount=df_year_sal['연령대'].value_counts()
df_age_band=DataFrame(vcount)
print(df_age_band)

df_age_band_sort = df_age_band.sort_index()
print(df_age_band_sort)

index_after ={}
for i in list(df_age_band_sort.index):
    index_after[i] = "%d대" %i
    
df_age_band_sort.rename(index=index_after,inplace=True)
print(df_age_band_sort)

pyplot.rcParams['font.family'] ='Malgun Gothic'

df_age_band_sort.plot.bar(rot=0)
pyplot.title('연령대 분포')
pyplot.grid()
pyplot.xlabel('연령대')
pyplot.ylabel('명')
pyplot.show()