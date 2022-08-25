import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)

input = sys.stdin.readline


def dfs(x):
    global answer
    visited[x] = 1
    cycle.append(x)
    cur = arr[x]
    if visited[cur]:
        if cur in cycle:
            answer += cycle[cycle.index(cur):]
        return
    else:
        dfs(cur)
    
    
    
n = int(input())
for i in range(n):
    m = int(input())
    arr = [0] + list(map(int,input().split()))
    visited = [0 for i in range(m+1)]
    answer = []
    for i in range(1,m+1):
        if visited[i]==0:
            cycle = []
            dfs(i)
    print(m-len(answer))