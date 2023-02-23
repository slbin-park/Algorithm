from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import sys

# sys.setrecursionlimit(10**5)


def isMove(x):
    if 0 <= x <= 500000:
        return True
    return False


n, m = map(int, input().split())

k = 1
dq = deque()
dq.append([0, n])
visited = [[99999999] * 500001 for i in range(2)]
visited[0][n] = 0
cur_time = 0
while dq:
    cnt, x = dq.popleft()
    # print(cnt, x)
    if isMove(x + 1):
        if visited[(cnt + 1) % 2][x + 1] > cnt + 1:
            visited[((cnt + 1)) % 2][x + 1] = cnt + 1
            dq.append([cnt + 1, x + 1])
    if isMove(x - 1):
        if visited[(cnt + 1) % 2][x - 1] > cnt + 1:
            visited[(cnt + 1) % 2][x - 1] = cnt + 1
            dq.append([cnt + 1, x - 1])
    if isMove(x * 2):
        if visited[(cnt + 1) % 2][x * 2] > cnt + 1:
            visited[(cnt + 1) % 2][x * 2] = cnt + 1
            dq.append([cnt + 1, x * 2])
while m <= 500000:
    if visited[cur_time % 2][m] <= cur_time:
        print(cur_time)
        exit()
    cur_time += 1
    m += cur_time
print(-1)