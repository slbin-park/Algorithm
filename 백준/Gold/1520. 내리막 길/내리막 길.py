import sys
from collections import deque
sys.setrecursionlimit(10**5)

def dfs(x, y):
    global visited
    if x == n - 1 and y == m - 1:
        return 1
    if visited[x][y] !=-1:
        return visited[x][y]
    visited[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] < arr[x][y] :
                visited[x][y] += dfs(nx, ny)
    return visited[x][y]

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split()))for _ in range(n)]
visited = [[-1 for i in range(m)] for i in range(n)]

print(dfs(0, 0))

