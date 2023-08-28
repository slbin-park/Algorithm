import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M, OIL = map(int, input().split())
arr = [[0 for i in range(N + 1)] for i in range(N + 1)]
people = []
for i in range(N):
    a = list(map(int, input().split()))
    for j in range(N):
        arr[i + 1][j + 1] = a[j]
texi_x, text_y = map(int, input().split())
for i in range(M):
    a, b, c, d = map(int, input().split())
    people.append([a, b, c, d])
    arr[a][b] = i + 2
dq = deque()


def get_dis(start_x, start_y, end_x, end_y):
    dq = deque()
    dq.append([start_x, start_y, 0])
    vis = [[0 for i in range(N + 1)] for i in range(N + 1)]
    if start_x == end_x and start_y == end_y:
        return 0
    while dq:
        x, y, cnt = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == end_x and ny == end_y:
                return cnt + 1
            if 0 < nx <= N and 0 < ny <= N:
                if vis[nx][ny] == 0 and arr[nx][ny] != 1:
                    vis[nx][ny] = 1
                    dq.append([nx, ny, cnt + 1])
    print(-1)
    exit(0)


def checkOIL(dis, oil):
    if dis > oil:
        # print(dis, oil, "123123")
        print(-1)
        exit(0)


while M:
    vis = [[0 for i in range(N + 1)] for i in range(N + 1)]
    dq = deque()
    dq.append([texi_x, text_y, 0])
    tmp_people = []
    vis[texi_x][text_y] = 1
    if arr[texi_x][text_y] != 0:
        tmp_people.append([0, texi_x, text_y, arr[texi_x][text_y]])
    while dq:
        x, y, cnt = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 < nx <= N and 0 < ny <= N:
                if vis[nx][ny] == 0 and arr[nx][ny] != 1:
                    dq.append([nx, ny, cnt + 1])
                    vis[nx][ny] = 1
                    if arr[nx][ny] != 0:
                        tmp_people.append([cnt + 1, nx, ny, arr[nx][ny]])
    if len(tmp_people) == 0:
        print(-1)
        exit(0)

    tmp_people.sort()

    checkOIL(tmp_people[0][0], OIL)
    OIL -= tmp_people[0][0]

    x, y, end_x, end_y = people[tmp_people[0][3] - 2]
    arr[x][y] = 0

    dis = get_dis(x, y, end_x, end_y)
    texi_x = end_x
    text_y = end_y
    checkOIL(dis, OIL)

    OIL += dis
    M -= 1
print(OIL)
