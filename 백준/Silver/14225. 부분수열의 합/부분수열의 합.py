import sys
import heapq
from copy import deepcopy
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n = int(input())
arr = list(map(int,input().split()))
vis = [0 for i in range(10000000)]
vis[0] = 1
def dfs(index,value):
    vis[value] = 1
    if index==n:
        return
    value+=arr[index]
    dfs(index+1,value)
    value-=arr[index]
    dfs(index+1,value)
dfs(0,0)
for i in range(2000000):
    if vis[i]==0:
        print(i)
        break;