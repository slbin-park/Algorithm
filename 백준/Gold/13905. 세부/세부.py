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
    return x
def union(x,y):
    x = find(x)
    y = find(y)
    if x>y:
        tmp = x
        x = y
        y = tmp
    if x!=y:
        parent[y] = x
n , m = map(int,input().split())
start,end = map(int,input().split())
parent = [i for i in range(n+1)]
arr = [list(map(int,input().split())) for i in range(m)]
arr.sort(key=lambda x : -x[2])
for i in range(m):
    u = arr[i][0]
    v = arr[i][1]
    w = arr[i][2]
    union(u,v)
    if find(start) == find(end):
        print(w)
        exit()
print(0)