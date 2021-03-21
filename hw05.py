# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 15:46:01 2021

@author: 黃仕聿
"""

#由系統產生七個整數數字(亂數1~100可重複)
#(遞增排序)印出結果 [23,56,14,67,34,57,99]
#由使用者輸入一個值去找尋串列中的值，以二分法顯示找尋過程
import random

data = []
for i in range(0,8):
    data.append(random.randint(1,100))
data.sort()
print(data)
ans = int(input('請選擇其中一個數字'))
while True:
    a=(len(data)-1)//2
    if ans > data[a]:
        del data[:a+1]
        print(data)
    elif ans == data[a]:
        break
    elif ans < data[a]:
        del data[a:]
        print(data)
print('找到了！')

