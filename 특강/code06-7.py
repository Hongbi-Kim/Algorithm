# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 17:22:38 2022

@author: khb16
"""
# 스택의 일반 구현

## 함수
# 스택이 꽉 찼는지 확인하는 함수
def isStackFull():
    global SIZE, stack, top
    if (top >= SIZE-1):
        return True
    else:
        return False
    
def push(data):
    global SIZE, stack, top
    if (isStackFull() == True):
        print("스택 꽉!")
        return
    top += 1
    stack[top] = data

# 스택이 비었는지 확인하는 함수
def isStackEmpty():
    global SIZE, stack, top
    if (top == -1) :
        return True
    else:
        return False

# 스택에서 데이터 추출    
def pop():
    global SIZE, stack, top
    if (isStackEmpty()) :
        print('스택 텅~')
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data
    
# 스택에서 top 위치의 데이터를 확인하는 함수
def peek():
    global SIZE, stack, top
    if (isStackEmpty()):
        print('스택 텅~')
        return None
    return stack[top]

## 전역
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1 




## 메인
stack = ['커피','녹차','꿀물','콜라','환타']
top = 4
print(isStackFull())
# True

stack = ['커피','녹차','꿀물','콜라',None]
top = 3
print(isStackFull())
# False

#---------------------------------------------------

push('맥주')
print(stack)
# ['커피', '녹차', '꿀물', '콜라', '맥주']

push('포도주')
# 스택 꽉!
print(stack)
# ['커피', '녹차', '꿀물', '콜라', '맥주']

#---------------------------------------------------

stack = ['커피',None,None,None,None]
top = 0
print(pop())
# 커피
print(pop())
# 스택 텅~
# None
