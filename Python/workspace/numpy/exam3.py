# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 16:33:51 2020

@author: kimyongkuk
"""

import numpy

data1 =['people','boy','girl',"man","woman"]
data2 =["1.5","2.5","3.5","4.5","5.5"]
data3 =["10","20","30","40","50","60"]

arr1 =numpy.array(data1)
arr2 =numpy.array(data2)
arr3 =numpy.array(data3)

print(arr1)
print(arr2)
print(arr3)

print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)#<U2 unicode max data length in =  2

#형변환
arr_f = arr2.astype(float)
print(arr_f)
print(arr_f.dtype)

arr_i = arr3.astype(int)
print(arr_i)
print(arr_i.dtype)

arr = arr_i.astype(str)
print(arr)
print(arr.dtype)