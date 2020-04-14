# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 18:55:59 2020

@author: kimyongkuk
@title:calendar
"""

import calendar

dayString = ("월","화","수","목","금","토","일")
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.calendar(2020))
print(calendar.month(2020,4))
cald=calendar.monthrange(2020,4)
print(cald)


