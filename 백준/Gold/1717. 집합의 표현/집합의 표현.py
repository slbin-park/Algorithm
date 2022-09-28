from copy import deepcopy
import heapq
from operator import truediv
from re import A, X
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
# list(combinations(items, 2))
# type(123.4) is float
LOG = 21
input = sys.stdin.readline


def find(x):
    if x !=parent[x]:
        parent[x] = find(parent[x])
        return parent[x]
    else:
        return x
def union(x,y):
    x = find(x)
    y = find(y)
    if x > y:
        tmp = x
        x = y
        y = tmp
    parent[y] = x
    
n , m = map(int,input().split())
parent = [i for i in range(n+1)]
for i in range(m):
    u,v,w = map(int,input().split())
    if u==0:
        union(v,w)
    else:
        v = find(v)
        w = find(w)
        
        if v==w:
            print('YES')
        else:
            print('NO')