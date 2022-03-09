# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 21:24:35 2022

@author: khb16
"""
# 2. 부품 찾기
# 1) 이진탐색
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
    
# N(가게의 부품 개수) 입력
n = int(input())
# 가게이 있는 전체 부품 번호를 공백으로 구분하여 입력
array = list(map(int, input().split()))
array.sort() # 이진 탐색을 수행하기 위해 사전에 정렬 수행
# M(손님이 확인 요청한 부품 개수) 입력
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')

'''
5

8 3 7 9 2

3

5 7 9
no yes yes 
'''

# 2) 집합 자료형 이용
n = int(input())
array = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end = ' ')
    else:
        print('No', end = ' ')

# ------------------------------------------------------------

# 3. 떡볶이 떡 만들기
# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력받기
n,m = list(map(int, input().split(' ')))
# 각 떡의 개별 높이 정보를 입력받기
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 덜 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1
        
# 정답 출력
print(result)
'''
4 6

19 15 10 17
15
'''

# ------------------------------------------------------------
# 4. 정렬된 배열에서 특정 수의 개수 구하기

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

n, x = map(int, input().split())
array = list(map(int, input().split()))

# 값이 [x,x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(count)
'''
7 2

1 1 2 2 2 2 3
4
'''