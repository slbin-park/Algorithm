from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import decimal
import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline
n, m, h = map(int, input().split())
CNT = 0

minCnt = 1e9


def dfs(x, y, curIdx, isMove):
    global CNT, minCnt
    # print(x, y, curIdx, isMove)
    if minCnt == 0 or minCnt == 1:
        return
    if x == h + 1:
        if y == curIdx:
            # for i in range(h + 1):
            #     print(arr[i])
            if y == n:
                minCnt = min(minCnt, CNT)
                return
            dfs(1, y + 1, y + 1, False)
    else:
        if arr[x][y] == 0 or isMove:
            dfs(x + 1, y, curIdx, False)
        else:
            dfs(x, arr[x][y], curIdx, True)
        nextY = y + 1 if y < n else y - 1
        # 사다리를 놓을수 있으면
        if arr[x][y] == 0 and arr[x][nextY] == 0 and CNT < 3:
            arr[x][y] = nextY
            arr[x][nextY] = y
            CNT += 1
            dfs(x, nextY, curIdx, True)
            CNT -= 1
            arr[x][y] = 0
            arr[x][nextY] = 0
        nextY = y - 1 if y > 1 else y + 1
        # 사다리를 놓을수 있으면
        if arr[x][y] == 0 and arr[x][nextY] == 0 and CNT < 3:
            arr[x][y] = nextY
            arr[x][nextY] = y
            CNT += 1
            dfs(x, nextY, curIdx, True)
            CNT -= 1
            arr[x][y] = 0
            arr[x][nextY] = 0
        # print("CNT = ", CNT)
        return False


arr = [[0 for i in range(n + 1)] for i in range(h + 1)]
for i in range(m):
    a, b = map(int, input().split())
    arr[a][b] = b + 1
    arr[a][b + 1] = b
# for i in range(h + 1):
#     print(arr[i])
dfs(1, 1, 1, False)
print(minCnt if minCnt != 1e9 else -1)
