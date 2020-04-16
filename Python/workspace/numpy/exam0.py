# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 15:30:42 2020

@author: kimyongkuk
"""


import numpy

data1=[1,2,3,4,5]
data2=[1.7,2,5.5,7,9.9]

#numpy 1차원 배열 생성
arr1= numpy.array(data1)
arr2= numpy.array(data2)#정수와 실수가 섞여있으면 모두 실수로 변환

print(arr1)
print(arr2)

#numpy 배열 속성
print(type(arr1),type(arr2))
#저장된 데이터 속성
print(arr1.dtype)
print(arr2.dtype)

dataA=[1,2,3]
dataB=[4,5,6]
dataC=[7,8,9]

#numpy 2차원배열 생성
arrZ=numpy.array([dataA,dataB,dataC])
print(arrZ)
print(arrZ.dtype)