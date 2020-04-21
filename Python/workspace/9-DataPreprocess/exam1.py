# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:45:10 2020

@author: kimyongkuk
"""


from pandas import DataFrame
from pandas import ExcelFile

xlsx = ExcelFile("data/children_house.xlsx")
df = xlsx.parse(xlsx.sheet_names[0])
print(df)

children_house = df.rename(index=df['지역'])
print(children_house)
