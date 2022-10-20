import sys
import heapq
from copy import deepcopy
input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n , m , k = map(int,input().split())
e,s,j = 1,1,1
i = 1
while e!=n or s!=m or j!=k:
    e+=1
    s+=1
    j+=1
    if e>15:
        e=1
    if s>28:
        s=1
    if j>19:
        j=1
    i+=1
print(i)