from copy import deepcopy
import heapq
from re import A
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)
# list(combinations(items, 2))
INF = 1e9
input = sys.stdin.readline

def bfs():
    dq.append([0,0])
    visited[0][0] = 0
    while dq:
        x,y = dq.popleft()
        if x == n-1 and y == n-1:
            return
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == -1:
                if arr[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y]
                    dq.appendleft([nx,ny])
                else:
                    visited[nx][ny] = visited[x][y]+1
                    dq.append([nx,ny])
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n = int(input())
arr = [[0 for i in range(n)]for i in range(n)]

b_cnt = 0
for i in range(n):
    inp = input().rstrip()
    for j in range(n):
        arr[i][j] = int(inp[j])
visited = [[-1 for i in range(n)]for i in range(n)]
dq = deque()
bfs()

print(visited[n-1][n-1])
