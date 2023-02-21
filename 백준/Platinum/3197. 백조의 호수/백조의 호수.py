from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import sys

# sys.setrecursionlimit(10**5)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    dq = deque()
    dq.append([x, y])
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if (arr[nx][ny] == "."
                        or arr[nx][ny] == "L") and visted[nx][ny] == 0:
                    if arr[nx][ny] == "L":
                        back.append([nx, ny])
                    visted[nx][ny] = cnt
                    dq.append([nx, ny])


def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        x, y = y, x
    parent[y] = parent[x]


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


INF = int(1e9)
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [['' for i in range(m)] for i in range(n)]
visted = [[0 for i in range(m)] for i in range(n)]

dq = deque()
for i in range(n):
    a = input().strip()
    for j in range(m):
        arr[i][j] = a[j]
cnt = 0
back = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == "L" and visted[i][j] == 0:
            back.append([i, j])
            cnt += 1
            visted[i][j] = cnt
            dfs(i, j)
        if arr[i][j] == "." and visted[i][j] == 0:
            cnt += 1
            visted[i][j] = cnt
            dfs(i, j)
        # 물근처에 있는 얼음들 dq에 넣음
        if arr[i][j] == "X":
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if arr[nx][ny] != "X":
                        dq.append([i, j])
                        break

parent = [i for i in range(cnt + 1)]
# 현재 물과 인접한 X에 부모 물번호 넣어주기
for i in range(len(dq)):
    x, y = dq.popleft()
    arr[x][y] = "."
    dq.append([x, y])

res = 0
asd = 0
while True:
    dq2 = deque()

    # for i in range(n):
    #     print(visted[i])
    # print(parent)
    # print()

    while dq:
        # asd += 1
        # print(asd)
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 방문한곳은 다시 방문 안함
                if arr[nx][ny] == "X" and visted[nx][ny] == 0:
                    dq2.append([nx, ny])
                    arr[nx][ny] = "."
                if visted[nx][ny] != 0 and visted[x][y] == 0:
                    visted[x][y] = find(visted[nx][ny])
                # 녹아서 물이고 부모가 아직 안정해져서 지금 물의 부모로 바꿈
                # 전에 녹은 물때문에 부모가 생겼을 경우 union 실행
                if visted[nx][ny] != 0 and visted[x][y] != 0:
                    union(parent[visted[nx][ny]], parent[visted[x][y]])

    # for i in range(n):
    #     print(visted[i])
    # print(parent)
    # print()

    res += 1
    # 백조1
    start = back[0]
    # 백조2
    end = back[1]
    if find(parent[visted[start[0]][start[1]]]) == find(
            parent[visted[end[0]][end[1]]]):
        print(res)
        break
    dq = dq2