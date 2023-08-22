import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

input = sys.stdin.readline
N, Q = map(int, input().split())
arr = [[0 for i in range(2 ** N)] for i in range(2 ** N)]
for i in range(2 ** N):
    arr[i] = list(map(int, input().split()))
fire = list(map(int, input().split()))

dq = deque()
res = 0
CNT = 0
vis = [[0] * (2 ** N) for i in range(2 ** N)]


def rotate(x, y, l):
    lrange = max(0, 2 ** l // 2)
    tmp = [[0 for i in range(2 ** l)] for i in range(2 ** l)]
    # 배열 복사
    for i in range(x, x + 2 ** l):
        for j in range(y, y + 2 ** l):
            tmp[i - x][j - y] = arr[i][j]
    # 왼쪽 위
    for i in range(x, x + lrange):
        for j in range(y, y + lrange):
            arr[i][j] = tmp[i - x + lrange][j - y]
    # 오른쪽 위
    for i in range(x, x + lrange):
        for j in range(y + lrange, y + lrange * 2):
            arr[i][j] = tmp[i - x][j - (y + lrange)]
    # 오른쪽 밑
    for i in range(x + lrange, x + lrange * 2):
        for j in range(y + lrange, y + lrange * 2):
            arr[i][j] = tmp[i - (x + lrange)][j - y]
    # 왼쪽 밑
    for i in range(x + lrange, x + lrange * 2):
        for j in range(y, y + lrange):
            arr[i][j] = tmp[i - x][j - y + lrange]


def ice_fire():
    tmp_ice = []
    for i in range(2 ** N):
        for j in range(2 ** N):
            if arr[i][j] > 0:
                if get_cnt(i, j) < 3:
                    tmp_ice.append([i, j])
                    # print(i, j)
    for x, y in tmp_ice:
        arr[x][y] -= 1
    # print()


def get_cnt(x, y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 2 ** N and 0 <= ny < 2 ** N:
            if arr[nx][ny] > 0:
                cnt += 1
    return cnt


for i in range(Q):
    l = fire[i]
    # print("=====회전 하기 전 ======")
    # for j in range(2 ** N):
    #     print(arr[j])
    # print()
    # for j in range(0, 2 ** N, 2 ** l):
    #     for k in range(0, 2 ** N, 2 ** l):
    #         rotate(j, k, l)
    new_board = [[0] * 2 ** N for _ in range(2 ** N)]  # 회전한 Board 저장 용

    # rotate
    r_size = 2 ** l  # 격자 사이즈
    for y in range(0, 2 ** N, r_size):  # 격자 시작 좌표 y축
        for x in range(0, 2 ** N, r_size):  # 격자 시작 좌표 x축
            for i in range(r_size):  # 열 인덱스
                for j in range(r_size):  # 행 인덱스
                    new_board[y + j][x + r_size - i - 1] = arr[y + i][x + j]
    # for j in range(2 ** N):
    #     print(arr[j])
    # print()
    arr = new_board
    ice_fire()

    # for j in range(2 ** N):
    #     print(arr[j])
    # print()

dq = deque()
res = 0
CNT = 0
vis = [[0] * (2 ** N) for i in range(2 ** N)]

for i in range(2 ** N):
    for j in range(2 ** N):
        if vis[i][j] == 0 and arr[i][j] > 0:
            dq.append([i, j])
            cnt = 1
            res += arr[i][j]
            vis[i][j] = 1
            while dq:
                x, y = dq.popleft()
                # print("x , y = ", x, y)
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < 2 ** N and 0 <= ny < 2 ** N:
                        if vis[nx][ny] == 0 and arr[nx][ny] > 0:
                            vis[nx][ny] = 1
                            cnt += 1
                            res += arr[nx][ny]
                            dq.append([nx, ny])
            CNT = max(CNT, cnt)
print(res)
print(CNT)
