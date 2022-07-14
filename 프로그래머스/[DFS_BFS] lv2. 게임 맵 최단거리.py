# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 12:25:03 2022

@author: khb16
"""
# DFS/BFS
# 게임 맵 최단거리

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]


from collections import deque
def solution(maps):
    
    n,m = len(maps), len(maps[0]) 
    dx, dy = [1,-1,0,0], [0,0,1,-1] 
    
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1        # 출발 인덱스에 1로 초기화
    
    queue = deque([(0,0)])   # 큐에 출발인덱스 삽입
    
    while queue:
        x, y = queue.popleft() # 현재 위치
        
        # 상하좌우 확인
        for i in range(4):
            nx = x + dx[i] 
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and maps[nx][ny] == 1:
                queue.append([nx, ny])               # 큐에 이동한 좌표 삽입
                visited[nx][ny] = visited[x][y] + 1  # 동한위치의 거리값에다가 이전거리값에 1을 더한 값 삽입
    
    return visited[n-1][m-1] # 도착위치의 거리값 리턴

solution(maps)

