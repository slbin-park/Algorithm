from copy import deepcopy
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)
# list(combinations(items, 2))
input = sys.stdin.readline


def bfs():
    while dq:
        index = dq.popleft()
        for item in arr[index]:
            if visited[item] == 0 :
                visited[item] = index
                dq.append(item)

n = int(input())
arr = [[]for i in range(n+1)]
visited = [0 for i in range(n+1)]
dq = deque()
for i in range(n-1):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
dq.append(1)
visited[1] = 1
bfs()
for i in range(2,n+1):
    print(visited[i])