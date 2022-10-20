import sys
import heapq
from copy import deepcopy
input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n = int(input())
arr = [list(map(int,input().split()))for i in range(n)]
start = []
link = []
res = 1e9
def check_():
    start_sum = 0
    for i in start:
        for j in start:
            start_sum+=arr[i-1][j-1]
    link_sum = 0
    for i in link:
        for j in link:
            link_sum+=arr[i-1][j-1]
    return abs(start_sum-link_sum)
def dfs(index):
    global res
    if index==n+1:
        res = min(res,check_())
    if len(start)<n//2:
        start.append(index)
        dfs(index+1)
        start.pop()
    if len(link)<n//2:
        link.append(index)
        dfs(index+1)
        link.pop()
dfs(1)
print(res)