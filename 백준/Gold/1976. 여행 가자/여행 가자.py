import sys
import heapq
from copy import deepcopy
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    else:
        return parent[x]
def union(x,y):
    x = parent[x]
    y = parent[y]
    if x > y:
        tmp = x
        x = y
        y = tmp
    if x!=y:
        parent[y] = x
        
n = int(input())
m = int(input())
parent = [i for i in range(n+1)]
for i in range(n):
    a = list(map(int,input().split()))
    for j in range(n):
        if a[j] == 1:
            b = find(i+1)
            c = find(j+1)
            union(b,c)
travel = list(map(int,input().split()))
for i in range(1,m):
    if(parent[travel[i]] != parent[travel[i-1]]):
        print('NO')
        exit(0)
print('YES')