# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 16:23:34 2020

@author: kimyongkuk
"""

import numpy

arr1 =numpy.zeros(10)
print(arr1)
print(arr1.dtype)
print(arr1.shape)


arr1 =numpy.zeros((3,4))
print(arr1)
print(arr1.dtype)
print(arr1.shape)

arr1 =numpy.ones((3,4))
print(arr1)
print(arr1.dtype)
print(arr1.shape)

arr1 =numpy.eye(3)
print(arr1)
print(arr1.dtype)
print(arr1.shape)