# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 23:27:08 2022

@author: khb16
"""

# 7-2 재귀 함수로 구현한 이진 탐색
## 함수
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

## 전역
# n(원소의 개수)와 target(찾고자 하는 문자열) 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))


## 메인    
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```
10 7

1 3 5 7 9 11 13 15 17 19
4
```


# 7-3 반복문으로 구현한 이진 탐색
## 함수
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

## 전역
# n(원소의 개수)와 target(찾고자 하는 문자열) 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))


## 메인    
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

```
10 7

1 3 5 7 9 11 13 15 17 19
4
```

# ----------------------------------------------------------
## 파이썬 이진탐색 라이브러리
from bisect import bisect_left, bisect_right
a = [1,2,4,4,8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))
# 2
# 4

# 값이 특정 범위에 속하는 데이터 개수 구하기
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 배열 선언
a = [1,2,3,3,3,3,4,4,8,9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a,4,4))

# 값이 [-1,3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))
# 2
# 6