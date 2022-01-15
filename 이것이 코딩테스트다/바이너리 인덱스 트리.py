# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 15:22:41 2022

@author: khb16
"""

# 바이너리 인덱스 트리 구현
n = 8
for i in range(n+1):
    print(i, "의 마지막 비트: ", (i & -i))
# 0 의 마지막 비트:  0
# 1 의 마지막 비트:  1
# 2 의 마지막 비트:  2
# 3 의 마지막 비트:  1
# 4 의 마지막 비트:  4
# 5 의 마지막 비트:  1
# 6 의 마지막 비트:  2
# 7 의 마지막 비트:  1
# 8 의 마지막 비트:  8

import sys
input = sys.stdin.readline

# 데이터의 개수(n), 변경 횟수(m), 구간 합 계산 횟수(k)
n,m,k = map(int, input().split())

# 전체 데이터의 개수는 최대 1,000,000개
arr = [0]*(n+1)
tree = [0]*(n+1)

# i번째 수까지의 누적 합 계산
def prefix_sum(i):
    result = 0
    while i>0:
        result += tree[i]
        # 0이 아닌 마지막 비트만큼 빼가면서 이동
        i -= (i & -i)
    return result

# i번째 수를 dif만큼 더하는 함수
def update(i, dif):
    while i <= n:
        tree[i] += dif
        i += (i & -i)
        
# start 부터 end까지의 구간 합을 계산
def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start-1)

for i in range(1, n+1):
    x = int(input())
    arr[i] = x
    update(i, x)
    
for i in range(m+k):
    a,b,c = map(int, input().split())
    # 업데이트 연산인 경우
    if a == 1:
        update(b, c-arr[b])
        arr[b] = c
    # 구간 합(interval sum) 연산인 경우
    else:
        print(interval_sum(b, c))
        
