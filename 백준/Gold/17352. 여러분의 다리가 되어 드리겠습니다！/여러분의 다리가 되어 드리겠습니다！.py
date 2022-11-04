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
    if x > y:
        tmp = x
        x = y
        y = tmp
    if x!=y:
        parent[y] = x
n = int(input())
parent = [i for i in range(n+1)]
for i in range(n-2):
    a,b = map(int,input().split())
    union(a,b)
prev = find(1)
for i in range(2,n+1):
    if prev != find(i):
        print(prev,i)
        break;