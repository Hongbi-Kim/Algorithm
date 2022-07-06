# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 11:48:36 2022

@author: khb16
"""
# [DFS/BFS] 프로그래머스 / # 타겟 넘버

# case 1
numbers = [4, 1, 2, 1]	
target = 4

calc = [0]
tmp = []
v = numbers.pop()
for i in calc:
    tmp.append(i + v)
    tmp.append(i - v)
calc = tmp

# case 2
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)'