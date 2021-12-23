import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    dq = deque()
    global res
    dq.append((start[0], start[1]))
    visited[start[0]][start[1]] = 0
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while True:
                if not (0 <= nx < m and 0 <= ny < n): break
                if arr[nx][ny] == '*': break
                if visited[nx][ny] < visited[x][y] + 1: break
                dq.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                nx = nx + dx[i]
                ny = ny + dy[i]


n, m = map(int, input().split())

arr = [[0 for i in range(n)] for i in range(m)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
c = []
visited = [[10 for i in range(n)] for i in range(m)]
for i in range(m):
    liinput = input().strip()
    for j in range(n):
        if liinput[j] == 'C':
            c.append([i, j])
        arr[i][j] = liinput[j]
start = []
start = c.pop()
bfs(start)
ex, ey = c.pop()
print(visited[ex][ey] - 1)
for i in range(m):
    print(visited[i])
