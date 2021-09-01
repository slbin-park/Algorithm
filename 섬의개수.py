import sys
from collections import deque
input = sys.stdin.readline
dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, 1, -1]
dq = deque()


def bfs():
    cnt = 0
    visited = [[0 for i in range(w)] for j in range(h)]
    for i in range(h):
        for j in range(w):
            if(arr[i][j] == 1 and visited[i][j] == 0):
                cnt += 1
                dq.append((i, j))
                while dq:
                    x, y = dq.pop()
                    for k in range(8):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx >= 0 and nx < h and ny >= 0 and ny < w:
                            if(arr[nx][ny] == 1 and visited[nx][ny] == 0):
                                dq.append((nx, ny))
                                visited[nx][ny] = 1
    return cnt


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [[0 for i in range(w)] for j in range(h)]
    for i in range(h):
        arr[i] = list(map(int, input().split()))
    print(bfs())
