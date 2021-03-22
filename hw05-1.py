# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 16:00:26 2021

@author: 黃仕聿
"""

#巴斯卡三角形

T = [[1],[1,1]]
count = 0
while True:
    l = len(T)-1
    a=[1]
    for i in range(0,l):
        a.append(T[l][i]+T[l][i+1])
    a.append(1)
    T.append(a)
    count += 1
    if count == 7:
        break
for j in T:
    for k in j:
        print('{}'.format(k),end=' ')
    print()
