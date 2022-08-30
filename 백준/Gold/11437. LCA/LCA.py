from copy import deepcopy
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)
# list(combinations(items, 2))
LOG = 21
input = sys.stdin.readline

n = int(input())
arr = [[] for i in range(n+1)]
d = [0] * (n+1) # 각 노드까지의 깊이 depth
c = [0] * (n+1) # 각 노드의 깊이 계산했는지
parent = [[0] * LOG for i in range(n+1)]

for i in range(n-1):
    u , v = map(int,input().split())
    arr[u].append(v)
    arr[v].append(u)

def dfs(x,depth):
    c[x] = 1
    d[x] = depth
    for item in arr[x]:
        if c[item]:
            continue
        parent[item][0] = x
        dfs(item,depth+1)

def set_parent():
    dfs(1,0)
    for i in range(1,LOG):
        for j in range(1,n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]
            # 2의 제곱으로 건너뛸 때의 부모 값 기록 
            # #( 2^i 번째 조상 노드 저장 - j의 2^i의 조상 = j의 2^(i-1) 조상의 2^(i-1) 조상)
            
def lca(a,b):
    if d[a] > d[b]:
        a,b = b,a
    for i in range(LOG -1 ,-1 , -1):
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]
    if a==b:
        return a
    for i in range(LOG -1 , -1 ,-1 ):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]

set_parent()

m = int(input())

for i in range(m):
    a, b = map(int,input().split())
    print(lca(a,b))