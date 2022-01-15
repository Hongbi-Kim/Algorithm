# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 01:36:25 2022

@author: khb16
"""

# 선택정렬과 기본 정렬 라이브러리 수행 시간 비교
# 라이브러리는 기본적으로 O(NlogN) 보장

from random import randint
import time

# 배열 10,000개의 정수를 삽입
array = []
for _ in range(10000):
    array.append(randint(1,100))

# 선택 정렬    
start_time = time.time()

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        
end_time = time.time()
print('선택 정렬 성능 측정: ', end_time - start_time)

# 배열을 다시 무작위로 초기화
array = []
for _ in range(10000):
    array.append(randint(1,100))
    
# 기본 정렬 라이브러리
start_time = time.time()
array.sort()
end_time = time.time()
print('기본 정렬 라이브러리 성능 측정: ', end_time-start_time)

# 선택 정렬 성능 측정:  17.82332730293274
# 기본 정렬 라이브러리 성능 측정:  0.000997781753540039
