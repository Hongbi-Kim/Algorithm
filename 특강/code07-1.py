# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 09:14:53 2022

@author: khb16
"""
# 큐
## 함수


## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

## 메인
rear += 1
queue[rear] = '화사'

rear += 1
queue[rear] = '솔라'

rear += 1
queue[rear] = '문별'

print("-----큐 상태-----")
print("[출구] <--" , end = ' ')
for i in range(0,len(queue),1):
    print(queue[i], end=' ')
print('<-- [입구]')
# -----큐 상태-----
# [출구] <-- 화사 솔라 문별 None None <-- [입구]

# 입장하세요.
front += 1
data = queue[front]
queue[front] = None
print("deQueue -->", data)
# deQueue --> 화사

front += 1
data = queue[front]
queue[front] = None
print("deQueue -->", data)
# deQueue --> 솔라

front += 1
data = queue[front]
queue[front] = None
print("deQueue -->", data)
# deQueue --> 문별

# -----큐 상태-----
# [출구] <-- None None None None None <-- [입구]

print(front, rear)
# 2 2