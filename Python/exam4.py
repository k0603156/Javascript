# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:31:54 2020

@author: kimyongkuk
"""
'''
students=[]
with open("test.txt","r",encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n","")
        print(line.split(","))
        students.append(line.split(","))
'''
'''

class Car:
    def drive(self):
        self.speed=10#함수가 호출되어야 생성
    
    def output1(self):
        print(self.model)
        print(self.color)
        print(self.speed)
        
print(type (Car))
print(type( Car()))

myCar =Car()
myCar.model ="E-Class"
myCar.color ="black"
myCar.drive()
myCar.output1()


'''

class Car:
    speed =5
    
    def drive(self):
        self.speed=10
    def output(self):
        print(Car.speed)
        print(self.speed)
        
print(Car.speed) #5

myCar = Car()
myCar.output() # 5 5
myCar.speed=11
myCar.output() # 5 11
print(myCar.speed) # 11
##새로운 객체를 생성해도 Class변수는 새로 생성되지 않음


class HelloWorld:
    message ='ni hao'
    def setEng(self):
        self.message ="hello"
    def setKor(self):
        self.message ="안녕"
    def setViet(self):
        message= "xin chao"#지역변수
    def sayHello(self):
        print(self.message)
        
hello= HelloWorld()

hello.setEng()
hello.sayHello()

hello.setViet()
hello.sayHello()

class Calc:
    def plus(self, x, y):
        return x+y
    def minus(self, x,y):
        return x-y
    def multiply(self,x,y):
        return x*y
    def divide(self,x,y):
        return x/y
    def f(self,x,y):
        result1=self.plus(x,y)
        result2=self.plus(x,y)
        result3=result1+result2
        return result3
    
print(Calc().f(1,2))


