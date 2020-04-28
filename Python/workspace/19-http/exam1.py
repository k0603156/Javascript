# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 18:47:24 2020

@author: kimyongkuk
"""
import requests
simple_text_url = 'http://192.168.0.96/simple_text.txt'

res = requests.get(simple_text_url)

if res.status_code != 200:
    print('[%d Error]' %(res.status_code, res.reson))
    quit()

res.encoding='utf-8'

print(res.text)
