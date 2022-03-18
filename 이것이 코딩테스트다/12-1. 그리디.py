# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 23:41:48 2022

@author: khb16
"""

# 1. 모험가 길드

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0  # 현재 그룹에 포함된 모험가의 수

for i in data:      # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1      # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0
print(result)

'''
5

2 3 1 2 2
2
'''

# -------------------------------------------------------------------

# 2
# 곱하기 혹은 더하기

data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)

'''
02984
576
'''

# --------------------------------------------------------------------

# 3
# 문자열 뒤집기












