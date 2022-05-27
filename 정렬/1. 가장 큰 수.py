# -*- coding: utf-8 -*-
"""
Created on Sat May 28 00:03:42 2022

@author: khb16
"""

# https://programmers.co.kr/learn/courses/30/lessons/42746

numbers = [6, 10, 2]           # return "6210"
numbers = [3, 30, 34, 5, 9]    # return "9534330"

# 답안 1
def solution(numbers):
    num = list(map(str, numbers))
    num.sort(key = lambda x: x*3, reverse = True)
    answer = int(''.join(num))
    return str(answer)

# 답안 2
def solution(numbers):
    num = list(map(str, numbers))
    num.sort(key = lambda x: x*3, reverse = True)
    answer = int(''.join(num))
    return str(answer)

# 답안 3
def solution(numbers):
    num = list(map(str, numbers))
    num.sort(key = lambda x: x*3, reverse = True)
    answer = int(''.join(num))
    return str(answer)