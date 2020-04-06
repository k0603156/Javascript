# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 15:33:47 2020

@author: kimyongkuk

* 아나콘다
* 스파이더
"""
from __future__ import print_function
from textwrap import TextWrapper



try:
    import __builtin__
    
except ImportError:
    import builtins as __builtin__
    
    #!TODO:  문자열 개행 '''개행이 되지 않'''
def print(*args, **kwargs):
    argstr='  '.join([str(x) for x in args])
    prefix = "       ->"
    preferredWidth = 70
    wrapper = TextWrapper(initial_indent=prefix, width=preferredWidth,subsequent_indent=' '*len(prefix))
    return __builtin__.print(wrapper.fill(argstr), **kwargs)

def title(title):
    __builtin__.print("\n##", title, end="\n\n")
    

title("comment")

'''
im comment
'''
"""
we r comments
"""

title("문자열의 반복")

print("python"*5)
#결과:pythonpythonpythonpythonpython

title("sep")

print("Hello","Python",sep="#")
#결과:Hello#Python

title("end")

print("Hello"*5,end="Python")
#결과:HelloHelloHelloHelloHelloPython
#줄바꿈이 되지않음 end 생략=줄바꿈이 default

title("help")

#help(print)
#결과:print(...) 해당함수의 명세...

title("variable")

_varName1 = "varData"
print(id(_varName1))#메모리주소확인
#변수자체가 참조변수
#메모리사이즈가 타입을 선언해 정해지지 않음 큰 숫자도 저장이 가능

title("type_check")

print(type (_varName1))
print(type (True))
#결과: <class 'str'> \n <class 'bool'>

title("dynamic type")

_varName1 = "varData2"
print(id(_varName1)) 
_varName1 = 7.7
print(type(_varName1))
print(id(_varName1))
#결과: <class 'float'>
#선언된 변수이름이 레퍼런스이기때문에 값을 새로 할당해 주소가 저장 됨 

title("타입 변환")

var1 = str(1+2)
print("addr",id(var1)) 
print(var1)
print("addr",id(var1)) 
print(int(var1))
print("addr",id(var1)) 
print(float(1+2))
var1 = str(var1)
print("addr",id(var1)) 
print(var1)
#결과:
#addr 1938704411248  *해당 값은 다를 수 있음
#3
#addr 1938704411248
#3
#addr 1938704411248
#3.0
#addr 1938704411248
#3

title("문자열 개행")

var2 = '''
p
y
t
h
o
n
'''
print(var2)
#결과:
#p
#y
#t
#h
#o
#n

title("Index")

st1 = "ABCDEFG"
print(st1[0])
print(st1[1])
print(st1[2])
print(st1[3])
print(st1[-3])
print(st1[-2])
print(st1[-1])
#결과:
#A
#B
#C
#D
#E
#F
#G

title("Slice")

print(st1[:3])
print(st1[3:4])
print(st1[4:])
print(st1[-3:])
#결과:
#ABC
#D
#EFG
#EFG

title("length")

print(len(st1))
#결과:7

title("문자열 인덱스로 접근 value 변경")

st2="DDD"
#st2[0]="x" TypeError: 'str' object does not support item assignment
st3= st2[:1]+"x"+st2[2:]
print(st3)

title("값이 있는지 체크")
print(bool(st2))


title("Input")

#inpt=input("입력")
#print(inpt)

title("Input&print&formatting")
'''
stadi=str(input("경기장은 어디입니까?"))
teamW=str(input("이긴 팀은 어디입니까?"))
teamL=str(input("진 팀은 어디입니까??"))
score=str(input("스코어는 몇대몇 입니까?"))
result=("""\
      오늘%s에서 야구경기가 열렸습니다.
      %s과 %s의 치열한 공방전을 펼쳤습니다.
      결국 %s은 %s에 %s로 승리했습니다.
""" %(stadi,teamW,teamL,teamW,teamL,score))

print(result)
'''


title("연산자")

print(2+1)
print(2-1)
print(2*1)
print(2/1)
print(2//1)
print(2%1)

#결과:
#3
#1
#2
#2.0 실수
#2
#0


title("포함 체크")

st4="comein"
print("in" in st4)#True
print("in" not in st4)#False

title("Addr of REF check")
print(id(st4))
st4a=st4
print(st4 is st4a)
print(st4 is not st4a)

a=1
b=2
c=1
print(a is b)#True 
print(a is c)#False
print(b is c)#False
#True 같은 값은 새로 생성하지않고 참조 
#False

title("자료의 참과 거짓 ")
print(bool(100))#True
print(bool(None))#False


title("Block")
#명령어를 묶는 단위 :로시작 이후 indent(들여쓰기)

title("if")
score=87
if(score >= 80 and score<90):
    print("B학점입니다.")