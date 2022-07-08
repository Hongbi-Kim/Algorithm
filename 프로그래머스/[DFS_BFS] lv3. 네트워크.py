# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 22:43:53 2022

@author: khb16
"""

# DFS/BFS
# 네트워크

computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
n = 3

for a, b in enumerate(computers[0]):
    print(a, b)
# 0 1
# 1 1
# 2 0

def dfs(x, computers, visited):
    visited[x] = True    # x노드 방문 처리
    for a, b in enumerate(computers[x]):
        if b == 1 and (not visited[a]):    # 연결되어 있고, 아직 방문하지 않았다면
            dfs(a, computers, visited)

def solution(n, computers):
    visited = [False] * n    # 방문기록 초기화
    cnt = 0    # 그룹 개수
    
    for i in range(n):
        if not visited[i]:
            dfs(i, computers, visited)
            cnt += 1
            
    return cnt

solution(n, computers)
# 2