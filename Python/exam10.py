# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 18:23:14 2020

@author: kimyongkuk
@title: date
"""
from datetime import date

print(date.today())
ndate=date(2020,10,5)
print(ndate)
print(f'{ndate.year}/{ndate.month}/{ndate.day}')

from datetime import datetime
n2date=datetime(2021,2,6,10,2,30)
print("{:%y/%m/%d %H:%M:%S}".format(n2date))

print("{:%D}".format(n2date))