# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 17:34:33 2020

@author: kimyongkuk
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


member_IDs =['m01','m02','m03','m04']
ex_before=[27,35,40,33]
ex_after=[30,38,42,37]

mem_num=len(member_IDs)
index =np.arange(mem_num)
plt.bar(index,ex_before)
plt.show()

colors=["r","g","b","c"]
plt.bar(index, ex_before,width=0.6, color=colors)


plt.barh(index,ex_before, height=0.6,color=colors,tick_label=member_IDs)
plt.show()