import sys
from collections import deque
sys.setrecursionlimit(10000)#재귀 최대깊이를 정해줌
input = sys.stdin.readline


def dfs(x):
    visited[x] = 1
    for i in arr[x]:
        if visited[i] == 0:
            dfs(i)


n, m = map(int, input().split())
arr = [[] for i in range(n)]
visited = [0 for i in range(n)]
cnt = 0

for i in range(m):
    a, b = map(int, input().split())
    arr[a-1].append(b-1)
    arr[b-1].append(a-1)

for i in range(n):
    if visited[i] == 0:
        dfs(i)
        cnt += 1
print(cnt)
