# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 15:18:13 2022

@author: khb16
"""
# 정렬
# 선택정렬
## 함수
def findMinIndex(ary):
    minIdx = 0
    for i in range(1,len(ary)):
        if (ary[minIdx] > ary[i]):
            minIdx = i
    return minIdx


## 전역
testAry = [55,88,33,77]

## 메인
minPos = findMinIndex(testAry)
print("최솟값 --> ", testAry[minPos])
# 최솟값 -->  33
