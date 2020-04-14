# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 18:55:44 2020

@author: kimyongkuk
"""


class Article :
    def __init__(self):
        self.num=0
        self.title=''

class FileArticle(Article):
    def __init__(self):
        self.fileName=''
    def __str__(self):
        return f'자료실 [번호={self.num}, 제목={self.title}, 첨부파일={self.fileName}]'
        
class QnaArticle(Article):
    def __init__(self):
        self.answer=''
    def __str__(self):
        return f'질문/답변 [번호={self.num}, 제목={self.title}, 답변={self.answer}]'
#문자숫자    
print("qwe".isalnum())
print("q2e f".isalnum())
#문자
print("qw3f".isalpha())
print("we f".isalpha())
print("wef".isalpha())
#시작이 대문자 중간에 숫자가 들어간경우 새로 
print("Te35T".istitle())
print("Te".istitle())
print("Te1t".istitle())

print(help(''))

st1= "Hello Python!"
st2= st1.zfill(20)
print(st2)
