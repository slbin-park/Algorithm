from copy import deepcopy
import heapq
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)
# list(combinations(items, 2))
INF = 1e9
input = sys.stdin.readline

def bfs():
    dq = deque()
    dq.append([1,0])
    visited[1][0] = 0
    while dq:
        number , clip  = dq.popleft()
        if visited[number][number] == -1:
            dq.append([number,number])
            visited[number][number] = visited[number][clip]+1
        if number+clip <= n and visited[number+clip][clip] == -1:
            dq.append([number+clip,clip])
            visited[number+clip][clip] = visited[number][clip]+1
        if number -1 > 0 and visited[number-1][clip]==-1:
            dq.append([number-1,clip])
            visited[number-1][clip] = visited[number][clip]+1
            
result = 1e9
n = int(input())
visited = [[-1 for i in range(n+1)] for i in range(n+1)]
bfs()
for i in range(n+1):
    if visited[n][i] != -1:
        result = min(result,visited[n][i])
print(result)