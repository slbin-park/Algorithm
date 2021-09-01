import sys
from collections import deque
sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def dfs(a, cnt):
    global res
    if visited[a] != 1 and len(arr[a]) == 1 and a != 1:
        res += cnt
        return
    visited[a] = 1
    for i in arr[a]:
        if visited[i] == 0:
            dfs(i, cnt+1)


n = int(input())
arr = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
res = 0
for i in range(n-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
dfs(1, 0)
if(res % 2 == 0):
    print('No')
else:
    print('Yes')
