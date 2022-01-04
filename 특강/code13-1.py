# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 16:06:24 2022

@author: khb16
"""
import random
# 순차 검색
## 함수
def seqSearch(ary, fData):
    pos = -1
    size = len(ary)
    print('## 비교한 데이터 -->', end = ' ')
    for i in range(size):
        print(ary[i], end=' ')
        if ary[i] == fData:
            pos = i
            break
        elif ary[i] > fData:
            break
    print()
    return pos

## 전역
dataAry = [random.randint(1,99) for _ in range(20)]
findData = dataAry[random.randint(0,len(dataAry)-1)]


## 메인
dataAry.sort()
print('배열 -->', dataAry)
position = seqSearch(dataAry, findData)
if position == -1:
    print(findData, ' 없다.')
else:
    print(findData, ':', position, ' 위치에 있음')
    
# 배열 --> [17, 91, 2, 86, 29, 85, 60, 37, 92, 33, 11, 87, 62, 67, 48, 59, 44, 5, 29, 36]    
## 비교한 데이터 --> 17 91 
# 62  없다.