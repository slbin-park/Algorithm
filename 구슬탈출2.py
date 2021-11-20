import sys
from collections import deque


def bfsr():
    global res
    visited = [[[[0 for i in range(m)] for i in range(n)] for i in range(m)]
               for i in range(n)]
    while dq:
        rx, ry, bx, by, cnt = dq.popleft()
        visited[rx][ry][bx][by] = 1
        if cnt > 10:
            break
        for i in range(4):
            rnx, rny, cntr = move(rx, ry, dx[i], dy[i])
            bnx, bny, cntb = move(bx, by, dx[i], dy[i])
            if board[bnx][bny] == 'O':
                continue
            elif board[rnx][rny] == 'O':
                print(cnt)
                return
            if rnx == bnx and rny == bny:
                if cntr < cntb:
                    bnx -= dx[i]
                    bny -= dy[i]
                else:
                    rnx -= dx[i]
                    rny -= dy[i]
            if visited[rnx][rny][bnx][bny] == 0:
                visited[rnx][rny][bnx][bny] = 1
                dq.append((rnx, rny, bnx, bny, cnt + 1))
    print(-1)


def move(x, y, nx, ny):
    cnt = 0
    while board[x + nx][y + ny] != '#' and board[x][y] != 'O':
        cnt += 1
        x += nx
        y += ny
    return x, y, cnt


input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
res = -1
n, m = map(int, input().split())
board = [['' for i in range(m)] for j in range(n)]
dq = deque()
x1, y1, x2, y2 = 0, 0, 0, 0
for i in range(n):
    a = input().strip()
    for j in range(m):
        if a[j] == 'B':
            x2 = i
            y2 = j
        if a[j] == 'R':
            x1 = i
            y1 = j
        board[i][j] = a[j]
dq.append((x1, y1, x2, y2, 1))
bfsr()