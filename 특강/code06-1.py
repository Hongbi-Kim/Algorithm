# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 17:15:50 2022

@author: khb16
"""

## 전역
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1 # 초깃값


## 메인
# 데이터 삽입 : push
top += 1
stack[top] = '커피'
top += 1
stack[top] = '녹차'
top += 1
stack[top] = '꿀물'
print("-----스택 상태-----")
for i in range(len(stack)-1,-1,-1):
    print(stack[i])
# None
# None
# 꿀물
# 녹차
# 커피

# 데이터 추출 : pop
data = stack[top] # '꿀물'
stack[top] = None
top -= 1
print('pop -->', data)
# pop --> 꿀물

data = stack[top] # '녹차'
stack[top] = None
top -= 1
print('pop -->', data)
# pop --> 녹차

data = stack[top] 
stack[top] = None
top -= 1
print('pop -->', data)
# pop --> 커피

print("----- 스택 상태-----")
for i in range(len(stack)-1,-1,-1):
    print(stack[i])
# ----- 스택 상태-----
# None
# None
# None
# None
# None    
