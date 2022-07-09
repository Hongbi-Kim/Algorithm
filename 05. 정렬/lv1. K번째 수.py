# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 23:46:25 2022

@author: khb16
"""
# 정렬
# K번째 수

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = []

for command in commands:
    a = sorted(array[command[0]-1:command[1]])
    answer.append(a[command[2]-1])
    
