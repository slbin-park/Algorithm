import sys
from collections import deque


def findbfs():
    visited[0][0][0] = 0
    fdq = deque()
    fdq.append((0, 0))
    dq.append((0, 0))
    while fdq:
        x, y = fdq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0 and visited[nx][ny][0] == 2:
                    dq.append((nx, ny))
                    visited[nx][ny][0] = 0


def bfs():
    res = 0
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1:
                    visited[nx][ny][0] -= 1
                    if visited[nx][ny][0] < 1:
                        arr[nx][ny] = 0
                        dq.append((nx, ny))
                        visited[nx][ny][1] = visited[x][y][1] + 1
                        res = max(res, visited[nx][ny][1])
                elif arr[nx][ny] == 0 and visited[nx][ny][0] == 2:
                    visited[nx][ny][0] = 0
                    visited[nx][ny][1] = visited[x][y][1]
                    dq.appendleft((nx, ny))
    return res


input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())
arr = [[0 for i in range(m)] for i in range(n)]
visited = [[[2, 0] for i in range(m)] for i in range(n)]
dq = deque()
for i in range(n):
    arr[i] = list(map(int, input().split()))

findbfs()
ans = bfs()
print(ans)
