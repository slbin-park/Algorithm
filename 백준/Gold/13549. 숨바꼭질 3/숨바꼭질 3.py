from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import decimal
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
dq = deque()
MAX = 100001
visited = [-1 for i in range(MAX)]
visited[n] = 0
dq.append([n, 0])
while dq:
    idx, cnt = dq.popleft()
    next = idx * 2
    if 0 <= next <= 100000 and (visited[next] == -1 or visited[next] > cnt):
        visited[next] = cnt
        dq.appendleft([next, cnt])
    next = idx + 1
    if 0 <= next <= 100000 and (visited[next] == -1 or visited[next] > cnt):
        visited[next] = cnt + 1
        dq.append([next, cnt + 1])
    next = idx - 1
    if 0 <= next <= 100000 and (visited[next] == -1 or visited[next] > cnt):
        visited[next] = cnt + 1
        dq.append([next, cnt + 1])

print(visited[m])
