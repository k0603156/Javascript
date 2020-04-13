# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:49:31 2020

@author: kimyongkuk
"""

import random 
 
class Lotto:

    def __init__(self, count):
        self.count=count
    def create(self):
        self.arr=[[int(random.random()*100) for x in range(1, 6)] for y in range(0, self.count)]
        return self
 
    def sort(self):
        self.arr.sort()
        return self
    
    def print(self):
        print(self.arr,sep="\n")

        
        
lotto = Lotto(5).create().sort().print()

class Triangle:
    def __init__(self, l=None, h=None):
        self.l=1 if l is None else l 
        self.h=2 if h is None else h
    def setTriangle(self, l, h):
        self.l=l
        self.h=h
        return self;
    def getArea(self):
        return self.l*self.h/2
print(Triangle().setTriangle(3,4).getArea())


class CalcParent1:
    def plus(self, x, y):
        return x+y

class CalcParent2:
    def plus(self, x, y):
        return x+y+1
    def minus(self, x, y):
        return x-y

class CalcChild(CalcParent1, CalcParent2):#같은 변수함수는 먼저 상속된 것만 
    def multiply(self, x, y):
        return x*y
    
print(CalcChild().plus(1,2))
    
