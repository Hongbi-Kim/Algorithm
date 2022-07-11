# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 23:05:12 2022

@author: khb16
"""

# 스택/큐
# 같은 숫자는 싫어

arr = [4,4,4,3,3]

# sol 1)
answer = []
answer.append(arr[0])
for i in range(len(arr)-1):
    if arr[i] != arr[i+1]:
        answer.append(arr[i+1])