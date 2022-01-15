# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 00:34:30 2022

@author: khb16
"""

# 정렬
# 데이터를 특정한 기준에 따라 순서대로 나열하는 것
# 일반적으로 문제 상황에 따라서 적절한 정렬 알고리즘이 공식처럼 나옴

# 1. 선택 정렬(Selection Sort)
# 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와
# 바꾸는 것을 반복

array = [7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):
    min_index = i # 가장 적은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프
print(array)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]    


# 시간 복잡도
# N-1번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 한다. (비교 연산 필요)
# 전체 연산 횟수 : N + (N-1) + ... + 2 = (N^2 + N -2) /2
# 빅오 표기법 O(N^2)

# 2. 삽입 정렬(Insertion Sort)
# 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입.
# 선택 정렬에 비해 구현 난이도가 높은 편이지만, 일반적으로 더 효율적으로 동작

array = [7,5,9,0,3,1,6,2,4,8]
for i in range(1, len(array)): 
    for j in range(i, 0, -1): # 인텍스 i부터 1까지 감소하며 반복하는 문법
        if array[j] < array[j-1] : # 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
print(array)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# 시간 복잡도
# O(N^2), 반복문이 두 번 중첩되어 사용
# 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작
# 최선의 경우 O(N)
