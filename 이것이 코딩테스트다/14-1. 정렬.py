# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 22:27:06 2022

@author: khb16
"""

# 23. 국영수
n = int(input())
students = [] # 학생 정보를 담을 리스트

# 모든 학생 정보를 입력받기
for _ in range(n):
    students.append(input().split())

students.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
# 감소하는 순서, 증가하는 순서, 감소하는 순서, 사전순 증가하는 순서

# 이름만 출력
for name in students:
    print(name[0])
    
# -------------------------------------------------------------------------

# 24. 안테나

n = int(input())
house = list(map(int, input().split()))

house.sort()

print(house[(n-1)//2])

# -------------------------------------------------------------------------

# 25. 실패율 
# https://programmers.co.kr/learn/courses/30/lessons/42889   
def solution(N, stages):
    answer = []
    length = len(stages)
    
    for i in range(1, N+1):
        count = stages.count(i)
        
        if length == 0:
            fail = 0
        else:
            fail = count / length
        answer.append((i, fail))
        length -= count
        
    answer = sorted(answer, key = lambda x: x[1], reverse = True)
    
    answer = [i[0] for i in answer]
    return answer
