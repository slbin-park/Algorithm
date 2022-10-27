import sys
from collections import deque

sys.setrecursionlimit(10**5)

input = sys.stdin.readline


def bfs():
    global res
    while dq:
        x, y = dq.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if sand[nx][ny]:
                    sand[nx][ny] -= 1
                    if sand[nx][ny] == 0:
                        dq.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1
                        res = max(res, visited[nx][ny])


res = 0
n, m = map(int, input().split())
sand = [[0 for i in range(m)] for i in range(n)]
visited = [[0 for i in range(m)] for i in range(n)]
dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, 1, -1]

dq = deque()
for i in range(n):
    a = input().strip()
    for j in range(m):
        if a[j] == '.':
            sand[i][j] = 0
            dq.append((i, j))
        if a[j] != '.':
            sand[i][j] = int(a[j])
bfs()
print(res)