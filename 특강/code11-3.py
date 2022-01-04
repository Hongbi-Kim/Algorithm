# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 15:41:45 2022

@author: khb16
"""
impport random
# 선택정렬 2
## 함수
def selectionSort(ary):
    n = len(ary)
    for i in range(0,n-1): # 0, 1, 2 (제일 작은 값)
        minIdx = i
        for k in range(i+1,n):
            if (ary[minIdx] > ary[k]):
                minIdx = k
            tmp = ary[i]
            ary[i] = ary[minIdx]
            ary[minIdx] = tmp
    return ary

## 전역
dataAry = [ random.randint(1,99) for _ in range(20)]

## 메인
print('정렬전 -->', dataAry)
dataAry = selectionSort(dataAry)
print('정렬후 -->', dataAry)
# 정렬전 --> [36, 60, 92, 55, 31, 45, 62, 96, 68, 75, 53, 9, 60, 14, 67, 68, 8, 36, 93, 67]
# 정렬후 --> [9, 14, 31, 36, 36, 8, 45, 53, 55, 60, 60, 62, 67, 67, 68, 68, 75, 92, 93, 96]