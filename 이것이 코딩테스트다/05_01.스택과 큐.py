# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 22:37:19 2022

@author: khb16
"""

# 1. 스택(stack)
# 선입후출 구조(First in last out) 또는 후입선출 구조(last in first out)
stack = []

# 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단
# [5, 2, 3, 1]
print(stack[::-1]) # 최상단
# [1, 3, 2, 5]

# 2. 큐(queue)
# 선입선출 구조(first in first out)
# 공정한 자료구조
from collections import deque
queue = deque()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
# deque([3, 7, 1, 4])