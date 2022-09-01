from copy import deepcopy
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)
# list(combinations(items, 2))

def bfs(i,j):
    dq = deque()
    dq.append([i,j])
    cur_cnt = 1
    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if visited[nx][ny]==0 and arr[nx][ny]==1:
                    dq.append([nx,ny])
                    visited[nx][ny] = 1
                    cur_cnt+=1
    return cur_cnt
dx = [1,-1,0,0]
dy = [0,0,1,-1]
m , n = map(int,input().split())
arr = []
for i in range(m):
    arr.append(list(map(int,input().split())))
visited = [[0]*n for i in range(m)]
cnt = 0
result = 0
for i in range(m):
    for j in range(n):
        if visited[i][j]==0 and arr[i][j] == 1:
            visited[i][j] = 1
            result = max(result,bfs(i,j))
            cnt+=1
if cnt==0 :
    print(0)
    print(0)
else:
    print(cnt)
    print(result)