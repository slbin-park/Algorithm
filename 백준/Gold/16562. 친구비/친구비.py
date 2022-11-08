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
    if pay[x-1] > pay[y-1]:
        tmp = x
        x = y
        y = tmp
    if x!=y:
        parent[y] = x
        
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n,m,k = map(int,input().split())
pay = list(map(int,input().split()))
parent = [i for i in range(n+1)]
arr = []
for i in range(m):
    a,b = map(int,input().split())
    arr.append([a,b])
for a,b in arr:
    union(a,b)
friend = [0 for i in range(n+1)]
res = 0
for i in range(1,n+1):
    cur_p = find(i)
    if friend[cur_p] == 0 :
        friend[cur_p] = 1
        res+=pay[cur_p-1]
if res <= k:
    print(res)
else:
    print("Oh no")