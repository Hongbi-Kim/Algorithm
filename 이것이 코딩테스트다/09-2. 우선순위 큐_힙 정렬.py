# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 21:29:32 2022

@author: khb16
"""
# 우선순위 큐 라이브러리를 활용한 힙 정렬 구현 예제

# 최소 힙
#import sys
import heapq
#input = sys.stdin.readline

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result
result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 최대 힙
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,-value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result
result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
# [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0]

    
n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

res = heapsort(arr)

for i in range(n):
    print(res[i])
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9