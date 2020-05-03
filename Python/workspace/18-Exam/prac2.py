# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:17:19 2020

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
gen_year = df.filter(['h12_g3','h12_g4'])
df_gen_year = gen_year.rename(columns={'h12_g3':'성별','h12_g4':'출생년도'})
yy = dt.datetime.now().year
df_gen_year['연령대'] = ((yy - df_gen_year['출생년도'] + 1)//10)*10
df_gen_year['성별'] = numpy.where(df_gen_year['성별'] ==1 ,'남자','여자')

print(df_gen_year.isna().sum())
df_age_gen_count =df_gen_year.groupby(['성별','연령대'], as_index=False).count()
print(df_age_gen_count)
df_age_gen = df_age_gen_count.rename(columns={'출생년도':'명'})
print(df_age_gen)
pv_age_gen=df_age_gen.pivot('연령대','성별','명')
print(pv_age_gen)

print(df_gen_year)