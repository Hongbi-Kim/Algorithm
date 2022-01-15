# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 00:49:53 2022

@author: khb16
"""

# 퀵 정렬
# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
# 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나
# 병합 정렬과 더불어 대부분의 프로그래밍언어의 정렬 라이브러리의 근간이 되는 알고리즘
# 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(Pivot)로 설정

# 분할(Divide)
# O(NlogN) 기대 가능, 최악의 경우 O(N^2)

array = [7,5,9,0,3,1,6,2,4,8]
def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start+1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot] :
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right -1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]            
            

# 파이썬의 장점을 살린 퀵 정렬 코드
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트
    
    left_side = [x for x in tail if x <= pivot] # 분할 된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할 된 오른쪽 부분
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
print(quick_sort(array))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]   
    


# 계수 정렬
# 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작
# 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능
# 데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일 때 최악의 경우에도 O(N+K) 보장
# 동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적
# 성적의 경우 100점을 맞은 학생이 여러명 일 수 있기 때문에 효과적

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array)+1)
for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 증가
for i in range(len(count)):  # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력          
# 0 0 1 1 2 2 3 4 5 5 6 7 8 9 9 