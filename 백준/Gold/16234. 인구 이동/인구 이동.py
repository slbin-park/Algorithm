import sys
import heapq
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    res = 0
    stack = []
    while dq:
        x,y, = dq.popleft()
        stack.append([x,y])
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if l<=abs(arr[x][y] - arr[nx][ny]) <=r and visited[nx][ny]==0:
                    visited[nx][ny] = 1
                    dq.append([nx,ny])
    if len(stack) > 1:
        for x,y in stack:
            res+= arr[x][y]
        for x,y in stack:
            arr[x][y] = res//len(stack)
        return 1
    return 0 
        
n,l,r = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
dq = deque()
cnt=0
while 1:
    visited = [[0 for i in range(n)]for i in range(n)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j]=1
                dq.append([i,j])
                if bfs()==1:
                    flag=1
    if flag==1:
        cnt+=1
    else:
        break;
print(cnt)