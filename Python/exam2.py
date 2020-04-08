# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 14:29:30 2020

@author: kimyongkuk
"""

var =70

if var<50:
    pass
elif var<60:
    pass
else:
    pass

'''
num1= int(input("첫번째 정수 입력:"))
num2= int(input("첫번째 정수 입력:"))

if num2 > num1:
    num1, num2 = num2, num1
print(num1,num2)#3 1


year = int(input("년도입력"))
if(year%4 ==0)and(year%100 !=0)or(year %400 ==0):
    print(str(year)+'년은 윤년입니다')
else:
    print(str(year)+'년은 평년입니다')
'''
'''
a='abcdcba'
print(a, "회문" if a==a[::-1]else"회문아님")
'''

'''
n1 = float(input('첫번째 실수 입력:'))
n2 = float(input('두번째 실수 입력:'))
s1 = str(input('연산자 입력:'))

if   s1=="*": res=n1*n2
elif s1=="/": res=n1*n2
elif s1=="%": res=n1%n2
print("%f %s %f: %f"%(n1,s1,n2,res))
'''
'''
scoreA = int(input("국어점수:"))
scoreB = int(input("영어점수:"))

scoreSum=scoreA+scoreB
scoreEvr=scoreSum/2
if 90 <= scoreEvr <= 100: grade="A"
elif 80 <= scoreEvr: grade="B"
elif 70 <= scoreEvr: grade="C"
elif 60 <= scoreEvr: grade="D"
else: grade="F"
print("총점 %d" %(scoreSum))
print("평균 %.1f" %(scoreEvr))
print("학점 %s" %(grade))
'''
'''
a = ""
for x in range(10):
    a+=str(x)+" " 
print(a)


for x in range(2,10):
    for y in range(1,10):
        print("%d*%d=%2d"%(x,y,x*y),end=" ")
    print()
    

tot=0
i=1
while True:
    if i>10:break
    tot+=i
    i+=1
print(tot)
'''

'''
t=0     #내보낼값
i=0     #곱할값
num3= int(input("1-100 사이 정수"))
while True:
    i+=1
    t=num3*i
    if t>=100:break;
    print(t)  
    
print("%d개"%(i-1))
'''
'''
while (True):
    num = int(input("몇단을 출력할지 입력하세요"))
    for x in range(1,10):
        print("%s*%s=%s"%(num,x,num*x))
    if input("next: Y ")!="Y": break
'''
'''

listA =["국어","영어",1,43.3,True]
listA.append(1)
print(len(listA))
print(listA)
print(*listA)

listA[1]=["수학"]
print(listA[1:3])
listA[2:3]=["국어","사회"]
print(listA.index(1))
listA.insert(4,"일본어")
print(listA)

listB=["국어","영어","수학"]
sorted(listB,reverse=True)
print(listB)

listC=["국어","영어","수학"]
listC.sort(reverse=True)
print(listC)

del(listC[1:3])
print(listC)

listD=["국어","국어","영어","영어","수학","수학"]
listD.remove("국어")
print(listD)
listD.clear()



listE=[[] for j in range(10)]

print(listE)

'''
SIZE=5
score=[]
rank=[]
for x in range(SIZE):
    temp=int(input(str(x+1)+"번 점수 입력:"))
    score.append(temp)
    rank.append(1)
    
#등수계산
for x in range(len(score)):
    for y in range(len(score)):
        if score[x] < score[y]: rank[x] +=1
#확인
for x in range(len(score)):
    print("{}점:{}등".format(score[x], rank[x]))

SIZE2=5
score2={}
rank2=[]

for x in range(SIZE2):
    temp2 = int(input(str(x+1) +"번 점수 입력:"))
    score2[temp2]=1

for x in score2.keys():
    for y in score2.keys():
        if x < y : score2[x] +=1

for x in range(score2.keys()):
    print("{}점:{}등".format(x,score[x]))