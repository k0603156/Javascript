# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 15:49:33 2020

@author: kimyongkuk
"""

import numpy

arr1 = numpy.arange(0,10,2)
print(arr1)
print(type(arr1))
print(arr1.dtype)

arr1 = numpy.arange(0,10)
arr1 = numpy.arange(5)


arr2 = numpy.arange(1,13).reshape(4,3)
print(arr2)
print(type(arr2))
print(arr2.dtype)
print(type(arr2))
print(arr2.shape)

arr3 = numpy.linspace(1,5,10) #1-5사이 데이터 10개
print(arr3)
print(type(arr3))
print(arr3.shape)

arr4 = numpy.linspace(1,10,10) #1-5사이 데이터 10개
print(arr4)
print(type(arr4))
print(arr4.shape)

