# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 17:08:18 2020

@author: kimyongkuk
@title: doc
"""

"""
import string

st1= string.ascii_letters+string.digits
print(st1)

while True:
    userId = input('your id:')
    
    for ch in userId:
        if ch not in st1:
            print('invalid user id')
            checkId=False
            break
        else: checkId= True
        
    if checkId:
        print('valid user id')
        break
"""


class AAA:
    "HELLO CLASS AAA"
    
    def ex(self):
            "HELLO METHOD ex"
            pass

print(__doc__)
print(AAA.__doc__)
print(AAA.ex.__doc__)
print(print.__doc__)