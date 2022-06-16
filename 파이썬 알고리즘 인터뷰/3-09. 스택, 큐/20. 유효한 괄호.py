# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 23:35:24 2022

@author: khb16
"""

# 스택, 큐
# 유효한 괄호

s = '()[]{}'

def isValid(s):
    stack = []
    table = {
        ')' : '(',
        '}' : '{',
        ']' : '['}
    # 스택 이용 예외 처리 및 일치 여부 판별
    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0

isValid(s)
# True