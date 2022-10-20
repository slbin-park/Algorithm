import sys
import heapq
from copy import deepcopy
input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
arr = [int(input())for i in range(9)]
arr.sort()
res = []
def dfs(index):
    if len(res)==7 and sum(res)==100:
        for i in range(7):
            print(res[i])
        exit()
    if index<9:
        res.append(arr[index])
        dfs(index+1)
        res.pop()
        dfs(index+1)
dfs(0)