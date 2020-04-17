# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 15:36:30 2020

@author: kimyongkuk
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.plot(1,2,"o",4,8,"^",4,20,"s")
plt.title("Plot Graph")
plt.grid(True)
plt.legend(['data1','data2'])
plt.show()