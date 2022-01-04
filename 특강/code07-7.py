# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 10:27:02 2022

@author: khb16
"""

## 함수
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear == SIZE-1):
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print("큐 꽉!")
        return
    rear += 1
    queue[rear] = data

def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear):
        print("큐 텅~")
        return True
    else:
        return False

def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐 텅~")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐 텅~")
        return None
    return queue[front+1]

## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

## 메인
queue = ['화사','솔라','문별','휘인','선미']
front = -1
rear = 4
print("큐가 꽉 찼는지 여부 -->", isQueueFull())
# 큐가 꽉 찼는지 여부 --> True

#--------------------------------------------------
SIZE = 5
queue = ['화사','솔라','문별','휘인',None]
front = -1
rear = 3

enQueue("선미")
print(queue)
# ['화사', '솔라', '문별', '휘인', '선미']
enQueue("재남")
# 큐 꽉!

#--------------------------------------------------
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

print("큐가 비었는지 여부 -->", isQueueEmpty())
# 큐 텅~
# 큐가 비었는지 여부 --> True

#--------------------------------------------------
SIZE = 5
queue = ['화사',None,None,None,None]
front = -1
rear = 0

retData = deQueue()
print("추출한 데이터 -->", retData)
print(queue)
# 추출한 데이터 --> 화사
# [None, None, None, None, None]

#--------------------------------------------------
SIZE = 5
queue = ['화사','솔라',None,None,None]
front = -1
rear = 1

retData = peek()
print('다음에 추출될 데이터 확인 --> ', retData)
# 다음에 추출될 데이터 확인 -->  화사
