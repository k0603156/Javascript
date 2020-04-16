# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 16:54:32 2020

@author: kimyongkuk
"""

import numpy

arr0 = numpy.random.rand(2,3,4)
print(arr0)

data1=[10,20,30,40]
data2=[50,60,70,80]
arr1= numpy.array(data1)
arr2= numpy.array(data2)

print(arr1*arr2)

print(arr1.std())#표준편차
print(arr1.var())#분산
print(arr1.max())
print(arr1.min())

