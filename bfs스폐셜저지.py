import sys
import collections
from collections import deque


def bfs():
    global flag
    b = 1
    dq.append(1)
    start = 1
    visited[1] = 1
    while dq:
        res = []
        x = dq.popleft()
        for i in arr[x]:
            if visited[i] == 0:
                visited[i] = 1
                res.append(i)
        for i in range(start, start + len(res)):
            if arr1[i] in res:
                dq.append(arr1[i])
            else:
                print(0)
                exit(0)
        start += len(res)
    print(1)


input = sys.stdin.readline
n = int(input())
arr = [[] for i in range(n + 1)]
visited = [0 for i in range(n + 1)]
flag = True
dq = deque()
for i in range(n - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
arr1 = list(map(int, input().split()))
for i in range(1, n + 1):
    arr[i].sort(reverse=True)

if arr1[0] != 1:
    print(0)
else:
    bfs()