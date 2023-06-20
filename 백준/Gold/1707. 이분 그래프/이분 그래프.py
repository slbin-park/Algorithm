from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import sys

sys.setrecursionlimit(10**5)


def bfs(start):
    dq = deque()
    dq.append([start, 1])
    visited[start] = 1
    while dq:
        idx, group = dq.popleft()
        for next in arr[idx]:
            if visited[next] == 0:
                visited[next] = -group
                dq.append([next, -group])
            elif visited[next] == group:
                return False
    return True


n = int(input())
for T in range(n):
    V, E = map(int, input().split())
    res = "YES"
    arr = [[] for i in range(V + 1)]
    visited = [0 for i in range(V + 1)]
    for i in range(E):
        u, v = map(int, input().split())
        arr[u].append(v)
        arr[v].append(u)
    for i in range(1, V + 1):
        if visited[i] == 0:
            if bfs(i) == False:
                res = "NO"
                break
    print(res)
