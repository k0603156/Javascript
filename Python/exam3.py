# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 14:53:39 2020

@author: kimyongkuk
"""

import math

def inputScore(*args): return [int(input(subject+"점수 입력:")) for subject in args]

def getAvg(*args): return sum(args)/len(args)
'''
def getGrade(arg):
    if   arg <=60:  return "F"
    elif arg <=70:  return "D"
    elif arg <=80:  return "C"
    elif arg <=90:  return "B"
    else:           return "A"
'''

def getGrade(arg): return "F" if arg <= 60 else chr(75-(math.ceil(arg/10)))
    
def output(arg): print(arg,"학점입니다.")

#output(getGrade(getAvg(*inputScore("영어","국어"))))


'''
#전역변수 사용
#default param사용
area=0
def calc_area(r=1):
    global area
    area = 3.14 * r **2

r = float(input("원의 반지름:"))
calc_area(r)
print("원의 넓이:", area)
'''

def add(a=1,b=100): return sum(range(a,b+1))

print(add(1,100))


#lambda
square = lambda x: x**2
print(square(2))

print((lambda x: x**2)(3))

print((lambda x,y,z: x+2*y+5*z)(1,2,3))

score =[70,80,90,87]

print("총점:{}, 평균:{}, 최대값:{}, 최소값:{}".format(sum(score), sum(score)/len(score), max(score), min(score)))


#file
w = open("test.txt","w")
for i in range(1,11):
    data = str(i) + "번 째 줄입니다.\n"
    w.write(data)
w.close()

r= open("test.txt","r")
while(True):
    line=r.readline()#한줄씩 읽기 
    if not line:break
    print(line, end="")
r.close()

r= open("test.txt","r")
lines=r.readlines()
r.close()
print(x for x in lines)

r= open("test.txt","r")
for line in r: #open(,"r") 기본은 readlines
    print(line,end="")
r.close()

with open("test.txt","w") as f:
    for i in range(1,6):
        data = str(i) +"번 째 줄입니다."
        f.write(data)

with open("test.txt","r") as r:
    lines =r.readlines();
    print(lines)
    
    