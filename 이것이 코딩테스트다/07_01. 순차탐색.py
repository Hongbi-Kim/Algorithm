# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 21:46:07 2022

@author: khb16
"""
# 7-1. 순차 탐색
## 함수
def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i

## 전역
n = 5
array = ['지효','사나','쯔위','정연','미나']

## 메인        
print("생성할 원소 개수를 입력한 다음 한 칸 띄고 참을 문자열 입력")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열 입력, 구분은 띄어쓰기 한 칸")
array = input().split()

target = '사나'
print(sequential_search(n, target, array))
# 1