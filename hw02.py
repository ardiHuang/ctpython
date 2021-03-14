# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:07:54 2021

@author: 黃仕聿
"""

# 1.使用者輸入一範圍的整數，求四的倍數?求哪些是質數?

start = int(input("初始值："))
end = int(input("最終值："))

print("4的倍數有：",end="")
for i in range(start,end+1):
    if i % 4 == 0:
        print(i,sep=",",end=" ")    
    
print()
        
print("質數有：",end="")
for j in range(1,end):
    check = 0
    for a in range(2,j):
        if j % a == 0:
            check=+1
    if check == 0 and j != 1:
        print(j,end=" ")
print("over")