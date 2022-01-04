import sys
from collections import deque


def dfs(a):
    dq.append(a)
    cur = []
    while dq:
        idx = dq.popleft()
        if arr[idx] == -1:
            for i in range(len(cur)):
                visited[cur[i]] = 1
            break
        if arr[idx] == -2:
            visited[a] = -2
            for i in range(len(cur)):
                visited[cur[i]] = -2
            break
        dq.append(arr[idx])
        cur.append(arr[idx])


input = sys.stdin.readline
dq = deque()
n = int(input())
res = 0
arr = list(map(int, input().split()))
visited = [-1 for i in range(n)]
m = int(input())
arr[m] = -2
visited[m] = -2
for i in range(n):
    dfs(i)
for i in range(n):
    if visited[i] == -1:
        res += 1
print(res)