# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 23:51:02 2022

@author: khb16
"""

# 카드 게임
# 3-3. min() 함수 이용
n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)
    
print(result) 
# 3 3

# 3 1 2

# 4 1 4

# 2 2 2
# 2

# 3-4. 2중 반복문 구조 이용
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)
print(result)
# 2 4

# 7 3 1 8

# 3 3 3 4
# 3
