import sys
from collections import deque
sys.setrecursionlimit(10000)  # 재귀 최대깊이를 정해줌
input = sys.stdin.readline


def dfs():
    dq.append(1)
    visited[1] = 1
    while dq:
        a = dq.pop()
        for i in arr[a]:
            if visited[i] == 0:
                visited[i] = a
                dq.append(i)


n = int(input())
dq = deque()
arr = [[0] for i in range(n+1)]
visited = [0 for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
dfs()
for i in range(2, n+1):
    print(visited[i])
