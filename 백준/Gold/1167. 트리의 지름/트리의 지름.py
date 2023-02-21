import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = [[] for i in range(n + 1)]
res = 0


def dfs(idx, cost):
    global res
    for i, c in arr[idx]:
        if visited[i] == 0:
            visited[i] = cost + c
            dfs(i, c + cost)


for i in range(n):
    cur = list(map(int, input().split()))
    i = 1
    while 1:
        if cur[i] == -1:
            break
        arr[cur[0]].append((cur[i], cur[i + 1]))
        i += 2
visited = [0 for i in range(n + 1)]
dfs(1, 0)
visited[1] = 0
res = 0
idx = 0
for i in range(2, n + 1):
    if res < visited[i]:
        res = visited[i]
        idx = i
visited = [0 for i in range(n + 1)]
dfs(idx, 0)
visited[idx] = 0
print(max(visited))