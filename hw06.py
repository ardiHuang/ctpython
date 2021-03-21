# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 16:18:29 2021

@author: 黃仕聿
"""

#由使用者輸入獲利金額(整數)
#十萬(含)以內，獎金10%
#如果獎金介於十萬至二十萬(含)，十萬以下獎金10%,剩餘獎金7%
#20萬~40萬(10%,7%,4%)

money = int(input('請輸入金額(1~40萬)'))
# bonus = 0
# if money <= 100000:
#     bonus += money*0.1
# elif money <= 200000:
#     bonus = 10000 + (money-100000)*0.07
# elif money<=500000 :
#     bonus = 10000 + 7000 + (money-200000)*0.03
# else :
#     bonus = 10000 + 7000 + 200000*0.03 + (money-400000)*0.01
    
# print('bonus={}'.format(int(bonus)))
    
bonus = 0
mRange = [0,100000,200000,400000]
mRate = {0:0,100000:0.1,200000:0.07,400000:0.03}
for i in range(0,len(mRange)):
    plus = (money-mRange[i-1])*mRate[mRange[i]]
    if money-mRange[i]<=0 and i == 0:
        bonus += money*mRate[mRange[i]]
        break
    elif money-mRange[i]<=0:
        bonus += plus
        break
    elif i == len(mRange)-1:
        bonus += plus
        break
    bonus += (mRange[i]-mRange[i-1])*mRate[mRange[i]]
print('bonus={:.0f}'.format(bonus))

    