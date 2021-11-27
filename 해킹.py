import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
cnt = [0] * (N + 1)
arr = []
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)


def bfs(start):
    visited = [0] * (N + 1)
    CNT = 0
    q = deque()
    visited[start] = 1
    q.append(start)
    while q:
        CNT += 1
        node = q.popleft()
        for nd in graph[node]:
            if visited[nd] == 0:
                visited[nd] = 1
                q.append(nd)
    return CNT


for i in range(1, N + 1):
    cnt[i] = bfs(i)

c = max(cnt)
for j in range(1, N + 1):
    if cnt[j] == c:
        print(j, end=' ')
