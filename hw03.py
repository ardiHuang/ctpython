# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 13:39:49 2021

@author: 黃仕聿
"""
import random

ans = random.randint(1, 100)
guess = 0
top = 100
bot = 1
count = 0

while ans != guess:
    print('輸入',bot,'~',top,'之間整數猜數：')
    guess = int(input())
    if ans == guess:
        print('猜對了')
    count += 1
    if count == 5:
        print('已猜錯五次')
        break
    if guess > ans :
        print('猜小一點')
        top = guess-1
    if guess < ans :
        print('猜大一點')
        bot = guess+1
    
    

