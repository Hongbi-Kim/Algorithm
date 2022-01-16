# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 13:57:34 2022

@author: khb16
"""

# DFS(Depth-First Search)
# 깊이 우선 탐색이라고도 부르며, 그래프에서 깊은 부분을 우선적으로 탐색

# 인접행렬
INF = 999999999
graph = [
    [0,7,5],
    [7,0,INF,
     5,INF,0]]
print(graph)
# [[0, 7, 5], [7, 0, 999999999, 5, 999999999, 0]]

# 인접리스트
# 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

# 노드 1에 연결된 노드 정보 저장
graph[1].append((0,7))

# 노드 2에 연결된 노드 정보 저장
graph[2].append((0,5))

print(graph)
# [[(1, 7), (2, 5)], [(0, 7)], [(0, 5)]]

# ----------------------------------------------------
# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]]

# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False] * 9

dfs(graph, 1, visited)
# 1 2 7 6 8 3 4 5 

# ----------------------------------------------------------------
# BFS(Breadth-First Search) ***
# 너비 우선 탐색

from collections import deque
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]]

# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False] * 9

bfs(graph, 1, visited)
# 1 2 3 8 7 4 5 6 

