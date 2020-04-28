# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 18:56:28 2020

@author: kimyongkuk
"""
from matplotlib import pyplot
from matplotlib.image import imread
from pandas import DataFrame
import requests
import json 

simple_url = 'http://192.168.0.96/simple.json'

res = requests.get(simple_url)

if res.status_code != 200:
    print('[%d Error]' %(res.status_code, res.reson))
    quit()

result = json.loads(res.text)
df=DataFrame([result])

img =imread(df.loc[0,'img'])
pyplot.imshow(img)
pyplot.axis('off')
pyplot.show()