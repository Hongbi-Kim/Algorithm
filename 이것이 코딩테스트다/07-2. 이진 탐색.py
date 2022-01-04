# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 23:27:08 2022

@author: khb16
"""

# 7-2 재귀 함수로 구현한 이진 탐색
## 함수
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

## 전역
array = [1,3,5,7,9,11,13,15,17,19]

## 메인    
n = 10
target = 7

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result)
# 3


# 7-3 반복문으로 구현한 이진 탐색
## 함수
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

## 전역
array = [1,3,5,7,9,11,13,15,17,19]

## 메인    
n = 10
target = 7

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result)
# 3
