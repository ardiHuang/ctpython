# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 11:21:19 2021

@author: 黃仕聿
"""

#由電腦亂數產生1~49之中六個不重複整數，請遞增排序印出
import random

arr = []
count = 0
while True:
    r = random.randint(1,49)
    if count == 6:
        break
    if arr.count(r) == 0:
        arr.append(r)
        count += 1
arr.sort()
print(arr)
        