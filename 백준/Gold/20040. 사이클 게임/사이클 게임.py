import sys
import heapq
from copy import deepcopy
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    return x
def union(x,y):
    x = find(x)
    y = find(y)
    if x > y:
        tmp = x
        x = y
        y = tmp
    parent[y] = x
        
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n,m = map(int,input().split())
parent = [i for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    if find(a) == find(b):
        print(i+1)
        exit(0)
    union(a,b)
print(0)