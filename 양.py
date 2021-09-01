import sys
from collections import deque
sys.setrecursionlimit(1000000)  # 재귀 최대깊이를 정해줌

input = sys.stdin.readline


def bfs():
    global v, o
    for i in range(n):
        for j in range(m):
            if arr[i][j] != '#' and visited[i][j] == 0:
                if visited[i][j] == 0:
                    dq.append([i, j])
                    cntv = cnto = 0
                    while dq:
                        x, y = dq.popleft()
                        if visited[x][y] == 0:
                            if arr[x][y] == 'v' and visited[x][y] == 0:
                                cntv += 1
                            if arr[x][y] == 'o' and visited[x][y] == 0:
                                cnto += 1
                            visited[x][y] = 1
                            for h in range(4):
                                nx = x+dx[h]
                                ny = y+dy[h]
                                if nx >= 0 and nx < n and ny >= 0 and ny < m:
                                    if arr[nx][ny] != '#' and visited[nx][ny] == 0:
                                        dq.append([nx, ny])
                    if cnto > cntv:
                        o += cnto
                    else:
                        v += cntv


n, m = map(int, input().split())
arr = [[[] for i in range(m)]for i in range(n)]
visited = [[0 for i in range(m)]for i in range(n)]
v = o = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dq = deque()
for i in range(n):
    a = input()
    for j in range(m):
        arr[i][j] = a[j]
bfs()
print(o, v)
