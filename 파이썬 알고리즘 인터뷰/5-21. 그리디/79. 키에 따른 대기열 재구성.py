# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 22:52:13 2022

@author: khb16
"""

# 그리디
# 키에 따른 대기열 재구성
# (h, k) h: 키, k: 앞에 줄 서 있는 사람들 중 자신의 키 이상인 사람들의 수

# 입력
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

# 풀이 1: 우선순위 큐 이용
# 우선순위 큐 자체가 매번 그때그때의 최소 또는 최댓값을 추출
# 파이썬은 최소 힙만 지원하기 때문에, 첫 번째 값을 음수로 변경해 최대 힙처럼 구현
import heapq

def reconstructQueue(people):
    heap = []
    # 키 역순, 인덱스 삽입
    for person in people:
        heapq.heappush(heap, (-person[0], person[1]))
        
    result = []
    # 키 역순, 인덱스 추출
    # heap = [(-7, 0), (-6, 1), (-7, 1), (-4, 4), (-5, 0), (-5, 2)]
    while heap:
        person = heapq.heappop(heap)
        result.insert(person[1], [-person[0], person[1]])
    return result

reconstructQueue(people)
# [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]