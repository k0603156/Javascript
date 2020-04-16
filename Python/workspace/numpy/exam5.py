# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:48:04 2020

@author: kimyongkuk
"""

import numpy

data1=[1,2,3,4]
data2=[10,20,30,40]

arr1 = numpy.array(data1).reshape(2,2)
arr2 = numpy.array(data2).reshape(2,2)

print(arr1)
print(arr2)

print(numpy.dot(arr1,arr2))#행렬곱
print(numpy.transpose(arr1))#전치행렬
print(numpy.linalg.inv(arr1))#역행렬
print(numpy.linalg.det(arr1))#행렬식


dataA= [10,20,30,40,50,60]
arrA= numpy.array(dataA)

print(arrA)

#1차원 인덱싱
print(arrA[2])
print(arrA[[1,3,5]])
print(arrA[arrA > 40])
#print(dataA[dataA>40])   #err

#2차원 인덱싱
arrB= numpy.arange(10,100,10).reshape(3,3)
print(arrB)
print(arrB[0,2])
print(arrB[0][2])
arrB[0,2]=35
print(arrB)

#행 변경

arrB[1] =numpy.array([34,54,21])
arrB[2] =[43,45,12]
print(arrB)


print(arrB[[0,2],[0,1]])

#1차원 슬라이싱
print(arrB[1:3])
arrB[2:4]= [35,45,55]
print(arrB)