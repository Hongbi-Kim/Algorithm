# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 16:24:21 2022

@author: khb16
"""
import random
# 이진 검색
## 함수
def binarySearch(ary, fData):
    pos = -1
    start = 0
    end = len(ary)-1
    while (start <= end):
        mid = (start + end) // 2
        if fData == ary[mid]:
            return mid
        elif fData > ary[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return pos


## 전역
dataAry = [random.randint(1,99) for _ in range(10)]
findData = dataAry[random.randint(0,len(dataAry)-1)]
dataAry.sort()

## 메인
print('배열 -->', dataAry)
position = binarySearch(dataAry, findData)
if position == -1:
    print(findData, ' 없다.')
else:
    print(findData, ':', position, ' 위치에 있음')
# 배열 --> [3, 10, 12, 20, 60, 67, 71, 87, 96, 98]
# 10 : 1  위치에 있음
