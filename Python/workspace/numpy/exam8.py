# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 16:40:18 2020

@author: kimyongkuk
"""


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

city=['서울','인천','대전','대구','울산','부산','광주']
lat=[37.56,37.45,36.35,35.89,35.53,35.18,35.16]
lng=[126.97,126.70,127.38,128.60,129.31,129.07,126.85]

pop_den=np.array([6154,2751,2839,2790,1066,4454,2995])*0.3

plt.rcParams['font.family'] ='Malgun Gothic'
plt.title("지역별 인구밀도(2017)")

plt.scatter(lng, lat, pop_den, c="b", alpha=0.5)


for d in zip(lng,lat,city):
    la,ln,ct=d
    plt.text(la,ln,ct)
    
plt.show()