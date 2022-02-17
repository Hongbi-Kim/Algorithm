# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 01:38:18 2022

@author: khb16
"""

# 문제3
n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로, 정수는 정수형으로 변환하여 저장
    array.append((input_data[0], int(input_data[1])))

# 키(Key)를 이용하여, 점수를 기준으로 정렬
array = sorted(array, key = lambda student: student[1])

# 정렬이 수행된 결과를 출력
for student in array:
    print(student[0], end = ' ')
    
'''
2

홍길동 95

이순신 77
이순신 홍길동
'''    

# 문제
# 4. 두 배열의 원소 교체
# 두 개의 배열 A와 B는 N개의 원소로 구성, 모두 자연수
# 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라 서로 바꾼다.
# K번 반복하여, 배열 A의 모든 원소의 합이 최대가 최도록 만들기


n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() # 오름차순
b.sort(reverse = True) # 내림차순

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))

# 5 3

# 1 2 5 4 3

# 5 5 6 6 5
# 26