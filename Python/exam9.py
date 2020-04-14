# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 17:44:25 2020

@author: kimyongkuk
@title: module
"""


import module

module.my_func()

import module as modl

modl.my_func()

from module import my_func

my_func()

from module import my_func as mf

mf()

import modules.module as mod2

mod2.my_func2()

