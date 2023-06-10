from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import sys

sys.setrecursionlimit(10**5)


input = sys.stdin.readline
n = int(input())
arr = [[] for i in range(n + 1)]
visited = [0 for i in range(n + 1)]
visited[1] = 1
res = 0
for i in range(n - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
dq = deque()
dq.append([1, 0])
while dq:
    idx, cnt = dq.popleft()
    if idx != 1 and len(arr[idx]) == 1:
        res += cnt
        continue
    for next in arr[idx]:
        if visited[next] == 0:
            visited[next] = 1
            dq.append([next, cnt + 1])
print("Yes" if res % 2 == 1 else "No")
