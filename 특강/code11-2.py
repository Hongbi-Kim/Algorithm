# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 15:24:27 2022

@author: khb16
"""
import random
# 선택정렬 1(가장 쉬운 정렬이지만, 실제로 써도 됨)
## 함수
def findMinIndex(ary):
    minIdx = 0
    for i in range(1,len(ary)):
        if (ary[minIdx] > ary[i]):
            minIdx = i
    return minIdx

## 전역
before = [ random.randint(1,99) for _ in range(20)]
after = []

## 메인
print('정렬 전 -->', before)
for i in range(len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del(before[minPos])
print('정렬 후-->', after)
# 정렬 전 --> [68, 85, 30, 78, 83, 67, 83, 94, 39, 62, 30, 90, 61, 70, 38, 29, 5, 74, 16, 93]
# 정렬 후--> [5, 16, 29, 30, 30, 38, 39, 61, 62, 67, 68, 70, 74, 78, 83, 83, 85, 90, 93, 94]
