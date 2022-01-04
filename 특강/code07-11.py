# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 11:22:31 2022

@author: khb16
"""
# 원형큐
## 함수
def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear):
        print("큐 텅~")
        return True
    else:
        return False
    
def isQueueFull():
    global SIZE, queue, front, rear
    if ((rear+1) % SIZE == front):
        return True
    else:
        return False
    
def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print("큐 꽉!")
        return
    rear = (rear+1) % SIZE
    queue[rear] = data
    
def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐 텅~")
        return None
    front = (front+1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐 텅~")
        return None
    return queue[(front+1) % SIZE]


## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = 0

## 메인
SIZE = 5
queue = [None, None, '문별','휘인','선미']
front = 1
rear = 4

enQueue("유정")
print("-----큐 상태-----")
print("[출구] <--" , end = ' ')
for i in range(0,len(queue),1):
    print(queue[i], end=' ')
print('<-- [입구]')
# [출구] <-- 유정 None 문별 휘인 선미 <-- [입구]

deQueue()
# [출구] <-- 유정 None None 휘인 선미 <-- [입구]