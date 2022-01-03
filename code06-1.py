# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 17:15:50 2022

@author: khb16
"""

## 전역
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1 # 초기화


## 메인
top += 1
stack[top] = '커피'
top += 1
stack[top] = '녹차'
top += 1
stack[top] = '꿀물'
print(stack)
# ['커피', '녹차', '꿀물', None, None]

data = stack[top]
stack[top] = None
top -= 1
print('팝 -->', data)
# 팝 --> 꿀물

data = stack[top]
stack[top] = None
top -= 1
print('팝 -->', data)
# 팝 --> 녹차













