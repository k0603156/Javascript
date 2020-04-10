# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 17:51:59 2020

@author: kimyongkuk
"""


class Score:
    def set(self):
        print(self)
        self.num = int(input("학번:"))
        self.name = int(input("이름:"))
        self.kor = int(input("국어:"))
        self.eng = int(input("영어:"))
        self.mat = int(input("수학:"))
        self.tot = self.kor+self.eng+self.mat
        self.avg=self.tot/3
        return self
    def output_title(self):
        print(self)
    #    print(f'{num} {name} {kor} {eng} {mat} {tot} {avg}')
    def output(self):
        print(self)
        print(f"""
              학번 {self.num}
              이름 {self.name}
              국어 {self.kor}
              영어 {self.eng}
              수학 {self.mat}
              총점{self.tot}
              평균{self.avg}""")
        
s1= Score()
s2= Score()
Score.set(s2).output()
