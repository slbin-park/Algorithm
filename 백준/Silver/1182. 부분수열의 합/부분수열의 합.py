import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

def dfs(x , value):
    global cnt
    if x>=n:
        return
    if value+arr[x] == m :
        cnt+=1
    dfs(x+1,value)
    dfs(x+1,value+arr[x])

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
cnt = 0
if n==1:
    if arr[0] == m:
        print(1)
    else:
        print(0)
    exit()
dfs(0,0)
print(cnt)