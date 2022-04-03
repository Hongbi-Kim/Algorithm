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
# 전부 0으로 바꾸는 경우와 전부 1로 바꾼는 경우 중에서 더 적은 횟수를 가지는 경우 계산

data = input()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대해서 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1
    
# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        # 다음 수에서 1로 바뀌는 경우
        if data[i+1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1
print(min(count0, count1))

'''
0001100
1
'''

# --------------------------------------------------------------------

# 4
# 만들 수 없는 금액
# 만들 수 없는 양의 정수 금액 중 최솟값

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력
print(target)

'''
5

3 2 1 1 9
8
'''








