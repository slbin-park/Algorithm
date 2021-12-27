import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    while dq:
        x, y, h = dq.popleft()
        if x == H - 1 and y == W - 1:
            return visited[x][y][h] - 1
        move(x, y, h)
        if h < n:
            move_h(x, y, h)

    return -1


def move(x, y, h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if check(nx, ny, h):

            visited[nx][ny][h] = visited[x][y][h] + 1
            dq.append((nx, ny, h))


def move_h(x, y, h):
    for i in range(8):
        nx = x + hx[i]
        ny = y + hy[i]
        if check(nx, ny, h):
            if visited[nx][ny][h + 1] == 0:
                visited[nx][ny][h + 1] = visited[x][y][h] + 1
                dq.append((nx, ny, h + 1))


def check(nr, nc, k):  # 이동 가능 여부 확인
    if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc][k] and arr[nr][
            nc] == 0:
        return True
    return False


n = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
hx = [-1, -2, -2, -1, 1, 2, 2, 1]
hy = [-2, -1, 1, 2, 2, 1, -1, -2]

dq = deque()
dq.append((0, 0, 0))

W, H = map(int, input().split())

visited = [[[0] * (n + 1) for i in range(W)] for i in range(H)]
visited[0][0][0] = 1

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
res = bfs()
print(res)