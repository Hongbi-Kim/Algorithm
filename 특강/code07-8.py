# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 11:04:33 2022

@author: khb16
"""

## 함수
# 개선
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear != SIZE-1):
        return False
    elif (rear == SIZE-1) and (front == -1):
        return True
    else:
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
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
SIZE = 5
queue = [None, None, '문별','휘인','선미']
front = 1
rear = 4

print("큐가 꽉 찼는지 여부 -->", isQueueFull())
# 큐가 꽉 찼는지 여부 --> False
print("큐 상태 -->", queue)
# 큐 상태 --> [None, '문별', '휘인', '선미', None]

enQueue('유정')
print("-----큐 상태-----")
print("[출구] <--" , end = ' ')
for i in range(0,len(queue),1):
    print(queue[i], end=' ')
print('<-- [입구]')
-----큐 상태-----
# [출구] <-- None 문별 휘인 선미 유정 <-- [입구]
