import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def dfs(n):
    result_dfs.append(n)
    visited[n] = 1
    for item in (arr[n]):
        if visited[item] == 0 :
            visited[item] = 1
            dfs(item)
def bfs():
    visited[V] = 1
    while dq:
        a = dq.popleft()
        for item in arr[a]:
            if visited[item] == 0:
                visited[item] = 1
                result_bfs.append(item)
                dq.append(item)
    
    
N , M , V = map(int,input().split())

arr = [[]for i in range(N+1)]

visited = [0 for i in range(N+1)]

result_dfs = []
result_bfs = []
result_bfs.append(V)

dq = deque()
dq.append(V)

for i in range(M):
    v1,v2 = map(int,input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

for i in range(N+1):
    arr[i].sort()

dfs(V)
visited = [0 for i in range(N+1)]
bfs()

print(*result_dfs)
print(*result_bfs)
